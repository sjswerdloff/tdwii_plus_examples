import logging
from typing import Iterator

import pydicom
import pynetdicom
from pydicom import DataElement, Dataset
from pydicom.valuerep import VR
from pynetdicom import UnifiedProcedurePresentationContexts
from pynetdicom.sop_class import UnifiedProcedureStepPull

import tdwii_plus_examples.tdwii_config as ae_config


def _create_code_seq_item(value: str | int, designator: str, meaning: str) -> Dataset:
    code_seq_item = Dataset()
    code_seq_item.CodeValue = value
    code_seq_item.CodingSchemeDesignator = designator
    code_seq_item.CodeMeaning = meaning
    return code_seq_item


def _unpack_code_seq_item(code_seq_item: Dataset) -> tuple[str, str, str]:
    code_value = ""
    coding_scheme_designator = ""
    code_meaning = ""
    if "CodeValue" in code_seq_item:
        code_value = code_seq_item.CodeValue
    if "CodingSchemeDesignator" in code_seq_item:
        coding_scheme_designator = code_seq_item.CodingSchemeDesignator
    if "CodeMeaning" in code_seq_item:
        code_meaning = code_seq_item.CodeMeaning
    return code_value, coding_scheme_designator, code_meaning


def get_ups(ds_query: pydicom.Dataset, scu_ae_title: str, scp_ae_title: str) -> Iterator[tuple[Dataset, Dataset | None]]:
    """_summary_

    Args:
        ds_query (pydicom.Dataset): query content/request
        scu_ae_title (str): The AE Title for the SCU (the requestor), typically the PPVS or TDS
        scp_ae_title (str): The AE Title for the SCP (being queried), the TMS

    Yields:
        Iterator[tuple[Dataset, Dataset | None]]: status,response_content tuples
    """
    ae = pynetdicom.AE(ae_title=scu_ae_title)
    ae.requested_contexts = UnifiedProcedurePresentationContexts
    query_model = UnifiedProcedureStepPull
    ups_responses = list()
    if scp_ae_title not in ae_config.known_ae_ipaddr:
        logging.error("Unable to query " + scp_ae_title + "not found in this TDW-II Application Entity configuration")
        return
    assoc = ae.associate(ae_config.known_ae_ipaddr[scp_ae_title], ae_config.known_ae_port[scp_ae_title], ae_title=scp_ae_title)
    if assoc.is_established:
        responses = assoc.send_c_find(ds_query, query_model=query_model)
        for status, response_content in responses:
            if status and status.Status in [0xFF00, 0xFF01]:
                ups_responses.append(response_content)

        assoc.release()
    else:
        logging.error("Unable to establish association with " + scp_ae_title)
        return

    return ups_responses


