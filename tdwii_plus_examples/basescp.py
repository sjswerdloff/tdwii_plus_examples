from argparse import Namespace

from pynetdicom import AE, evt
from pynetdicom.apps.common import setup_logging

from tdwii_plus_examples.transport_handler import handle_open, handle_close


class BaseSCP:
    def __init__(self,
                 ae_title: str = "BASE_SCP",
                 bind_address: str = "",
                 port: int = 11112,
                 logger=None):

        """
        Initializes a DICOM SCP instance without presentation contexts.

        Args:
            ae_title (str): The SCP Application Entity Title.
                            Defaults to "BASE_SCP".
            bind_address (str): The SCP hostname or IP address.
                            Defaults to empty string.
            port (int): The SCP port number.
                            Defaults to 11112. (registered for DICOM at IANA)
            logger (optional): A logging object.
                            If None, a default debug logger will be used.
        """
        if logger is None:
            logger_args = Namespace(log_type="d", log_level="debug")
            self.logger = setup_logging(logger_args, "base_scp")
        else:
            self.logger = logger

        self.ae_title = ae_title
        self.bind_address = bind_address
        self.port = port

        self.ae = AE(self.ae_title)

        self._add_contexts()

        self.handlers = []
        self._add_handlers()

        self.threaded_server = None

    def _add_contexts(self):
        # self.ae.add_supported_context(Verification, ALL_TRANSFER_SYNTAXES)
        pass  # base class, do nothing, pure virtual

    def _add_handlers(self):
        # To define actions when a TCP connection in opened or closed
        # self.handlers.append((evt.EVT_CONN_OPEN, handle_open, [None, self.logger]))
        # self.handlers.append((evt.EVT_CONN_CLOSE, handle_close, [None, self.logger]))
        pass  # base class, do nothing, pure virtual

    def run(self):
        # Listen for incoming association requests
        self.threaded_server = self.ae.start_server((self.bind_address, self.port), evt_handlers=self.handlers, block=False)

    def stop(self):
        self.ae.shutdown()
