#!/usr/bin/env python
"""
A DICOM UPS Pull N-SET SCU CLI application.

This application modifies a UPS instance on a remote SCP using the N-SET DIMSE service.
"""

import argparse
import logging
import sys

from pydicom import Dataset
from pynetdicom.sop_class import UnifiedProcedureStepPush

from tdwii_plus_examples.tests.utils.generate_sop_instances import generate_ups
from tdwii_plus_examples.upspullnactionscu import UPSPullNActionSCU
from tdwii_plus_examples.upspullnsetscu import UPSPullNSetSCU
from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU


def main():
    parser = argparse.ArgumentParser(description="Modify a DICOM UPS instance using N-SET")
    parser.add_argument("ip", type=str, help="IP address of called AE")
    parser.add_argument("port", type=int, help="TCP port number of called AE")
    parser.add_argument("ae_title", type=str, help="Called Application Entity Title")
    parser.add_argument("--create", action="store_true", help="Create a new UPS instance before modifying")
    parser.add_argument("--claim", action="store_true", help="Claim the UPS before modifying")
    parser.add_argument("--sop_instance_uid", type=str, default=None, help="SOP Instance UID of the UPS to modify")
    parser.add_argument("--transaction_uid", type=str, default=None, help="Transaction UID to use (if claiming)")
    parser.add_argument("--progress", type=str, default="10", help="ProcedureStepProgress value")
    parser.add_argument("--description", type=str, default="Started", help="ProcedureStepProgressDescription value")
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
    logger = logging.getLogger("upspullnsetscu")
    logger.setLevel(log_level)

    # Optionally create a new UPS instance
    if args.create:
        ups_instance = generate_ups()
        push_scu = UPSPushNCreateSCU(
            calling_ae_title="UPSPUSH",
            called_ae_title=args.ae_title,
            called_ip=args.ip,
            called_port=args.port,
            logger=logger,
        )
        num_created_instances = push_scu.create_ups_instances([ups_instance])
        if num_created_instances != 1:
            print("Failed to create UPS instance.")
            sys.exit(1)
        sop_instance_uid = ups_instance.SOPInstanceUID
        print(f"Created UPS instance: {sop_instance_uid}")
    else:
        if not args.sop_instance_uid:
            print("You must provide --sop_instance_uid if not creating a new UPS.")
            sys.exit(1)
        sop_instance_uid = args.sop_instance_uid

    # Optionally claim the UPS
    if args.claim:
        change_state_scu = UPSPullNActionSCU(
            calling_ae_title="UPSPULL",
            called_ae_title=args.ae_title,
            called_ip=args.ip,
            called_port=args.port,
            logger=logger,
        )
        tx_uid = change_state_scu.claim_ups(sop_instance_uid)
        if not tx_uid:
            print("Failed to claim UPS instance.")
            sys.exit(1)
        print(f"Claimed UPS instance with Transaction UID: {tx_uid}")
    else:
        tx_uid = args.transaction_uid
        if not tx_uid:
            print("You must provide --transaction_uid if not claiming the UPS.")
            sys.exit(1)

    # Build the modification list dataset
    modification_list = Dataset()
    modification_list.AffectedSOPInstanceUID = sop_instance_uid
    modification_list.AffectedSOPClassUID = UnifiedProcedureStepPush
    modification_list.TransactionUID = tx_uid
    sequence_item = Dataset()
    sequence_item.ProcedureStepProgress = args.progress
    sequence_item.ProcedureStepProgressDescription = args.description
    modification_list.ProcedureStepProgressInformationSequence = [sequence_item]

    # Modify the UPS
    scu = UPSPullNSetSCU(
        calling_ae_title="UPSPULLSCU",
        called_ae_title=args.ae_title,
        called_ip=args.ip,
        called_port=args.port,
        logger=logger,
    )
    result = scu.modify_ups(sop_instance_uid, modification_list)
    if result.status_category == "Success":
        print("UPS modification successful.")
    else:
        print(f"UPS modification failed: {result.status_description}")


if __name__ == "__main__":
    main()
