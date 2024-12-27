#!/usr/bin/env python
import argparse
import logging

from tdwii_plus_examples.cstorescp import CStoreSCP

from pydicom.uid import UID
from pynetdicom.status import Status


def my_handler(event, args, logger):
    """
    Example of a custom handler for C-STORE requests.

    This handler logs all arguments passed to it, as well as information
    of the C-STORE-RQ message. It's meant to be used as a starting point for
    writing your own custom handlers.

    Parameters
    ----------
    event : pynetdicom.event.event
        The event that triggered the handler
    args : argparse.Namespace
        The arguments passed to the handler
    logger : logging.Logger
        The logger instance

    Returns
    -------
    status : pynetdicom.sop_class.Status or int
        The return status of the handler
    """
    logger.info("Custom handler for %s called", event.request.msg_type)

    # Log all arguments
    args_dict = vars(args)
    for key in args_dict:
        logger.info("\twith argument  %s: %s", key, args_dict[key])

    # Log the C-STORE request information
    request_info = {
        "MessageID": event.request.MessageID,
        "AffectedSOPClassUID": event.request.AffectedSOPClassUID,
        "AffectedSOPInstanceUID": event.request.AffectedSOPInstanceUID,
        "Priority": event.request.Priority,
        "MoveOriginatorApplicationEntityTitle":
            event.request.MoveOriginatorApplicationEntityTitle,
        "MoveOriginatorMessageID": event.request.MoveOriginatorMessageID
    }

    for key, value in request_info.items():
        if key == "AffectedSOPClassUID":
            logger.info("Command Set %s: %s (%s)", key, value, UID(value).name)
        else:
            logger.info("Command Set %s: %s", key, value)

    data_set_info = (
        f"{event.request.DataSet.getbuffer().nbytes} bytes"
        if event.request.DataSet is not None else "Absent"
    )
    logger.info("Command Set Data Set: %s", data_set_info)

    return Status.SUCCESS


def main():
    parser = argparse.ArgumentParser(
        description="Run a DICOM Storage SCP."
    )
    parser.add_argument(
        '-a', '--ae_title', type=str, default='ECHO_SCP',
        help='Application Entity Title'
    )
    parser.add_argument(
        '-b', '--bind_address', type=str, default='',
        help='Specific IP address or hostname, omit to bind to all interfaces'
    )
    parser.add_argument(
        '-p', '--port', type=int, default=11112,
        help='Port number'
    )
    parser.add_argument(
        '-s', '--sop_classes', nargs='+',
        help='List of SOP Class UID or valid keywords from PS3.6 Annex A'
    )
    parser.add_argument(
        '-t', '--transfer_syntaxes', nargs='+',
        help='List of Transfer syntax to support'
    )
    parser.add_argument(
        '-c', '--custom_handler', type=str,
        help='Custom C-STORE handler function'
    )
    parser.add_argument(
        '-o', '--output_directory', type=str,
        help='Output directory, defaults to current working directory'
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='Set log level to INFO'
    )
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='Set log level to DEBUG'
    )

    args = parser.parse_args()

    log_level = logging.WARNING
    if args.verbose:
        log_level = logging.INFO
    elif args.debug:
        log_level = logging.DEBUG

    logging.basicConfig(level=log_level)
    logger = logging.getLogger('storescp')

    if args.custom_handler:
        # Custom handler should be a function defined in the global namespace
        # at the module level, so we use globals() to look it up.
        # This allows passing a function name as a string argument.
        handler = globals().get(args.custom_handler)
    else:
        handler = None

    logger.info("Starting up the DICOM Storage SCP...")
    cstorescp = CStoreSCP(
        ae_title=args.ae_title,
        bind_address=args.bind_address,
        port=args.port,
        logger=logger,
        sop_classes=args.sop_classes,
        transfer_syntaxes=args.transfer_syntaxes,
        custom_handler=handler,
        store_directory=args.output_directory
    )
    cstorescp.run()
    # Keep the main application running
    try:
        while True:
            pass  # You can replace this with your main application logic
    except KeyboardInterrupt:
        logger.info("Shutting down the DICOM Storage SCP...")


if __name__ == "__main__":
    main()
