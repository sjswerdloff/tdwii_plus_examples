#!/usr/bin/env python
"""
A DICOM UPS Pull N-SET SCU CLI application.

This application modifies a UPS instance on a remote SCP using the N-SET DIMSE service.
"""

import argparse
import logging
import sys
from typing import Any

from pydicom import dcmread
from pydicom.uid import UID

from tdwii_plus_examples.tests.utils.generate_sop_instances import generate_ups
from tdwii_plus_examples.upspullnactionscu import UPSPullNActionSCU
from tdwii_plus_examples.upspullnsetscu import UPSPullNSetSCU
from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU


def _csv_to_tuple(val: str) -> tuple[str, ...]:
    return tuple(x.strip() for x in val.split(","))


def main():  # sourcery skip: remove-redundant-if
    parser = _build_parser()
    args = parser.parse_args()
    _check_args(args, parser)
    logger = _setup_logger(args)
    sop_instance_uid, tx_uid = _get_ups_info(args, parser, logger)

    # Create the N-SET SCU instance
    scu = UPSPullNSetSCU(
        calling_ae_title="UPSPULLSCU",
        called_ae_title=args.ae_title,
        called_ip=args.ip,
        called_port=args.port,
        logger=logger,
    )

    # Update UPS Progress Information if requested
    if args.progress:
        try:
            progress_value = int(args.progress[0])
        except ValueError:
            parser.error("--progress value must be an integer")
        progress_description = str(args.progress[1]) if len(args.progress) > 1 else None

        # Update UPS progress info
        print(f"Updating progress info: progress_value={progress_value}, progress_description={progress_description}")
        result = scu.update_progress_information(sop_instance_uid, tx_uid, progress_value, progress_description)

    elif args.start:
        result = _modify_start_info(args, scu, sop_instance_uid, tx_uid)

    elif args.end:
        print("Updating end info")
        result = scu.update_end_info(sop_instance_uid, tx_uid)

    elif args.cancel is not None:
        print(f"Updating cancel info with reason: {args.cancel}")
        result = scu.update_cancel_info(sop_instance_uid, tx_uid, args.cancel)

    elif args.output:
        # Parse each output info string into a tuple
        output_information_args = []
        output_information_args.extend(_csv_to_tuple(info_str) for info_str in args.output)
        print(f"Updating output information with: {output_information_args}")
        result = scu.update_output_information(sop_instance_uid, tx_uid, output_information_args)

    elif args.list:
        # Load the modification list from raw DICOM dataset file
        modification_list = dcmread(args.list, force=True)

        # Modify the UPS
        result = scu.modify_ups(sop_instance_uid, modification_list)

    if result.status_category == "Success":
        print("UPS modification successful.")
    else:
        print(f"UPS modification failed: {result.status_description}")


