#!/usr/bin/env python
"""Create an RT Ion Beams Treatment Record from a provided RT Ion Plan
Run as a script, it writes the RT Ion Beams Treatment Record to the local directory with RX_{SOPInstanceUID}.dcm file name
Returns:
    RtIonBeamsTreatmentRecord: the treatment record as a domain model object wrapped around a pydicom dataset
"""

import inspect
import logging
import sys
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Dict, Tuple

from pydicom import dcmread, dcmwrite
from pydicom.datadict import add_dict_entry
from pydicom.uid import (
    ImplicitVRLittleEndian,
    RTIonBeamsTreatmentRecordStorage,
    generate_uid,
)

# from tdwii_plus_examples.domain_model.applicator_sequence_item import (
#     ApplicatorSequenceItem,
# )
# from tdwii_plus_examples.domain_model.block_slab_sequence_item import (
#     BlockSlabSequenceItem as CArmBlockSlabSequenceItem,
# )
from tdwii_plus_examples.domain_model.block_slab_sequence_item_1 import (
    BlockSlabSequenceItem as IonBlockSlabSequenceItem,
)
from tdwii_plus_examples.domain_model.ion_beam_sequence_item import IonBeamSequenceItem
from tdwii_plus_examples.domain_model.ion_block_sequence_item import (
    IonBlockSequenceItem,
)
from tdwii_plus_examples.domain_model.ion_control_point_delivery_sequence_item import (
    IonControlPointDeliverySequenceItem,
)
from tdwii_plus_examples.domain_model.ion_control_point_sequence_item import (
    IonControlPointSequenceItem,
)
from tdwii_plus_examples.domain_model.ion_range_compensator_sequence_item import (
    IonRangeCompensatorSequenceItem,
)
from tdwii_plus_examples.domain_model.ion_wedge_sequence_item import (
    IonWedgeSequenceItem,
)
from tdwii_plus_examples.domain_model.lateral_spreading_device_sequence_item import (
    LateralSpreadingDeviceSequenceItem,
)
from tdwii_plus_examples.domain_model.range_modulator_sequence_item import (
    RangeModulatorSequenceItem,
)
from tdwii_plus_examples.domain_model.range_shifter_sequence_item import (
    RangeShifterSequenceItem,
)

# from tdwii_plus_examples.domain_model.recorded_block_sequence_item import (
#     RecordedBlockSequenceItem as RecordedPhotonBlockSequenceItem,
# )
from tdwii_plus_examples.domain_model.recorded_block_sequence_item_1 import (
    RecordedBlockSequenceItem as RecordedIonBlockSequenceItem,
)
from tdwii_plus_examples.domain_model.recorded_block_slab_sequence_item import (
    RecordedBlockSlabSequenceItem,
)
from tdwii_plus_examples.domain_model.recorded_compensator_sequence_item import (
    RecordedCompensatorSequenceItem as RecordedIonCompensatorSequence,
)

# from tdwii_plus_examples.domain_model.recorded_compensator_sequence_item_1 import (
#     RecordedCompensatorSequenceItem as RecordedPhotonCompensatorSequenceItem,
# )
from tdwii_plus_examples.domain_model.recorded_lateral_spreading_device_sequence_item import (
    RecordedLateralSpreadingDeviceSequenceItem,
)
from tdwii_plus_examples.domain_model.recorded_range_modulator_sequence_item import (
    RecordedRangeModulatorSequenceItem,
)
from tdwii_plus_examples.domain_model.recorded_range_shifter_sequence_item import (
    RecordedRangeShifterSequenceItem,
)
from tdwii_plus_examples.domain_model.recorded_snout_sequence_item import (
    RecordedSnoutSequenceItem,
)
from tdwii_plus_examples.domain_model.recorded_wedge_sequence_item import (
    RecordedWedgeSequenceItem,
)
from tdwii_plus_examples.domain_model.referenced_rt_plan_sequence_item import (
    ReferencedRTPlanSequenceItem,
)

