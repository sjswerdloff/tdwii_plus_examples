from pydicom import Dataset
from pydicom.uid import UID
from pynetdicom.association import Association
from pynetdicom.sop_class import (
    UnifiedProcedureStepPush,
    UPSFilteredGlobalSubscriptionInstance,
    UPSGlobalSubscriptionInstance,
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

    def __init__(self, logger, called_ip, called_port, called_ae_title, calling_ae_title):
        super().__init__(logger, called_ip, called_port, called_ae_title, calling_ae_title)

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

        assoc.release()
        self.logger.debug("Association released after subscribing")

        return self._handle_response(rsp_status, action_reply)

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
        assoc = self._associate()
        if assoc.is_established:
            self.logger.debug("Association established for ...")
            if matching_keys is not None:
                self.logger.debug("Filtered Global Subscription")
                self.logger.debug(matching_keys)
            else:
                self.logger.debug("Global (Unfiltered) Subscription")

            action_type_id = 3

            success, msg = self._send_upswatchnaction_request(
                assoc=assoc,
                action_type_id=action_type_id,
                deletion_lock=lock,
                matching_keys=matching_keys,
            )
            if success:
                if matching_keys is None:
                    self.logger.info("Global subscription successful")
                else:
                    self.logger.info("Filtered global subscription successful")
            else:
                self.logger.error(msg)

    def unsubscribe_globally(self):
        """Unsubscribe from receiving UPS Event Reports for all existing
        and new UPS Instances.
        """
        assoc = self._associate()
        if assoc.is_established:
            self.logger.debug("Association established for unsubscribing.")

            action_type_id = 4

            success, msg = self._send_upswatchnaction_request(
                assoc=assoc,
                action_type_id=action_type_id,
            )
            if success:
                self.logger.info("Global unsubscription successful")
            else:
                self.logger.error(msg)

    def suspend_global_subscription(self):
        """Unsubscribe from receiving UPS Event Reports for all new UPS
        Instances only.
        """
        assoc = self._associate()
        if assoc.is_established:
            self.logger.debug("Association established for suspending subscription.")

            action_type_id = 5

            success, msg = self._send_upswatchnaction_request(
                assoc=assoc,
                action_type_id=action_type_id,
            )
            if success:
                self.logger.info("Suspend global subscription successful")
            else:
                self.logger.error(msg)

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
        assoc = self._associate()
        if assoc.is_established:
            self.logger.debug("Association established for Subscription to " f"UPS SOP Instance {instance_uid}")

            action_type_id = 3

            success, msg = self._send_upswatchnaction_request(
                assoc=assoc,
                action_type_id=action_type_id,
                instance_uid=instance_uid,
                deletion_lock=lock,
            )
            if success:
                self.logger.info(f"Subscription to UPS SOP Instance {instance_uid} " "successful")
            else:
                self.logger.error(msg)

    def unsubscribe(self, instance_uid: UID):
        """Unsubscribe from receiving UPS Event Reports for a specific
        UPS Instance.
        Parameters
        ----------
        instance_uid: pydicom.uid.UID
                The SOP Instance UID of the UPS Instance to Unsubscribe to.
        lock : bool
            Set to *true* to request the SCP to keep the UPS when it is
            Canceled or Completed.
        """
        assoc = self._associate()
        if assoc.is_established:
            self.logger.debug("Association established for unsubscribing from " f"UPS SOP Instance {instance_uid}")

            action_type_id = 4

            success, msg = self._send_upswatchnaction_request(
                assoc=assoc,
                action_type_id=action_type_id,
                instance_uid=instance_uid,
            )
            if success:
                self.logger.info(f"Unsubscribing from UPS SOP Instance {instance_uid} " "successful")
            else:
                self.logger.error(msg)
