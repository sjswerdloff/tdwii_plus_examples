from pydicom import Dataset
from pydicom.uid import UID
from pynetdicom.association import Association
from pynetdicom.sop_class import (
    UnifiedProcedureStepPush,
    UnifiedProcedureStepWatch,
    UPSFilteredGlobalSubscriptionInstance,
    UPSGlobalSubscriptionInstance,
)
from pynetdicom.status import UNIFIED_PROCEDURE_STEP_SERVICE_CLASS_STATUS

from tdwii_plus_examples._dicom_exceptions import (
    AssociationError,
    ContextWarning,
    ResponseError,
    ResponseUnknown,
    ResponseWarning,
)
from tdwii_plus_examples.basescu import BaseSCU


class UPSWatchNActionSCU(BaseSCU):
    """
    A subclass of the BaseSCU class that implements a DICOM Service
    Class User (SCU) for the N-ACTION - Un/Subscribe DIMSE of the
    Service Group Applicable to UPS Watch SOP Class.

    This class provides functionality for subscribing to receive UPS
    Event Reports for specific or all UPS Instances managed by the SCP
    and for unsubscribing or suspending the subscription.

    Usage:
        To use the UPSWatchNActionSCU class, create an instance and call
        the subscribe_globally, unsubscribe, or suspend methods.

    Attributes:
        calling_ae_title (str) : The title of the calling AE
        called_ae_title (str)  : The title of the called AE
        called_ip (str)        : The IP address or hostname of the called AE
        called_port (int)      : Theport number of the called AE
        logger(logging.Logger) : A logger instance

    Methods:
        subscribe_globally(self, lock: bool = False)
            Subscribes to receive UPS Event Reports for all UPS Instances.
        unsubscribe(self)
            Unsubscribes from receiving UPS Event Reports.
        suspend(self)
            Suspends the global subscription.
    """

    def __init__(
        self, logger, calling_ae_title: str = None, called_ip: str = None, called_port: int = None, called_ae_title: str = None
    ):
        super().__init__(
            logger,
            calling_ae_title=calling_ae_title,
            called_ip=called_ip,
            called_port=called_port,
            called_ae_title=called_ae_title,
        )

    def _add_requested_context(self):
        """
        Adds the DICOM UPS Push SOP Class presentation context to the AE.
        Default transfer syntaxes are included.
        """
        super()._add_requested_context()
        self.ae.add_requested_context(UnifiedProcedureStepWatch)
        self.logger.debug(
            "Verification Presentation context added:\n" + "\n".join(str(ctx) for ctx in self.ae.requested_contexts)
        )

    def _send_upswatchnaction_request(
        self,
        assoc: Association,
        action_type_id: int,
        instance_uid: UID = UPSGlobalSubscriptionInstance,
        deletion_lock: bool = False,
        matching_keys: Dataset = None,
    ) -> tuple:
        """
        Send an N-ACTION - Un/Subscribe request.

        Parameters
        ----------
        action_type_id : int
            The *Action Type ID* to use.
        instance_uid: pydicom.uid.UID
            The SOP Instance UID of the UPS Instance to Un/Subscribe to.
            Default: UPS Watch well-known UID for Global Subscription or
            for Filtered Global Subscription if matching_keys are present.
        deletion_lock : bool
            The *Deletion Lock* attribute value (default: FALSE).
        matching_keys : pydicom.Dataset
            The *Matching Keys* to filter the UPS to subscribe to.

        Required action_info attributes are specified in PS3.4 Table CC.2.3-1
        with corrections from CP 2505.
        +----------------------------+----+---------------+------------+-----+
        | Action Type Name           | ID | Attribute Name| Tag        | SCU |
        +----------------------------+----+---------------+------------+-----+
        | Subscribe to Receive UPS   | 3  | Receiving AE  | (0074,1234)| 1   |
        | Event Reports              |    +---------------+------------+-----+
        |                            |    | Deletion Lock | (0074,1230)| 1   |
        |                            |    +---------------+------------+-----+
        |                            |    | Matching Keys |            | 1C  |
        |                            |    | (see Section  |            |     |
        |                            |    | CC.2.3.3.1)   |            |     |
        +----------------------------+----+---------------+------------+-----+
        | Unsubscribe from Receiving | 4  | Receiving AE  | (0074,1234)| 1   |
        | UPS Event Reports          |    |               |            |     |
        +----------------------------+----+---------------+------------+-----+
        | Suspend Global Subscription| 5  | Receiving AE  | (0074,1234)| 1   |
        +----------------------------+----+---------------+------------+-----+

        Returns
        -------
        bool:
            True if the request was successful, False otherwise.
        str:
            The message indicating the outcome of the request derived from
            the status code from the N-ACTION - Un/Subscribe response.

        Valid status codes are specified in PS3.4 Table CC.2.3-3
        +----------------+-----------------------------------+-------------+
        | Service Status | Further Meaning                   | Status Code |
        +----------------+-----------------------------------+-------------+
        | Success        | The requested change of           | 0000        |
        |                | subscription state was performed  |             |
        +----------------+-----------------------------------+-------------+
        | Warning        | Deletion Lock not granted.        | B301        |
        +----------------+-----------------------------------+-------------+
        | Failure        | Failed: Specified SOP Instance    | C307        |
        |                | UID does not exist or is not a    |             |
        |                | UPS Instance managed by this SCP  |             |
        |                +-----------------------------------+-------------+
        |                | Failed: Receiving AE Title is     | C308        |
        |                | Unknown to this SCP               |             |
        |                +-----------------------------------+-------------+
        |                | Failed: Specified action not      | C314        |
        |                | appropriate for specified         |             |
        |                | instance                          |             |
        |                +-----------------------------------+-------------+
        |                | Failed: SCP does not support      | C315        |
        |                | Event Reports                     |             |
        +----------------+-----------------------------------+-------------+
        """
        action_info = Dataset()
        action_info.ReceivingAE = self.calling_ae_title
        if action_type_id == 3:
            action_info.DeletionLock = str(deletion_lock).upper()
            if matching_keys is not None:
                instance_uid = UPSFilteredGlobalSubscriptionInstance
                for elem in matching_keys:
                    action_info.add(elem)
        rsp_status = Dataset()
        self.logger.debug("Sending N-ACTION request")
        rsp_status, action_reply = assoc.send_n_action(
            dataset=action_info,
            action_type=action_type_id,
            class_uid=UnifiedProcedureStepPush,
            instance_uid=instance_uid,
        )

        try:
            self.status = self._handle_response(rsp_status, action_reply)
        except ResponseWarning as warning:
            self.logger.warning(
                f"{warning.message} (Status Code: {warning.status_code})")
            raise
        except ResponseError as error:
            self.logger.error(
                f"{error.message} (Status Code: {error.status_code})")
            raise
        except ResponseUnknown as unknown:
            self.logger.error(
                f"{unknown.message} (Status Code: {unknown.status_code})")
            raise
        finally:
            self.assoc.release()
            self.logger.debug("Association released")

    def _toggle_subscription(self, action_type_id, instance_uid=UPSGlobalSubscriptionInstance, lock=False, matching_keys=None):
        safe_to_proceed = False
        try:
            self._associate()
            safe_to_proceed = True
        except AssociationError as error:
            self.logger.error(str(error))
            raise
        except ContextWarning as warning:
            accepted_sop_names = [
                f"[{UID(uid).name}]" for uid in warning.accepted_sop_classes]
            self.logger.warning(
                f"{warning} - Accepted Transfer Syntaxes: {', '.join(accepted_sop_names)}")
            if "[Unified Procedure Step - Watch SOP Class]" in accepted_sop_names:
                safe_to_proceed = True
            raise
        finally:
            if safe_to_proceed:
                self._send_upswatchnaction_request(
                    assoc=self.assoc,
                    action_type_id=action_type_id,
                    instance_uid=instance_uid,
                    deletion_lock=lock,
                    matching_keys=matching_keys,
                )
            else:
                self.logger.error("UPS Push SOP Class not accepted")
                if self.assoc:
                    self.assoc.release()
                    self.logger.debug("Association released")

    def subscribe_globally(self, lock: bool = False, matching_keys=None):
        """Subscribe to receive UPS Event Reports for all existing
        and new UPS Instances (w/ or w/o Deletion Lock).
        Parameters
        ----------
        lock : bool
            Set to *true* to request the SCP to keep a UPS when it is
            Canceled or Completed.
        matching_keys : pydicom.Dataset
            The *Matching Keys* to filter the UPS to subscribe to.
        """
        if matching_keys is not None:
            self.logger.debug("Filtered Global Subscription")
            self.logger.debug(matching_keys)
        else:
            self.logger.debug("(Unfiltered) Global Subscription")
        self._toggle_subscription(
            action_type_id=3, lock=lock, matching_keys=matching_keys)

    def unsubscribe_globally(self):
        """Unsubscribe from receiving UPS Event Reports for all existing
        and new UPS Instances.
        """
        self.logger.debug("Global Unsubscription")
        self._toggle_subscription(action_type_id=4)

    def suspend_global_subscription(self):
        """Unsubscribe from receiving UPS Event Reports for all new UPS
        Instances only.
        """
        self.logger.debug("Suspend Global Subscription")
        self._toggle_subscription(action_type_id=5)

    def subscribe(self, instance_uid: UID, lock: bool = False):
        """Subscribe to receive UPS Event Reports for a specific
        UPS Instance (w/ or w/o Deletion Lock).
        Parameters
        ----------
        instance_uid: pydicom.uid.UID
            The SOP Instance UID of the UPS Instance to subscribe to.
        lock : bool
            Set to *true* to request the SCP to keep the UPS when it is
            Canceled or Completed.
        """
        self.logger.debug("Single UPS Subscription")
        self._toggle_subscription(
            action_type_id=3, instance_uid=instance_uid, lock=lock)

    def unsubscribe(self, instance_uid: UID):
        """Unsubscribe from receiving UPS Event Reports for a specific
        UPS Instance.
        Parameters
        ----------
        instance_uid: pydicom.uid.UID
                The SOP Instance UID of the UPS Instance to Unsubscribe to.
        """
        self.logger.debug("Single UPS Unsubscription")
        self._toggle_subscription(action_type_id=4, instance_uid=instance_uid)

    def _get_status_description(self, status_code):
        return UNIFIED_PROCEDURE_STEP_SERVICE_CLASS_STATUS.get(status_code, ("Unknown", "Unknown status code"))[1]
