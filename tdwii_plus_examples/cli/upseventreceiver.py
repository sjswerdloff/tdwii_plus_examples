#!/usr/bin/env python
import argparse
import logging
import time

from pydicom.uid import UID
from pynetdicom.status import Status
from pydicom.dataset import Dataset

from tdwii_plus_examples.upsneventreceiver import UPSNEventReceiver
from tdwii_plus_examples.upsneventhandler import UPS_EVENT_TYPES


def my_upsevent_callback(upseventtype, upseventinfo, logger):
    """
    Example of a UPS Event callback for processing incoming UPS events.

    This callback logs all arguments passed to it, as well as information
    of the N-EVENT-REPORT-RQ message. It's meant to be used as a starting 
    point for writing your own callback.

    Parameters
    ----------
    upseventinfo : pydicom.dataset.Dataset.
        The N-EVENT-REPORT-RQ Event Information dataset.
    logger : logging.Logger
        The logger instance
    """
    logger.info("UPS Event callback for %s called",
                UPS_EVENT_TYPES[upseventtype])

    if UPS_EVENT_TYPES[upseventtype] == "UPS State Report":
        logger.info("UPS State Report")


def main(loop_forever=True):  # Add a parameter to control the loop
    parser = argparse.ArgumentParser(
        description="Run a DICOM UPS Event Receiver (SCU)."
    )
    parser.add_argument(
        '-a', '--ae_title', type=str, default='UPSEVENT_RCV',
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
        '-t', '--transfer_syntaxes', nargs='+',
        help='List of Transfer syntax to support'
    )
    parser.add_argument(
        '-c', '--callback', type=str,
        help='UPS Event callback function'
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
    logger = logging.getLogger('upseventreceiver')

    if args.callback:
        # Callback should be a function defined in the global namespace
        # at the module level, so we use globals() to look it up.
        # This allows passing a function name as a string argument.
        callback = globals().get(args.callback)
    else:
        callback = None

    logger.info("Starting up the DICOM UPS Event Receiver (SCU) ...")
    upsneventrcv = UPSNEventReceiver(
        ae_title=args.ae_title,
        bind_address=args.bind_address,
        port=args.port,
        logger=logger,
        transfer_syntaxes=args.transfer_syntaxes,
        ups_event_callback=callback,
    )
    upsneventrcv.run()
    logger.info("DICOM UPS Event Receiver (SCU) is running...")
    # Keep the main application running
    try:
        while loop_forever:
            time.sleep(1)  # Sleep to prevent high CPU usage
    except KeyboardInterrupt:
        logger.info("Shutting down the UPS Event Receiver (SCU) ...")


if __name__ == "__main__":
    main()