# from tdwii_plus_examples.domain_model.referenced_rt_plan_sequence_item_4 import (
#     ReferencedRTPlanSequenceItem as Alt4ReferencedRTPlanSequenceItem,
# )
# from tdwii_plus_examples.domain_model.referenced_rt_plan_sequence_item_5 import (
#     ReferencedRTPlanSequenceItem as Alt5ReferencedRTPlanSequenceItem,
# )
from tdwii_plus_examples.domain_model.rt_ion_beams_treatment_record import (
    RtIonBeamsTreatmentRecord,
)
from tdwii_plus_examples.domain_model.rt_ion_plan import RtIonPlan
from tdwii_plus_examples.domain_model.snout_sequence_item import SnoutSequenceItem
from tdwii_plus_examples.domain_model.treatment_machine_sequence_item import (
    TreatmentMachineSequenceItem,
)
from tdwii_plus_examples.domain_model.treatment_session_ion_beam_sequence_item import (
    TreatmentSessionIonBeamSequenceItem,
)


def get_properties(cls):
    return {name: prop for name, prop in inspect.getmembers(cls, lambda x: isinstance(x, property))}


properties_not_to_copy = ["SOPInstanceUID", "SOPClassUID"]


def _create_recorded_wedge(ion_wedge: IonWedgeSequenceItem) -> RecordedWedgeSequenceItem:
    recorded_wedge = RecordedWedgeSequenceItem()
    recorded_wedge.AccessoryCode = ion_wedge.AccessoryCode
    recorded_wedge.WedgeAngle = ion_wedge.WedgeAngle
    recorded_wedge.WedgeID = ion_wedge.WedgeID
    recorded_wedge.WedgeNumber = ion_wedge.WedgeNumber
    recorded_wedge.WedgeOrientation = ion_wedge.WedgeOrientation
    recorded_wedge.WedgeType = ion_wedge.WedgeType
    # no place to record ion_wedge.IsocenterToWedgeTrayDistance
    return recorded_wedge


def _create_recorded_snout(snout: SnoutSequenceItem) -> RecordedSnoutSequenceItem:
    recorded_snout = RecordedSnoutSequenceItem()
    recorded_snout.AccessoryCode = snout.AccessoryCode
    recorded_snout.SnoutID = snout.SnoutID
    return recorded_snout


def _create_recorded_range_shifter(range_shifter: RangeShifterSequenceItem) -> RecordedRangeShifterSequenceItem:
    recorded_range_shifter = RecordedRangeShifterSequenceItem()
    recorded_range_shifter.AccessoryCode = range_shifter.AccessoryCode
    recorded_range_shifter.RangeShifterID = range_shifter.RangeShifterID
    recorded_range_shifter.ReferencedRangeShifterNumber = range_shifter.RangeShifterNumber
    return recorded_range_shifter


def _create_recorded_range_modulator(range_modulator: RangeModulatorSequenceItem) -> RecordedRangeModulatorSequenceItem:
    recorded_range_modulator = RecordedRangeModulatorSequenceItem()
    recorded_range_modulator.AccessoryCode = range_modulator.AccessoryCode
    recorded_range_modulator.BeamCurrentModulationID = range_modulator.BeamCurrentModulationID
    recorded_range_modulator.RangeModulatorID = range_modulator.RangeModulatorID
    recorded_range_modulator.RangeModulatorType = range_modulator.RangeModulatorType
    recorded_range_modulator.ReferencedRangeModulatorNumber = range_modulator.RangeModulatorNumber
    return recorded_range_modulator


def _create_recorded_compensator(ion_compensator: IonRangeCompensatorSequenceItem) -> RecordedIonCompensatorSequence:
    recorded_compensator = RecordedIonCompensatorSequence()
    recorded_compensator.AccessoryCode = ion_compensator.AccessoryCode
    recorded_compensator.CompensatorID = ion_compensator.CompensatorID
    recorded_compensator.ReferencedCompensatorNumber = ion_compensator.CompensatorNumber
    return recorded_compensator


def _create_recorded_block_slab(block_slab: IonBlockSlabSequenceItem) -> RecordedBlockSlabSequenceItem:
    recorded_block_slab = RecordedBlockSlabSequenceItem()
    recorded_block_slab.AccessoryCode = block_slab.AccessoryCode
    recorded_block_slab.BlockSlabNumber = block_slab.BlockSlabNumber
    return recorded_block_slab


def _create_recorded_block(ion_block: IonBlockSequenceItem) -> RecordedIonBlockSequenceItem:
    recorded_block = RecordedIonBlockSequenceItem()
    recorded_block.AccessoryCode = ion_block.AccessoryCode
    recorded_block.BlockName = ion_block.BlockName
    recorded_block.ReferencedBlockNumber = ion_block.BlockNumber
    recorded_block.BlockTrayID = ion_block.BlockTrayID
    recorded_block.NumberOfBlockSlabItems = ion_block.NumberOfBlockSlabItems
    if recorded_block.NumberOfBlockSlabItems > 0:
        for block_slab in ion_block.BlockSlabSequence:
            recorded_block.add_RecordedBlockSlab(_create_recorded_block_slab(block_slab))
    return recorded_block


