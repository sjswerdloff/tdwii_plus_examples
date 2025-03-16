#!/usr/bin/env python
"""
A DICOM Verfication Service Class Provider (SCP) application.

This application starts an Application Entity (AE) server implementing
the Verification Service Class.

Usage:
    echoscp [options]

Options:
    -h, --help          Show this help message and exit
    -a, --ae_title      Application Entity Title (default: ECHOSCP)
    -b, --bind_address  Specific IP address or hostname
    -p, --port          Port number (default: 11112)
    -v, --verbose       Set log level to INFO
    -d, --debug         Set log level to DEBUG
"""

import argparse
import atexit
import logging
import time

from tdwii_plus_examples.cechoscp import CEchoSCP


def main(loop_forever=True):  # Add a parameter to control the loop
    parser = argparse.ArgumentParser(description="Run a DICOM Verification SCP.")
    parser.add_argument("-a", "--ae_title", type=str, default="", help="Application Entity Title")
    parser.add_argument(
        "-b", "--bind_address", type=str, default="", help="Specific IP address or hostname, omit to bind to all interfaces"
    )
    parser.add_argument("-p", "--port", type=int, default=None, help="Port number")
    parser.add_argument("-v", "--verbose", action="store_true", help="Set log level to INFO")
    parser.add_argument("-d", "--debug", action="store_true", help="Set log level to DEBUG")

    args = parser.parse_args()

    log_level = logging.WARNING
    if args.verbose:
        log_level = logging.INFO
    elif args.debug:
        log_level = logging.DEBUG

    logging.basicConfig(level=log_level)
    logger = logging.getLogger("echoscp")
    logger.setLevel(log_level)

    logger.info("Starting up the DICOM Verification SCP...")
    cechoscp = CEchoSCP(ae_title=args.ae_title, bind_address=args.bind_address, port=args.port, logger=logger)
    cechoscp.run()
    # Keep the main application running
    atexit.register(cechoscp.stop)
    try:
        while loop_forever:
            time.sleep(1)  # Sleep to prevent high CPU usage
    except KeyboardInterrupt:
        logger.info("Shutting down the DICOM Verification SCP...")
        loop_forever = False


if __name__ == "__main__":
    main()
