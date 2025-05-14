from pydicom import DataElement, Dataset, Sequence
from pydicom.uid import UID
from pydicom.valuerep import VR
from pynetdicom.sop_class import UnifiedProcedureStepPull

from tdwii_plus_examples._dicom_macros import create_code_seq_item
from tdwii_plus_examples.basescu import BaseSCU


class UPSPullCFindSCU(BaseSCU):
    """
    A subclass of BaseSCU that implements the C-FIND DIMSE operation
    for the Unified Procedure Step Pull SOP Class.

    This class is derived from BaseSCU and implements the necessary methods
    to request UPS Pull presentation contexts and perform C-FIND requests
    to query UPS instances.
    """

    def __init__(self, logger=None, calling_ae_title=None, called_ip=None, called_port=None, called_ae_title=None):
        """
        Initializes a UPSPullCFindSCU instance.

        Parameters
        ----------
        logger : Logger, optional
            The logger instance for logging messages.
        calling_ae_title : str, optional
            The AE title of the calling AE.
        called_ip : str, optional
            The IP address of the called AE.
        called_port : int, optional
            The port number of the called AE.
        called_ae_title : str, optional
            The AE title of the called AE.
        """
        super().__init__(
            logger,
            calling_ae_title=calling_ae_title,
            called_ip=called_ip,
            called_port=called_port,
            called_ae_title=called_ae_title,
        )
        self.logger.debug("UPSPullCFindSCU initialized")

    def _add_requested_context(self):
        """Adds the Unified Procedure Step Pull SOP Class presentation context."""
        super()._add_requested_context()
        self.ae.add_requested_context(UnifiedProcedureStepPull)
        self.logger.debug(f"UPS Pull Presentation context added: {UnifiedProcedureStepPull}")

    def create_ups_query(
        self,
        ups_uid: str = "",
        machine_name: str = "",
        procedure_step_state: str = "SCHEDULED",
        scheduled_no_sooner_than: str = None,
        scheduled_no_later_than: str = None,
    ) -> Dataset:
        """Construct query for the UPS per RO-58, or directly if the UPS UID is already known e.g. via UPS Event
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
        # TODO: split into 2 methods, one to check if a specific UPS is still in SCHEDULED state
        # and one to search for UPS. We could also create this is a TDWIICFindSCU for RO-58 if ever we
        # would implement other IHE transactions with different requirements. This is why I made it an
        # instance method and not a @classmethod or @staticmethod method.
        ds = Dataset()
        # Request only the UPS with matching UID
        ds.add(DataElement("SOPInstanceUID", VR.UI, None))

        if ups_uid:  # Really weird, with an empty string ups_uid is said to be bool
            if len(ups_uid) > 0:
                ds.SOPInstanceUID = ups_uid
                # avoid over filtering.  If the UID is known, the caller can determine if the procedure step state
                # is a value that makes it uninteresting, i.e. if they only wanted it if it was still scheduled.
                procedure_step_state = ""

        # Request that the patient name and patient id be populated in the response
        ds.add(DataElement("PatientName", VR.PN, ""))
        ds.add(DataElement("PatientID", VR.LO, ""))

        # Request only RT Treatments with Internal Verification
        # Formally, only this kind of work item is allowed in TDW-II,
        # however, there is also a RT Treatment QA item, so this could be left as an empty sequence
        # as an extension of TDW-II
        scheduled_work_item_code_seq = Sequence()
        # Code Value shall be retrieved with Single Value Matching.
        # Coding Scheme Designator shall be retrieved with Single Value Matching.
        # Code Meaning shall not be used as Matching Key
        scheduled_work_item = create_code_seq_item("121726", "DCM", "")
        scheduled_work_item_code_seq.append(scheduled_work_item)

        ds.add(DataElement("ScheduledWorkitemCodeSequence", VR.SQ, scheduled_work_item_code_seq))

        # Request that the Input Information Sequence be populated in the response
        # This is the key information needed by a Performer or a Watcher (Co-Performer)
        # so it can gather up the reference data for the treatment session
        ds.add(DataElement("InputInformationSequence", VR.SQ, Sequence()))

        # Request only those UPS that are for the given treatment machine name
        # For a query that is specific to a unique UPS, an empty value for the machine name means match any
        # but because it's already a unique UPS, the use or lack of filtering isn't an issue either way.
        # could use designator of 99IHERO2008 or 99IHERO2018, but leaving that empty to allow match to either
        # Discussion: For the ScheduledStationNameCodeSequence, the Code Designator is defined by the TMS.
        # Also removing the Code Meaning which should not be used as matching key
        scheduled_station_name_item = create_code_seq_item(machine_name, "", "")
        # R in PS3.4 Table CC.2.5-3
        ds.add(DataElement("ScheduledStationNameCodeSequence", VR.SQ, Sequence([scheduled_station_name_item])))

        ds.add(DataElement("ProcedureStepState", VR.SH, procedure_step_state))

        ds.add(DataElement("ScheduledProcessingParametersSequence", VR.SQ, Sequence()))

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

    def get_ups(self, ds_query: Dataset) -> list[Dataset]:
        """
        Perform UPS C-FIND-RQ and return responses that have UPS content.

        Args:
            ds_query (pydicom.Dataset): query content/request

        Returns:
            list[Dataset]: List of response datasets with UPS content.
        """
        # Establish association with the SCP
        success, details = self._associate(required_sop_classes=[UnifiedProcedureStepPull])

        if details.status == "Error":
            self.logger.error(f"Association failed: {details.description}")
            return []

        if details.status == "Warning":
            accepted_sop_names = [f"[{UID(uid).name}]" for uid in details.accepted_sop_classes]
            self.logger.warning(f"{details.description} - Accepted SOP Classes: {', '.join(accepted_sop_names)}")

        ups_responses = []
        try:
            # Send the C-FIND request
            self.logger.debug(f"Sending C-FIND request with Identifier: {ds_query}")
            responses = self.assoc.send_c_find(ds_query, query_model=UnifiedProcedureStepPull)

            for response in responses:
                if isinstance(response, tuple):
                    rsp_status, rsp_dataset = response
                else:
                    rsp_status = response
                    rsp_dataset = None
                # Handle the response
                self.logger.debug(f"Response status: {rsp_status}")
                self.logger.debug(f"Response dataset: {rsp_dataset}")

                result = self._handle_response(rsp_status, rsp_dataset)

                if result.status_category == "Pending":
                    self.logger.info("Pending response received")
                    if rsp_dataset is not None:
                        ups_responses.append(rsp_dataset)
                    else:
                        self.logger.error("Pending response contains no Dataset")
                        break
                    continue
                elif result.status_category == "Success":
                    self.logger.info("C-FIND request successful")
                elif result.status_category == "Failure":
                    self.logger.error(f"C-FIND request failed: {result.status_description}")
                    break
        finally:
            self.assoc.release()

        return ups_responses

    def _get_status_description(self, status_code):
        """
        Retrieves the description for a specific UPS status code.

        Args:
            status_code (int): The status code to look up.

        Returns:
            str: The description of the status code.
        """
        from pynetdicom.status import UNIFIED_PROCEDURE_STEP_SERVICE_CLASS_STATUS

        return UNIFIED_PROCEDURE_STEP_SERVICE_CLASS_STATUS.get(status_code, ("Unknown", "Unknown status code"))[1]
