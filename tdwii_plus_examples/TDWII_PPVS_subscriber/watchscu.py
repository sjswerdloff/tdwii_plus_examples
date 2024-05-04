# WatchSCU.py
import logging
from typing import Optional, Tuple

from pydicom import Dataset
from pydicom.errors import InvalidDicomError
from pydicom.uid import UID
from pynetdicom import AE, Association, UnifiedProcedurePresentationContexts
from pynetdicom.sop_class import UnifiedProcedureStepPush, UPSGlobalSubscriptionInstance


class WatchSCU:
    def __init__(
        self,
        calling_ae_title: str,
        receiving_ae_title: str = None,
    ):
        self.calling_ae_title = calling_ae_title
        if receiving_ae_title is None:
            self.receiving_ae_title = self.calling_ae_title
        else:
            self.receiving_ae_title = receiving_ae_title

    def create_action_info(self, match_on_beam_number: bool = False, match_on_step_state: bool = False) -> Dataset:
        return create_action_info(match_on_beam_number=match_on_beam_number, match_on_step_state=match_on_step_state)

    def set_subscription_ae(self, watched_ae_title: str, ip_addr: str = None, port: int = None):
        self.watched_ae_title = watched_ae_title
        self.ip_addr = ip_addr
        self.port = port

    def subscribe(
        self, watched_ae_title: str = None, ip_addr: str = None, port: int = None, matching_keys: Dataset = None
    ) -> bool:
        success = True
        watched_ip_addr = ip_addr
        if watched_ip_addr is None:
            watched_ip_addr = self.ip_addr
        watched_port = port
        if watched_port is None:
            watched_port = self.port
        if watched_ae_title is None:
            watched_ae_title = self.watched_ae_title

        ae = AE(ae_title=self.calling_ae_title)
        assoc = ae.associate(
            watched_ip_addr,
            watched_port,
            contexts=UnifiedProcedurePresentationContexts,
            ae_title=watched_ae_title,
        )
        if assoc.is_established:
            try:
                status, response = send_global_watch_registration(
                    calling_ae_title=self.calling_ae_title,
                    receiving_ae_title=self.receiving_ae_title,
                    assoc=assoc,
                    action_info=matching_keys,
                )
                dbg_message = f"Status: {status}  response {response}"
                logging.getLogger().debug(dbg_message)
            except InvalidDicomError:
                logging.getLogger().error("Bad DICOM: ")
                success = False
            except Exception as exc:
                logging.getLogger().error("Watch Registration (N-ACTION-RQ) failed")
                logging.getLogger().exception(exc)
                success = False

            assoc.release()
        else:
            logging.getLogger().error("Watch Registration failed to make Association")
            success = False

        return success

    def unsubscribe(
        self, watched_ae_title: str = None, ip_addr: str = None, port: int = None, matching_keys: Dataset = None
    ) -> bool:
        success = True
        watched_ip_addr = ip_addr
        if watched_ip_addr is None:
            watched_ip_addr = self.ip_addr
        watched_port = port
        if watched_port is None:
            watched_port = self.port
        if watched_ae_title is None:
            watched_ae_title = self.watched_ae_title

        ae = AE(ae_title=self.calling_ae_title)
        assoc = ae.associate(
            watched_ip_addr,
            watched_port,
            contexts=UnifiedProcedurePresentationContexts,
            ae_title=watched_ae_title,
        )
        if assoc.is_established:
            try:
                status, response = send_global_watch_delete_registration(
                    calling_ae_title=self.calling_ae_title,
                    receiving_ae_title=self.receiving_ae_title,
                    assoc=assoc,
                    action_info=matching_keys,
                )
                dbg_message = f"Status: {status}  response {response}"
                logging.getLogger().debug(dbg_message)
            except InvalidDicomError:
                logging.getLogger().error("Bad DICOM: ")
                success = False
            except Exception as exc:
                logging.getLogger().error("Watch Delete Registration (N-ACTION-RQ) failed")
                logging.getLogger().exception(exc)
                success = False

            assoc.release()
        else:
            logging.getLogger().error("Watch Delete Registration failed to make Association")
            success = False

        return success


def send_action(
    assoc: Association,
    class_uid: UID,
    instance_uid: UID,
    action_type=3,
    action_info=None,
) -> Tuple[Dataset, Optional[Dataset]]:
    """Send an N-ACTION request via `assoc`

    Parameters
    ----------
    assoc : association.Association
        The association sending the request.
    class_uid : pydicom.uid.UID
        The *Requested SOP Class UID* to use.
    instance_uid: pydicom.uid.UID
        The *Requested SOP Instance UID* to use.
    action_type : int, optional
        The *Action Type ID* to use.  default 3, global subscription
    action_info : None or pydicom.dataset.Dataset, optional
        The *Action Information* to use.
    """
    return assoc.send_n_action(action_info, action_type, class_uid, instance_uid)


def send_global_watch_registration(
    calling_ae_title: str, receiving_ae_title: str, assoc: Association, action_info: Dataset = None
):
    """_summary_

    Args:
        calling_ae_title (str): _description_
        receiving_ae_title (str): _description_
        assoc (Association): _description_
        action_info (Dataset, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    ds = action_info
    if ds is None:
        ds = Dataset()
        ds.DeletionLock = "FALSE"
        ds.RequestingAE = calling_ae_title
        ds.ReceivingAE = receiving_ae_title
        ds.RequestedSOPInstanceUID = UPSGlobalSubscriptionInstance
        ds.RequestedSOPClassUID = UnifiedProcedureStepPush
        # ds.RequestedSOPClassUID = UnifiedProcedureStepWatch
    return send_action(
        assoc=assoc,
        class_uid=ds.RequestedSOPClassUID,
        instance_uid=ds.RequestedSOPInstanceUID,
        action_type=3,  # subscribe
        action_info=ds,
    )


def send_global_watch_delete_registration(
    calling_ae_title: str, receiving_ae_title: str, assoc: Association, action_info: Dataset = None
):
    """_summary_

    Args:
        calling_ae_title (str): _description_
        receiving_ae_title (str): _description_
        assoc (Association): _description_
        action_info (Dataset, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    ds = action_info
    if ds is None:
        ds = Dataset()
        ds.DeletionLock = "FALSE"
        ds.RequestingAE = calling_ae_title
        ds.ReceivingAE = receiving_ae_title
        ds.RequestedSOPInstanceUID = UPSGlobalSubscriptionInstance
        ds.RequestedSOPClassUID = UnifiedProcedureStepPush
        # ds.RequestedSOPClassUID = UnifiedProcedureStepWatch
    return send_action(
        assoc=assoc,
        class_uid=ds.RequestedSOPClassUID,
        instance_uid=ds.RequestedSOPInstanceUID,
        action_type=4,  # unsubscribe
        action_info=ds,
    )


def create_action_info(match_on_beam_number: bool = False, match_on_step_state: bool = False) -> Dataset:
    if not (match_on_beam_number or match_on_step_state):
        return None
    else:
        ds = Dataset()
        # populate with the sequence and elements
        logging.getLogger().error("Matching Keys for WatchSCU Not Implemented")
        return ds
