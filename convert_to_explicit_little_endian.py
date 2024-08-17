#!/usr/bin/env python
""" if the data contains private elements that aren't known to pydicom,
    and the file is transmitted to qrscp or some other system that doesn't handle unknown privates
    when using *implicit* little endian,
    then this conversion is needed to avoid data loss later on.
    @author: stuartswerdloff
"""
import sys
from pathlib import Path

from pydicom import dcmread
from pydicom.uid import ExplicitVRLittleEndian


def convert(filename: str | Path, output_filename: str | Path):
    try:
        f = open(filename, "rb")
        ds = dcmread(f, force=True)

        f.close()
        ds.is_little_endian = True

        # if the data contains private elements that aren't known to pydicom,
        # and the file is transmitted to qrscp or some other system that doesn't handle unknown privates
        # when using *implicit* little endian,
        # then this is needed to avoid data loss later on.
        ds.is_implicit_VR = False

        ds.ensure_file_meta()
        ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
        ds.fix_meta_info()
        ds.save_as(output_filename, write_like_original=False)
    except IOError:
        print("Cannot read input file {0!s}".format(filename))
        raise


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"{sys.argv[0]} input_file_path output_file_path")
        sys.exit()

    filename = sys.argv[1]
    output_filename = sys.argv[2]
    print(filename)
    try:
        convert(filename=filename, output_filename=output_filename)
    except IOError:
        print("Cannot read input file {0!s}".format(filename))
        sys.exit()
