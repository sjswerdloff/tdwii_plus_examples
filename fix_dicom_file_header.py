#!/usr/bin/env python
"""fixes meta info for a streamed dicom file so that other tools can read and send it
    @author: stuartswerdloff
"""
import sys

from pydicom import dcmread

if len(sys.argv) < 3:
    print(f"{sys.argv[0]} input_file_path output_file_path")
    sys.exit()

filename = sys.argv[1]
output_filename = sys.argv[2]
print(filename)
try:
    f = open(filename, "rb")
    ds = dcmread(f, force=True)

    f.close()

    ds.save_as(output_filename, write_like_original=False)
except IOError:
    print("Cannot read input file {0!s}".format(filename))
    sys.exit()
