#!/usr/bin/env python
import json
import math
import sys

from pydicom import Dataset, datadict, dcmread, dcmwrite

from impac_privates import impac_private_dict

if __name__ == "__main__":
    energy_range_mm_dict = {}
    energy_string_range_dict = {}
    ion_plan_ds: Dataset = None
    # Values calculated on PSTAR NIST web site at integer energies in MeV
    # Assuming Linear Interpolation between integer energies is close enough
    # for non-clinical purposes, like testing workflow/interoperability.
    with open("proton_range_millimeters_water.json", "r") as f:
        energy_string_range_dict = json.load(f)
    energy_range_mm_dict = {int(x): y for x, y in energy_string_range_dict.items()}

    datadict.add_private_dict_entries("IMPAC", impac_private_dict)

    with open(sys.argv[1], "rb") as g:
        ion_plan_ds = dcmread(g)

    try:
        impac_block = ion_plan_ds.IonBeamSequence[0].private_block(0x300B, "IMPAC")
        if 0x04 in impac_block:
            print(f"File already contains IMPAC private for {impac_private_dict[0x300B1004][2]}")
            if len(sys.argv) < 2:  # unless they want to force it with a -f or something
                sys.exit()
    except KeyError:
        pass  # no impac block so we're good to go

    new_plan_name = sys.argv[1].removesuffix(".dcm") + "_ims_pvt.dcm"
    for beam in ion_plan_ds.IonBeamSequence:
        if beam.ScanMode not in ["MODULATED", "MODULATED_SPEC"]:
            print(f"Scan Mode is {beam.ScanMode} which isn't supported in this script/module")
            sys.exit()
        cp_sequence = beam.IonControlPointSequence
        cp_energy_list = [x.NominalBeamEnergy for x in cp_sequence]
        max_energy = max(cp_energy_list)
        min_energy = min(cp_energy_list)
        ceiling_max_energy = math.ceil(max_energy)
        floor_max_energy = math.floor(max_energy)
        ceiling_max_weight = max_energy - floor_max_energy

        ceiling_min_energy = math.ceil(min_energy)
        floor_min_energy = math.floor(min_energy)
        ceiling_min_weight = min_energy - floor_min_energy

        # this isn't taking in to account a Range Shifter or a Range Modulator
        # but for simple interoperability and workflow testing, it will do.
        distal_range_millimeters = (
            energy_range_mm_dict[floor_max_energy] * (1.0 - ceiling_max_weight)
            + energy_range_mm_dict[ceiling_max_energy] * ceiling_max_weight
        )
        proximal_range_millimeters = (
            energy_range_mm_dict[floor_min_energy] * (1.0 - ceiling_min_weight)
            + energy_range_mm_dict[ceiling_min_energy] * ceiling_min_weight
        )
        sobp_equivalent_mm = round(distal_range_millimeters - proximal_range_millimeters, ndigits=1)

        beam_max_radius_squared = 0
        for cp in cp_sequence:
            x_values = cp.ScanSpotPositionMap[0::2]
            y_values = cp.ScanSpotPositionMap[1::2]
            tuple_list = []
            r_squared_list = [x * x + y * y for x, y in zip(x_values, y_values)]
            max_r_squared = max(r_squared_list)
            if beam_max_radius_squared < max_r_squared:
                beam_max_radius_squared = max_r_squared

        beam_max_radius = math.sqrt(beam_max_radius_squared)
        new_private_block = beam.private_block(0x300B, "IMPAC", create=True)
        new_private_block.add_new(0x04, "FL", round(distal_range_millimeters, 1))
        new_private_block.add_new(0x02, "FL", round(beam_max_radius, 1))
        new_private_block.add_new(0x0E, "FL", round(sobp_equivalent_mm, 1))

    dcmwrite(
        new_plan_name, ion_plan_ds, write_like_original=True
    )  # assume the input was ExplicitLittleEndian for later tasks, see convert_to_explicit_little_endian.py
    print(f"Wrote updated file to {new_plan_name}")
