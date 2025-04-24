from pydicom import Dataset
from pydicom.uid import UID
from pynetdicom.association import Association
from pynetdicom.sop_class import UnifiedProcedureStepPush

from tdwii_plus_examples.basescu import BaseSCU


class UPSPushNCreateSCU(BaseSCU):
    """
    A subclass of BaseSCU that implements the N-CREATE DIMSE operation
    for the Unified Procedure Step Push SOP Class.

    This class provides functionality for creating UPS instances on a
    remote SCP.

    Attributes:
        logger (logging.Logger): A logger instance.
        calling_ae_title (str): The title of the calling AE.
        called_ae_title (str): The title of the called AE.
        called_ip (str): The IP address or hostname of the called AE.
        called_port (int): The port number of the called AE.
    """

    def __init__(
        self,
        logger=None,
        calling_ae_title: str = None,
        called_ip: str = None,
        called_port: int = None,
        called_ae_title: str = None,
    ):
        super().__init__(
            logger,
            calling_ae_title=calling_ae_title,
            called_ip=called_ip,
            called_port=called_port,
            called_ae_title=called_ae_title,
        )

    def _add_requested_context(self):
        """Add the Unified Procedure Step Push SOP Class presentation context."""
        super()._add_requested_context()
        self.ae.add_requested_context(UnifiedProcedureStepPush)
        self.logger.debug(f"UPS Push Presentation context added: \n{self.ae.requested_contexts[0]}")

    def create_ups_instances(self, instances: list[Dataset]) -> int:
        """
        Create UPS instances on the remote SCP.

        Parameters:
            instances (list[Dataset]): A list of DICOM datasets representing the UPS instances to create.
            called_ae_title (str, optional): The AE title of the remote SCP. Defaults to None.

        Returns:
            int: The number of UPS instances successfully created.
        """
        valid_instances = [instance for instance in instances if instance.SOPClassUID == UnifiedProcedureStepPush]
        if not instances:
            self.logger.warning("No valid instances with SOPClassUID matching UnifiedProcedureStepPush.")
            return 0
        if len(valid_instances) < len(instances):
            self.logger.warning(
                f"Some instances were ignored because their SOPClassUID did not match UnifiedProcedureStepPush. "
                f"Total instances provided: {len(instances)}, valid instances: {len(valid_instances)}"
            )
        assoc_result = self._associate()
        success_count = 0

        if not self._handle_association_status(assoc_result):
            return 0

        for msg_id, instance in enumerate(valid_instances, start=0):
            result = self._send_upspushncreate_request(
                assoc=self.assoc,
                attribute_list=instance,
                class_uid=instance.SOPClassUID,
                instance_uid=instance.SOPInstanceUID,
                msg_id=msg_id,
            )
            if result.status_category == "Success":
                success_count += 1
            else:
                self.logger.error(
                    f"Failed to create UPS instance {instance.SOPInstanceUID}: "
                    f"{result.status_description} (Status: {result.status_code})"
                )

        self.assoc.release()
        self.logger.debug("Association released")

        return success_count

    def _handle_association_status(self, assoc_result) -> bool:
        if assoc_result.status == "Error":
            self.logger.error(f"Association failed: {assoc_result.description}")
            return False
        if assoc_result.status == "Warning":
            accepted_sop_names = [f"[{UID(uid).name}]" for uid in assoc_result.accepted_sop_classes]
            self.logger.warning(f"{assoc_result.description} - Accepted SOP Classes: {', '.join(accepted_sop_names)}")
            if "[Unified Procedure Step - Push SOP Class]" not in accepted_sop_names:
                self.assoc.release()
                self.logger.error(f"Association failed: {assoc_result.description}")
                return False
        return True

    def _send_upspushncreate_request(
        self,
        assoc: Association,
        attribute_list: Dataset = None,
        class_uid: UID = UnifiedProcedureStepPush,
        instance_uid: UID = None,
        msg_id: int = 1,
    ) -> tuple:
        """
        Send an UPS Push N-CREATE request.

        Parameters
        ----------
        assoc : Association
            The Association object representing the established connection to the SCP.
        attribute_list : pydicom.Dataset
            The Attribute identifiers and values of the UPS Instance to create.
        class_uid : pydicom.uid.UID
            The SOP Class UID of the UPS Instance to create.
        instance_uid: pydicom.uid.UID
            The SOP Instance UID of the UPS Instance to create.
        msg_id : int
            The identifier of the request Message (default: 1).

        Required attribute_list attributes are specified in PS3.4 Table CC.2.5-3
        N-CREATE Usage column.

        Returns
        -------
        PrimitiveResult:
            A named tuple containing the status category, status code, status description, and dataset,
            indicating the outcome of the request.

        Valid status codes are specified in PS3.4 Table CC.2.5-4.
        +----------------+-----------------------------------+-------------+
        | Service Status | Further Meaning                   | Status Code |
        +----------------+-----------------------------------+-------------+
        | Success        | The UPS was created as requested  | 0000        |
        +----------------+-----------------------------------+-------------+
        | Warning        | The UPS was created with          | B300        |
        |                | modifications                     |             |
        +----------------+-----------------------------------+-------------+
        | Failure        | Failed: The provided value of     | C309        |
        |                | UPS State was not "SCHEDULED".    |             |
        +----------------+-----------------------------------+-------------+
        """
        rsp_status = Dataset()
        self.logger.debug("Sending N-CREATE request")
        rsp_status, attribute_list = assoc.send_n_create(
            dataset=attribute_list,
            class_uid=class_uid,
            instance_uid=instance_uid,
            msg_id=msg_id,
        )

        return self._handle_response(rsp_status, attribute_list)
