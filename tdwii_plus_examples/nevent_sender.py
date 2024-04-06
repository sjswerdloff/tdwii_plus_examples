#!/usr/bin/env python
"""nevent_sender

Used for sending events to AE's who subscribes for UPS Events
Currently at the toy level of functionality:
Sends a series of Procedure Step State change notifications
"""

import argparse
import os
import sys
from configparser import ConfigParser
from pathlib import Path
from typing import Optional, Tuple

from pydicom import Dataset, dcmread
from pydicom.errors import InvalidDicomError
from pydicom.uid import UID
from pynetdicom import AE, Association, UnifiedProcedurePresentationContexts
from pynetdicom._globals import DEFAULT_MAX_LENGTH
from pynetdicom.apps.common import setup_logging
from pynetdicom.sop_class import UnifiedProcedureStepPush

# Maybe add these back in as imports as part of generalizing this example
# UnifiedProcedureStepWatch,
# UPSFilteredGlobalSubscriptionInstance,
# UPSGlobalSubscriptionInstance,


__version__ = "0.1.0"


def send_nevent(
    assoc: Association,
    class_uid: UID,
    instance_uid: UID,
    event_type=1,
    event_info=None,
) -> Tuple[Dataset, Optional[Dataset]]:
    """Send an N-EVENT request via `assoc`

    Parameters
    ----------
    assoc : association.Association
        The association sending the request.
    class_uid : pydicom.uid.UID
        The *Requested SOP Class UID* to use.
    instance_uid: pydicom.uid.UID
        The *Requested SOP Instance UID* to use.
    event_type : int, optional
        The *Event Type ID* to use.  default 1, UPS State Report
    event_info : None or pydicom.dataset.Dataset, optional
        The *Event Information* to use.
    """
    return assoc.send_n_event_report(event_info, event_type, class_uid, instance_uid)


def send_ups_state_report(
    assoc: Association,
    instance_uid: UID,
    step_state: str,
    input_readiness_state: str = "READY",
    reason_for_cancellation: str = None,
    discontinuation_reason_code_seq: Dataset = None,
):
    event_info = Dataset()
    event_info.ProcedureStepState = step_state

    event_info.InputReadinessState = input_readiness_state
    if reason_for_cancellation:
        event_info.ReasonForCancellation = reason_for_cancellation
    if discontinuation_reason_code_seq:
        event_info.ProcedureStepDiscontinuationReasonCodeSequence = (
            discontinuation_reason_code_seq
        )

    return send_nevent(
        assoc,
        UnifiedProcedureStepPush,
        instance_uid,
        event_type=1,
        event_info=event_info,
    )


def send_ups_cancel_requested():
    pass


def send_ups_progress_report():
    pass


def send_ups_scp_status_change():
    pass


def send_ups_assigned():
    pass


def _setup_argparser():
    """Setup the command line arguments"""
    # Description
    parser = argparse.ArgumentParser(
        description=(
            "The nevent_sender application implements a Service Class User "
            "(SCU) for the UPS Event Class. "
            "Real world applications will often embed the nevent_sender functionality in an SCP"
            "With the nevent_sender acting under role reversal (i.e.) as an SCU within the SCP"
        ),
        usage="nevent_sender [options] addr port",
    )

    # Parameters
    req_opts = parser.add_argument_group("Parameters")
    req_opts.add_argument(
        "addr", help="TCP/IP address or hostname of DICOM peer", type=str
    )
    req_opts.add_argument("port", help="TCP/IP port number of peer", type=int)

    # General Options
    gen_opts = parser.add_argument_group("General Options")
    gen_opts.add_argument(
        "--version", help="print version information and exit", action="store_true"
    )
    output = gen_opts.add_mutually_exclusive_group()
    output.add_argument(
        "-q",
        "--quiet",
        help="quiet mode, print no warnings and errors",
        action="store_const",
        dest="log_type",
        const="q",
    )
    output.add_argument(
        "-v",
        "--verbose",
        help="verbose mode, print processing details",
        action="store_const",
        dest="log_type",
        const="v",
    )
    output.add_argument(
        "-d",
        "--debug",
        help="debug mode, print debug information",
        action="store_const",
        dest="log_type",
        const="d",
    )
    gen_opts.add_argument(
        "-ll",
        "--log-level",
        metavar="[l]",
        help=("use level l for the logger (critical, error, warn, info, debug)"),
        type=str,
        choices=["critical", "error", "warn", "info", "debug"],
    )

    # Configuration file Options
    fdir = os.path.abspath(os.path.dirname(__file__))
    fpath = os.path.join(fdir, "default.ini")
    gen_opts.add_argument(
        "-c",
        "--config",
        metavar="[f]ilename",
        help="use configuration file f",
        default=fpath,
    )

    # Network Options
    net_opts = parser.add_argument_group("Network Options")
    net_opts.add_argument(
        "-aet",
        "--calling-aet",
        metavar="[a]etitle",
        help="set my calling AE title (default: WATCH_SCU)",
        type=str,
        default="WATCH_SCU",
    )
    net_opts.add_argument(
        "-aec",
        "--called-aet",
        metavar="[a]etitle",
        help="set called AE title of peer (default: WATCH_SCP)",
        type=str,
        default="WATCH_SCP",
    )
    net_opts.add_argument(
        "-aer",
        "--receiver-aet",
        metavar="[a]etitle",
        help="set receiver AE title of peer (default: EVENT_SCP)",
        type=str,
        default="EVENT_SCP",
    )
    net_opts.add_argument(
        "-ta",
        "--acse-timeout",
        metavar="[s]econds",
        help="timeout for ACSE messages (default: 30 s)",
        type=float,
        default=30,
    )
    net_opts.add_argument(
        "-td",
        "--dimse-timeout",
        metavar="[s]econds",
        help="timeout for DIMSE messages (default: 30 s)",
        type=float,
        default=30,
    )
    net_opts.add_argument(
        "-tn",
        "--network-timeout",
        metavar="[s]econds",
        help="timeout for the network (default: 30 s)",
        type=float,
        default=30,
    )
    net_opts.add_argument(
        "-pdu",
        "--max-pdu",
        metavar="[n]umber of bytes",
        help=(
            f"set max receive pdu to n bytes (0 for unlimited, "
            f"default: {DEFAULT_MAX_LENGTH})"
        ),
        type=int,
        default=DEFAULT_MAX_LENGTH,
    )

    # Transfer Syntaxes
    ts_opts = parser.add_argument_group("Transfer Syntax Options")
    syntax = ts_opts.add_mutually_exclusive_group()
    syntax.add_argument(
        "-xe",
        "--request-little",
        help="request explicit VR little endian TS only",
        action="store_true",
    )
    syntax.add_argument(
        "-xb",
        "--request-big",
        help="request explicit VR big endian TS only",
        action="store_true",
    )
    syntax.add_argument(
        "-xi",
        "--request-implicit",
        help="request implicit VR little endian TS only",
        action="store_true",
    )

    # Misc Options
    # misc_opts = parser.add_argument_group("Miscellaneous Options")

    return parser.parse_args()


