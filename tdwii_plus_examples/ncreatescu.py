#!/usr/bin/env python
"""A UPS N-CREATE SCU application.

Used for uploading DICOM UPS SOP Instances to a UPS SCP.
"""

import argparse
import errno
import os
import sys
from pathlib import Path

from pydicom import dcmread
from pydicom.errors import InvalidDicomError
from pydicom.uid import (
    DeflatedExplicitVRLittleEndian,
    ExplicitVRBigEndian,
    ExplicitVRLittleEndian,
    ImplicitVRLittleEndian,
)
from pynetdicom import AE, UnifiedProcedurePresentationContexts
from pynetdicom._globals import DEFAULT_MAX_LENGTH
from pynetdicom.apps.common import get_files, setup_logging
from pynetdicom.sop_class import UnifiedProcedureStepPush

__version__ = "0.3.0"


def _setup_argparser():
    """Setup the command line arguments"""
    # Description
    parser = argparse.ArgumentParser(
        description=(
            "The ncreatescu application implements a Service Class User "
            "(SCU) for the Unified Procedure Step Push Service Class. For each DICOM "
            "file on the command line it sends a N-CREATE-RQ message to a "
            "UPS Service Class Provider (SCP) and waits for a response."
        ),
        usage="ncreatescu [options] addr port path",
    )

    # Parameters
    req_opts = parser.add_argument_group("Parameters")
    req_opts.add_argument("addr", help="TCP/IP address or hostname of DICOM peer", type=str)
    req_opts.add_argument("port", help="TCP/IP port number of peer", type=int)
    req_opts.add_argument(
        "path",
        metavar="path",
        nargs="+",
        help="DICOM file or directory to be transmitted",
        type=str,
    )

    # General Options
    gen_opts = parser.add_argument_group("General Options")
    gen_opts.add_argument("--version", help="print version information and exit", action="store_true")
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

    # Input Options
    in_opts = parser.add_argument_group("Input Options")
    in_opts.add_argument(
        "-r",
        "--recurse",
        help="recursively search the given directory",
        action="store_true",
    )

    # Network Options
    net_opts = parser.add_argument_group("Network Options")
    net_opts.add_argument(
        "-aet",
        "--calling-aet",
        metavar="[a]etitle",
        help="set my calling AE title (default: ncreatescu)",
        type=str,
        default="ncreatescu",
    )
    net_opts.add_argument(
        "-aec",
        "--called-aet",
        metavar="[a]etitle",
        help="set called AE title of peer (default: ANY-SCP)",
        type=str,
        default="ANY-SCP",
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
        help=(f"set max receive pdu to n bytes (0 for unlimited, " f"default: {DEFAULT_MAX_LENGTH})"),
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
    misc_opts = parser.add_argument_group("Miscellaneous Options")
    misc_opts.add_argument(
        "-cx",
        "--required-contexts",
        help=("only request the presentation contexts required for the " "input DICOM file(s)"),
        action="store_true",
    )

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
        print(f"ncreatescu.py v{__version__}")
        sys.exit()

    APP_LOGGER = setup_logging(args, "ncreatescu")
    APP_LOGGER.debug(f"ncreatescu.py v{__version__}")
    APP_LOGGER.debug("")

    lfiles, badfiles = get_files(args.path, args.recurse)

    for bad in badfiles:
        APP_LOGGER.error(f"Cannot access path: {bad}")

    ae = AE(ae_title=args.calling_aet)
    ae.acse_timeout = args.acse_timeout
    ae.dimse_timeout = args.dimse_timeout
    ae.network_timeout = args.network_timeout

    if args.required_contexts:
        # Only propose required presentation contexts
        lfiles, contexts = get_contexts(lfiles, APP_LOGGER)
        try:
            for abstract, transfer in contexts.items():
                for tsyntax in transfer:
                    ae.add_requested_context(abstract, tsyntax)
        except ValueError:
            raise ValueError(
                "More than 128 presentation contexts required with "
                "the '--required-contexts' flag, please try again "
                "without it or with fewer files"
            )
    else:
        # Propose the default presentation contexts
        if args.request_little:
            transfer_syntax = [ExplicitVRLittleEndian]
        elif args.request_big:
            transfer_syntax = [ExplicitVRBigEndian]
        elif args.request_implicit:
            transfer_syntax = [ImplicitVRLittleEndian]
        else:
            transfer_syntax = [
                ExplicitVRLittleEndian,
                ImplicitVRLittleEndian,
                DeflatedExplicitVRLittleEndian,
                ExplicitVRBigEndian,
            ]

        for cx in UnifiedProcedurePresentationContexts:
            ae.add_requested_context(cx.abstract_syntax, transfer_syntax)

    if not lfiles:
        APP_LOGGER.warning("No suitable DICOM files found")
        sys.exit()

    try:
        # Request association with remote
        assoc = ae.associate(args.addr, args.port, ae_title=args.called_aet, max_pdu=args.max_pdu)
        if assoc.is_established:
            ii = 1
            for fpath in lfiles:
                APP_LOGGER.info(f"Sending file: {fpath}")
                try:
                    ds = dcmread(fpath, force=True)  # set force flag to allow raw DICOM files
                    status = assoc.send_n_create(
                        ds,
                        UnifiedProcedureStepPush,
                        ds.SOPInstanceUID,
                        ii,
                        meta_uid=UnifiedProcedureStepPush,
                    )
                    APP_LOGGER.debug(f"Status: {status}")
                    # dataset: Dataset,
                    # class_uid: Union[str, UID],
                    # instance_uid: Optional[Union[str, UID]] = None,
                    # msg_id: int = 1,
                    # meta_uid: Optional[Union[str, UID]] = None,
                    ii += 1
                except InvalidDicomError:
                    APP_LOGGER.error(f"Bad DICOM file: {fpath}")
                    sys.exit(errno.EFTYPE)  # Inappropriate file type or format
                except Exception as exc:
                    APP_LOGGER.error(f"Create failed: {fpath}")
                    APP_LOGGER.exception(exc)
                    sys.exit(errno.EIO)  # Input/output error

            assoc.release()
        else:
            sys.exit(1)
    except Exception as exc:
        APP_LOGGER.error("Association request failed")
        APP_LOGGER.exception(exc)
        sys.exit(1)  # Exit with code 1 on any exception related to opening an association


if __name__ == "__main__":
    main()
