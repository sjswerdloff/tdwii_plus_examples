import inspect
import traceback

from pynetdicom import AE, evt

from tdwii_plus_examples.basehandlers import handle_close, handle_open
from tdwii_plus_examples.utils.logger import init_logger
from tdwii_plus_examples.utils.validation import validate_port


def get_full_call_stack():
    """Get the complete call stack including code outside the exception path"""
    stack = inspect.stack()
    return [
        {
            "function": frame_info.function,
            "filename": frame_info.filename,
            "lineno": frame_info.lineno,
            "code": (frame_info.code_context[0].strip() if frame_info.code_context else None),
        }
        for frame_info in stack
    ]


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

    def __init__(self, ae_title: str = "BASE_SCP", bind_address: str = "", port: int = 11112, logger=None, **kwargs):
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
        self.logger = init_logger(logger, "base_scp", "BaseSCP")

        if not bind_address:
            self.bind_address = ""
            self.logger.info("bind_address empty, binding to all interfaces")
        elif isinstance(bind_address, str):
            self.bind_address = bind_address
            self.logger.debug(f"bind_address set to {bind_address}")
        else:
            raise TypeError("bind_address must be a string or None")

        self.port = validate_port(port, self.logger)

        if not ae_title:
            self.ae_title = "BASE_SCP"
            self.logger.info("AE title not provided, using default: %s" % self.ae_title)
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
        self.logger.debug("BaseSCP._add_contexts")
        pass  # base class, do nothing, pure virtual

    def _add_handlers(self):
        """
        Adds handlers for processing TCP events from incoming associations.

        This method is intended to be overridden in derived classes.
        """
        self.logger.debug("BaseSCP._add_handlers")
        # To define actions when a TCP connection in opened or closed
        self.handlers.append((evt.EVT_CONN_OPEN, handle_open, [self.logger]))
        self.handlers.append((evt.EVT_CONN_CLOSE, handle_close, [self.logger]))

    def run(self):
        """
        Start the SCP server and listen for incoming association requests

        This method starts an SCP server and begins listening for incoming
        association requests.  The server is run in a separate thread and will
        not block the calling thread.
        """
        self.logger.debug("BaseSCP.run")
        # Listen for incoming association requests
        try:
            self.threaded_server = self.ae.start_server(
                (self.bind_address, self.port), evt_handlers=self.handlers, block=False
            )
            if self.threaded_server is not None:
                self.logger.info("SCP server started successfully")
        except Exception as e:
            self.logger.error("SCP server failed to start: %s", e)
            self.logger.error(traceback.format_exc())
            # Log the full call stack
            call_stack = get_full_call_stack()
            self.logger.error("Full call stack:")
            for i, frame in enumerate(call_stack):
                self.logger.error(f"{i}: {frame['function']} in {frame['filename']}:{frame['lineno']}")
                if frame["code"]:
                    self.logger.error(f"   Code: {frame['code']}")

    def stop(self):
        """
        Stop the SCP server.

        This method shuts down the SCP server by terminating any active
        association servers and thread of the AE.
        """
        self.ae.shutdown()
