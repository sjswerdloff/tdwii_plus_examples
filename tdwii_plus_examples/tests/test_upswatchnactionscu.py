import logging
import unittest
from logging.handlers import MemoryHandler
from unittest.mock import MagicMock, patch

from parameterized import parameterized
from pydicom import Dataset, Sequence
from pydicom.uid import UID
from pynetdicom.association import Association
from pynetdicom.sop_class import (
    UnifiedProcedureStepEvent,
    UnifiedProcedureStepPush,
    UnifiedProcedureStepWatch,
    UPSFilteredGlobalSubscriptionInstance,
    UPSGlobalSubscriptionInstance,
    Verification,
)

from tdwii_plus_examples.dicom_exceptions import AssociationError, ContextWarning
from tdwii_plus_examples.upswatchnactionscu import UPSWatchNActionSCU


def create_matching_keys():
    matching_keys = Dataset()
    item = Dataset()
    item.CodeValue = "MyMachineName"
    item.CodingSchemeDesignator = "99IHERO2008"
    item.CodeMeaning = "MyMachineName treatment machine"
    seq = Sequence([item])
    matching_keys.ScheduledStationNameCodeSequence = seq
    return matching_keys


class TestUPSWatchNActionSCU(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the logger for this test case to DEBUG level
        # with a stream handler to print the log messages to the console
        cls.test_logger = logging.getLogger("test_basescu")
        cls.test_logger.setLevel(logging.INFO)
        cls.stream_handler = logging.StreamHandler()
        cls.test_logger.addHandler(cls.stream_handler)

    def setUp(self):
        # Set up the logger for the BaseSCU to DEBUG level
        # with a memory handler to store up to 100 log messages
        self.scu_logger = logging.getLogger("basescu")
        self.scu_logger.setLevel(logging.DEBUG)
        self.memory_handler = MemoryHandler(100)
        self.scu_logger.addHandler(self.memory_handler)

        self.scu = UPSWatchNActionSCU(
            logger=self.scu_logger,
            calling_ae_title="CALLING_AE",
            called_ip="127.0.0.1",
            called_port=11112,
            called_ae_title="CALLED_AE",
        )
        self.assoc = MagicMock(spec=Association)
        self.scu.assoc = self.assoc

    def test_add_requested_context(self):
        self.assertTrue(
            any(ctx.abstract_syntax in [UnifiedProcedureStepWatch, Verification] for ctx in self.scu.ae.requested_contexts)
        )

    @parameterized.expand(
        [
            (3, UPSGlobalSubscriptionInstance, True, create_matching_keys()),
            (3, UPSGlobalSubscriptionInstance, False, None),
            (3, "1.2.3.4", False, None),
            (4, UPSGlobalSubscriptionInstance, False, None),
            (4, "1.2.3.4", False, None),
            (5, UPSGlobalSubscriptionInstance, False, None),
        ]
    )
    def test_send_upswatchnaction_request(self, action_type_id, instance_uid, deletion_lock, matching_keys):
        with patch("tdwii_plus_examples.upswatchnactionscu.UPSWatchNActionSCU._handle_response") as mock_handle_response:
            mock_handle_response.return_value = "Success"

            # Configure the mock to return a tuple with two values
            rsp_status = Dataset()
            rsp_status.Status = 0x0000  # Example status code indicating success
            self.assoc.send_n_action.return_value = (rsp_status, Dataset())

            self.scu._send_upswatchnaction_request(
                assoc=self.assoc,
                action_type_id=action_type_id,
                instance_uid=instance_uid,
                deletion_lock=deletion_lock,
                matching_keys=matching_keys,
            )

            # Verify the action_info dataset
            action_info = self.assoc.send_n_action.call_args[1]["dataset"]
            self.assertEqual(action_info.ReceivingAE, self.scu.calling_ae_title)
            if action_type_id == 3:
                self.assertEqual(action_info.DeletionLock, str(deletion_lock).upper())
                if matching_keys is not None:
                    self.assertEqual(
                        self.assoc.send_n_action.call_args[1]["instance_uid"], UPSFilteredGlobalSubscriptionInstance
                    )
                    for elem in matching_keys:
                        self.assertIn(elem.tag, action_info)
                else:
                    self.assertEqual(self.assoc.send_n_action.call_args[1]["instance_uid"], instance_uid)
            else:
                self.assertEqual(self.assoc.send_n_action.call_args[1]["instance_uid"], instance_uid)

            # Verify the call to send_n_action
            self.assoc.send_n_action.assert_called_once_with(
                dataset=action_info,
                action_type=action_type_id,
                class_uid=UnifiedProcedureStepPush,
                instance_uid=self.assoc.send_n_action.call_args[1]["instance_uid"],
            )

    @parameterized.expand(
        [
            ("success", None, None, True),
            ("association_error", AssociationError("Association failed"), None, False),
            (
                "context_warning_accepted",
                ContextWarning(
                    "Context warning",
                    accepted_sop_classes=[Verification, UnifiedProcedureStepWatch],
                    refused_sop_classes=[UnifiedProcedureStepEvent],
                ),
                None,
                True,
            ),
            (
                "context_warning_not_accepted",
                ContextWarning(
                    "Context warning", accepted_sop_classes=[Verification], refused_sop_classes=[UnifiedProcedureStepWatch]
                ),
                None,
                False,
            ),
        ]
    )
    def test_toggle_subscription(self, name, associate_exception, warning_exception, safe_to_proceed):
        if associate_exception:
            self.scu._associate = MagicMock(side_effect=associate_exception)
        elif warning_exception:
            self.scu._associate = MagicMock(side_effect=warning_exception)
        else:
            self.scu._associate = MagicMock()

        action_type_id = 3
        instance_uid = UPSGlobalSubscriptionInstance
        lock = True
        matching_keys = create_matching_keys()

        if safe_to_proceed:
            # Configure the mock to return a tuple with a valid Dataset and another Dataset
            rsp_status = Dataset()
            rsp_status.Status = 0x0000  # Example status code indicating success
            self.assoc.send_n_action.return_value = (rsp_status, Dataset())

        if associate_exception or warning_exception:
            with self.assertRaises((AssociationError, ContextWarning)):
                with patch(
                    "tdwii_plus_examples.upswatchnactionscu.UPSWatchNActionSCU._send_upswatchnaction_request"
                ) as mock_send_request:
                    self.scu._toggle_subscription(
                        action_type_id=action_type_id, instance_uid=instance_uid, lock=lock, matching_keys=matching_keys
                    )
        else:
            with patch(
                "tdwii_plus_examples.upswatchnactionscu.UPSWatchNActionSCU._send_upswatchnaction_request"
            ) as mock_send_request:
                self.scu._toggle_subscription(
                    action_type_id=action_type_id, instance_uid=instance_uid, lock=lock, matching_keys=matching_keys
                )

        if safe_to_proceed:
            mock_send_request.assert_called_once_with(
                assoc=self.assoc,
                action_type_id=action_type_id,
                instance_uid=instance_uid,
                deletion_lock=lock,
                matching_keys=matching_keys,
            )
        else:
            mock_send_request.assert_not_called()
            self.assertTrue(
                any("UPS Watch SOP Class not accepted" in record.getMessage() for record in self.memory_handler.buffer)
            )
            self.assoc.release.assert_called_once()
            self.assertTrue(any("Association released" in record.getMessage() for record in self.memory_handler.buffer))

    @parameterized.expand(
        [
            (True, create_matching_keys(), "Filtered Global Subscription"),
            (False, None, "(Unfiltered) Global Subscription"),
        ]
    )
    def test_subscribe_globally(self, lock, matching_keys, expected_log_message):
        with patch(
            "tdwii_plus_examples.upswatchnactionscu.UPSWatchNActionSCU._toggle_subscription"
        ) as mock_toggle_subscription:
            self.scu.subscribe_globally(lock=lock, matching_keys=matching_keys)
            mock_toggle_subscription.assert_called_once_with(action_type_id=3, lock=lock, matching_keys=matching_keys)
            self.assertTrue(any(expected_log_message in record.getMessage() for record in self.memory_handler.buffer))
            if matching_keys is not None:
                self.assertTrue(any(str(matching_keys) in record.getMessage() for record in self.memory_handler.buffer))
            # Log the messages from memory_handler
            for record in self.memory_handler.buffer:
                self.test_logger.debug(record.getMessage())

    @patch("tdwii_plus_examples.upswatchnactionscu.UPSWatchNActionSCU._toggle_subscription")
    def test_unsubscribe_globally(self, mock_toggle_subscription):
        self.scu.unsubscribe_globally()
        mock_toggle_subscription.assert_called_once_with(action_type_id=4)
        self.assertTrue(any("Global Unsubscription" in record.getMessage() for record in self.memory_handler.buffer))

    @patch("tdwii_plus_examples.upswatchnactionscu.UPSWatchNActionSCU._toggle_subscription")
    def test_suspend_global_subscription(self, mock_toggle_subscription):
        self.scu.suspend_global_subscription()
        mock_toggle_subscription.assert_called_once_with(action_type_id=5)
        self.assertTrue(any("Suspend Global Subscription" in record.getMessage() for record in self.memory_handler.buffer))

    @patch("tdwii_plus_examples.upswatchnactionscu.UPSWatchNActionSCU._toggle_subscription")
    def test_subscribe(self, mock_toggle_subscription):
        instance_uid = UID("1.2.3.4")
        self.scu.subscribe(instance_uid=instance_uid, lock=True)
        mock_toggle_subscription.assert_called_once_with(action_type_id=3, instance_uid=instance_uid, lock=True)
        self.assertTrue(any("Single UPS Subscription" in record.getMessage() for record in self.memory_handler.buffer))

    @patch("tdwii_plus_examples.upswatchnactionscu.UPSWatchNActionSCU._toggle_subscription")
    def test_unsubscribe(self, mock_toggle_subscription):
        instance_uid = UID("1.2.3.4")
        self.scu.unsubscribe(instance_uid=instance_uid)
        mock_toggle_subscription.assert_called_once_with(action_type_id=4, instance_uid=instance_uid)
        self.assertTrue(any("Single UPS Unsubscription" in record.getMessage() for record in self.memory_handler.buffer))


if __name__ == "__main__":
    unittest.main()
