#!/usr/bin/env python
"""
A CLI tool to generate DICOM UPS modification list files for the upsmodify CLI application.

Generates DICOM datasets for Unified Procedure Step (UPS) N-SET requests, such as progress updates,
and saves them as raw DICOM datasets. Easily extensible for other UPS modification types.
"""

import argparse
import sys

from tdwii_plus_examples.generate_modification_list import generate_progress_update, save_modification_list


def main():
    parser = argparse.ArgumentParser(description="Generate a DICOM modification list file for N-SET.")
    parser.add_argument("sop_instance_uid", type=str, help="SOP Instance UID")
    parser.add_argument("transaction_uid", type=str, help="Transaction UID")
    parser.add_argument("output_file", type=str, help="Output DICOM file path")

    subparsers = parser.add_subparsers(dest="update_type", required=True, help="Type of update to generate")

    # Progress update
    progress_parser = subparsers.add_parser("progress", help="Generate a progress update modification list")
    progress_parser.add_argument("progress", type=int, help="Progress value (integer)")
    progress_parser.add_argument("--description", type=str, help="Progress description (optional)")

    # TODO: Add more subparsers for other update types here

    args = parser.parse_args()

    if args.update_type == "progress":
        ds = generate_progress_update(args.sop_instance_uid, args.transaction_uid, args.progress, args.description)
    else:
        print(f"Unknown update type: {args.update_type}")
        sys.exit(1)

    save_modification_list(ds, args.output_file)

    print(f"Saved modification list dataset to {args.output_file}")


if __name__ == "__main__":
    main()