def _create_recorded_lateral_spreading_device(
    lateral_spreading_device: LateralSpreadingDeviceSequenceItem,
) -> RecordedLateralSpreadingDeviceSequenceItem:
    recorded_lateral_spreading_device = RecordedLateralSpreadingDeviceSequenceItem()
    recorded_lateral_spreading_device.AccessoryCode = lateral_spreading_device.AccessoryCode
    recorded_lateral_spreading_device.LateralSpreadingDeviceID = lateral_spreading_device.LateralSpreadingDeviceID
    recorded_lateral_spreading_device.ReferencedLateralSpreadingDeviceNumber = (
        lateral_spreading_device.LateralSpreadingDeviceNumber
    )
    return recorded_lateral_spreading_device


def DICOMDateAndTime(dt: datetime = None) -> Tuple[str, str]:
    # Set creation date/time
    if dt is None:
        dt = datetime.now()
    dicom_date = dt.strftime("%Y%m%d")
    dicom_time = dt.strftime("%H%M%S")  # long format with seconds
    return dicom_date, dicom_time


def beam_meterset_scaling_factors(plan: RtIonPlan) -> Dict[int, Decimal]:
    beam_meterset_dict = {}
    beam_meterset_scaling_dict = {}
    for ref_beam in plan.FractionGroupSequence[0].ReferencedBeamSequence:
        beam_number = ref_beam.ReferencedBeamNumber
        beam_meterset = ref_beam.BeamMeterset
        beam_meterset_dict[beam_number] = beam_meterset

    for beam in plan.IonBeamSequence:
        final_cumulative_meterset_weight = beam.FinalCumulativeMetersetWeight
        beam_number = beam.BeamNumber
        beam_meterset_scaling_dict[beam_number] = beam_meterset_dict[beam_number] / final_cumulative_meterset_weight
    return beam_meterset_scaling_dict


