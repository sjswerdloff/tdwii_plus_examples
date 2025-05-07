#!/usr/bin/env python
"""
A DICOM UPS Push Service Class Provider (SCU) application.

This application implements a UPS Push N-CREATE SOP Class SCU.
It uses the DIMSE N-CREATE Service to create UPS instances on a remote SCP.

Usage:
    upspushncreatescu [options] ip port path

Arguments:
    ip    IP address of called AE
    port  TCP port number of called AE
    path  DICOM file or directory containing UPS instances to create

Options:
    -h, --help               Show this help message and exit
    -aet, --ae_title         Application Entity Title (default: UPSPUSHSCU)
    -aec, --called_ae_title  Called Application Entity Title (default: ANYSCP)
    -e, --echo               Verification of DICOM connection with Called AET
    -v, --verbose            Set log level to INFO
    -d, --debug              Set log level to DEBUG
"""

import argparse
import logging
import os
import sys
from pathlib import Path

from pydicom import dcmread
from pynetdicom.apps.common import get_files

from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU


def get_contexts(fpaths, app_logger):
    """Return the valid DICOM files and their Presentation Context.

    Parameters
    ----------
    fpaths : list of str
        A list of paths to the files to try and get data from.

    Returns
    -------
    list of str, dict
        A list of paths to valid DICOM files and the {SOP Class UID :
        [Transfer Syntax UIDs]} that can be used to create the required
        presentation contexts.
    """
    good, bad = [], []
    contexts = {}
    for fpath in fpaths:
        path = os.fspath(Path(fpath).resolve())
        try:
            ds = dcmread(path)
        except Exception as e:
            bad.append((f"Bad DICOM file: {e}", path))
            continue

        try:
            sop_class = ds.SOPClassUID
            tsyntax = ds.file_meta.TransferSyntaxUID
        except Exception as e:
            bad.append((f"Unknown SOP Class or Transfer Syntax UID: {e}", path))
            continue

        tsyntaxes = contexts.setdefault(sop_class, [])
        if tsyntax not in tsyntaxes:
            tsyntaxes.append(tsyntax)

        good.append(path)

    for reason, path in bad:
        app_logger.error(f"{reason}: {path}")

    return good, contexts


def main():
    parser = argparse.ArgumentParser(description="Send a DICOM UPS Push N-CREATE request")
    parser.add_argument("ip", type=str, help="IP address or hotname of called AE")
    parser.add_argument("port", type=int, help="TCP port number of called AE")
    parser.add_argument(
        "path", metavar="path", nargs="+", help="DICOM file or directory containing UPS instances to create", type=str
    )
    parser.add_argument("-r", "--recurse", help="recursively search the given directory", action="store_true")
    parser.add_argument("-aet", "--ae_title", type=str, default="UPSPUSHSCU", help="Application Entity Title")
    parser.add_argument("-aec", "--called_ae_title", type=str, default="ANYSCP", help="Called Application Entity Title")
    parser.add_argument("-e", "--echo", action="store_true", help="Verification of DICOM connection with Called AET")
    parser.add_argument("-v", "--verbose", action="store_true", help="Set log level to INFO")
    parser.add_argument("-d", "--debug", action="store_true", help="Set log level to DEBUG")
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress all log output")

    args = parser.parse_args()

    if args.quiet:
        log_level = logging.CRITICAL
    elif args.verbose:
        log_level = logging.INFO
    elif args.debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.WARNING

    logging.basicConfig(level=log_level)
    logger = logging.getLogger("upspushncreatescu")
    logger.setLevel(log_level)

    logger.info(f"Initializing UPSPushCreateSCU instance with remote SCP {args.called_ae_title}@{args.ip}:{args.port}")
    scu = UPSPushNCreateSCU(
        logger=logger,
        calling_ae_title=args.ae_title,
        called_ip=args.ip,
        called_port=args.port,
        called_ae_title=args.called_ae_title,
    )

    # Verification requested
    if args.echo:
        print("Verification (C-ECHO) request")
        num_created_instances = scu.verify()
        if num_created_instances.status_category == "Success":
            print("Verification (C-ECHO) successful")
        else:
            print(f"Verification (C-ECHO) failed: {num_created_instances.status_description}")

    # UPS instances creation requested
    elif args.path is not None:
        valid_paths, invalid_paths = get_files(args.path, args.recurse)

        for path in invalid_paths:
            logger.error(f"Cannot access path: {path}")

        # TODO: restrict SCU to required transfer syntaxes only
        # this could be achieved by adding the required transfer syntaxes to the
        # initialization of the SCU instance and reading the required transfer syntaxes
        # from the file meta information of the DICOM files
        dicom_file_paths, contexts = get_contexts(valid_paths, logger)

        if not dicom_file_paths:
            logger.warning("No suitable DICOM files found")
            sys.exit()

        instances = []
        for dicom_file_path in dicom_file_paths:
            logger.info(f"Sending file: {dicom_file_path}")
            try:
                ds = dcmread(dicom_file_path, force=True)  # set force flag to allow raw DICOM files
                instances.append(ds)
            except Exception as e:
                logger.error(f"Failed to read DICOM file {dicom_file_path}: {e}")
                continue

        num_created_instances = scu.create_ups_instances(instances)

        if num_created_instances == len(dicom_file_paths):
            print("UPS creation successful")
        elif num_created_instances > 0:
            print("Some UPS instances creation failed")
        else:
            print("UPS creation failed")


if __name__ == "__main__":
    main()
