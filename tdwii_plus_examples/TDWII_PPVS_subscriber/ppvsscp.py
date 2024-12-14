import os
from time import sleep

from pynetdicom import ALL_TRANSFER_SYNTAXES, AllStoragePresentationContexts

from tdwii_plus_examples import tdwii_config
from tdwii_plus_examples.basescp import BaseSCP
from tdwii_plus_examples.TDWII_PPVS_subscriber.nevent_receiver import NEventReceiver
from tdwii_plus_examples.TDWII_PPVS_subscriber.storescp import StoreSCP


class PPVS_SCP(NEventReceiver, StoreSCP):
    def __init__(
        self,
        ae_title: str = "PPVS_SCP",
        port: int = -1,
        logger=None,
        bind_address: str = "",
        storage_presentation_contexts=AllStoragePresentationContexts,
        transfer_syntaxes=ALL_TRANSFER_SYNTAXES,
        custom_cstore_handler=None,
        nevent_callback=None,
        store_directory=os.path.curdir,
    ):
        # self.storage_presentation_contexts = storage_presentation_contexts
        # self.transfer_syntaxes = transfer_syntaxes
        if port < 1:
            port = tdwii_config.known_ae_port[ae_title]
        self.nevent_callback = nevent_callback
        StoreSCP.__init__(
            self,
            ae_title=ae_title,
            port=port,
            logger=logger,
            bind_address=bind_address,
            custom_handler=custom_cstore_handler,
            storage_presentation_contexts=storage_presentation_contexts,
            transfer_syntaxes=transfer_syntaxes,
            store_directory=store_directory,
        )
        NEventReceiver.__init__(
            self,
            nevent_callback=nevent_callback,
            ae_title=ae_title,
            port=port,
            logger=logger,
            bind_address=bind_address,
        )

    def _add_contexts(self):
        StoreSCP._add_contexts(self)
        NEventReceiver._add_contexts(self)

    def _add_handlers(self):
        StoreSCP._add_handlers(self)
        NEventReceiver._add_handlers(self)

    def run(self):
        # Listen for incoming association requests
        BaseSCP.run(self)


if __name__ == "__main__":
    my_scp = PPVS_SCP()
    my_scp.run()
    while True:
        sleep(100)  # sleep forever
