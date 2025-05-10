from pydicom import Dataset
from pydicom.uid import UID, generate_uid
from pynetdicom.sop_class import UnifiedProcedureStepPull, UnifiedProcedureStepPush
from pynetdicom.status import UNIFIED_PROCEDURE_STEP_SERVICE_CLASS_STATUS

from tdwii_plus_examples._ups_action_type_id import UPSActionTypeID
from tdwii_plus_examples.basescu import BaseSCU

# UPS Procedure Step State constants
SCHEDULED: str = "SCHEDULED"
IN_PROGRESS: str = "IN PROGRESS"
CANCELED: str = "CANCELED"
COMPLETED: str = "COMPLETED"

ALLOWED_STEP_STATES = (IN_PROGRESS, CANCELED, COMPLETED)


class UPSPullNActionSCU(BaseSCU):
    """
    A subclass of BaseSCU that implements the N-ACTION DIMSE operation
    for the Unified Procedure Step Pull SOP Class.

    This class is derived from BaseSCU and implements the necessary methods
    to request UPS Pull presentation contexts and perform N-ACTION requests
    to change the state of a UPS instance.

    Attributes:
        logger: A logger instance.
        calling_ae_title: The title of the calling AE.
        called_ae_title: The title of the called AE.
        called_ip: The IP address or hostname of the called AE.
        called_port: The port number of the called AE.
    """

    def __init__(self, logger=None, calling_ae_title=None, called_ip=None, called_port=None, called_ae_title=None):
        """
        Initializes a UPSPullNActionSCU instance.

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
        # Dictionary to store transaction UIDs for each UPS instance IN PROGRESS
        self.ups_transaction_info = {}

        self.logger.debug("UPSPullNActionSCU initialized")

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

    def claim_ups(self, sop_instance_uid):
        """Claims a SCHEDULED UPS instance by generating a transaction UID, setting its state to IN PROGRESS,
        and sending an N-ACTION request.

        Args:
            sop_instance_uid (str): The SOP Instance UID of the UPS to claim.

        Returns:
            pydicom.uid.UID | None: The transaction UID generated to lock the UPS, or None on failure.
        """
        action_info = Dataset()

        # To take control of a SCHEDULED UPS, an SCU shall generate a Transaction UID
        transaction_uid = generate_uid()

        # and submit a state change to IN PROGRESS
        action_info.ProcedureStepState = IN_PROGRESS

        # including the Transaction UID in the submission.
        action_info.TransactionUID = transaction_uid

        result = self._change_ups_state(sop_instance_uid, action_info)

        # The SCU shall record and use the Transaction UID in future N-ACTION and N-SET requests for that UPS instance.
        if result.status_category == "Success":
            self.ups_transaction_info[sop_instance_uid] = transaction_uid
            return transaction_uid

        return None

    def complete_ups(self, sop_instance_uid, transaction_uid=None):
        """Completes an IN PROGRESS UPS instance.

        Upon completion of an IN PROGRESS UPS it controls, an SCU shall
        submit a state change to COMPLETED.

        Args:
            sop_instance_uid (str): The SOP Instance UID of the UPS.
            transaction_uid (str, optional): The Transaction UID of the UPS.
                If not provided, the stored transaction UID will be used.

        Returns:
            bool: True if the UPS was successfully completed, False otherwise.
        """
        result = self._close_ups(sop_instance_uid, transaction_uid, COMPLETED)
        return result.status_category == "Success"

    def cancel_ups(self, sop_instance_uid, transaction_uid=None):
        """Cancels an IN PROGRESS UPS instance.

        To cancel an IN PROGRESS UPS, an SCU shall submit a state change to CANCELED.

        Args:
            sop_instance_uid (str): The SOP Instance UID of the UPS.
            transaction_uid (str, optional): The Transaction UID of the UPS.
                If not provided, the stored transaction UID will be used.

        Returns:
            bool: True if the UPS was successfully canceled, False otherwise.
        """
        result = self._close_ups(sop_instance_uid, transaction_uid, CANCELED)
        return result.status_category == "Success"

    def _close_ups(self, sop_instance_uid, transaction_uid, state):
        """Sets the state of a UPS instance to COMPLETED or CANCELED.

        Args:
            sop_instance_uid (str): The SOP Instance UID of the UPS.
            transaction_uid (UID, optional): The transaction UID.
                If not provided, the stored one will be used.
            state (str): The desired state of the UPS ("COMPLETED" or "CANCELED").

        Returns:
            PrimitiveResult: The result of the N-ACTION operation.
        """
        if not transaction_uid:
            try:
                transaction_uid = self.ups_transaction_info[sop_instance_uid]
                self.logger.debug(f"Using stored transaction UID: {transaction_uid}")
            except KeyError:
                msg = "No Transaction UID found for the given SOP Instance UID"
                self.logger.error(msg)
                return self.PrimitiveResult("TransactionUIDFailure", 0xD001, msg, None)

        action_info = Dataset()
        action_info.ProcedureStepState = state
        action_info.TransactionUID = transaction_uid

        self.logger.debug(f"Setting UPS state to {state} with transaction UID {transaction_uid}")
        result = self._change_ups_state(sop_instance_uid, action_info)

        if result.status_category == "Success":
            self.logger.info(f"Successfully set UPS state to {state}")
            # Remove stored transaction_uid if present in the dict
            self.ups_transaction_info.pop(sop_instance_uid, None)

        return result

    def _change_ups_state(self, sop_instance_uid, action_info):
        """
        Sends an N-ACTION request to change the state of a UPS instance.

        Args:
            sop_instance_uid (str): The SOP Instance UID of the UPS to act upon.
            action_info (pydicom.Dataset): The Change UPS State Action Information
                see PS3.4 Table CC.2.1-1.

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

        # Send the N-ACTION request
        self.logger.debug(f"Sending N-ACTION request for SOP Instance UID: {sop_instance_uid}")
        rsp_status, action_reply = self.assoc.send_n_action(
            dataset=action_info,
            action_type=UPSActionTypeID.CHANGE_UPS_STATE.value,
            class_uid=UnifiedProcedureStepPull,
            instance_uid=sop_instance_uid,
            meta_uid=UnifiedProcedureStepPush,
        )

        # Handle the response
        result = self._handle_response(rsp_status, action_reply)

        if result.status_category == "Success":
            self.logger.info("N-ACTION request successful")
        else:
            self.logger.error(f"N-ACTION request failed: {result.status_description}")

        self.assoc.release()

        return result
