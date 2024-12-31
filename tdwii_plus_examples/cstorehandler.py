import os
from pynetdicom.status import Status
from pydicom.dataset import Dataset
from pydicom.filewriter import write_file_meta_info
from pydicom.uid import DeflatedExplicitVRLittleEndian
from pynetdicom.dsutils import encode


# Define the specific Status Code values for the C-STORE Response
Status.add('UNABLE_TO_DECODE_DATASET', 0xC210)  # Failure to decode the dataset
Status.add('MISSING_ARGUMENT', 0xC212)  # Failure to process the request
Status.add('OUT_OF_RESOURCES', 0xA700)  # Failure to store the dataset
Status.add('UNABLE_TO_STORE_DATASET', 0xA701)  # Failure to store the dataset

# Define prefixes for SOP classes commmonly used in Radiotherapy
SOP_CLASS_PREFIXES = {
    "1.2.840.10008.5.1.4.1.1.2": ("CT", "CT Image Storage"),
    "1.2.840.10008.5.1.4.1.1.4": ("MR", "MR Image Storage"),
    "1.2.840.10008.5.1.4.1.1.7": ("SC", "Secondary Capture Image Storage"),
    "1.2.840.10008.5.1.4.1.1.128": (
        "PT", "Positron Emission Tomography Image Storage"),
    "1.2.840.10008.5.1.4.1.1.481.1": (
        "RI", "RTIMG", "RTIMAGE",
        "RT Image Storage"),
    "1.2.840.10008.5.1.4.1.1.481.2": (
        "RD", "RTDOSE",
        "RT Dose Storage"),
    "1.2.840.10008.5.1.4.1.1.481.3": (
        "RS", "RTSTRUCT", "RTSTRUCTURESET",
        "RT Structure Set Storage"),
    "1.2.840.10008.5.1.4.1.1.481.4": (
        "RR", "RTREC", "RTRECORD",
        "RT Beam Treatment Record Storage"),
    "1.2.840.10008.5.1.4.1.1.481.5": (
        "RP", "RTPLAN", "RTPLAN",
        "RT Plan Storage"),
    "1.2.840.10008.5.1.4.1.1.481.6": (
        "BR", "RTBYREC", "RTBRACHYRECORD",
        "RT Brachy Treatment Record Storage"),
    "1.2.840.10008.5.1.4.1.1.481.7": (
        "SR", "SUMREC", "RTSUMRECORD",
        "RT Treatment Summary Record Storage"),
    "1.2.840.10008.5.1.4.1.1.481.8": (
        "RN", "RTIONPLN", "RTIONPLAN",
        "RT Ion Plan Storage"),
    "1.2.840.10008.5.1.4.1.1.481.9": (
        "IR", "RTIONREC", "RTIONRECORD",
        "RT Ion Beams Treatment Record Storage"),
    "1.2.840.10008.5.1.4.34.7": (
        "BDI", "RTBDI", "RTBEAMDELIVERYINSTRUCTION",
        "RT Beams Delivery Instruction Storage"),
    "1.2.840.10008.5.1.4.1.1.66.1": (
        "REG", "IMREG", "IMAGEREGISTRATION",
        "Spatial Registration Storage"),
    "1.2.840.10008.5.1.4.1.1.66.3": (
        "DIR", "DEFIMREG", "DEFORMABLEIMAGEREGISTRATION",
        "Deformable Spatial Registration Storage")
}


def handle_cstore(event, args, app_logger):
    """Handler for evt.EVT_C_STORE.

    Parameters
    ----------
    event : pynetdicom.event.event
        The event corresponding to a C-STORE request.
    args : argparse.Namespace
        The namespace containing the arguments to use. The namespace should
        contain ``args.ignore`` and ``args.output_directory`` attributes:
        - ``args.ignore``: ``bool`` indicating whether to ignore the
          request or not. Defaults to ``False`` if attribute is not present.
        - ``args.output_directory``: ``str`` indicating the directory
          where the incoming DICOM instance should be stored. Required.
    app_logger : logging.Logger
        The application's logger.

    Returns
    -------
    status : pynetdicom.sop_class.Status or int
        A valid return status code, see PS3.4 Annex B.2.3 or the
        ``StorageServiceClass`` implementation for the available statuses
    """
    # Create the response status assuming success
    # consistently using Dataset object with Status element (vs int)
    status_ds = Dataset()
    status_ds.Status = Status.SUCCESS

    # Return Success status code if the C-STORE request is to be ignored
    if hasattr(args, 'ignore'):
        if args.ignore:
            app_logger.info("Ignoring C-STORE request")
            return status_ds
        else:
            app_logger.info("Processing C-STORE request")
    else:
        app_logger.warning(
            "args.ignore attribute not present, processing C-STORE request")

    # Check that the output directory argument is present and not None
    if not hasattr(args, 'output_directory') or args.output_directory is None:
        app_logger.error("args.output_directory attribute not present or None")
        status_ds.Status = Status.MISSING_ARGUMENT
        return status_ds

    # Read the incoming Data Set
    try:
        ds = event.dataset
        # Remove any File Meta Information elements (group 0x0002) elements
        # that may have been included
        ds = ds[0x00030000:]
    except Exception:
        app_logger.exception("Unable to decode the data set")
        status_ds.Status = Status.UNABLE_TO_DECODE_DATASET
        return status_ds

    # Add the File Meta Information elements from the incoming Command Set
    # Note: Implementation Class UID and Implementation Version Name are set
    # to PYNETDICOM_IMPLEMENTATION_UID and PYNETDICOM_IMPLEMENTATION_VERSION
    ds.file_meta = event.file_meta

    # Because pydicom uses deferred reads for its decoding, decoding errors
    # are hidden until encountered by accessing a faulty element
    try:
        sop_class = ds.SOPClassUID
        sop_instance = ds.SOPInstanceUID
    except Exception:
        app_logger.exception(
            "Unable to decode the data set and/or the command set"
        )
        status_ds.Status = Status.UNABLE_TO_DECODE_DATASET
        return status_ds

    # Get a prefix of the SOP Class for the filename
    try:
        sop_prefix = SOP_CLASS_PREFIXES[sop_class][0]
    except KeyError:
        sop_prefix = "UN"

    filename = f"{sop_prefix}.{sop_instance}.dcm"
    app_logger.info(f"Storing DICOM file: {filename}")

    # Store the received dataset as a DICOM Part 10 file

    filename = os.path.join(args.output_directory, filename)
    # Create the output directory if not present
    try:
        os.makedirs(args.output_directory, exist_ok=True)
    except Exception:
        app_logger.exception(
            f"Unable to create the output directory: {args.output_directory}"
        )
        status_ds.Status = Status.OUT_OF_RESOURCES
        return status_ds

    # Warn of overwriting if the file already exists
    if os.path.exists(filename):
        app_logger.warning("DICOM file already exists, overwriting")

    # Write the file
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

    except IOError:
        app_logger.exception(
            "Could not write file to specified directory: "
            f"{os.path.dirname(filename)}"
        )
        status_ds.Status = Status.OUT_OF_RESOURCES
    except Exception:
        app_logger.exception(
            "Could not write file to specified directory: "
            f"{os.path.dirname(filename)}"
        )
        status_ds.Status = Status.UNABLE_TO_STORE_DATASET

    return status_ds
