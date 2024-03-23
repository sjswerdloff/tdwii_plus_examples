"""Utility classes and functions for the apps."""

import logging
import os
from struct import pack

from pydicom import dcmread
from pydicom.datadict import tag_for_keyword, repeater_has_keyword, get_entry
from pydicom.dataset import Dataset
from pydicom.filewriter import write_file_meta_info
from pydicom.tag import Tag
from pydicom.uid import DeflatedExplicitVRLittleEndian

from pynetdicom.dsutils import encode


def handle_store(event, args, app_logger):
    """Handle a C-STORE request.

    Parameters
    ----------
    event : pynetdicom.event.event
        The event corresponding to a C-STORE request.
    args : argparse.Namespace
        The namespace containing the arguments to use. The namespace should
        contain ``args.ignore`` and ``args.output_directory`` attributes.
    app_logger : logging.Logger
        The application's logger.

    Returns
    -------
    status : pynetdicom.sop_class.Status or int
        A valid return status code, see PS3.4 Annex B.2.3 or the
        ``StorageServiceClass`` implementation for the available statuses
    """
    if args.ignore:
        return 0x0000

    try:
        ds = event.dataset
        # Remove any Group 0x0002 elements that may have been included
        ds = ds[0x00030000:]
    except Exception as exc:
        app_logger.error("Unable to decode the dataset")
        app_logger.exception(exc)
        # Unable to decode dataset
        return 0x210

    # Add the file meta information elements
    ds.file_meta = event.file_meta

    # Because pydicom uses deferred reads for its decoding, decoding errors
    #   are hidden until encountered by accessing a faulty element
    try:
        sop_class = ds.SOPClassUID
        sop_instance = ds.SOPInstanceUID
    except Exception as exc:
        app_logger.error(
            "Unable to decode the received dataset or missing 'SOP Class "
            "UID' and/or 'SOP Instance UID' elements"
        )
        app_logger.exception(exc)
        # Unable to decode dataset
        return 0xC210

    try:
        # Get the elements we need
        mode_prefix = SOP_CLASS_PREFIXES[sop_class][0]
    except KeyError:
        mode_prefix = "UN"

    filename = f"{mode_prefix}.{sop_instance}.dcm"
    app_logger.info(f"Storing DICOM file: {filename}")

    status_ds = Dataset()
    status_ds.Status = 0x0000

    # Try to save to output-directory
    if args.output_directory is not None:
        filename = os.path.join(args.output_directory, filename)
        try:
            os.makedirs(args.output_directory, exist_ok=True)
        except Exception as exc:
            app_logger.error("Unable to create the output directory:")
            app_logger.error(f"    {args.output_directory}")
            app_logger.exception(exc)
            # Failed - Out of Resources - IOError
            status_ds.Status = 0xA700
            return status_ds

    if os.path.exists(filename):
        app_logger.warning("DICOM file already exists, overwriting")

    try:
        if event.context.transfer_syntax == DeflatedExplicitVRLittleEndian:
            # Workaround for pydicom issue #1086
            with open(filename, "wb") as f:
                f.write(b"\x00" * 128)
                f.write(b"DICM")
                write_file_meta_info(f, event.file_meta)
                f.write(encode(ds, False, True, True))
        else:
            # We use `write_like_original=False` to ensure that a compliant
            #   File Meta Information Header is written
            ds.save_as(filename, write_like_original=False)

        status_ds.Status = 0x0000  # Success
    except IOError as exc:
        app_logger.error("Could not write file to specified directory:")
        app_logger.error(f"    {os.path.dirname(filename)}")
        app_logger.exception(exc)
        # Failed - Out of Resources - IOError
        status_ds.Status = 0xA700
    except Exception as exc:
        app_logger.error("Could not write file to specified directory:")
        app_logger.error(f"    {os.path.dirname(filename)}")
        app_logger.exception(exc)
        # Failed - Out of Resources - Miscellaneous error
        status_ds.Status = 0xA701

    return status_ds


SOP_CLASS_PREFIXES = {
    "1.2.840.10008.5.1.4.1.1.2": ("CT", "CT Image Storage"),
    "1.2.840.10008.5.1.4.1.1.2.1": ("CTE", "Enhanced CT Image Storage"),
    "1.2.840.10008.5.1.4.1.1.4": ("MR", "MR Image Storage"),
    "1.2.840.10008.5.1.4.1.1.4.1": ("MRE", "Enhanced MR Image Storage"),
    "1.2.840.10008.5.1.4.1.1.128": ("PT", "Positron Emission Tomography Image Storage"),
    "1.2.840.10008.5.1.4.1.1.130": ("PTE", "Enhanced PET Image Storage"),
    "1.2.840.10008.5.1.4.1.1.481.1": ("RI", "RT Image Storage"),
    "1.2.840.10008.5.1.4.1.1.481.2": ("RD", "RT Dose Storage"),
    "1.2.840.10008.5.1.4.1.1.481.5": ("RP", "RT Plan Storage"),
    "1.2.840.10008.5.1.4.1.1.481.8": ("RN", "RT Ion Plan Storage"),
    "1.2.840.10008.5.1.4.1.1.481.9": ("RX", "RT Ion Beams Treatment Record Storage"),
    "1.2.840.10008.5.1.4.1.1.481.3": ("RS", "RT Structure Set Storage"),
    "1.2.840.10008.5.1.4.1.1.1": ("CR", "Computed Radiography Image Storage"),
    "1.2.840.10008.5.1.4.1.1.6.1": ("US", "Ultrasound Image Storage"),
    "1.2.840.10008.5.1.4.1.1.6.2": ("USE", "Enhanced US Volume Storage"),
    "1.2.840.10008.5.1.4.1.1.12.1": ("XA", "X-Ray Angiographic Image Storage"),
    "1.2.840.10008.5.1.4.1.1.12.1.1": ("XAE", "Enhanced XA Image Storage"),
    "1.2.840.10008.5.1.4.1.1.20": ("NM", "Nuclear Medicine Image Storage"),
    "1.2.840.10008.5.1.4.1.1.7": ("SC", "Secondary Capture Image Storage"),
    "1.2.840.10008.5.1.4.34.7": ("RB", "RT Beams Delivery Instruction Storage​"),
}
