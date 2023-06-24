#!/usr/bin/env python
"""rename any UPS C-FIND-RSP response files, which are UPS Push instances to use their SOP Instance UID"""

import os
import sys

from pydicom import Dataset, dcmread, dcmwrite


def main(args):
    if args is None:
        args = sys.argv
    remove_old = False
    ds = dcmread(args[1], force=True)
    if ds is not None:
        sopInstanceUID = str(ds.SOPInstanceUID)
        filename = f"UPS_{sopInstanceUID}.dcm"
        dcmwrite(filename, ds)
        if remove_old:
            if os.path.exists(filename):
                os.remove(args[1])


if __name__ == "__main__":
    main(sys.argv)
