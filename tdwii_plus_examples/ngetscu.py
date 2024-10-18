import logging
import sys
from typing import Iterator, List

import pydicom
import pynetdicom
from pydicom import DataElement, Dataset
from pynetdicom import UnifiedProcedurePresentationContexts
from pynetdicom.sop_class import UnifiedProcedureStepPush

import tdwii_plus_examples.tdwii_config as ae_config


def nget_ups(
    attribute_list: List[DataElement], ups_instance_uid: str, scu_ae_title: str, scp_ae_title: str
) -> Iterator[tuple[Dataset, Dataset | None]]:
    """Perform UPS N-GET-RQ and return responses that have UPS content

    Args:
        ds_query (pydicom.Dataset): query content/request
        scu_ae_title (str): The AE Title for the SCU (the requestor), typically the PPVS or TDS
        scp_ae_title (str): The AE Title for the SCP (being queried), the TMS

    Yields:
        Iterator[tuple[Dataset, Dataset | None]]: status,response_content tuples
    """
    ae = pynetdicom.AE(ae_title=scu_ae_title)
    ae.requested_contexts = UnifiedProcedurePresentationContexts
    query_model = UnifiedProcedureStepPush
    ups_responses = list()

    if scp_ae_title not in ae_config.known_ae_ipaddr:
        logging.error("Unable to query " + scp_ae_title + " not found in this TDW-II Application Entity configuration")
        return
    identifier_list = set([x.tag for x in attribute_list])
    # SOP Class UID, SOP Instance UID, Transaction UID are not allowed
    disallowed_tags = set([0x00080016, 0x00080018, 0x00081195])
    identifier_list.difference_update(disallowed_tags)
    for tag in identifier_list:
        print(tag)

    assoc = ae.associate(ae_config.known_ae_ipaddr[scp_ae_title], ae_config.known_ae_port[scp_ae_title], ae_title=scp_ae_title)
    if assoc.is_established:
        responses = assoc.send_n_get(
            identifier_list=list(identifier_list), class_uid=query_model, instance_uid=ups_instance_uid
        )
        for response_content in responses:
            ups_responses.append(response_content)

        assoc.release()
    else:
        logging.error("Unable to establish association with " + scp_ae_title)
        return

    return ups_responses


if __name__ == "__main__":
    ae_config.load_ae_config()
    scp_ae_title = sys.argv[1]
    scu_ae_title = sys.argv[2]
    ups_instance_uid = sys.argv[3]
    # print(f"SCP = {scp_ae_title} ; SCU = {scu_ae_title} ; UID = {ups_instance_uid}")
    ds_query = Dataset()
    ds_query.PatientID = ""
    ds_query.PatientName = ""
    ds_query.SOPInstanceUID = ups_instance_uid  # this will get moved over to the RequestedSOPInstanceUID inside the nget_ups()
    ds_query.OutputInformationSequence = pydicom.Sequence()
    attribute_list = list(ds_query.iterall())
    # for query_attribute in attribute_list:
    #     print(query_attribute)
    # wrap the call in a list because what gets returned is an iterator and I'm too lazy to iterate on it right now
    responses = list(
        nget_ups(
            attribute_list=attribute_list,
            ups_instance_uid=ups_instance_uid,
            scu_ae_title=scu_ae_title,
            scp_ae_title=scp_ae_title,
        )
    )
    print(responses)
