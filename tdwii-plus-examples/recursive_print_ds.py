#!/usr/bin/env python

import sys

from pydicom import dataset, dcmread
from pydicom.dataelem import DataElement
from pydicom.tag import Tag


def print_ds(ds, indent_level=0):
    indent_string = ""
    for i in range(indent_level):
        indent_string += ">"
    for elem in ds:
        print(indent_string, elem)
        if elem.VR == "SQ":
            seq_index = 0
            for seq_item in elem.value:
                seq_index += 1
                print(indent_string, "--- item #", seq_index)
                print_ds(seq_item, indent_level + 1)


def _print_seq_only(ds, indent_level=0):
    indent_string = ""
    for i in range(indent_level):
        indent_string += ">"
    seq_only_list = [x for x in ds if (x.VR == "SQ")]
    for seq in seq_only_list:
        print(indent_string, seq.name, seq.tag)
        for seq_item in seq.value:
            _print_seq_only(seq_item, indent_level + 1)


def main(args):
    if args is None:
        args = sys.argv
    ds = dcmread(args[1], force=True)
    print_ds(ds)


if __name__ == "__main__":
    main(sys.argv)
