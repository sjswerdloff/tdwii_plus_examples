from typing import cast

from pydicom.dataset import Dataset
from pydicom.uid import UID
from pynetdicom import AE, Association
from pynetdicom.sop_class import Verification
from pynetdicom.status import GENERAL_STATUS, Status, code_to_category

from tdwii_plus_examples._dicom_exceptions import (
    AssociationError,
    ContextWarning,
    ResponseError,
    ResponseWarning,
    ResponseCancel,
    ResponsePending,
    ResponseUnknown,
)


class BaseSCU:
    """
    The BaseSCU class is a base class for DICOM Service Class Providers (SCUs).

    This class provides basic functionality for creating and managing
    a DICOM Service Class Provider (SCU) including setting up the
    Application Entity (AE), establishing and Association with an SCP and
    handling incoming responses from SCP.

    Usage:
        To use the BaseSCU class, create a subclass and override
        the [_add_contexts] method to add requested presentation contexts.

    Attributes:
        ae_title (str): The title of the Application Entity (AE)
        bind_address (str): The IP address or hostname of the AE
        port (int): The port number the AE will listen on
        logger(logging.Logger): A logger instance

    Methods:
        _add_requested_contexts(self)
            Adds presentation contexts to the SCU instance.
        _associate(self)
            Open an Association of the SCU instance to an SCP.
        _handle_response(self)
            Handle the response of the request sent by the SCU.
        all_contexts_accepted(self, assoc)
            Check if all requested presentation contexts were accepted.
        verify()
            Send a Verification (C-ECHO) request from the SCU
    """

    def __init__(
        self, logger, calling_ae_title: str = None, called_ip: str = None, called_port: int = None, called_ae_title: str = None
    ):
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
        Adds the DICOM UPS Push SOP Class presentation context to the AE.
        Default transfer syntaxes are included.

        This method may be overridden in derived classes if another SOP
        Class needs to be negotiated.
        """
        self.ae.add_requested_context(Verification)
        self.logger.debug(f"Verification Presentation context added: \n {self.ae.requested_contexts[0]}")

    def _associate(self):
        """
        Establish an association with the remote AE and check contexts.

        Raises:
            AssociationError: If the association could not be established.
            ContextWarning: If some requested presentation contexts were not accepted.
                            The list of accepted SOP classes (list of pydicom.uid.UID) can be accessed via the
                            `accepted_sop_classes` attribute of the exception.
                            The list of refused SOP classes (list of pydicom.uid.UID) can be accessed via the
                            `refused_sop_classes` attribute of the exception.
        """
        if (self.called_ip is None or self.called_ip == "") or self.called_port is None:
            raise AssociationError("Called AE parameters not set")
        else:
            if self.called_ae_title is None:
                self.called_ae_title = "ANYSCP"
                self.logger.warning(f"Using default Called Application Entity Title: {self.called_ae_title}")

            self.assoc = self.ae.associate(self.called_ip, self.called_port, ae_title=self.called_ae_title)
            if not self.assoc.is_established:
                raise AssociationError("Association could not be established")
            self.logger.debug("Association established")

            # Initialize status of future requests
            self.status = False

            # Check if all requested contexts were accepted
            self._all_contexts_accepted(self.assoc)

    def _all_contexts_accepted(self, assoc: Association) -> bool:
        """
        Check if all requested presentation contexts were accepted.

        Args:
            assoc (Association): The established association object.

        Returns:
            bool: True if all requested presentation contexts were accepted, False otherwise.

        Raises:
            ContextWarning: If some requested presentation contexts were not accepted.
                            The list of accepted SOP classes (list of pydicom.uid.UID) can be accessed via the
                            `accepted_sop_classes` attribute of the exception.
                            The list of refused SOP classes (list of pydicom.uid.UID) can be accessed via the
                            `refused_sop_classes` attribute of the exception.
        """
        requested_abstract_syntaxes = {ctx.abstract_syntax for ctx in self.ae.requested_contexts}
        accepted_abstract_syntaxes = {ctx.abstract_syntax for ctx in assoc.accepted_contexts}

        refused_abstract_syntaxes = requested_abstract_syntaxes - accepted_abstract_syntaxes

        if refused_abstract_syntaxes:
            accepted_sop_classes = [UID(uid) for uid in accepted_abstract_syntaxes]
            refused_sop_classes = [UID(uid) for uid in refused_abstract_syntaxes]
            raise ContextWarning(
                "The following SOP classes were not accepted",
                accepted_sop_classes=accepted_sop_classes,
                refused_sop_classes=refused_sop_classes,
            )

        return True

    def _handle_response(self, rsp_status, rsp_dataset):
        """
        Handle the response from the SCP.

        Parameters
        ----------
        rsp_status : Status
            The response status.
        rsp_dataset : Dataset
            The response dataset.

        Raises
        ------
        ResponseWarning
            If the request was successful but with a warning.
        ResponseError
            If the request failed.

        Returns
        -------
        bool
            True if the request was successful, False otherwise.
        """
        self.status = False
        self.logger.debug("Received Response:")
        self.logger.debug(f"Status Type: {type(rsp_status)}")
        self.logger.debug(f"Status Value: {rsp_status}")

        # check if Status contains empty dataset
        if rsp_status is None or len(rsp_status) == 0:
            self.logger.error("Response Status is None or empty")
            raise ResponseError(0xFFFF, "Empty Status, SCP timed out, aborted or sent an invalid response")

        # check if Dataset contains empty dataset
        if rsp_dataset is None or len(rsp_dataset) == 0:
            self.logger.debug("Response Dataset is None or empty")
        else:
            if isinstance(rsp_dataset, Dataset):
                rsp_ds = Dataset(rsp_dataset)
                self.logger.debug(f"Response Dataset: {rsp_ds}")
            else:
                self.logger.debug("Response Dataset is not a DICOM Dataset")

        # For an SCU, the status can belong to Success, Failure, Warning, Pending, or Unknown category
        if rsp_status.Status == Status.SUCCESS:
            self.status = True
            message = "Request successful"
            self.logger.debug(message)
            return self.status
        else:
            status_code = cast(int, rsp_status.Status)
            category = code_to_category(cast(int, status_code))
            description = self._get_status_description(status_code)
            self.logger.debug(f"Status Category: {category}")
            self.logger.debug(f"Status Description: {description}")
            if category == "Failure":
                raise ResponseError(status_code, description)
            elif category == "Warning":
                raise ResponseWarning(status_code, description)
            elif category == "Cancel":
                raise ResponseCancel(status_code, description)
            elif category == "Pending":
                raise ResponsePending(status_code, description)
            elif category == "Unknown":
                raise ResponseUnknown(status_code, description)
            else:
                return self.status

    def _get_status_description(self, status_code):
        return GENERAL_STATUS.get(status_code, ("Unknown", "Unknown status code"))[1]

    def set_called_ae(self, called_ip: str, called_port: int, called_ae_title: str = None):
        self.called_ip = called_ip
        self.called_port = called_port
        if called_ae_title is None or called_ae_title == "":
            self.called_ae_title = called_ae_title
        else:
            self.called_ae_title == "ANYSCU"
            self.logger.warning(f"Using default Called Application Title: {self.called_ae_title}")

    def verify(self):
        """
        Send a C-ECHO request to Called AET.

        This method establishes an association with the remote AE, checks if
        all requested SOP classes were accepted, sends a C-ECHO request to
        verify communication, and handles the response. It logs the status
        of the association and the verification process.

        Raises
        -------
        AssociationError:
            If the association could not be established.
        ContextWarning:
            If some requested presentation contexts were not accepted.
        ResponseWarning:
            If the request was successful but with a warning.
        ResponseError:
            If the request failed.
        ResponseUnknown:
            If the request failed with an unknown status.
        """
        safe_to_proceed = False
        try:
            self._associate()
            safe_to_proceed = True
        except AssociationError as error:
            self.logger.error(str(error))
            raise
        except ContextWarning as warning:
            accepted_sop_names = [f"[{UID(uid).name}]" for uid in warning.accepted_sop_classes]
            self.logger.warning(f"{warning} - Accepted Transfer Syntaxes: {', '.join(accepted_sop_names)}")
            if "[Verification SOP Class]" in accepted_sop_names:
                safe_to_proceed = True
                raise
        finally:
            if safe_to_proceed:
                try:
                    self._handle_response(self.assoc.send_c_echo(), None)
                    self.logger.info("Verification (C-ECHO) successful")
                except ResponseWarning as warning:
                    self.logger.warning(self._get_status_description(warning.status_code))
                    raise
                except ResponseError as error:
                    self.logger.error(self._get_status_description(error.status_code))
                    raise
                except ResponseUnknown as unknown:
                    self.logger.error(self._get_status_description(unknown.status_code))
                    raise
                finally:
                    self.assoc.release()
                    self.logger.debug("Association released")
            else:
                if self.assoc:
                    self.assoc.release()
                    self.logger.debug("Association released")
