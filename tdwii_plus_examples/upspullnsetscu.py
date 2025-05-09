from datetime import datetime

from pydicom import Dataset
from pydicom.uid import UID
from pynetdicom.sop_class import UnifiedProcedureStepPull, UnifiedProcedureStepPush
from pynetdicom.status import UNIFIED_PROCEDURE_STEP_SERVICE_CLASS_STATUS

from tdwii_plus_examples._dicom_macros import create_code_seq_item, create_referenced_instances_and_access_item
from tdwii_plus_examples.basescu import BaseSCU


class UPSPullNSetSCU(BaseSCU):
    """
    A subclass of BaseSCU that implements the N-SET DIMSE operation
    for the Unified Procedure Step Pull SOP Class.

    This class is derived from BaseSCU and implements the necessary methods
    to request UPS Pull presentation contexts and perform N-SET requests
    to modify a UPS instance.
    It also provide methods to modify specific sets of attributes of the Progress
    Information and Performed Procedure Information Modules.

    Attributes:
        logger: A logger instance.
        calling_ae_title: The title of the calling AE.
        called_ae_title: The title of the called AE.
        called_ip: The IP address or hostname of the called AE.
        called_port: The port number of the called AE.
    """

    def __init__(self, logger=None, calling_ae_title=None, called_ip=None, called_port=None, called_ae_title=None):
        """
        Initializes a UPSNSetSCU instance.

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
        self.logger.debug("UPSNSetSCU initialized")

    def _add_requested_context(self):
        """Adds the Unified Procedure Step Pull SOP Class presentation context."""
        super()._add_requested_context()
        self.ae.add_requested_context(UnifiedProcedureStepPull)
        self.logger.debug(f"UPS Pull Presentation context added: {UnifiedProcedureStepPull}")

    def _get_status_description(self, status_code):
        """
        Retrieves the description for a specific UPS status code.

        Args:
            status_code (int): The status code to look up.

        Returns:
            str: The description of the status code.
        """
        return UNIFIED_PROCEDURE_STEP_SERVICE_CLASS_STATUS.get(status_code, ("Unknown", "Unknown status code"))[1]

    def modify_ups(self, sop_instance_uid: str | UID, modification_list: Dataset):
        """
        Modifies a UPS instance by sending an N-SET request.

        Args:
            sop_instance_uid (str): The SOP Instance UID of the UPS to modify.
            modification_list (pydicom.Dataset): The dataset containing the modifications.

        Returns:
            PrimitiveResult: A named tuple containing the status category, status code,
            status description, and response dataset.
        """
        # Establish association with the SCP
        success, details = self._associate(required_sop_classes=[UnifiedProcedureStepPull])

        if details.status == "Error":
            return self.PrimitiveResult("AssocFailure", 0xD000, details.description, None)

        if details.status == "Warning":
            accepted_sop_names = [f"[{UID(uid).name}]" for uid in details.accepted_sop_classes]
            self.logger.warning(f"{details.description} - Accepted SOP Classes: {', '.join(accepted_sop_names)}")

        # Send the N-SET request
        self.logger.debug(f"Sending N-SET request for SOP Instance UID: {sop_instance_uid}")
        success = False
        responses = self.assoc.send_n_set(
            dataset=modification_list,
            class_uid=UnifiedProcedureStepPull,
            instance_uid=sop_instance_uid,
            meta_uid=UnifiedProcedureStepPush,
        )
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
            # The following logic is directly adapted from former NSetSCU class to follow current
            # behavior of UPS SCP N-SET handler returning a Pending status instead of Success.
            if result.status_category == "Pending":
                self.logger.info("Pending response received")
                success = True
                continue
            elif result.status_code == 0xFFFF or result.status_category == "Success" and success:
                self.logger.info("N-SET request successful")
            elif result.status_code != 0x0000:
                success = False
                if result.status_code != 0xFFFF:
                    self.logger.error(f"N-SET request failed: {result.status_description}")

        self.assoc.release()

        return self.PrimitiveResult("Success", 0x0000, "", None) if success else result

    def update_progress_information(
        self, sop_instance_uid: str | UID, tx_uid: str | UID, progress: int, description: str = None
    ):
        """
        Updates the progress of a UPS instance by sending an N-SET request with progress information.

        This method builds a modification list dataset containing the progress and optional description,
        then calls modify_ups to send the update.

        This method may be overridden by derived subclasses to update additional UPS attributes
        as needed for specific workflows.

        Args:
            sop_instance_uid (str): The SOP Instance UID of the UPS to update.
            tx_uid (str): The Transaction UID for the UPS.
            progress (int): The progress percentage (0-100) to set for the UPS.
            description (str, optional): The progress description to set for the UPS.

        Returns:
            PrimitiveResult: The result of the N-SET operation.
        """
        # TODO: Create a subclass overriding this method to add Procedure Step Progress Parameters Sequence Items
        # required by TDW-II
        modification_list = Dataset()
        # TODO: remove as AffectedSOPInstanceUID and AffectedSOPClassUID are not expected in a Data Set as they are
        # Command Set Elements. Also requires modification in UPS SCP N-SET handler.
        modification_list.AffectedSOPInstanceUID = str(sop_instance_uid)
        modification_list.AffectedSOPClassUID = UnifiedProcedureStepPush
        modification_list.TransactionUID = str(tx_uid)
        sequence_item = Dataset()
        sequence_item.ProcedureStepProgress = str(progress)
        if description is not None:
            sequence_item.ProcedureStepProgressDescription = description
        modification_list.ProcedureStepProgressInformationSequence = [sequence_item]
        return self.modify_ups(sop_instance_uid, modification_list)

    def update_start_info(
        self,
        sop_instance_uid: str | UID,
        tx_uid: str | UID,
        station_name,
        workitem_code,
        human_performer=None,
        human_performer_name=None,
    ):
        """
        Updates the start information of a UPS instance by sending an N-SET request with information
        expected to be available after the UPS has been set in progress.

        This method may be overridden by derived subclasses to update additional UPS attributes
        as needed for specific workflows.

        Args:
            sop_instance_uid (str): The SOP Instance UID of the UPS to update.
            tx_uid (str): The Transaction UID for the UPS.
            station_name (tuple or Dataset): The station name code as a
                Tuple (value, designator, meaning) or a Dataset.
            workitem_code (tuple or Dataset): The workitem code as a
                Tuple (value, designator, meaning) or a Dataset.
            human_performer (tuple or Dataset, optional): The human performer code as a
                Tuple (value, designator, meaning) or a Dataset.
            human_performer_name (str, optional): The name of the human performer.

        Returns:
            PrimitiveResult: The result of the N-SET operation.
        """
        if station_name is None or workitem_code is None:
            raise ValueError("Both station_name and workitem_code are required and must be provided.")

        modification_list = Dataset()
        modification_list.AffectedSOPInstanceUID = str(sop_instance_uid)
        modification_list.AffectedSOPClassUID = UnifiedProcedureStepPush
        modification_list.TransactionUID = str(tx_uid)

        sequence_item = Dataset()
        sequence_item.PerformedProcedureStepStartDateTime = datetime.now().strftime("%Y%m%d%H%M%S")

        if isinstance(station_name, tuple):
            sequence_item.StationNameCodeSequence = [create_code_seq_item(*station_name)]
        else:
            sequence_item.StationNameCodeSequence = [station_name]

        if isinstance(workitem_code, tuple):
            sequence_item.ScheduledWorkitemCodeSequence = [create_code_seq_item(*workitem_code)]
        else:
            sequence_item.ScheduledWorkitemCodeSequence = [workitem_code]

        # Actual Human Performers Sequence (0040,4035)
        if human_performer is not None or human_performer_name is not None:
            performer_item = Dataset()
            if human_performer is not None:
                if isinstance(human_performer, tuple):
                    performer_item.HumanPerformerCodeSequence = [create_code_seq_item(*human_performer)]
                else:
                    performer_item.HumanPerformerCodeSequence = [human_performer]
            if human_performer_name is not None:
                performer_item.HumanPerformerName = human_performer_name
            sequence_item.ActualHumanPerformersSequence = [performer_item]

        modification_list.UnifiedProcedureStepPerformedProcedureSequence = [sequence_item]
        return self.modify_ups(sop_instance_uid, modification_list)

    def update_end_info(self, sop_instance_uid: str | UID, tx_uid: str | UID):
        """
        Updates the end information of a UPS instance by sending an N-SET request with information
        expected to be available just before the UPS completion.

        This method may be overridden by derived subclasses to update additional UPS attributes
        as needed for specific workflows.

        Args:
            sop_instance_uid (str): The SOP Instance UID of the UPS to update.
            tx_uid (str): The Transaction UID for the UPS.

        Returns:
            PrimitiveResult: The result of the N-SET operation.
        """
        modification_list = Dataset()
        modification_list.AffectedSOPInstanceUID = str(sop_instance_uid)
        modification_list.AffectedSOPClassUID = UnifiedProcedureStepPush
        modification_list.TransactionUID = str(tx_uid)

        sequence_item = Dataset()
        sequence_item.PerformedProcedureStepEndDateTime = datetime.now().strftime("%Y%m%d%H%M%S")

        modification_list.UnifiedProcedureStepPerformedProcedureSequence = [sequence_item]
        return self.modify_ups(sop_instance_uid, modification_list)

    def update_cancel_info(self, sop_instance_uid: str | UID, tx_uid: str | UID, reason: str = None):
        """
        Updates the cancel information of a UPS instance by sending an N-SET request with information
        expected to be available just before the UPS cancelation.

        This method may be overridden by derived subclasses to update additional UPS attributes
        as needed for specific workflows.

        Args:
            sop_instance_uid (str): The SOP Instance UID of the UPS to update.
            tx_uid (str): The Transaction UID for the UPS.

        Returns:
            PrimitiveResult: The result of the N-SET operation.
        """
        modification_list = Dataset()
        modification_list.AffectedSOPInstanceUID = str(sop_instance_uid)
        modification_list.AffectedSOPClassUID = UnifiedProcedureStepPush
        modification_list.TransactionUID = str(tx_uid)
        sequence_item = Dataset()
        sequence_item.ProcedureStepCancellationDateTime = datetime.now().strftime("%Y%m%d%H%M%S")  # Could be filled by SCP
        if reason is not None:
            sequence_item.ReasonForCancellation = reason
        modification_list.ProcedureStepProgressInformationSequence = [sequence_item]
        return self.modify_ups(sop_instance_uid, modification_list)

    def update_output_information(self, sop_instance_uid: str | UID, tx_uid: str | UID, output_information_args):
        """
        Updates the output information of a UPS instance by sending an N-SET request.

        Args:
            sop_instance_uid (str): The SOP Instance UID of the UPS to update.
            tx_uid (str): The Transaction UID for the UPS.
            output_information_args (list): List of tuples/lists, each containing the arguments for
                create_referenced_instances_and_access_item. Each item should be:
                    (retrieve_ae_title, study_instance_uid, series_instance_uid, sop_class_uid, sop_instance_uid)

        Returns:
            PrimitiveResult: The result of the N-SET operation.
        """
        modification_list = Dataset()
        modification_list.AffectedSOPInstanceUID = str(sop_instance_uid)
        modification_list.AffectedSOPClassUID = UnifiedProcedureStepPush
        modification_list.TransactionUID = str(tx_uid)

        sequence_item = Dataset()
        # Build OutputInformationSequence using the helper for each item in output_information_args
        sequence_item.OutputInformationSequence = [
            create_referenced_instances_and_access_item(*args) for args in output_information_args
        ]

        modification_list.UnifiedProcedureStepPerformedProcedureSequence = [sequence_item]
        return self.modify_ups(sop_instance_uid, modification_list)
