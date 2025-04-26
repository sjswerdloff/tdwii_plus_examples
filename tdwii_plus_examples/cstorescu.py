from pydicom import Dataset
from pydicom.uid import UID, ExplicitVRLittleEndian
from pynetdicom.association import Association
from pynetdicom.presentation import PresentationContext, StoragePresentationContexts, build_context
from pynetdicom.status import STORAGE_SERVICE_CLASS_STATUS

from tdwii_plus_examples.basescu import BaseSCU

# List of storage SOP Classes
storage_sop_classes = [cx.abstract_syntax for cx in StoragePresentationContexts]


class CStoreSCU(BaseSCU):
    """
    A subclass of BaseSCU that implements the C-STORE DIMSE operation
    for specified Storage SOP Classes.

    This class provides functionality for storage of SOP instances on a
    remote SCP.

    Attributes:
        logger (logging.Logger): A logger instance.
        calling_ae_title (str): The title of the calling AE.
        called_ae_title (str): The title of the called AE.
        called_ip (str): The IP address or hostname of the called AE.
        called_port (int): The port number of the called AE.
        contexts (list[PresentationContext]): The Storage Presentation
            Contexts to use for C-STORE operations
    """

    def __init__(
        self,
        logger=None,
        calling_ae_title: str = None,
        called_ip: str = None,
        called_port: int = None,
        called_ae_title: str = None,
        contexts: PresentationContext = None,
    ):
        self.contexts = self._validate_contexts(contexts)
        super().__init__(
            logger,
            calling_ae_title=calling_ae_title,
            called_ip=called_ip,
            called_port=called_port,
            called_ae_title=called_ae_title,
        )

    def _add_requested_context(self):
        """
        Adds the storage presentation contexts specified in the constructor.

        This method is called by the `BaseSCU` constructor. It adds the
        necessary presentation contexts for the storage operations.
        """
        # Add Verification context from BaseSCU
        super()._add_requested_context()
        # Add Storage contexts
        if self.contexts:
            for context in self.contexts:
                self.ae.add_requested_context(context.abstract_syntax, context.transfer_syntax[0])
                self.logger.debug(f"Storage Presentation contexts added: \n{self.ae.requested_contexts[1:]}")

    def set_contexts(self, contexts: list[PresentationContext]):
        for context in contexts:
            self.ae.add_requested_context(context.abstract_syntax, context.transfer_syntax[0])
            self.logger.debug(f"Storage Presentation contexts added: \n{self.ae.requested_contexts[1:]}")
        self.contexts = self.contexts.append(contexts)

    def set_contexts_from_files(self, instances: list[Dataset]):
        """
        Adds storage presentation contexts from a list of DICOM datasets.

        This method determines the SOP Class UID from each dataset and adds
        a corresponding presentation context using ExplicitVRLittleEndian transfer
        syntax.

        Args:
            instances (list[Dataset]): A list of DICOM datasets.
        """
        # Favouring ExplicitLittleEndian to avoid issues with QRSCP when there are private elements
        # There is a catch-22 if you have privates *and* a string type element with length > 64K
        # For RT SS with way too much data in the contours or RT Ion Plan with compensator voxel thickness with
        # a large number of rows and columns... some of the elements can exceed 64K and then the explicit syntax
        # doesn't have room in the 16 bit unsigned integer for lengths (in bytes) > 64k
        contexts_in_files = [
            build_context(instance.SOPClassUID, transfer_syntax=[ExplicitVRLittleEndian]) for instance in instances
        ]
        for abstract_syntax, transfer_syntaxes in contexts_in_files.items():
            self.ae.add_requested_context(abstract_syntax, transfer_syntaxes[0])
            self.logger.debug(f"Storage Presentation contexts added: \n{self.ae.requested_contexts[1:]}")
        self.contexts = self.contexts.append(contexts_in_files)

    def store_instances(self, instances: list[Dataset]) -> int:
        """
        Stores DICOM instances on the remote SCP.

        Parameters:
            instances (list[Dataset]): A list of DICOM datasets representing the DICOM instances to store.
            called_ae_title (str, optional): The AE title of the remote SCP. Defaults to None.

        Returns:
            int: The number of DICOM instances successfully stored.
        """
        assoc_result = self._associate()
        success_count = 0

        if not self._handle_association_status(assoc_result):
            return 0

        for msg_id, instance in enumerate(instances, start=0):
            result = self._send_cstore_request(
                assoc=self.assoc,
                dataset=instance,
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

    def _validate_contexts(self, contexts):
        """Validates that all provided contexts are Storage SOP Classes.

        Args:
            contexts: A list of PresentationContext objects.

        Returns:
            The validated list of contexts if all are storage contexts, otherwise raises a ValueError.

        Raises:
            ValueError: If any of the provided contexts is not a Storage SOP Class.
        """
        if not contexts:
            return []
        invalid_contexts = [
            context for context in contexts if not self.is_storage_presentation_context(context.abstract_syntax)
        ]
        if invalid_contexts:
            error_message = (
                "Only Storage Presentation Contexts are allowed. "
                f"Invalid contexts: {[ctx.abstract_syntax for ctx in invalid_contexts]}"
            )
            raise ValueError(error_message)
        return contexts

    def is_storage_presentation_context(self, context):
        return context in storage_sop_classes

    def _handle_association_status(self, assoc_result) -> bool:
        """Handles the association status returned by the SCP.

        Handles the association result and verifies that all requested
        presentation contexts have been accepted.

        Args:
            assoc_result: The result of the association request.

        Returns:
            True if the association was successful and all requested presentation
            contexts were accepted, False otherwise.
        """
        if assoc_result.status == "Error":
            self.logger.error(f"Association failed: {assoc_result.description}")
            return False
        if assoc_result.status == "Warning":
            accepted_contexts = {UID(uid): 0x00 for uid in assoc_result.accepted_sop_classes}
            if any(accepted_contexts.get(context.abstract_syntax) != 0x00 for context in self.contexts):
                not_accepted = [
                    str(context.abstract_syntax)
                    for context in self.contexts
                    if accepted_contexts.get(context.abstract_syntax) != 0x00
                ]
                self.logger.warning(f"{assoc_result.description} - Not Accepted SOP Classes: {', '.join(not_accepted)}")
                self.assoc.release()
                self.logger.error("Association failed: Not all required presentation contexts were accepted.")
                return False
        return True

    def _send_cstore_request(self, assoc: Association, dataset: Dataset, msg_id: int = 1) -> tuple:
        """
        Send an C-STORE request.

        Parameters
        ----------
        assoc : Association
            The Association object representing the established connection to the SCP.
        dataset : pydicom.Dataset
            The Attributes of the Composite SOP Instance to be stored.
        msg_id : int
            The identifier of the request Message (default: 1).

        Returns
        -------
        PrimitiveResult:
            A named tuple containing the status category, status code, status description, and dataset,
            indicating the outcome of the request.

        Valid status codes are specified in PS3.7 Section 9.1.1.1.9 Status.
        """
        rsp_status = Dataset()
        self.logger.debug("Sending C-STORE request")
        rsp_status = assoc.send_c_store(
            dataset=dataset,
            msg_id=msg_id,
        )

        return self._handle_response(rsp_status, None)

    def _get_status_description(self, status_code):
        """Retrieves the description for a given status code.

        Checks storage service specific status codes, then general status codes.

        Args:
            status_code: The status code to look up.

        Returns:
            str: The description part of the status code, or "Unknown" if not found.
        """
        description = STORAGE_SERVICE_CLASS_STATUS.get(status_code, None)
        if description is None:
            description = super()._get_status_description(status_code)
        return description[1]
