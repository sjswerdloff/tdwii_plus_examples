import os
from time import sleep

from tdwii_plus_examples import tdwii_config
from tdwii_plus_examples.cstorescp import CStoreSCP
from tdwii_plus_examples.upsneventreceiver import UPSNEventReceiver


class PPVS_SCP(CStoreSCP, UPSNEventReceiver):
    def __init__(
        self,
        ae_title: str = "PPVS_SCP",
        port: int = -1,
        logger=None,
        bind_address: str = "",
        storage_sop_classes=None,
        transfer_syntaxes=None,
        custom_cstore_handler=None,
        ups_event_callback=None,
        store_directory=os.path.curdir,
    ):
        if port < 1:
            port = tdwii_config.known_ae_port[ae_title]

        try:
            super().__init__(
                ae_title=ae_title,
                port=port,
                logger=logger,
                bind_address=bind_address,
                sop_classes=storage_sop_classes,
                transfer_syntaxes=transfer_syntaxes,
                custom_handler=custom_cstore_handler,
                store_directory=store_directory,
                ups_event_callback=ups_event_callback,
            )
        except Exception as e:
            if logger:
                logger.error(f"Failed to initialize PPVS_SCP: {e}")
            else:
                print(f"Failed to initialize PPVS_SCP: {e}")
            raise


if __name__ == "__main__":
    my_scp = PPVS_SCP()
    my_scp.run()
    while True:
        sleep(100)  # sleep forever
