# StoreSCU.py
import logging

from pydicom import Dataset
from pydicom.uid import ExplicitVRLittleEndian

# from pydicom.errors import InvalidDicomError
# from pydicom.uid import UID
from pynetdicom import AE  # , Association, UnifiedProcedurePresentationContexts
from pynetdicom.presentation import build_context

from tdwii_plus_examples import tdwii_config

# from typing import Optional, Tuple


# from pynetdicom.sop_class import UnifiedProcedureStepPush, UPSGlobalSubscriptionInstance
# from pynetdicom import ALL_TRANSFER_SYNTAXES, AllStoragePresentationContexts, evt


class StoreSCU:
    def __init__(
        self,
        sending_ae_title: str,
        receiving_ae_title: str,
    ):
        self.calling_ae_title = sending_ae_title
        self.receiving_ae_title = receiving_ae_title
        tdwii_config.load_ae_config()

    def store(self, iods: list[Dataset], receiving_ae_title: str = None) -> bool:
        ae = AE(ae_title=self.calling_ae_title)
        dest_ae_title = self.receiving_ae_title
        if receiving_ae_title is not None:
            dest_ae_title = receiving_ae_title
        # Favouring ExplicitLittleEndian to avoid issues with QRSCP when there are private elements
        # There is a catch-22 if you have privates *and* a string type element with length > 64K
        # For RT SS with way too much data in the contours or RT Ion Plan with compensator voxel thickness with
        # a large number of rows and columns... some of the elements can exceed 64K and then the explicit syntax
        # doesn't have room in the 16 bit unsigned integer for lengths (in bytes) > 64k
        contexts_in_iods = [build_context(x.SOPClassUID, transfer_syntax=[ExplicitVRLittleEndian]) for x in iods]
        assoc = ae.associate(
            tdwii_config.known_ae_ipaddr[dest_ae_title],
            tdwii_config.known_ae_port[dest_ae_title],
            contexts=contexts_in_iods,
            ae_title=dest_ae_title,
        )
        success = False
        if assoc.is_established:
            msg_id = 0
            success = True
            for iod in iods:
                msg_id += 1
                response = assoc.send_c_store(iod, msg_id=msg_id)
                if response.Status != 0x0000:
                    success = False
                    error_msg = (
                        f"Failed with status {response.Status} when trying to transmit {iod.SOPInstanceUID} to {dest_ae_title}"
                    )
                    logging.error(error_msg)
                    break
            assoc.release()
        else:
            assoc.rejected_contexts
            error_msg = f"Failed to form association with {dest_ae_title}"
            logging.error(error_msg)
            logging.error("Rejected contexts:")
            logging.error(assoc.rejected_contexts)
        return success