def create_ups_query(
    ups_uid: str = "",
    machine_name: str = "",
    procedure_step_state: str = "SCHEDULED",
    scheduled_no_sooner_than: str = None,
    scheduled_no_later_than: str = None,
) -> Dataset:
    """Query for the UPS per RO-58, or directly if the UPS UID is already known e.g. via UPS Event
    Args:
        ups_uid (str): The SOP Instance UID for the specific Unified Procedure Step. Empty default
        machine_name (str): The name of the treatment machine as specified in the RT (Ion) Plan.
            Empty default but should be populated.
        procedure_step_state (str): SCHEDULED/IN PROGRESS/COMPLETED/CANCELED, "SCHEDULED" default
        scheduled_no_sooner_than (datetime):  earliest possible matching start datetime. Empty default
        scheduled_no_later_than (datetime): latest possible matching start datetime. Empty default

    Returns:
        Dataset: A query dataset requesting the specific UPS instance
    """
    ds = Dataset()
    # Request only the UPS with matching UID
    ds.add(DataElement("SOPInstanceUID", VR.UI, None))

    if ups_uid:  # Really weird, with an empty string ups_uid is said to be bool
        if len(ups_uid) > 0:
            ds.SOPInstanceUID = ups_uid
            # avoid over filtering.  If the UID is known, the caller can determine if the procedure step state
            # is a value that makes it uninteresting, i.e. if they only wanted it if it was still scheduled.
            procedure_step_state = ""

    procedure_step_state = ""  # Typically SCHEDULED or IN PROGRESS, but for known UPS, match anything
    # Request that the patient name and patient id be populated in the response
    ds.add(DataElement("PatientName", VR.PN, ""))
    ds.add(DataElement("PatientID", VR.LO, ""))

    # Request only RT Treatments with Internal Verification
    # Formally, only this kind of work item is allowed in TDW-II,
    # however, there is also a RT Treatment QA item, so this could be left as an empty sequence
    # as an extension of TDW-II
    scheduled_work_item_code_seq = pydicom.Sequence()
    scheduled_work_item = _create_code_seq_item("121726", "DCM", "")
    scheduled_work_item_code_seq.append(scheduled_work_item)

    ds.add(DataElement("ScheduledWorkitemCodeSequence", VR.SQ, scheduled_work_item_code_seq))

    # Request that the Input Information Sequence be populated in the response
    # This is the key information needed by a PPVS so it can gather up the reference data for the patient
    ds.add(DataElement("InputInformationSequence", VR.SQ, pydicom.Sequence()))

    # Request only those UPS that are for the given treatment machine name
    # For a query that is specific to a unique UPS, an empty value for the machine name means match any
    # but because it's already a unique UPS, the use or lack of filtering isn't an issue either way.
    # could use designator of 99IHERO2008 or 99IHERO2018, but leaving that empty to allow match to either
    scheduled_station_name_item = _create_code_seq_item("", "", machine_name)
    ds.add(DataElement("ScheduledStationNameCodeSequence", VR.SQ, pydicom.Sequence([scheduled_station_name_item])))

    ds.add(DataElement("ProcedureStepState", VR.SH, procedure_step_state))

    ds.add(DataElement("ScheduledProcessingParametersSequence", VR.SQ, pydicom.Sequence()))

    ds.add(DataElement("WorklistLabel", VR.LO, ""))

    start_datetime_string = ""
    end_datetime_string = ""
    if scheduled_no_sooner_than is not None:
        start_datetime_string = scheduled_no_sooner_than
    if scheduled_no_later_than is not None:
        end_datetime_string = scheduled_no_later_than

    if scheduled_no_sooner_than is None and scheduled_no_later_than is None:
        ds.add(DataElement("ScheduledProcedureStepStartDateTime", VR.DT, ""))
    else:
        ds.add(DataElement("ScheduledProcedureStepStartDateTime", VR.DT, f"{start_datetime_string}-{end_datetime_string}"))

    return ds


def response_content_to_dict(response_content: Dataset) -> dict[str, str]:
    """Convert a UPS C-FIND response in to a more easily handled dictionary

    Args:
        response_content (Dataset): The UPS C-FIND-RSP dataset

    Returns:
        dict[str,str]: a python dict that flattens the hierarchy to just names and string values
    """
    displayable = {
        "PatientName": "",
        "PatientID": "",
        "ScheduledDateTime": "",
        "Machine": "",
        "TreatmentDeliveryType": "",
        "PlanLabel": "",
        "WorklistLabel": "",
        "CurrentFractionNumber": "",
        "TotalFractionsPlanned": "",
        "ProcedureStepState": "",
    }
    if "PatientName" in response_content:
        displayable["PatientName"] = response_content["PatientName"].repval
    if "PatientID" in response_content:
        displayable["PatientID"] = response_content["PatientID"].repval
    if "ScheduledProcessingParametersSequence" in response_content:
        for item in response_content["ScheduledProcessingParametersSequence"]:
            if "ConceptNameCodeSequence" in item:
                code_value, coding_scheme, _ = _unpack_code_seq_item(item["ConceptNameCodeSequence"][0])
                if code_value == "121740" and coding_scheme == "DCM":
                    displayable["TreatmentDeliveryType"] = item.TextValue
                elif code_value == "2018001" and coding_scheme == "99IHERO2018":
                    displayable["PlanLabel"] = item.TextValue
                elif code_value == "2018002" and coding_scheme == "99IHERO2018":
                    displayable["CurrentFractionNumber"] = str(item.NumericValue)
                elif code_value == "2018003" and coding_scheme == "99IHERO2018":
                    displayable["TotalFractionsPlanned"] = str(item.NumericValue)
    if "WorklistLabel" in response_content:
        displayable["WorklistLabel"] = response_content["WorklistLabel"].repval
    if "ProcedureStepState" in response_content:
        displayable["ProcedureStepState"] = response_content.ProcedureStepState
    if "ScheduledProcedureStepStartDateTime" in response_content:
        displayable["ScheduledDateTime"] = response_content.ScheduledProcedureStepStartDateTime

    return displayable
