#!/usr/bin/env python
"""
A DICOM UPS Pull N-SET SCU CLI application.

This application modifies a UPS instance on a remote SCP using the N-SET DIMSE service.
"""

import argparse
import logging
import sys

from pydicom import dcmread

from tdwii_plus_examples.tests.utils.generate_sop_instances import generate_ups
from tdwii_plus_examples.upspullnactionscu import UPSPullNActionSCU
from tdwii_plus_examples.upspullnsetscu import UPSPullNSetSCU
from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU


def _parse_code_seq_item(val):
    return tuple(x.strip() for x in val.split(",")) if "," in val else val


def main():  # sourcery skip: remove-redundant-if
    parser = _build_parser()
    args = parser.parse_args()
    logger = _setup_logger(args)
    sop_instance_uid, tx_uid = _prepare_modification_context(args, parser, logger)

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

    # Update UPS Performed Start Information if requested
    elif args.start:
        result = _modify_start_info(args, scu, sop_instance_uid, tx_uid)

    # Update UPS end information if requested
    elif args.end:
        print("Updating end info")
        result = scu.update_end_info(sop_instance_uid, tx_uid)

    # Update UPS cancel information if requested
    elif args.cancel is not None:
        print(f"Updating cancel info with reason: {args.cancel}")
        result = scu.update_cancel_info(sop_instance_uid, tx_uid, args.cancel)

    # Update UPS output information if requested
    elif args.output:
        # Parse each output info string into a tuple
        output_information_args = []
        for info_str in args.output:
            parts = [x.strip() for x in info_str.split(",")]
            output_information_args.append(tuple(parts))
        print(f"Updating output information with: {output_information_args}")
        result = scu.update_output_information(sop_instance_uid, tx_uid, output_information_args)

    # Update UPS with provided Modifition List if no specific update requested
    elif args.list:
        # Load the modification list from raw DICOM dataset file
        modification_list = dcmread(args.list, force=True)

        # Modify the UPS
        result = scu.modify_ups(sop_instance_uid, modification_list)

    if result.status_category == "Success":
        print("UPS modification successful.")
    else:
        print(f"UPS modification failed: {result.status_description}")


# TODO Rename this here and in `main`
def _modify_start_info(args, scu, sop_instance_uid, tx_uid):
    station_name = args.start[0]
    workitem_code = args.start[1]
    human_performer = args.start[2] if len(args.start) > 2 else None
    human_performer_name = args.start[3] if len(args.start) > 3 else None

    # Convert to tuple if comma-separated (e.g. "CODE,DESIGNATOR,MEANING")
    station_name = _parse_code_seq_item(station_name)
    workitem_code = _parse_code_seq_item(workitem_code)
    human_performer = _parse_code_seq_item(human_performer) if human_performer else None

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


def _build_parser():
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
            "Update UPS start info: station_name workitem_code [human_performer] [human_performer_name].\n"
            'Example: --start "GTR1, TMS, Gantry 1" "121726, DCM, RT Treatment with Internal Verification"'
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
            "Provide 1 or more output info items, each as a comma-separated string:\n"
            "retrieve_ae_title,study_instance_uid,series_instance_uid,sop_class_uid,sop_instance_uid\n"
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


def _prepare_modification_context(args, parser, logger):
    """
    Prepare and validate all required context for UPS modification:
    - Handles creation and claiming of UPS if requested.
    - Validates and returns sop_instance_uid and tx_uid.
    - Performs argument checks for progress and start options.
    """
    # Optionally create a new UPS instance
    if args.create:
        sop_instance_uid = _create_sample_ups(args, logger)
    else:
        if not args.sop_instance_uid:
            print("You must provide --sop_instance_uid if not creating a new UPS.")
            sys.exit(1)
        sop_instance_uid = args.sop_instance_uid

    # Optionally claim the UPS
    if args.claim:
        tx_uid = _claim_ups(args, sop_instance_uid, logger)
        if not tx_uid:
            print("Failed to claim UPS instance.")
            sys.exit(1)
        print(f"Claimed UPS instance with Transaction UID: {tx_uid}")
    else:
        tx_uid = args.transaction_uid
        if not tx_uid:
            print("You must provide --transaction_uid if not claiming the UPS.")
            sys.exit(1)

    # Argument checks for progress
    if args.progress and len(args.progress) > 2:
        parser.error("--progress takes at most 2 arguments: value [description]")

    # Argument checks for start
    if args.start:
        if not (len(args.start) >= 2 and len(args.start) <= 4):
            parser.error(
                "--start requires at least 2 and at most 4 arguments: "
                "station_name workitem_code [human_performer] [human_performer_name]"
            )

        # Only checks, no assignments
        if not _is_code_seq_arg(args.start[0]):
            parser.error("--start: station_name must be a tuple of 3 strings or a pydicom.Dataset")
        if not _is_code_seq_arg(args.start[1]):
            parser.error("--start: workitem_code must be a tuple of 3 strings or a pydicom.Dataset")
        if len(args.start) > 2:
            if args.start[2] is not None and not _is_code_seq_arg(args.start[2]):
                parser.error("--start: human_performer must be a tuple of 3 strings or a pydicom.Dataset")
        if len(args.start) > 3:
            if args.start[3] is not None and not isinstance(args.start[3], str):
                parser.error("--start: human_performer_name must be a string if provided")

    # Argument checks for output
    if args.output:
        if len(args.output) < 1:
            parser.error("--output requires at least one output info item")
        for info_str in args.output:
            parts = [x.strip() for x in info_str.split(",")]
            if len(parts) != 5:
                parser.error(
                    "--output: each OUTPUT_INFO must have 5 comma-separated values: "
                    "retrieve_ae_title,study_instance_uid,series_instance_uid,sop_class_uid,sop_instance_uid"
                )

    return sop_instance_uid, tx_uid


def _is_tuple_of_3(val):
    return isinstance(val, tuple) and len(val) == 3 and all(isinstance(x, str) for x in val)


def _is_code_seq_arg(val):
    from pydicom.dataset import Dataset

    if isinstance(val, Dataset):
        return True
    if _is_tuple_of_3(val):
        return True
    return isinstance(val, str) and val.count(",") == 2


def _setup_logger(args):
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


def _create_sample_ups(args, logger):
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
    result = ups_instance.SOPInstanceUID
    print(f"Created UPS instance: {result}")
    return result


def _claim_ups(args, sop_instance_uid, logger):
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
