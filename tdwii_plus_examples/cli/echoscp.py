#!/usr/bin/env python
import argparse
import logging

from tdwii_plus_examples.cechoscp import CEchoSCP


def main():
    parser = argparse.ArgumentParser(
        description="Run a DICOM Verification SCP."
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
    logger = logging.getLogger('echoscp')

    logger.info("Starting up the DICOM Verification SCP...")
    cechoscp = CEchoSCP(ae_title=args.ae_title, bind_address=args.bind_address,
                        port=args.port, logger=logger)
    cechoscp.run()
    # Keep the main application running
    try:
        while True:
            pass  # You can replace this with your main application logic
    except KeyboardInterrupt:
        logger.info("Shutting down the DICOM Verification SCP...")


if __name__ == "__main__":
    main()
