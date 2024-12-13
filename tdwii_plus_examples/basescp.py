from argparse import Namespace
import logging

from pynetdicom import AE, evt, ALL_TRANSFER_SYNTAXES
from pynetdicom.apps.common import setup_logging
from pynetdicom.sop_class import Verification

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
            Required, default: "BASE_SCP"

        bind_address : str
            The IP address or hostname of the AE
            Required, default: ""

        port: int
            The port number to listen on
            Required, default: 11112 (as registered for DICOM at IANA)

        logger: logging.Logger
            A logger instance
            Optional, default: None, a debug logger will be used.
        """
        if logger is None:
            self.logger = setup_logging(Namespace(log_type="d", 
                                                  log_level="debug"), 
                                                  "base_scp")
        elif not isinstance(logger, logging.Logger):
            raise TypeError("logger must be an instance of logging.Logger")
        else:
            self.logger = logger

        if not isinstance(bind_address, str) or not bind_address.strip():
            raise ValueError("bind_address must be a non-empty string")
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
        pass    # base class, do nothing, pure virtual
    def _add_handlers(self):
        # To define actions when a TCP connection in opened or closed
        self.handlers.append((evt.EVT_CONN_OPEN, handle_open,
                              [self.logger]))
        self.handlers.append((evt.EVT_CONN_CLOSE, handle_close,
                              [self.logger]))

    def run(self):
        # Listen for incoming association requests
        self.threaded_server = self.ae.start_server(
            (self.bind_address, self.port),
            evt_handlers=self.handlers,
            block=False)

    def stop(self):
        self.ae.shutdown()
