from pydicom.dataset import Dataset
from pynetdicom import AE
from pynetdicom.sop_class import UnifiedProcedureStepPush
from pynetdicom.status import UNIFIED_PROCEDURE_STEP_SERVICE_CLASS_STATUS, Status


class BaseSCU:
    STATUS_FAILURE: str = "Failure"
    STATUS_WARNING: str = "Warning"

    def __init__(self, logger, called_ip, called_port, called_ae_title, calling_ae_title):
        """
        Initializes a new instance of the Base SCU AE class.
        This method sets up the AE with the provided parameters
        and adds the requested presentation context to negotiate
        the UPS Push SOP Class.

        Parameters
        ----------
        logger : Logger
            The logger instance for logging messages.
        called_ip : str
            The IP address of the called AE.
        called_port : int
            The port number of the called AE.
        called_ae_title : str
            The AE title of the called AE.
        calling_ae_title : str
            The AE title of the calling AE.
        """
        self.logger = logger
        self.called_ip = called_ip
        self.called_port = called_port
        self.called_ae_title = called_ae_title
        self.calling_ae_title = calling_ae_title

        # Create an AE instance
        self.ae = AE(ae_title=self.calling_ae_title)
        self._add_requested_context()

    def _add_requested_context(self):
        """
        Adds the DICOM UPS Push SOP Class presentation context to the AE.
        Default transfer syntaxes are included.

        This method may be overridden in derived classes if another SOP
        Class needs to be negotiated.
        """
        self.ae.add_requested_context(UnifiedProcedureStepPush)
        self.logger.debug(f"Presentation context added: \n{self.ae.requested_contexts[0]}")

    def _associate(self):
        """Establish an association with the remote AE"""
        return self.ae.associate(self.called_ip, self.called_port, ae_title=self.called_ae_title)

    def _handle_response(self, rsp_status, rsp_dataset):
        """
        Handle the response from the SCP.

        Parameters
        ----------
        rsp_status : Status
            The response status.
        rsp_dataset :Dataset
            The response dataset.

        Returns
        -------
        bool: True if the request was successful, False otherwise.
        str: The message indicating the outcome of the request.

        """
        self.logger.debug("Received Response:")
        self.logger.debug(f"Status Type: {type(rsp_status)}")
        self.logger.debug(f"Status Value: {rsp_status}")

        if rsp_dataset is None or len(rsp_dataset) == 0:
            self.logger.debug("Response Dataset is None or empty")
        else:
            if isinstance(rsp_dataset, Dataset):
                rsp_ds = Dataset(rsp_dataset)
                self.logger.debug(f"Response Dataset: {rsp_ds}")
            else:
                self.logger.debug("Response Dataset is not a DICOM Dataset")

        if rsp_status.Status == Status.SUCCESS:
            message = "Request successful"
            self.logger.debug(message)
            return True, message
        else:
            status, message = UNIFIED_PROCEDURE_STEP_SERVICE_CLASS_STATUS.get(rsp_status.Status, (None, None))
            if status == self.STATUS_WARNING:
                self.logger.warning(message)
                return True, f"Request successful, but {message}"
            elif status == self.STATUS_FAILURE:
                self.logger.error(message)
                return False, f"Request failed: {message}"
            else:
                self.logger.info("Unknown status code")
            return False, (f"Request failed: {message}")
