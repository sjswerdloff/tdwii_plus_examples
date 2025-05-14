#!/usr/bin/env python
import argparse
import logging
import os

from pydicom.dataset import FileMetaDataset
from pydicom.uid import PYDICOM_IMPLEMENTATION_UID, ExplicitVRLittleEndian

from tdwii_plus_examples.upspullcfindscu import UPSPullCFindSCU


def main():
    parser = argparse.ArgumentParser(description="UPS C-FIND SCU (UPS Query)")
    parser.add_argument("ip", type=str, help="IP address or hostname of called AE")
    parser.add_argument("port", type=int, help="TCP port number of called AE")
    parser.add_argument("-aet", "--ae_title", type=str, default="UPSFINDSCU", help="Application Entity Title")
    parser.add_argument("-aec", "--called_ae_title", type=str, default="ANYSCP", help="Called Application Entity Title")
    parser.add_argument("--ups_uid", type=str, default="", help="SOP Instance UID for the specific UPS (optional)")
    parser.add_argument("--machine", type=str, default="", help="Treatment machine name (optional)")
    parser.add_argument("--state", type=str, default="SCHEDULED", help="Procedure Step State (default: SCHEDULED)")
    parser.add_argument("--start", type=str, default=None, help="UPS start Date and Time (optional)")
    parser.add_argument("--end", type=str, default=None, help="UPS End Date and Time (optional)")
    parser.add_argument(
        "--save",
        type=str,
        default=None,
        metavar="DIR",
        help="Directory to save matching UPS responses as a DICOM Part 10 file",
    )
    parser.add_argument("--raw", action="store_true", help="Save as raw DICOM dataset (no File Meta Information)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Set log level to INFO")
    parser.add_argument("-d", "--debug", action="store_true", help="Set log level to DEBUG")
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress all log output")

    args = parser.parse_args()

    if args.quiet:
        log_level = logging.CRITICAL
    elif args.verbose:
        log_level = logging.INFO
    elif args.debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.WARNING

    logging.basicConfig(level=log_level)
    logger = logging.getLogger("upsfind")
    logger.setLevel(log_level)

    logger.info(f"Initializing UPSPullCFindSCU instance with remote SCP {args.called_ae_title}@{args.ip}:{args.port}")
    scu = UPSPullCFindSCU(
        logger=logger,
        calling_ae_title=args.ae_title,
        called_ip=args.ip,
        called_port=args.port,
        called_ae_title=args.called_ae_title,
    )

    # Build the UPS query dataset using the provided options
    ds_query = scu.create_ups_query(
        ups_uid=args.ups_uid,
        machine_name=args.machine,
        procedure_step_state=args.state,
        scheduled_no_sooner_than=args.start,
        scheduled_no_later_than=args.end,
    )

    # Perform the C-FIND operation
    ups_responses = scu.get_ups(ds_query)

    if not ups_responses:
        print("No UPS instances found matching the query.")
    else:
        print(f"Found {len(ups_responses)} UPS instance(s):")
        for i, ds in enumerate(ups_responses, 1):
            print(f"\n--- UPS Instance {i} ---")
            print(ds)
            if args.save:
                os.makedirs(args.save, exist_ok=True)
                # Use SOPInstanceUID as filename if present, else index
                if hasattr(ds, "SOPInstanceUID") and ds.SOPInstanceUID:
                    filename = f"UPS_{ds.SOPInstanceUID}.dcm"
                else:
                    filename = f"UPS_{i}.dcm"
                file_path = os.path.join(args.save, filename)
                # Set transfer syntax attributes before saving
                ds.is_little_endian = True
                ds.is_implicit_VR = False
                if not args.raw:
                    # Add file meta information for Part 10
                    file_meta = FileMetaDataset()
                    file_meta.MediaStorageSOPClassUID = ds.SOPClassUID
                    file_meta.MediaStorageSOPInstanceUID = ds.SOPInstanceUID
                    file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
                    file_meta.ImplementationClassUID = PYDICOM_IMPLEMENTATION_UID
                    ds.file_meta = file_meta
                try:
                    ds.save_as(file_path, write_like_original=args.raw)
                    print(f"Saved UPS Identifier {i} to {file_path}")
                except Exception as e:
                    print(f"Failed to save UPS Identifier {i} to {file_path}: {e}")


if __name__ == "__main__":
    main()