def get_contexts(fpaths, app_logger):
    """Return the valid DICOM files and their context values.

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
        except Exception:
            bad.append(("Bad DICOM file", path))
            continue

        try:
            sop_class = ds.SOPClassUID
            tsyntax = ds.file_meta.TransferSyntaxUID
        except Exception:
            bad.append(("Unknown SOP Class or Transfer Syntax UID", path))
            continue

        tsyntaxes = contexts.setdefault(sop_class, [])
        if tsyntax not in tsyntaxes:
            tsyntaxes.append(tsyntax)

        good.append(path)

    for reason, path in bad:
        app_logger.error(f"{reason}: {path}")

    return good, contexts


def main(args=None):
    """Run the application."""
    if args is not None:
        sys.argv = args

    args = _setup_argparser()

    if args.version:
        print(f"nevent_sender.py v{__version__}")
        sys.exit()

    APP_LOGGER = setup_logging(args, "nevent_sender")
    APP_LOGGER.debug(f"nevent_sender.py v{__version__}")
    APP_LOGGER.debug("")

    APP_LOGGER.debug("Using configuration from:")
    APP_LOGGER.debug(f"  {args.config}")
    APP_LOGGER.debug("")
    config = ConfigParser()
    config.read(args.config)

    ae = AE(ae_title=args.calling_aet)
    ae.acse_timeout = args.acse_timeout
    ae.dimse_timeout = args.dimse_timeout
    ae.network_timeout = args.network_timeout

    # Propose the default presentation contexts
    # if args.request_little:
    #     transfer_syntax = [ExplicitVRLittleEndian]
    # elif args.request_big:
    #     transfer_syntax = [ExplicitVRBigEndian]
    # elif args.request_implicit:
    #     transfer_syntax = [ImplicitVRLittleEndian]
    # else:
    #     transfer_syntax = [
    #         ExplicitVRLittleEndian,
    #         ImplicitVRLittleEndian,
    #         ExplicitVRBigEndian,
    #     ]

    # Request association with remote
    assoc = ae.associate(
        args.addr,
        args.port,
        contexts=UnifiedProcedurePresentationContexts,
        ae_title=args.called_aet,
        max_pdu=args.max_pdu,
    )
    if assoc.is_established:
        try:
            status, response = send_ups_state_report(assoc, UID("1.2.3.4"), "SCHEDULED")
            APP_LOGGER.info(f"Status: {os.linesep}{status}")
            APP_LOGGER.info(f"Response: {os.linesep}{response}")
            status, response = send_ups_state_report(
                assoc, UID("1.2.3.4"), "IN PROGRESS"
            )
            APP_LOGGER.info(f"Status: {os.linesep}{status}")
            APP_LOGGER.info(f"Response: {os.linesep}{response}")
            status, response = send_ups_state_report(assoc, UID("1.2.3.4"), "COMPLETED")
            APP_LOGGER.info(f"Status: {os.linesep}{status}")
            APP_LOGGER.info(f"Response: {os.linesep}{response}")
        except InvalidDicomError:
            APP_LOGGER.error("Bad DICOM: ")
        except Exception as exc:
            APP_LOGGER.error(
                "UPS State Report as Event Notification (N-EVENT-REPORT-RQ) failed"
            )
            APP_LOGGER.exception(exc)

        assoc.release()
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
