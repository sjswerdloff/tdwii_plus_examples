from time import sleep

from pynetdicom import ALL_TRANSFER_SYNTAXES, evt
from pynetdicom.sop_class import Verification

from tdwii_plus_examples.basescp import BaseSCP
from tdwii_plus_examples.TDWII_PPVS_subscriber.nevent_receiver_handlers import (
    handle_echo,
)


class EchoSCP:
    def __init__(self, ae_title: str = "ECHO_SCP", port: int = 11112, logger=None, bind_address: str = ""):
        BaseSCP.__init__(self, ae_title=ae_title, port=port, logger=logger, bind_address=bind_address)

    def _add_contexts(self):
        BaseSCP._add_contexts(self)
        self.ae.add_supported_context(Verification, ALL_TRANSFER_SYNTAXES)

    def _add_handlers(self):
        BaseSCP._add_handlers(self)
        self.handlers.append((evt.EVT_C_ECHO, handle_echo, [None, self.logger]))

    def run(self):
        # Listen for incoming association requests
        BaseSCP.run(self)


if __name__ == "__main__":
    myecho_scp = EchoSCP()
    myecho_scp.run()
    while True:
        sleep(100)  # sleep forever