def populate_rt_ion_beams_treatment_record(
    referenced_rt_plan: RtIonPlan, current_fraction_number: int = 1
) -> RtIonBeamsTreatmentRecord:
    """_summary_

    Args:
        referenced_rt_plan (RtIonPlan): The RT Ion Plan that the treatment record is based on

    Returns:
        RtIonBeamsTreatmentRecord: A perfectly delivered treatment session that matches the plan referenced
    """
    my_tx_record: RtIonBeamsTreatmentRecord = RtIonBeamsTreatmentRecord()
    my_tx_record.SOPClassUID = RTIonBeamsTreatmentRecordStorage
    my_tx_record.SOPInstanceUID = generate_uid()
    my_tx_record.SeriesInstanceUID = generate_uid()
    dicom_date, dicom_time = DICOMDateAndTime()
    my_tx_record.SeriesDate = dicom_date
    my_tx_record.SeriesTime = dicom_time

    my_tx_record.InstanceCreationDate = dicom_date
    my_tx_record.InstanceCreationTime = dicom_time
    my_tx_record.TreatmentDate = dicom_date
    my_tx_record.TreatmentTime = dicom_time
    ref_plan_seq_item = ReferencedRTPlanSequenceItem()
    ref_plan_seq_item.ReferencedSOPClassUID = referenced_rt_plan.SOPClassUID
    ref_plan_seq_item.ReferencedSOPInstanceUID = referenced_rt_plan.SOPInstanceUID

    my_tx_record.add_ReferencedRTPlan(ref_plan_seq_item)

    treatment_machine = TreatmentMachineSequenceItem()
    treatment_machine.Manufacturer = "tdwii_plus_examples"
    treatment_machine.ManufacturerModelName = "ions r us"
    treatment_machine.DeviceSerialNumber = "1"
    treatment_machine.InstitutionAddress = referenced_rt_plan.InstitutionAddress
    treatment_machine.InstitutionName = referenced_rt_plan.InstitutionName
    treatment_machine.InstitutionalDepartmentName = referenced_rt_plan.InstitutionalDepartmentName
    my_tx_record.SyntheticData = "YES"
    my_tx_record.add_TreatmentMachine(treatment_machine)

    my_tx_record.SoftwareVersions = ["tdwii_plus_examples", "0.1"]
    my_tx_record.Manufacturer = "tdwii_plus_examples"
    my_tx_record.ManufacturerModelName = "PerfectTreatmentDelivery4U"
    python_date_time_now = datetime.now()
    inter_beam_time_duration = timedelta(seconds=300)
    cp_time_duration = timedelta(seconds=3)
    beam_meterset_scaling_dict = beam_meterset_scaling_factors(plan=referenced_rt_plan)

    plan_property_dict = get_properties(RtIonPlan)
    plan_property_keys = plan_property_dict.keys()
    tx_record_property_dict = get_properties(RtIonBeamsTreatmentRecord)
    tx_record_property_keys = tx_record_property_dict.keys()

    logging.info("Treatment Record values copied from Plan")
    for plan_key in plan_property_keys:
        if plan_key in properties_not_to_copy or plan_key.startswith("Series") or plan_key.startswith("Instance"):
            continue
        if plan_key in tx_record_property_keys:
            value = getattr(referenced_rt_plan, plan_key)
            setattr(my_tx_record, plan_key, value)
            info_message = f"Plan {plan_key}"
            logging.info(info_message)
    beam_property_keys = get_properties(IonBeamSequenceItem).keys()
    session_beam_property_keys = get_properties(TreatmentSessionIonBeamSequenceItem).keys()
    control_point_property_keys = get_properties(IonControlPointSequenceItem).keys()
    delivery_control_point_property_keys = get_properties(IonControlPointDeliverySequenceItem).keys()
    first_cp = True
    first_beam = True
    beam_start_time = python_date_time_now
    for beam in referenced_rt_plan.IonBeamSequence:
        session_beam = TreatmentSessionIonBeamSequenceItem()
        session_beam.CurrentFractionNumber = current_fraction_number
        beam_start_time += inter_beam_time_duration
        my_tx_record.add_TreatmentSessionIonBeam(session_beam)
        beam_number = beam.BeamNumber
        meterset_scaling_factor = beam_meterset_scaling_dict[beam_number]
        session_beam.DeliveredPrimaryMeterset = beam.FinalCumulativeMetersetWeight * meterset_scaling_factor
        if beam.ApplicatorSequence is not None:
            session_beam.ApplicatorSequence = beam.ApplicatorSequence
        if beam.IonBlockSequence is not None:
            for block in beam.IonBlockSequence:
                session_beam.add_RecordedBlock(_create_recorded_block(block))
        if beam.RangeModulatorSequence is not None:
            for range_modulator in beam.RangeModulatorSequence:
                session_beam.add_RecordedRangeModulator(_create_recorded_range_modulator(range_modulator))
        if beam.RangeShifterSequence is not None:
            for range_shifter in beam.RangeShifterSequence:
                session_beam.add_RecordedRangeShifter(_create_recorded_range_shifter(range_shifter))
        if beam.IonRangeCompensatorSequence is not None:
            for compensator in beam.IonRangeCompensatorSequence:
                session_beam.add_RecordedCompensator(_create_recorded_compensator(compensator))
        if beam.IonWedgeSequence is not None:
            for ion_wedge in beam.IonWedgeSequence:
                session_beam.add_RecordedWedge(_create_recorded_wedge(ion_wedge))
        if beam.SnoutSequence is not None:
            for snout in beam.SnoutSequence:
                session_beam.add_RecordedSnout(_create_recorded_snout(snout))
        if beam.LateralSpreadingDeviceSequence is not None:
            for lateral in beam.LateralSpreadingDeviceSequence:
                session_beam.add_RecordedLateralSpreadingDevice(_create_recorded_lateral_spreading_device(lateral))

        for beam_key in beam_property_keys:
            if beam_key in session_beam_property_keys:
                value = getattr(beam, beam_key)
                setattr(session_beam, beam_key, value)
                if first_beam:
                    info_message = f"Beam {beam_key}"
                    logging.info(info_message)
            else:
                referenced_beam_key = "Referenced" + beam_key
                if referenced_beam_key in session_beam_property_keys:
                    value = getattr(beam, beam_key)
                    setattr(session_beam, referenced_beam_key, value)
                    if first_beam:
                        info_message = f"Beam {beam_key} for {referenced_beam_key}"
                        logging.info(info_message)

        if first_beam:
            treatment_machine.TreatmentMachineName = beam.TreatmentMachineName
            treatment_machine.Manufacturer = beam.Manufacturer
            treatment_machine.ManufacturerModelName = beam.ManufacturerModelName
        first_beam = False

        control_point_start_time = beam_start_time
        for cp in beam.IonControlPointSequence:
            delivery_cp = IonControlPointDeliverySequenceItem()
            session_beam.add_IonControlPointDelivery(delivery_cp)
            delivery_cp.SpecifiedMeterset = cp.CumulativeMetersetWeight * meterset_scaling_factor
            delivery_cp.DeliveredMeterset = delivery_cp.SpecifiedMeterset  # perfect delivery
            if cp.ScanSpotMetersetWeights is not None:
                if isinstance(cp.ScanSpotMetersetWeights, list):
                    delivery_cp.ScanSpotMetersetsDelivered = [x * meterset_scaling_factor for x in cp.ScanSpotMetersetWeights]
                elif isinstance(cp.ScanSpotMetersetWeights, float):
                    # single value gets returned as float instead of list of float
                    delivery_cp.ScanSpotMetersetsDelivered = [meterset_scaling_factor * cp.ScanSpotMetersetWeights]

            control_point_start_time += cp_time_duration
            dicom_date, dicom_time = DICOMDateAndTime(control_point_start_time)
            delivery_cp.TreatmentControlPointDate = dicom_date
            delivery_cp.TreatmentControlPointTime = control_point_start_time
            for cp_key in control_point_property_keys:
                if cp_key in delivery_control_point_property_keys:
                    value = getattr(cp, cp_key)
                    setattr(delivery_cp, cp_key, value)
                    if first_cp:
                        info_message = f"Control Point {cp_key}"
                        logging.info(info_message)
                else:
                    referenced_cp_key = "Referenced" + cp_key
                    if referenced_cp_key in delivery_control_point_property_keys:
                        value = getattr(cp, cp_key)
                        setattr(delivery_cp, referenced_cp_key, value)
                        if first_cp:
                            info_message = f"Control Point {cp_key} for {referenced_cp_key}"
                            logging.info(info_message)

            first_cp = False

    return my_tx_record


