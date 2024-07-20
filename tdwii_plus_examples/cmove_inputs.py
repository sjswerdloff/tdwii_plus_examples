#!/usr/bin/env python
"""cmove_inputs:  iterates through the input information sequence of a UPS Push SOP (e.g. a C-FIND-RSP)
and issues a C-MOVE-RQ for each input from it's specified storage AE
Requires a configuration json file containing a list of AE Title/Address/Port
"""
import json
import re
import sys
from pathlib import Path

import pydicom
from pydicom.dataset import Dataset
from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import StudyRootQueryRetrieveInformationModelMove

from tdwii_plus_examples import tdwii_config

# from pynetdicom.apps import movescu

# known_ae_ipaddr = {
#     "ANY_SCP": "127.0.0.1",
#     "TDD_SCP": "127.0.0.1",
#     "IMS_IHERO_TMS1": "10.211.55.8",
# }
# known_ae_port = {"ANY_SCP": 10403, "TDD_SCP": 10402, "IMS_IHERO_TMS1": 10401}

known_ae_ipaddr = tdwii_config.known_ae_ipaddr
known_ae_port = tdwii_config.known_ae_port


def get_ip_addr_for_ae_title(retrieve_ae_title):
    return known_ae_ipaddr[retrieve_ae_title]


def get_port_for_ae_title(retrieve_ae_title):
    return known_ae_port[retrieve_ae_title]


def cmove_specific_input(
    retrieve_ae_title,
    dest_ae_title,
    patient_id,
    study_uid,
    series_uid,
    instance_uid,
    cache_dir: Path | str = None,
    calling_ae_title: str = None,
):
    """C-MOVE request for a specific instance
    Will also work at SERIES level if sop_instance_uid is None, but unable to check for cached data for a series
    until the cache dir is made hierarchical

    Args:
        retrieve_ae_title (_type_): _description_
        dest_ae_title (_type_): _description_
        patient_id (str): DICOM Patient ID
        study_uid (_type_): _description_
        series_uid (_type_): _description_
        instance_uid (_type_): _description_
    """
    print(
        f"Move Study {study_uid}, Series {series_uid}, Instance {instance_uid} \
        for Patient ID {patient_id} from {retrieve_ae_title} to {dest_ae_title}"
    )

    debug_logger()

    # Initialise the Application Entity
    ae = AE()

    # Add a requested presentation context
    ae.add_requested_context(StudyRootQueryRetrieveInformationModelMove)

    # Create out identifier (query) dataset
    ds = Dataset()
    ds.QueryRetrieveLevel = "IMAGE"
    # Unique key for PATIENT level
    ds.PatientID = patient_id
    # Unique key for STUDY level
    ds.StudyInstanceUID = study_uid
    # Unique key for SERIES level
    ds.SeriesInstanceUID = series_uid
    # Unique key for IMAGE level
    ds.SOPInstanceUID = instance_uid

    if instance_uid is None or len(instance_uid) == 0:
        ds.QueryRetrieveLevel = "SERIES"
    else:
        cached_iods = _load_cached_iods_list(cache_dir=cache_dir)
        if instance_uid in cached_iods:
            info_message = f"Requested SOP instance {instance_uid} is already in cache directory {cache_dir}"
            return

    ip_addr = get_ip_addr_for_ae_title(retrieve_ae_title)
    port = get_port_for_ae_title(retrieve_ae_title)
    # Associate with peer AE at to issue C-MOVE-RQ, e.g. qrscp with AE Title QRSCP, or MOSAIQ (tm) at IMS_IHERO_TMS1
    if calling_ae_title is None:
        calling_ae_title = dest_ae_title  # assume that its a request to move to self
    assoc = ae.associate(ip_addr, port, ae_title=calling_ae_title)

    if assoc.is_established:
        # Use the C-MOVE service to send the identifier
        responses = assoc.send_c_move(ds, dest_ae_title, StudyRootQueryRetrieveInformationModelMove)
        for status, identifier in responses:
            if status:
                print("C-MOVE query status: 0x{0:04x}".format(status.Status))
            else:
                print("Connection timed out, was aborted or received invalid response")

        # Release the association
        assoc.release()
    else:
        print("Association rejected, aborted or never connected")


def cmove_inputs(ds, local_store_ae_title, cache_dir: Path | str = None):
    """Given a particular UPS C-FIND-RSP, issue a C-MOVE-RQ for the inputs

    Args:
        ds: the UPS-CFIND-RSP
        local_store_ae_title (str): the destination for the C-MOVE to issue it's C-STORE where you want
        the RT (Ion) Plan and RTBDI to go
        cache_dir (Path|str): if there is a cache directory, don't try to move the instances that are already present
    """

    iis = ds.InputInformationSequence
    patient_id = ds.PatientID
    cached_iods = _load_cached_iods_list(cache_dir=cache_dir)

    for iis_index in range(len(iis)):
        iis_item = iis[iis_index]
        study_uid = iis_item.StudyInstanceUID
        series_uid = iis_item.SeriesInstanceUID
        ref_instance_seq = iis_item.ReferencedSOPSequence
        dicom_retrieval_seq = iis_item.DICOMRetrievalSequence
        retrieve_ae_title = dicom_retrieval_seq[0].RetrieveAETitle
        for ref_instance_index in range(len(ref_instance_seq)):
            instance_uid = ref_instance_seq[ref_instance_index].ReferencedSOPInstanceUID
            if str(instance_uid) not in cached_iods:
                cmove_specific_input(
                    retrieve_ae_title,
                    local_store_ae_title,
                    patient_id,
                    study_uid,
                    series_uid,
                    instance_uid,
                )
            else:
                print(f"{instance_uid} is already in cache directory")


def _load_cached_iods_list(cache_dir: Path | str = None) -> list[Path | str]:
    cached_iods = list()

    if cache_dir is not None:
        prefix_pattern = r"[a-zA-Z]"  # get rid of the RP, RB. REG or other prefixes
        for cached_path in Path(cache_dir).glob("**/*.dcm"):
            cached_filename = cached_path.name
            no_suffix = str(cached_filename).removesuffix(".dcm")
            uid = re.sub(prefix_pattern, "", no_suffix).removeprefix(".").removeprefix("_")
            cached_iods.append(uid)
    return cached_iods


def main(args=None):
    """Run the application."""
    local_store_ae_title = "STORE_SCP"
    path = "rsp000001.dcm"
    ae_config_file = "ApplicationEntities.json"
    if args is not None and len(args) > 2:
        local_store_ae_title = args[1]
        path = args[2]
    with open(ae_config_file, "r") as f:
        ae_config_list = json.load(f)
    for ae in ae_config_list:
        known_ae_ipaddr[ae["AETitle"]] = ae["IPAddr"]
        known_ae_port[ae["AETitle"]] = ae["Port"]
    ds = pydicom.dcmread(path, force=True)
    cmove_inputs(ds, local_store_ae_title)


if __name__ == "__main__":
    main(sys.argv)
