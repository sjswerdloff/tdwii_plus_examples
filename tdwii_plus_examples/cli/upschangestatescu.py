#!/usr/bin/env python
"""
A DICOM UPS Pull Service Class User (SCU) application.

This application implements a UPS Pull N-ACTION - Change UPS State SOP Class SCU.
It uses the DIMSE N-ACTION Service to change the state of UPS instances on a remote SCP.

Usage:
    upschangestatescu [options] ip port ups_uid state [transaction_uid]

Arguments:
    ip              IP address of called AE
    port            TCP port number of called AE
    ups_uid         SOP Instance UID of the UPS instance
    state           Requested procedure step state ("IN PROGRESS", "CANCELED", or "COMPLETED")
    transaction_uid Transaction UID of the UPS (required if state is "CANCELED" or "COMPLETED")

Options:
    -h, --help               Show this help message and exit
    -aet, --ae_title         Application Entity Title (default: UPSPULLSCU)
    -aec, --called_ae_title  Called Application Entity Title (default: ANYSCP)
    -e, --echo               Verification of DICOM connection with Called AET
    -v, --verbose            Set log level to INFO
    -d, --debug              Set log level to DEBUG
    -q, --quiet              Suppress all log output
"""

import argparse
import logging

from tdwii_plus_examples.upspullnactionscu import UPSPullNActionSCU


def main():
    parser = argparse.ArgumentParser(description="Send a DICOM UPS Push N-CREATE request")
    parser.add_argument("ip", type=str, help="IP address or hotname of called AE")
    parser.add_argument("port", type=int, help="TCP port number of called AE")
    parser.add_argument("ups_uid", help="SOP Instance UID of the UPS", type=str)
    parser.add_argument(
        "state",
        nargs="?",
        choices=["IN PROGRESS", "CANCELED", "COMPLETED"],
        default="IN PROGRESS",
        help='Requested procedure step state (default: "IN PROGRESS")',
    )
    parser.add_argument(
        "transaction_uid",
        nargs="?",
        type=str,
        default=None,
        help="Transaction UID of the UPS (required for CANCELED or COMPLETED)",
    )

    parser.add_argument("-aet", "--ae_title", type=str, default="UPSPULLSCU", help="Application Entity Title")
    parser.add_argument("-aec", "--called_ae_title", type=str, default="ANYSCP", help="Called Application Entity Title")
    parser.add_argument("-e", "--echo", action="store_true", help="Verification of DICOM connection with Called AET")
    parser.add_argument("-v", "--verbose", action="store_true", help="Set log level to INFO")
    parser.add_argument("-d", "--debug", action="store_true", help="Set log level to DEBUG")
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress all log output")

    args = parser.parse_args()

    # Argument consistency checks
    if not args.echo and not args.ups_uid:
        parser.error("Either -e/--echo or a ups_uid must be provided")
    if args.echo and args.ups_uid:
        print("Warning: ups_uid argument is ignored when using -e/--echo option")
    if args.state == "IN PROGRESS" and args.transaction_uid:
        parser.error("transaction_uid should not be provided when state is IN PROGRESS")
    if args.state in ("CANCELED", "COMPLETED") and not args.transaction_uid:
        parser.error("transaction_uid argument is required when state is CANCELED or COMPLETED")

    if args.quiet:
        log_level = logging.CRITICAL
    elif args.verbose:
        log_level = logging.INFO
    elif args.debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.WARNING

    logging.basicConfig(level=log_level)
    logger = logging.getLogger("upspullnactionscu")
    logger.setLevel(log_level)

    logger.info(f"Initializing UPSPullNActionSCU instance with remote SCP {args.called_ae_title}@{args.ip}:{args.port}")
    scu = UPSPullNActionSCU(
        logger=logger,
        calling_ae_title=args.ae_title,
        called_ip=args.ip,
        called_port=args.port,
        called_ae_title=args.called_ae_title,
    )

    # Verification requested
    if args.echo:
        print("Verification (C-ECHO) request")
        result = scu.verify()
        if result.status_category == "Success":
            print("Verification (C-ECHO) successful")
        else:
            print(f"Verification (C-ECHO) failed: {result.status_description}")

    # UPS instances state change requested
    elif args.ups_uid is not None:
        ups_instance_uid = args.ups_uid
        if args.state == "IN PROGRESS":
            if args.transaction_uid:
                parser.error("transaction_uid should not be provided when state is IN PROGRESS")
            result = scu.claim_ups(ups_instance_uid)
        elif args.state in ("CANCELED", "COMPLETED"):
            if not args.transaction_uid:
                parser.error("transaction_uid argument is required when state is CANCELED or COMPLETED")
            if args.state == "CANCELED":
                result = scu.cancel_ups(ups_instance_uid, args.transaction_uid)
            else:
                result = scu.complete_ups(ups_instance_uid, args.transaction_uid)
        else:
            parser.error(f"Unknown state: {args.state}")

        if result:
            print(f"Change UPS State to {args.state} successful")
        else:
            print("Change UPS State failed")


if __name__ == "__main__":
    main()
