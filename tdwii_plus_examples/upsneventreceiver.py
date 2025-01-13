from argparse import Namespace
import logging

from pydicom.uid import (
    UID, ImplicitVRLittleEndian, ExplicitVRLittleEndian
)
from pynetdicom import DEFAULT_TRANSFER_SYNTAXES, evt

from pynetdicom.apps.common import setup_logging

from tdwii_plus_examples.cechoscp import CEchoSCP
from tdwii_plus_examples.upsneventhandler import handle_nevent, nevent_callback
from tdwii_plus_examples._dicom_uids import (
    validate_transfer_syntaxes,
    UPS_SOP_CLASSES,
)


class UPSNEventReceiver(CEchoSCP):
    """
    A subclass of the CEchoSCP class that implements the DICOM UPS Event
    Service Receiver which role is defined as a Service Class User (SCU).
    As this may be perceived as counter-intuitive for a network listener,
    the term Receiver is used instead. This "reversal" of the roles is
    common for notification services where a SCP, here the UPS SCP,
    notifies an SCU of state changes as described in section CC.2.4 of
    DICOM PS3.4.

    The Unified Procedure Step - Event SOP Class is supported with
    default transfer syntaxes unless otherwise specified.

    Usage:
        Create an instance of UPSNEventReceiver and call the run method
        inherited from the BaseSCP grandparent class to start listening
        for incoming DICOM association requests.

    Attributes:
        ae_title (str): The title of the Application Entity (AE)
        bind_address (str): The IP address or hostname of the AE
        port (int): The port number the AE will listen on
        logger (logging.Logger): A logger instance
        transfer_syntaxes (list): A list of transfer syntaxes to support
        ups_event_callback (function): A function to process UPS State
            Changes Reports in received N-EVENT-REPORT requests.

    Methods:
        _add_contexts(self)
            Adds presentation contexts to the Receiver instance.
        _add_handlers(self)
            Adds handlers for DICOM communication events to the Receiver
            instance.
    """

    def __init__(self,
                 ae_title: str = "EVENT_REPORT_RCV",
                 bind_address: str = "",
                 port: int = 11112,
                 logger=None,
                 transfer_syntaxes=None,
                 ups_event_callback=None,
                 **kwargs):
        """
        Initializes a new instance of the NEventReceiver class.
        This method creates an AE with UPS Event presentation context.

        Parameters
        ----------
        ae_title : str
            The title of the Application Entity (AE)
            Optional, default: "EVENT_REPORT_RCV"

        bind_address : str
            A specific IP address or hostname of the AE
            Optional, default: "" will bind to all interfaces.

        port: int
            The port number to listen on
            Optional, default: 11112 (as registered for DICOM at IANA)

        logger: logging.Logger
            A logger instance
            Optional, default: None, a debug logger will be used

        transfer_syntaxes: list of str/pydicom.uid.UID
            A list of transfer syntaxes to support
            (names must be valid Transfer Syntax UIDs, Names or Keywords
            from PS3.6 Annex A, invalid UIDs and names will be ignored).
            The order of the transfer syntaxes in the list can be used
            to set the preferred syntax to accept when multiple ones are
            proposed.
            Optional, default: None, pynetdicom default transfer syntaxes
            are supported with Explicit VR Little Endian as the preferred
            syntax.

        ups_event_callback: function
            A function to process UPS State Changes Reports in received
            N-EVENT-REPORT requests.
            Optional, default: None, upseventhandler.nevent_callback function
        """
        if logger is None:
            self.logger = setup_logging(
                Namespace(log_type=None, log_level="debug"), "nevent_receiver")
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
        self.logger.debug("UPSNEventReceiver.__init__")

        if not ae_title:
            self.ae_title = "EVENT_REPORT_RCV"
            self.logger.info("AE title not provided, using default: %s",
                             self.ae_title)
        else:
            self.ae_title = ae_title

        self.transfer_syntaxes = transfer_syntaxes
        if transfer_syntaxes is not None:
            self._valid_transfer_syntaxes, self._invalid_transfer_syntaxes = (
                validate_transfer_syntaxes(transfer_syntaxes)
            )
            if self._invalid_transfer_syntaxes:
                self.logger.warning(
                    "Ignoring invalid Transfer Syntaxes: %s",
                    list(self._invalid_transfer_syntaxes.keys()))

        self.logger.debug(
            f"UPS Event Callback: {ups_event_callback} "
            f"type is {type(ups_event_callback)}")
        if ups_event_callback is None:
            self.logger.warning("No ups_event_callback defined, "
                                "using default callback")
            self.ups_event_callback = nevent_callback
        elif not callable(ups_event_callback):
            self.logger.warning(f"{ups_event_callback} is not a known "
                                "function, using default callback")
            self.ups_event_callback = nevent_callback
        else:
            self.ups_event_callback = ups_event_callback
            self.logger.debug(
                f"UPS Event Callback: {self.ups_event_callback}"
            )

        super().__init__(
            ae_title=ae_title,
            bind_address=bind_address,
            port=port,
            logger=logger,
            **kwargs)

    def _add_contexts(self):
        """
        Adds the DICOM UPS Event SOP Class presentation context to the AE.

        This method overrides the CEchoSCP parent class method to add support
        for the UPS Event SOP Class.
        Implicit VR Little Endian, Implicit VR Big Endian, Explicit VR Little
        Endian and Deflated Explicit VR Little Endian transfer syntaxes are
        included by default unless otherwise specified in the constructor.
        """
        self.logger.debug("UPSNEventReceiver._add_contexts")
        super()._add_contexts()

        sop_class = UPS_SOP_CLASSES["UnifiedProcedureStepEvent"]

        if self.transfer_syntaxes is None or not self.transfer_syntaxes:
            self.logger.debug("No transfer syntaxes specified, using defaults")
            transfer_syntaxes = DEFAULT_TRANSFER_SYNTAXES.copy()
            # Make ExplicitVRLittleEndian the preferred transfer syntax
            transfer_syntaxes.remove(UID(ExplicitVRLittleEndian))
            transfer_syntaxes = [UID(ExplicitVRLittleEndian)] + \
                transfer_syntaxes
        else:
            if ImplicitVRLittleEndian not in list(
                    self._valid_transfer_syntaxes.values()):
                transfer_syntaxes = (
                    list(self._valid_transfer_syntaxes.values()) +
                    [ImplicitVRLittleEndian]
                )
            else:
                transfer_syntaxes = list(
                    self._valid_transfer_syntaxes.values())

        self.logger.debug(f"Supported Transfer Syntaxes: {transfer_syntaxes}")

        self.ae.add_supported_context(sop_class, transfer_syntaxes)

    def _add_handlers(self):
        """
        Adds a handler for for processing incoming N-EVENT-REPORT requests.

        This method overrides the CEchoSCP parent class method to add a
        handler for the UPS Event SOP Class.
        """
        self.logger.debug("UPSNEventReceiver._add_handlers")
        super()._add_handlers()
        self.handlers.append((evt.EVT_N_EVENT_REPORT, handle_nevent,
                              [self.ups_event_callback, self.logger]))
