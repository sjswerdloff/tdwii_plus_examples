import os
from argparse import Namespace
import logging

from pydicom.uid import UID, ImplicitVRLittleEndian, AllTransferSyntaxes
from pynetdicom import DEFAULT_TRANSFER_SYNTAXES, evt
from pynetdicom.presentation import (
    StoragePresentationContexts,
    AllStoragePresentationContexts,
)
from pynetdicom.apps.common import setup_logging

from tdwii_plus_examples.cechoscp import CEchoSCP
from tdwii_plus_examples.cstorehandler import handle_cstore


class CStoreSCP(CEchoSCP):
    """
    A subclass of the CEchoSCP class that implements the DICOM Storage
    Service Class Provider (SCP).

    Unless otherwise specified, The first 128 Storage SOP Classes from all
    SOP Classes sorted by abtract syntax SOP Class UID are supported with the
    Implicit VR Little Endian, Implicit VR Big Endian, Explicit VR Little
    Endian and Deflated Explicit VR Little Endian transfer syntaxes.

    Usage:
        Create an instance of CStoreSCP and call the run method inherited
        from the BaseSCP grandparent class to start listening for incoming
        DICOM association requests.

    Attributes:
        ae_title (str): The title of the Application Entity (AE)
        bind_address (str): The IP address or hostname of the AE
        port (int): The port number the AE will listen on
        logger (logging.Logger): A logger instance
        sop_classes (list): A list of SOP Classes to support
        transfer_syntaxes (list): A list of transfer syntaxes to support
        custom_handler (function): A function to handle C-STORE requests
        store_directory (str): The directory to store files

    Methods:
        _add_contexts(self)
            Adds presentation contexts to the SCP instance.
        _add_handlers(self)
            Adds handlers for DICOM communication events to the SCP instance.
    """

    def __init__(self,
                 ae_title: str = "STORE_SCP",
                 bind_address: str = "",
                 port: int = 11112,
                 logger=None,
                 sop_classes=None,
                 transfer_syntaxes=None,
                 custom_handler=None,
                 store_directory=None,
                 ):
        """
        Initializes a new instance of the CStoreSCP class.
        This method creates an AE without presentation contexts.

        Parameters
        ----------
        ae_title : str
            The title of the Application Entity (AE)
            Optional, default: "STORE_SCP"

        bind_address : str
            A specific IP address or hostname of the AE
            Optional, default: "" will bind to all interfaces.

        port: int
            The port number to listen on
            Optional, default: 11112 (as registered for DICOM at IANA)

        logger: logging.Logger
            A logger instance
            Optional, default: None, a debug logger will be used

        sop_classes: list of str or pydicom.uid.UID
            A list of SOP Classes UIDs or names to support
            (names must be valid SOP Class Keywords from PS3.6 Annex A,
            invalid UIDs and names will be ignored)
            Optional, default: None, First 128 SOP Classes are supported

        transfer_syntaxes: list of str/pydicom.uid.UID
            A list of transfer syntaxes UIDs or names to support
            (names must be valid Transfer Syntax Keywords from PS3.6 Annex A,
            invalid UIDs and names will be ignored)
            Optional, default: None, pynetdicom default transfer syntaxes are
            supported

        custom_handler: function
            A function to handle C-STORE requests
            Optional, default: None, cstorehandler.handle_cstore function

        store_directory: str
            The directory to store files
            Optional, default: current directory
        """
        if logger is None:
            self.logger = setup_logging(
                Namespace(log_type=None, log_level="debug"), "cstore_scp")
            self.logger.info(
                "Logger not provided, using default logger with level %s",
                logging.getLevelName(self.logger.level)
            )
        elif isinstance(logger, logging.Logger):
            self.logger = logger
            self.logger.debug(
                "Logger set to %s with level %s",
                logger.name, logging.getLevelName(logger.getEffectiveLevel())
            )

        if not ae_title:
            self.ae_title = "STORE_SCP"
            self.logger.info("AE title not provided, using default: %s",
                             self.ae_title)
        else:
            self.ae_title = ae_title

        self.sop_classes = sop_classes
        if sop_classes is not None:
            self._valid_sop_classes, self._invalid_sop_classes = (
                self._validate_syntaxes(sop_classes, "SOP Class")
            )
            if self._invalid_sop_classes:
                self.logger.warning("Ignoring invalid SOP Classes: %s",
                                    self._invalid_sop_classes)

        self.transfer_syntaxes = transfer_syntaxes
        if transfer_syntaxes is not None:
            self._valid_transfer_syntaxes, self._invalid_transfer_syntaxes = (
                self._validate_syntaxes(transfer_syntaxes, "Transfer Syntax")
            )
            if self._invalid_transfer_syntaxes:
                self.logger.warning("Ignoring invalid Transfer Syntaxes: %s",
                                    self._invalid_transfer_syntaxes)

        self.logger.debug(
            f"Custom handler: {custom_handler} type is {type(custom_handler)}")
        if custom_handler is None:
            self.logger.warning("No custom_handler defined, "
                                "using default handler")
            self.handle_store = handle_cstore
        elif not callable(custom_handler):
            self.logger.warning(f"{custom_handler} is not a known function, "
                                "using default handler")
            self.handle_store = handle_cstore
        else:
            self.handle_store = custom_handler
            self.logger.debug(f"Custom handler: {self.handle_store}")

        if store_directory is None:
            self.store_directory = os.getcwd()
        else:
            self.store_directory = store_directory
        self.logger.debug(f"Store directory: {self.store_directory}")

        super().__init__(
            ae_title=self.ae_title,
            bind_address=bind_address,
            port=port,
            logger=logger)

    def _validate_syntaxes(self, items, uid_type):
        # Sort valid and invalid items based on the UID type
        self.logger.debug(f"Validating {uid_type} list: {items}")

        # Construct a mapping of valid keywords and UIDs for syntax validation
        valid_syntaxes = {
            ctx.abstract_syntax: UID(ctx.abstract_syntax).keyword
            for ctx in AllStoragePresentationContexts
        } if uid_type == 'SOP Class' else {
            ctx: UID(ctx).keyword
            for ctx in AllTransferSyntaxes
        }

        # Check each item in the provided list
        valid_items = []
        invalid_items = []
        for item in items:
            keyword = valid_syntaxes.get(item)
            if keyword is not None:
                valid_items.append(item)
                self.logger.debug(f"Valid {uid_type} : {item}")
            elif item in valid_syntaxes.values():
                valid_items.append(
                    next(UID for UID, keyword in valid_syntaxes.items()
                         if keyword == item))
                self.logger.debug(f"Valid {uid_type} : {item}")
            else:
                invalid_items.append(item)
                self.logger.debug(f"Invalid {uid_type} : {item}")

        return valid_items, invalid_items

    def _add_contexts(self):
        """
        Adds the DICOM Storage SOP Classes presentation context to the AE.

        This method overrides the CEchoSCP parent class method to add support
        for the first 128 Storage SOP Classes (sorted by SOP Class UID) or for
        the SOP Classes specified by the constructor.
        Implicit VR Little Endian, Implicit VR Big Endian, Explicit VR Little
        Endian and Deflated Explicit VR Little Endian transfer syntaxes are
        included by default unless otherwise specified in the constructor.
        """
        super()._add_contexts()
        if self.sop_classes is None:
            sop_classes = [
                context.abstract_syntax
                for context in StoragePresentationContexts
            ]
        else:
            sop_classes = self._valid_sop_classes
        self.logger.debug(f"Supported Storage SOP Classes: {sop_classes}")

        if self.transfer_syntaxes is None:
            transfer_syntaxes = DEFAULT_TRANSFER_SYNTAXES
        else:
            if ImplicitVRLittleEndian not in self._valid_transfer_syntaxes:
                transfer_syntaxes = [ImplicitVRLittleEndian] + \
                    self._valid_transfer_syntaxes
            else:
                transfer_syntaxes = self._valid_transfer_syntaxes
        self.logger.debug(f"Supported Transfer Syntaxes: {transfer_syntaxes}")

        for sop_class in sop_classes:
            self.ae.add_supported_context(sop_class, transfer_syntaxes)

    def _add_handlers(self):
        """
        Adds a handler for for processing incoming C-STORE requests.

        This method overrides the CEchoSCP parent class method to add a handler
        for the Storage SOP Classes.
        """
        super()._add_handlers()
        args = Namespace(ignore=False, output_directory=self.store_directory)
        self.handlers.append((evt.EVT_C_STORE, self.handle_store,
                              [args, self.logger]))