if __name__ == "__main__":
    add_dict_entry(0x0008001C, "CS", "SyntheticData", "Synthetic Data", "1", "")
    add_dict_entry(0x00120022, "LO", "IssuerOfClinicalTrialProtocolID", "Issuer of Clinical Trial Protocol ID", "1", "")
    add_dict_entry(0x00120073, "LO", "IssuerOfClinicalTrialSeriesID", "Issuer of Clinical Trial Series ID", "1", "")
    add_dict_entry(0x00120032, "LO", "IssuerOfClinicalTrialSiteID", "Issuer of Clinical Trial Site ID", "1", "")
    add_dict_entry(0x00120041, "LO", "IssuerOfClinicalTrialSubjectID", "Issuer of Clinical Trial Subject ID", "1", "")
    add_dict_entry(
        0x00120041, "LO", "IssuerOfClinicalTrialSubjectReadingID", "Issuer of Clinical Trial Subject Reading ID", "1", ""
    )
    add_dict_entry(0x00120055, "LO", "IssuerOfClinicalTrialTimePointID", "Issuer of Clinical Trial Time Point ID", "1", "")
    add_dict_entry(
        0x00120023, "SQ", "OtherClinicalTrialProtocolIDsSequence", "Other Clinical Trial Protocol IDs Sequence", "1", ""
    )
    add_dict_entry(0x00181204, "DA", "DateOfManufacture", "Date Of Manufacture", "1", "")
    add_dict_entry(0x00181205, "DA", "DateOfInstallation", "Date Of Installation", "1", "")

    ds_plan = None
    if len(sys.argv) > 1:
        ds_plan = dcmread(sys.argv[1], force=True)
    else:
        print(f"Usage: {sys.argv[0]} RTIonPlan_file")
        sys.exit()
    my_plan: RtIonPlan = RtIonPlan(ds_plan)
    my_tx_record = populate_rt_ion_beams_treatment_record(my_plan)
    tx_record_ds = my_tx_record.to_dataset()
    tx_record_ds.ensure_file_meta()
    tx_record_ds.is_implicit_VR = False
    tx_record_ds.is_little_endian = True
    tx_record_ds.file_meta.TransferSyntaxUID = ImplicitVRLittleEndian
    record_filename = "RX_" + str(my_tx_record.SOPInstanceUID) + ".dcm"
    dcmwrite(record_filename, tx_record_ds, write_like_original=False)
    print(f"all done. wrote {record_filename}")
