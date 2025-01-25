#!/usr/bin/env python
"""
A DICOM UPS Watch Service Class Provider (SCU) application.

This application implements a UPS Watch N-ACTION - Un/Subscribe SOP
Class SCU. It uses the DIMSE N-ACTION Service to subscribe with an SCP
in order to receive UPS State Change Event Reports, or to unsubscribe
to no longer receive Event Reports.

Usage:
    upswatchscu [options] ip port

Arguments:
    ip    IP address of called AE
    port  TCP port number of called AE
    uid   SOP Instance UID of watched UPS (global subscription if omitted)

Options:
    -h, --help               Show this help message and exit
    -aet, --ae_title         Application Entity Title (default: WATCHSCU)
    -aec, --called_ae_title  Called Application Entity Title (default: ANYSCP)
    -l, --lock               Lock watched UPS from deletion
    -m, --machine
    -v, --verbose            Set log level to INFO
    -d, --debug              Set log level to DEBUG
"""

import argparse
import logging

from pydicom import Dataset, Sequence

from tdwii_plus_examples.upswatchnactionscu import UPSWatchNActionSCU


def main():
    parser = argparse.ArgumentParser(description="Send a DICOM UPS Watch N-ACTION - Un/Subscribe request")
    parser.add_argument("ip", type=str, help="IP address or hotname of called AE")
    parser.add_argument("port", type=int, help="TCP port number of called AE")
    parser.add_argument(
        "uid", nargs="?", default=None, help="SOP Instance UID of watched UPS (global subscription if omitted)"
    )
    parser.add_argument("-aet", "--ae_title", type=str, default="WATCHSCU", help="Application Entity Title")
    parser.add_argument("-aec", "--called_ae_title", type=str, default="ANYSCP", help="Called Application Entity Title")
    parser.add_argument("-l", "--lock", action="store_true", help="Lock watched UPS from deletion")
    parser.add_argument("-m", "--machine", type=str, default=None, help="machine name for filtered global subscription")
    parser.add_argument("-u", "--unsubscribe", action="store_true", help="Unsubscribe")
    parser.add_argument("-v", "--verbose", action="store_true", help="Set log level to INFO")
    parser.add_argument("-d", "--debug", action="store_true", help="Set log level to DEBUG")

    args = parser.parse_args()

    log_level = logging.WARNING
    if args.verbose:
        log_level = logging.INFO
    elif args.debug:
        log_level = logging.DEBUG

    logging.basicConfig(level=log_level)
    logger = logging.getLogger("upswatchscu")
    logger.setLevel(log_level)

    logger.info(f"Trying to establish association with {args.ae_title}@{args.ip}:{args.port}")
    scu = UPSWatchNActionSCU(
        logger=logger,
        calling_ae_title=args.ae_title,
        called_ae_title=args.called_ae_title,
        called_ip=args.ip,
        called_port=args.port,
    )
    if args.uid is None:
        if not args.unsubscribe:
            if args.machine is not None:
                # Create a filter to watch the UPS scheduled for a specific machine
                ds = Dataset()
                # Create a sequence item
                item = Dataset()
                item.CodeValue = args.machine
                item.CodingSchemeDesignator = "99IHERO2008"
                item.CodeMeaning = f"{args.machine} treatment machine"
                # Add the item to a sequence
                seq = Sequence([item])
                # Add the sequence to the ScheduledStationNameCodeSequence element
                ds.ScheduledStationNameCodeSequence = seq
            else:
                ds = None
            scu.subscribe_globally(lock=args.lock, matching_keys=ds)
        else:
            scu.unsubscribe_globally()
    else:
        if not args.unsubscribe:
            scu.subscribe(lock=args.lock, instance_uid=args.uid)
        else:
            scu.unsubscribe(instance_uid=args.uid)


if __name__ == "__main__":
    main()
