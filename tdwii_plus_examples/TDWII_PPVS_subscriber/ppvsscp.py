import logging
import os
import sys
from argparse import Namespace
from configparser import ConfigParser
from datetime import datetime
from typing import Tuple
from time import sleep
import pydicom.config
from pynetdicom.apps.common import handle_store

from pynetdicom import (
    AE,
    ALL_TRANSFER_SYNTAXES,
    AllStoragePresentationContexts,
    _config,
    _handlers,
    evt,
)
from pynetdicom.apps.common import setup_logging
from pynetdicom.sop_class import Verification
from pynetdicom.utils import set_ae

from basescp import BaseSCP
from echoscp import EchoSCP
from neventscp import NEventSCP
from storescp import StoreSCP

class PPVS_SCP(NEventSCP,StoreSCP):
    def __init__(self,
                 ae_title:str="PPVS_SCP",
                 port:int=11112,
                 logger=None,
                 bind_address:str="",
                 storage_presentation_contexts=AllStoragePresentationContexts,
                 transfer_syntaxes=ALL_TRANSFER_SYNTAXES,
                 custom_cstore_handler = None,
                 nevent_callback = None,
                 store_directory=os.path.curdir
                 ):
        # self.storage_presentation_contexts = storage_presentation_contexts
        # self.transfer_syntaxes = transfer_syntaxes
        self.nevent_callback = nevent_callback
        StoreSCP.__init__(self,
                         ae_title=ae_title,
                         port=port,
                         logger=logger,
                         bind_address=bind_address,
                         custom_handler=custom_cstore_handler,
                         storage_presentation_contexts=storage_presentation_contexts,
                         transfer_syntaxes=transfer_syntaxes,
                         store_directory=store_directory)
        NEventSCP.__init__(self,
                           nevent_callback=nevent_callback,
                           ae_title=ae_title,
                           port=port,
                           logger=logger,
                           bind_address=bind_address,
                           )
        
              
    def _add_contexts(self):
        StoreSCP._add_contexts(self)
        NEventSCP._add_contexts(self)

        
        


    def _add_handlers(self):
       StoreSCP._add_handlers(self)
       NEventSCP._add_handlers(self)

    def run(self):
        # Listen for incoming association requests
        BaseSCP.run(self)

if __name__ == '__main__':
    my_scp = PPVS_SCP()
    my_scp.run()
    while True: sleep(100) # sleep forever
    