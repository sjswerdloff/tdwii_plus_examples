
from argparse import Namespace
from pynetdicom import AE
from pynetdicom.apps.common import setup_logging


class BaseSCP:
    def __init__(self, ae_title: str = "BASE_SCP", port: int = 11112, logger=None, bind_address: str = ""):

        self.ae_title = ae_title
        self.port = port
        if logger is None:
            logger_args = Namespace(log_type="d", log_level="debug")
            self.logger = setup_logging(logger_args, "base_scp")
        else:
            self.logger = logger
        self.bind_address = bind_address
        self.threaded_server = None
        self.ae = AE(self.ae_title)
        self.handlers = []
        self._add_contexts()
        self._add_handlers()

    def _add_contexts(self):
        # self.ae.add_supported_context(Verification, ALL_TRANSFER_SYNTAXES)
        pass  # base class, do nothing, pure virtual

    def _add_handlers(self):
        # self.handlers.append((evt.EVT_C_ECHO, handle_echo, [None, self.logger]))
        pass  # base class, do nothing, pure virtual

    def run(self):
        # Listen for incoming association requests
        self.threaded_server = self.ae.start_server((self.bind_address, self.port), evt_handlers=self.handlers, block=False)
