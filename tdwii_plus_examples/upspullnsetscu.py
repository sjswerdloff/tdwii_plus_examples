from pydicom import Dataset
from pydicom.uid import UID
from pynetdicom.sop_class import UnifiedProcedureStepPull, UnifiedProcedureStepPush
from pynetdicom.status import UNIFIED_PROCEDURE_STEP_SERVICE_CLASS_STATUS

from tdwii_plus_examples.basescu import BaseSCU


class UPSPullNSetSCU(BaseSCU):
    """
    A subclass of BaseSCU that implements the N-SET DIMSE operation
    for the Unified Procedure Step Pull SOP Class.

    This class is derived from BaseSCU and implements the necessary methods
    to request UPS Pull presentation contexts and perform N-SET requests
    to modify a UPS instance.

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

    def modify_ups(self, sop_instance_uid: str, modification_list: Dataset):
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
        assoc_result = self._associate(required_sop_classes=[UnifiedProcedureStepPull])

        if assoc_result.status == "Error":
            return self.PrimitiveResult("AssocFailure", 0xD000, assoc_result.description, None)

        if assoc_result.status == "Warning":
            accepted_sop_names = [f"[{UID(uid).name}]" for uid in assoc_result.accepted_sop_classes]
            self.logger.warning(f"{assoc_result.description} - Accepted SOP Classes: {', '.join(accepted_sop_names)}")

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
