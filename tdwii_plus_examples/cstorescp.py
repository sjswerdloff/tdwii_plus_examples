import os
from argparse import Namespace

from pydicom.uid import UID, ImplicitVRLittleEndian, AllTransferSyntaxes
from pynetdicom import DEFAULT_TRANSFER_SYNTAXES, evt
from pynetdicom.presentation import (
    StoragePresentationContexts,
    AllStoragePresentationContexts,
)

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
                 store_directory=os.path.curdir,
                 ):
        """
        Initializes a new instance of the CStoreSCP class.
        This method creates an AE without presentation contexts.

        Parameters
        ----------
        ae_title : str
            The title of the Application Entity (AE)
            Optional, default: "ECHO_SCP"

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
        super().__init__(
            ae_title=ae_title,
            bind_address=bind_address,
            port=port,
            logger=logger)

        self.sop_classes = sop_classes
        if sop_classes is not None:
            self._valid_sop_classes, self._invalid_sop_classes = (
                self._validate_syntaxes(sop_classes, "SOP Class")
            )
            if self._invalid_sop_classes:
                print("Warning: Ignoring invalid SOP Classes:",
                      self._invalid_sop_classes)

        self.transfer_syntaxes = transfer_syntaxes
        if transfer_syntaxes is not None:
            self._valid_transfer_syntaxes, self._invalid_transfer_syntaxes = (
                self._validate_syntaxes(transfer_syntaxes, "Transfer Syntax")
            )
            if self._invalid_transfer_syntaxes:
                print("Warning: Ignoring invalid Transfer Syntaxes:",
                      self._invalid_transfer_syntaxes)

        if not callable(custom_handler):
            self.logger.warning(f"{custom_handler} is not a known "
                                "function, using default handler")
            self.handle_store = handle_cstore
        else:
            self.handle_store = custom_handler
        self.store_directory = store_directory

    def _validate_syntaxes(self, items, uid_type):
        # Get valid UIDs and keywords based on the UID type
        if uid_type == 'SOP Class':
            valid_uids = {
                ctx.abstract_syntax for ctx in AllStoragePresentationContexts}
            valid_keywords = {name for name in dir(
                UID) if getattr(UID, name) in valid_uids}
        elif uid_type == 'Transfer Syntax':
            valid_uids = {
                ctx.transfer_syntax for ctx in AllTransferSyntaxes}
            valid_keywords = {name for name in dir(
                UID) if getattr(UID, name) in valid_uids}
        else:
            raise ValueError(f"Unknown UID type: {uid_type}")

        # Initialize lists to store valid and invalid items
        valid_items = []
        invalid_items = []

        # Check each item in the provided list
        for item in items:
            if item in valid_uids or item in valid_keywords:
                valid_items.append(item)
            else:
                invalid_items.append(item)

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
            sop_classes = StoragePresentationContexts
        else:
            sop_classes = self._valid_sop_classes

        if self.transfer_syntaxes is None:
            transfer_syntaxes = DEFAULT_TRANSFER_SYNTAXES
        else:
            if ImplicitVRLittleEndian not in self._valid_transfer_syntaxes:
                transfer_syntaxes = [ImplicitVRLittleEndian] + \
                    self._valid_transfer_syntaxes
            else:
                transfer_syntaxes = self._valid_transfer_syntaxes

        self.ae.add_supported_context(sop_classes, transfer_syntaxes)

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
