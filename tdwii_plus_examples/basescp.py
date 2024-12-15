from argparse import Namespace

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
        logger: A logger instance (optional)

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
        ae_title : str
            The title of the Application Entity (AE)
            Optional, default: "BASE_SCP"

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
            self.logger = setup_logging(
                Namespace(log_type="d", log_level="debug"), "base_scp")
        # elif not isinstance(self.logger, logging.Logger):
        #     raise TypeError("logger must be an instance of logging.Logger")
        else:
            self.logger = logger

        if not isinstance(bind_address, str):
            raise ValueError("bind_address must be a string")
        if not bind_address:
            self.logger.debug("bind_address empty, binding to all interfaces")
        self.bind_address = bind_address

        if not isinstance(port, int):
            raise TypeError("port must be an integer")
        self.port = port

        if not isinstance(ae_title, str):
            raise TypeError("ae_title must be a string")
        self.ae_title = ae_title
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
        Adds handlers for processing DICOM events from incoming associations.

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
        self.threaded_server = self.ae.start_server(
            (self.bind_address, self.port),
            evt_handlers=self.handlers,
            block=False)

    def stop(self):
        """
        Stop the SCP server.

        This method shuts down the SCP server by terminating any active
        association servers and thread of the AE.
        """
        self.ae.shutdown()
