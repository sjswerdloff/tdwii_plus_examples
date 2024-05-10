import os
from argparse import Namespace
from time import sleep

from basescp import BaseSCP
from cstore_handler import handle_store
from echoscp import EchoSCP
from pynetdicom import ALL_TRANSFER_SYNTAXES, AllStoragePresentationContexts, evt


class StoreSCP(EchoSCP):
    def __init__(
        self,
        ae_title: str = "STORE_SCP",
        port: int = 11112,
        logger=None,
        bind_address: str = "",
        storage_presentation_contexts=AllStoragePresentationContexts,
        transfer_syntaxes=ALL_TRANSFER_SYNTAXES,
        custom_handler=None,
        store_directory=os.path.curdir,
    ):
        self.storage_presentation_contexts = storage_presentation_contexts
        self.transfer_syntaxes = transfer_syntaxes
        if custom_handler is None:
            self.handle_cstore = handle_store
        else:
            self.handle_cstore = custom_handler
        self.store_directory = store_directory
        EchoSCP.__init__(self, ae_title=ae_title, port=port, logger=logger, bind_address=bind_address)

    def _add_contexts(self):
        EchoSCP._add_contexts(self)
        for context in self.storage_presentation_contexts:
            self.ae.add_supported_context(context.abstract_syntax, self.transfer_syntaxes)

    def _add_handlers(self):
        EchoSCP._add_handlers(self)
        args = Namespace(ignore=False, output_directory=self.store_directory)

        self.handlers.append((evt.EVT_C_STORE, self.handle_cstore, [args, self.logger]))

    def run(self):
        # Listen for incoming association requests
        BaseSCP.run(self)


if __name__ == "__main__":
    my_scp = StoreSCP()
    my_scp.run()
    while True:
        sleep(100)  # sleep forever
