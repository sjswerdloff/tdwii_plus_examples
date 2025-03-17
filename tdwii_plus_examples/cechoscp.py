import logging
from argparse import Namespace

from pynetdicom import evt
from pynetdicom.apps.common import setup_logging
from pynetdicom.sop_class import Verification

from tdwii_plus_examples.basescp import BaseSCP
from tdwii_plus_examples.cechohandler import handle_cecho


class CEchoSCP(BaseSCP):
    """
    A subclass of the BaseSCP class that implements the DICOM Verification
    Service Class Provider (SCP).

    Usage:
        Create an instance of CEchoSCP and call the run method inherited
        from the BaseSCP parent class to start listening for incoming
        DICOM association requests.
        The CEchoSCP class is generally not used directly. Instead, create
        a subclass and override the [_add_contexts] and [_add_handlers] methods
        to add presentation contexts and handlers for specific DICOM services.

    Attributes:
        ae_title (str): The title of the Application Entity (AE)
        bind_address (str): The IP address or hostname of the AE
        port (int): The port number the AE will listen on
        logger (logging.Logger): A logger instance

    Methods:
        _add_contexts(self)
            Adds presentation contexts to the SCP instance.
        _add_handlers(self)
            Adds handlers for DICOM communication events to the SCP instance.
    """

    def __init__(self, ae_title: str = "ECHO_SCP", bind_address: str = "", port: int = 11112, logger=None, **kwargs):
        """
        Initializes a new instance of the CEchoSCP class.
        This method creates an AE with the Verification presentation context.

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
            Optional, default: None, a debug logger will be used.
        """
        if logger is None:
            self.logger = setup_logging(Namespace(log_type=None, log_level="debug"), "cecho_scp")
            self.logger.info(
                "Logger not provided, using default logger with level %s", logging.getLevelName(self.logger.level)
            )
        elif isinstance(logger, logging.Logger):
            self.logger = logger
            self.logger.debug("Logger set to %s with level %s", logger.name, logging.getLevelName(logger.getEffectiveLevel()))
        else:
            raise TypeError("logger must be an instance of logging.Logger")
        self.logger.debug("CEchoSCP.__init__")

        if not ae_title:
            self.ae_title = "ECHO_SCP"
            self.logger.info("AE title not provided, using default: %s", self.ae_title)
        else:
            self.ae_title = ae_title

        super().__init__(ae_title=self.ae_title, bind_address=bind_address, port=port, logger=logger, **kwargs)

    def _add_contexts(self):
        """
        Adds the DICOM Verification SOP Class presentation context to the AE.
        Only the default Implicit VR Little Endian transfer syntax is included.

        This method overrides the base class method to add support for the
        Verification SOP Class which is required for any DICOM SCP.

        This method is intended to be overridden in derived classes.
        """
        self.logger.debug("CEchoSCP._add_contexts")
        super()._add_contexts()
        self.ae.add_supported_context(Verification, "1.2.840.10008.1.2")

    def _add_handlers(self):
        """
        Adds a handler for for processing incoming C-ECHO requests.

        This method overrides the base class method to add a handler
        for the Verification SOP Class, allowing the AE to respond
        to C-ECHO requests.

        This method is intended to be overridden in derived classes.
        """
        self.logger.debug("CEchoSCP._add_handlers")
        super()._add_handlers()
        self.handlers.append((evt.EVT_C_ECHO, handle_cecho, [self.logger]))