def _modify_start_info(
    args: argparse.Namespace,
    scu: "UPSPullNSetSCU",
    sop_instance_uid: str,
    tx_uid: str,
) -> "UPSPullNSetSCU.PrimitiveResult":
    station_name = args.start[0]
    workitem_code = args.start[1]
    human_performer = None
    human_performer_name = None

    # Convert comma-separated strings to to tuple
    station_name = _csv_to_tuple(station_name)
    workitem_code = _csv_to_tuple(workitem_code)

    if len(args.start) > 2:
        val = args.start[2]
        if _is_code_seq_arg(val):
            human_performer = _csv_to_tuple(val)
        else:
            human_performer_name = val

    # Update UPS start info
    print(
        "Updating start info: "
        f"station_name={station_name}, workitem_code={workitem_code}, "
        f"human_performer={human_performer}, human_performer_name={human_performer_name}"
    )
    return scu.update_start_info(
        sop_instance_uid,
        tx_uid,
        station_name=station_name,
        workitem_code=workitem_code,
        human_performer=human_performer,
        human_performer_name=human_performer_name,
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Modify a DICOM UPS instance using N-SET", formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("ip", type=str, help="IP address of called AE")
    parser.add_argument("port", type=int, help="TCP port number of called AE")
    parser.add_argument("--ae_title", type=str, help="Called Application Entity Title")
    parser.add_argument("--create", action="store_true", help="Create a new UPS instance before modifying")
    parser.add_argument("--claim", action="store_true", help="Claim the UPS before modifying")
    parser.add_argument("--sop_instance_uid", type=str, default=None, help="SOP Instance UID of the UPS to modify")
    parser.add_argument("--transaction_uid", type=str, default=None, help="Transaction UID to use (if claiming)")
    parser.add_argument(
        "--progress",
        nargs="+",
        type=str,
        metavar=("PROGRESS", "DESCRIPTION"),
        help="Procedure Step Progress value (and optionally Progress Description)",
    )
    parser.add_argument(
        "--start",
        nargs="+",
        type=str,
        metavar=("STATION_NAME", "OTHERS"),
        help=(
            "Update UPS start info: station_name workitem_code [human_performer|human_performer_name].\n"
            "Provide 2 code sequence items, each as a comma-separated string.\n"
            "Optionally provide either a code sequence (3 comma-separated components) or a Person Name string (no spaces).\n"
            'Example: --start "GTR1, TMS, Gantry 1" "121726, DCM, RT Treatment with Internal Verification" "Alice^Smith"'
        ),
    )
    parser.add_argument("--end", action="store_true", help="Update UPS end info.")
    parser.add_argument(
        "--cancel", type=str, metavar="REASON", help="Update UPS cancel info. Provide a reason for cancellation (required)."
    )
    parser.add_argument(
        "--output",
        nargs="+",
        metavar="OUTPUT_INFO",
        help=(
            "Update UPS output information.\n"
            "Provide a comma-separated string with the following information:\n"
            "retrieve_ae_title, study_instance_uid, series_instance_uid, sop_class_uid, sop_instance_uid\n"
            'Example: --output "<AET>, <StudyInstanceUID>, <SeriesInstanceUID>, <SOPClassUID>, <SOPInstanceUID>"'
        ),
    )
    parser.add_argument(
        "--list",
        type=str,
        help="Path to raw DICOM dataset file containing Modification List",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Set log level to INFO")
    parser.add_argument("-d", "--debug", action="store_true", help="Set log level to DEBUG")
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress all log output")
    return parser


def _check_args(
    args: argparse.Namespace,
    parser: argparse.ArgumentParser,
):
    # Argument checks for progress
    if args.progress and len(args.progress) > 2:
        parser.error("--progress takes at most 2 arguments: value [description]")

    # Argument checks for start
    if args.start:
        if len(args.start) < 2 or len(args.start) > 3:
            parser.error(
                "--start requires at least 2 and at most 3 arguments: "
                "station_name workitem_code [human_performer|human_performer_name]. "
            )

        # Validate station_name and workitem_code
        for idx, label in enumerate(("station_name", "workitem_code")):
            if not _is_code_seq_arg(args.start[idx]):
                parser.error(f"--start: {label} must be a string of 3 comma-separated components")

        # Validate human_performer or human_performer_name if present
        if len(args.start) > 2:
            val = args.start[2]
            if not isinstance(val, str):
                parser.error("--start: third argument must be a string (either a code sequence item or a Person Name)")
            is_code_seq = _is_code_seq_arg(val)
            is_valid_pn = "," not in val and " " not in val and val != ""
            if not (is_code_seq or is_valid_pn):
                parser.error(
                    "--start: third argument must be either a string of 3 comma-separated components (code sequence)"
                    " or a Person Name (PN) string without spaces"
                )

    # Argument checks for output
    if args.output:
        if len(args.output) < 1:
            parser.error("--output requires at least one string with 5 comma-separated values")
        for info_str in args.output:
            if not _is_csv(info_str, 5):
                parser.error("--output: each OUTPUT_INFO must be a string with 5 comma-separated values: ")


def _get_ups_info(
    args: argparse.Namespace,
    parser: argparse.ArgumentParser,
    logger: logging.Logger,
) -> tuple[str, str]:
    """
    Prepare and validate all required context for UPS modification:
    - Handles creation and claiming of UPS if requested.
    - Validates and returns sop_instance_uid and tx_uid.
    - Performs argument checks for progress and start options.
    """
    # Optionally create a new UPS instance
    if args.create:
        sop_instance_uid = _ncreate_sample_ups(args, logger)
    else:
        if not args.sop_instance_uid:
            parser.error("You must provide --sop_instance_uid if not creating a new UPS.")
        sop_instance_uid = args.sop_instance_uid

    # Optionally claim the UPS
    if args.claim:
        tx_uid = _claim_ups(args, sop_instance_uid, logger)
        if not tx_uid:
            parser.error("Failed to claim UPS instance.")
        print(f"Claimed UPS instance with Transaction UID: {tx_uid}")
    else:
        tx_uid = args.transaction_uid
        if not tx_uid:
            parser.error("You must provide --transaction_uid if not claiming the UPS.")

    return sop_instance_uid, tx_uid


def _is_code_seq_arg(val: Any) -> bool:
    return _is_csv(val, 3)


def _is_csv(val: Any, n: int) -> bool:
    """Return True if val is a string with n comma-separated components."""
    if isinstance(val, str):
        parts = [x.strip() for x in val.split(",")]
        return len(parts) == n
    return False


def _setup_logger(args: argparse.Namespace) -> logging.Logger:
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
    return logger


def _ncreate_sample_ups(args: argparse.Namespace, logger: logging.Logger) -> str:
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
        print("Failed to create UPS instance in SCP.")
        sys.exit(1)
    result = ups_instance.SOPInstanceUID
    print(f"Created UPS instance in SCP: {result}")
    return result


def _claim_ups(
    args: argparse.Namespace,
    sop_instance_uid: str,
    logger: logging.Logger,
) -> str | UID:
    change_state_scu = UPSPullNActionSCU(
        calling_ae_title="UPSPULL",
        called_ae_title=args.ae_title,
        called_ip=args.ip,
        called_port=args.port,
        logger=logger,
    )
    return change_state_scu.claim_ups(sop_instance_uid)


if __name__ == "__main__":
    main()
