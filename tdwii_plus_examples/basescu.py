import logging
from argparse import Namespace
from collections import namedtuple

from pydicom.dataset import Dataset
from pydicom.uid import UID
from pynetdicom import AE, Association
from pynetdicom.apps.common import setup_logging
from pynetdicom.sop_class import Verification
from pynetdicom.status import GENERAL_STATUS, code_to_category


class BaseSCU:
    """
    The BaseSCU class is a base class for DICOM Service Class Users (SCUs).

    This class provides basic functionality for creating and managing
    a DICOM Service Class Provider (SCU) including setting up the
    Application Entity (AE), establishing and Association with an SCP and
    handling incoming responses from SCP.
    It also implements the Verification SOP Class SCU.

    Usage:
        To use the BaseSCU class, create a subclass then,
        override:
        - [_add_contexts] method to add requested presentation contexts.
        - [_get_status_description] method to add response status codes.
        use:
        - [_associate] method to implement Service primitives requests

    Attributes:
        ae_title (str): The title of the Application Entity (AE)
        bind_address (str): The IP address or hostname of the AE
        port (int): The port number the AE will listen on
        logger(logging.Logger): A logger instance

    Methods:
        _add_requested_context()
            Adds the Verification SOP Class presentation context.
            Should be overridden by subclasses.
        _associate()
            Establishes association with remote AE.
        _get_status_description()
            Retrieves the description for a given status code.
            Should be overridden by subclasses.
        set_called_ae()
            Sets the called AE parameters.
        verify()
            Sends a verification request.
    """

    def __init__(
        self,
        logger=None,
        calling_ae_title: str = None,
        called_ip: str = None,
        called_port: int = None,
        called_ae_title: str = None,
    ):
        """
        Initializes a BaseSCU instance.

        This method sets up the AE and calls the method _add_requested_context
        which is meant to be overriden by subclasses.
        BaseSCU adds the Verification SOP Class presentation context.

        Parameters
        ----------
        logger : Logger
            The logger instance for logging messages.
        called_ip : str
            The IP address of the called AE.
        called_port : int
            The port number of the called AE.
        called_ae_title : str, optional
            The AE title of the called AE. If None, "ANY-SCP" is used.
        calling_ae_title : str
            The AE title of the calling AE.
        """
        if logger is None:
            self.logger = setup_logging(Namespace(log_type=None, log_level="debug"), "base_scu")
            self.logger.info(
                "Logger not provided, using default logger with level %s", logging.getLevelName(self.logger.level)
            )
        elif isinstance(logger, logging.Logger):
            self.logger = logger
            self.logger.debug("Logger set to %s with level %s", logger.name, logging.getLevelName(logger.getEffectiveLevel()))
        else:
            raise TypeError("logger must be an instance of logging.Logger")
        self.logger.debug("BaseSCU.__init__")

        if calling_ae_title is None or calling_ae_title == "":
            self.calling_ae_title = "BASESCU"
            self.logger.warning(f"Using default Application Entity Title: {self.calling_ae_title}")
        else:
            self.calling_ae_title = calling_ae_title
        if called_ip is not None or called_ip != "":
            self.called_ip = called_ip
        else:
            self.called_ip = None
        self.called_port = called_port

        if called_ae_title is not None or called_ae_title != "":
            self.called_ae_title = called_ae_title

        # Create an AE instance
        self.ae = AE(ae_title=self.calling_ae_title)
        self._add_requested_context()
        self.assoc = None
        self.status = False

    def _add_requested_context(self):
        """
        Adds the DICOM Verification SOP Class presentation context to the AE.
        Default transfer syntaxes are included.

        Derived classes *must* override this method to add the presentation
        contexts for the specific SOP Classes they support.
        """
        self.ae.add_requested_context(Verification)
        self.logger.debug(f"Verification Presentation context added: \n {self.ae.requested_contexts[0]}")

    # Create a named tuple to hold the result of the Association
    AssociationResult = namedtuple("AssociationResult", ["status", "description", "accepted_sop_classes"])

    def _associate(self, required_sop_classes=None):
        """
        Establishes an association with the remote AE.

        Returns:
            tuple: (success: bool, result: AssociationResult)
                - success (bool): True if association status is "Success", False otherwise.
                - result (AssociationResult): The association result namedtuple.
        """
        result = self._attempt_association(required_sop_classes)
        return (result.status == "Success"), result

    def _attempt_association(self, required_sop_classes=None):
        if (self.called_ip is None or self.called_ip == "") or self.called_port is None:
            return self.AssociationResult(status="Error", description="Called AE parameters not set", accepted_sop_classes=[])

        if self.called_ae_title is None:
            self.called_ae_title = "ANYSCP"
            self.logger.warning(f"Using default Called Application Entity Title: {self.called_ae_title}")

        self.assoc = self.ae.associate(self.called_ip, self.called_port, ae_title=self.called_ae_title)
        if not self.assoc.is_established:
            return self.AssociationResult(
                status="Error", description="Association could not be established", accepted_sop_classes=[]
            )

        self.logger.debug("Association established")

        # Initialize status of future requests
        self.status = False

        # Check if all SOP Classes of requested contexts were accepted
        result = self._check_accepted_sop_classes(self.assoc)
        if result.status:
            return self.AssociationResult(
                status="Success",
                description="All requested SOP Classes were accepted",
                accepted_sop_classes=[UID(uid) for uid in result.accepted_sop_classes],
            )
        else:
            # Check if all required contexts were accepted
            return self._validate_sop_classes(result, required_sop_classes)

    def _check_accepted_sop_classes(self, assoc: Association) -> AssociationResult:
        """
        Check if all requested DICOM SOP classes are accepted.

        Returns an AssociationResult indicating "Success" if all SOP classes are accepted
        and "Warning" if only some are accepted.

        Args:
            assoc (pynetdicom.association.Association): The established association.

        Returns:
            An AssociationResult namedtuple.
        """
        requested_abstract_syntaxes = {ctx.abstract_syntax for ctx in self.ae.requested_contexts}
        accepted_abstract_syntaxes = {ctx.abstract_syntax for ctx in assoc.accepted_contexts}

        rejected_abstract_syntaxes = requested_abstract_syntaxes - accepted_abstract_syntaxes

        if rejected_abstract_syntaxes:
            accepted_sop_classes = [UID(uid) for uid in accepted_abstract_syntaxes]
            self.logger.warning(
                "The following SOP Classes were rejected: " + ", ".join(str(uid) for uid in rejected_abstract_syntaxes)
            )
            return self.AssociationResult(status=False, description="", accepted_sop_classes=accepted_sop_classes)

        return self.AssociationResult(
            status=True,
            description="",
            accepted_sop_classes=[UID(uid) for uid in accepted_abstract_syntaxes],
        )

    def _validate_sop_classes(self, assoc_result, required_sop_classes=None):
        """Validates if all required SOP classes are accepted.

        Args:
            assoc_result (AssociationResult): The association result.
            required_sop_classes (list, optional): A list of required SOP Class UIDs.

        Returns:
            An AssociationResult namedtuple.
        """
        accepted_sop_classes = {UID(uid) for uid in assoc_result.accepted_sop_classes}

        # Use a set for efficient check
        if required_sop_classes:
            required_sop_classes = {UID(uid) for uid in required_sop_classes}
        else:
            required_sop_classes = {context.abstract_syntax for context in self.ae.requested_contexts}

        if not required_sop_classes.issubset(accepted_sop_classes):
            missing_sop_classes = list(required_sop_classes - accepted_sop_classes)
            description = f"The following required SOP classes were rejected: {', '.join(map(str, missing_sop_classes))}"
            self.logger.error(description)
            self.assoc.release()
            return self.AssociationResult("Error", description, list(accepted_sop_classes))

        return self.AssociationResult("Success", "All required SOP classes were accepted", list(accepted_sop_classes))

    # Create a named tuple to hold the response status and dataset
    PrimitiveResult = namedtuple("PrimitiveResult", ["status_category", "status_code", "status_description", "dataset"])

    def _handle_response(self, rsp_status, rsp_dataset) -> PrimitiveResult:
        """
        Handle the response from the SCP.

        Parameters
        ----------
        rsp_status : Status
            The response status.
        rsp_dataset : Dataset
            The response dataset.

        Returns
        -------
        PrimitiveResult:
            A named tuple containing the status category, status code, status description, and dataset.
        """

        self.logger.debug("Received Response:")
        self.logger.debug(f"Status Type: {type(rsp_status)}")
        self.logger.debug(f"Status Value: {rsp_status}")

        if rsp_status is None or len(rsp_status) == 0:
            self.logger.error("Response Status is None or empty")
            return self.PrimitiveResult(
                "Failure", 0xFFFF, "Empty Status, SCP timed out, aborted or sent an invalid response", None
            )

        if rsp_dataset is None or len(rsp_dataset) == 0:
            self.logger.debug("Response Dataset is None or empty")
            rsp_ds = None
        else:
            if isinstance(rsp_dataset, Dataset):
                rsp_ds = Dataset(rsp_dataset)
                self.logger.debug(f"Response Dataset: {rsp_ds}")
            else:
                self.logger.error("Response Dataset is not a DICOM Dataset")
                rsp_ds = None

        status_code = int(rsp_status.Status)
        category = code_to_category(status_code)
        description = self._get_status_description(status_code)
        self.logger.debug(f"Status Category: {category}")
        self.logger.debug(f"Status Description: {description}")

        return self.PrimitiveResult(category, status_code, description, rsp_ds)

    def _get_status_description(self, status_code):
        """
        Retrieves the description for a given status code.

        This method retrieves the description associated with a given status
        code from the GENERAL_STATUS dictionary. If the status code is not
        found, it returns "Unknown".  This method is intended to be overridden
        by subclasses to provide more specific status descriptions.

        Args:
            status_code (int): The status code to look up.

        Returns:
            str: The description of the status code.
        """
        return GENERAL_STATUS.get(status_code, ("Unknown", "Unknown status code"))[1]

    def set_called_ae(self, called_ip: str, called_port: int, called_ae_title: str = None):
        """
        Sets the called AE parameters.

        This method allows setting the called AE parameters (IP, port, and
        AE title) after the BaseSCU object has been initialized.  It's
        useful when the called AE information is not available during
        object creation.

        Args:
            called_ip (str): The IP address of the called AE.
            called_port (int): The port number of the called AE.
            called_ae_title (str, optional): The AE title of the called AE.
                Defaults to "ANY-SCP".
        """
        self.called_ip = called_ip
        self.called_port = called_port
        if called_ae_title is None or called_ae_title == "":
            self.called_ae_title == "ANYSCP"
            self.logger.warning(f"Using default Called Application Title: {self.called_ae_title}")
        else:
            self.called_ae_title = called_ae_title

    def verify(self):
        """
        Send a C-ECHO request to Called AET.

        This method establishes an association with the remote AE, checks if
        all requested SOP classes were accepted, sends a C-ECHO request to
        verify communication, and handles the response. It logs the status
        of the association and the verification process.

        Returns
        -------
        PrimitiveResult:
            A named tuple containing the status category, status code, status description, and dataset.
        """
        success, details = self._associate(required_sop_classes=[Verification])

        if details.status == "Error":
            return self.PrimitiveResult("AssocFailure", 0xD000, details.description, None)

        if details.status == "Warning":
            accepted_sop_names = [f"[{UID(uid).name}]" for uid in details.accepted_sop_classes]
            self.logger.warning(f"{details.description} - Accepted SOP Classes: {', '.join(accepted_sop_names)}")
            if "[Verification SOP Class]" not in accepted_sop_names:
                self.assoc.release()
                return self.PrimitiveResult("AssocFailure", 0xD001, details.description, None)

        result = self._handle_response(self.assoc.send_c_echo(), None)

        if result.status_category == "Success":
            self.logger.info("Verification (C-ECHO) successful")
        else:
            self.logger.error(f"Verification (C-ECHO) failure: {result.status_description}")

        self.assoc.release()

        return result
