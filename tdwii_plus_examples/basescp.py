from argparse import Namespace
import logging

from pynetdicom import AE, evt
from pynetdicom.apps.common import setup_logging

from tdwii_plus_examples.basehandlers import handle_open, handle_close


class BaseSCP:
    """
    The BaseSCP class is a base class for DICOM Service Class Providers (SCPs).

    This class provides basic functionality for creating and managing
    a DICOM Service Class Provider (SCP) including setting up the
    Application Entity (AE) and handling incoming associations.

    Usage:
        To use the BaseSCP class, create a subclass and override
        the [_add_contexts] and [_add_handlers] methods
        to add presentation contexts and handlers for specific DICOM services.

    Attributes:
        ae_title (str): The title of the Application Entity (AE)
        bind_address (str): The IP address or hostname of the AE
        port (int): The port number the AE will listen on
        logger(logging.Logger): A logger instance

    Methods:
        _add_contexts(self)
            Adds presentation contexts to the SCP instance.
        _add_handlers(self)
            Adds handlers for DICOM communication events to the SCP instance.
        run(self)
            Starts the SCP AE thread.
        stop(self)
            Stops the SCP AE.
    """

    def __init__(self,
                 ae_title: str = "BASE_SCP",
                 bind_address: str = "",
                 port: int = 11112,
                 logger=None):
        """
        Initializes a new instance of the BaseSCP class.
        This method creates an AE without presentation contexts.

        Parameters
        ----------
        ae_title : str or None
            The title of the Application Entity (AE)
            Optional, default: "BASE_SCP"

        bind_address : str or None
            A specific IP address or hostname of the AE
            Optional, default: "" will bind to all interfaces.

        port: int or None
            The port number to listen on
            Optional, default: 11112 (as registered for DICOM at IANA)

        logger: logging.Logger or None
            A logger instance
            Optional, default: None, a debug level logger will be used.
        """
        if logger is None:
            self.logger = setup_logging(
                Namespace(log_type=None, log_level="debug"), "base_scp")
            self.logger.info(
                f"No logger provided, using default logger with level"
                f" {logging.getLevelName(self.logger.level)}")
        elif isinstance(logger, logging.Logger):
            self.logger = logger
            self.logger.info(
                f"Logger set to {logger.name} with level"
                f" {logging.getLevelName(logger.level)}")
        else:
            raise TypeError("logger must be an instance of logging.Logger")

        if not bind_address:
            self.bind_address = ""
            self.logger.info("bind_address empty, binding to all interfaces")
        elif isinstance(bind_address, str):
            self.bind_address = bind_address
            self.logger.debug(f"bind_address set to {bind_address}")
        else:
            raise TypeError("bind_address must be a string or None")

        if port is None:
            self.port = 11112
            self.logger.info("Port not provided, using default port 11112")
        elif isinstance(port, int):
            if port < 0:
                raise ValueError("port must not be negative")
            elif 0 <= port <= 1023 and port != 104:
                raise ValueError(
                    "port must not be in the range (0-1023), except 104")
            elif port == 104:
                self.port = port
                self.logger.warning("DICOM port 104 may need admin privileges")
            elif port in range(1024, 11111) or port in range(11161, 49151):
                self.port = port
                self.logger.warning(
                    "Registered port (1024-49151) may be used by others")
            elif port > 65535:
                raise ValueError("port must not exceed 65535")
            else:
                self.port = port
                self.logger.debug(f"port set to {port}")
        else:
            raise TypeError("port must be an integer or None")

        if not ae_title:
            self.ae_title = "BASE_SCP"
            self.logger.info("ae_title not provided, using default ae_title")
        elif isinstance(ae_title, str):
            self.ae_title = ae_title
            self.logger.debug(f"ae_title set to {ae_title}")
        else:
            raise TypeError("ae_title must be a string or None")

        self.ae = AE(self.ae_title)

        self._add_contexts()

        self.handlers = []
        self._add_handlers()

        self.threaded_server = None

    def _add_contexts(self):
        """
        Adds DICOM presentation contexts to the SCP class.

        This method is intended to be overridden in derived classes.
        """
        pass    # base class, do nothing, pure virtual

    def _add_handlers(self):
        """
        Adds handlers for processing TCP events from incoming associations.

        This method is intended to be overridden in derived classes.
        """
        # To define actions when a TCP connection in opened or closed
        self.handlers.append((evt.EVT_CONN_OPEN, handle_open,
                              [self.logger]))
        self.handlers.append((evt.EVT_CONN_CLOSE, handle_close,
                              [self.logger]))

    def run(self):
        """
        Start the SCP server and listen for incoming association requests

        This method starts an SCP server and begins listening for incoming
        association requests.  The server is run in a separate thread and will
        not block the calling thread.
        """
        # Listen for incoming association requests
        try:
            self.threaded_server = self.ae.start_server(
                (self.bind_address, self.port),
                evt_handlers=self.handlers,
                block=False)
            if self.threaded_server is not None:
                self.logger.info("SCP server started successfully")
        except Exception as e:
            self.logger.error("SCP server failed to start: %s", e)

    def stop(self):
        """
        Stop the SCP server.

        This method shuts down the SCP server by terminating any active
        association servers and thread of the AE.
        """
        self.ae.shutdown()
