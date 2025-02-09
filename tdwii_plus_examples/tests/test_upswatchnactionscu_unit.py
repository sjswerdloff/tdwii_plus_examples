import logging
import unittest
from logging.handlers import MemoryHandler
from unittest.mock import MagicMock, patch

from parameterized import parameterized
from pydicom import Dataset, Sequence
from pydicom.uid import UID
from pynetdicom.association import Association
from pynetdicom.sop_class import (
    UnifiedProcedureStepPush,
    UnifiedProcedureStepWatch,
    UPSFilteredGlobalSubscriptionInstance,
    UPSGlobalSubscriptionInstance,
    Verification,
)

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

            # Verify the call to _handle_response
            mock_handle_response.assert_called_once_with(rsp_status, Dataset())

        # Verify the response
        self.assertEqual(mock_handle_response.return_value, "Success")

    @parameterized.expand(
        [
            (
                "with_watch_sop_class",
                [UID("1.2.840.10008.5.1.4.34.6.2")],
                "[Unified Procedure Step - Watch SOP Class]",
                "Warning",
            ),
            ("without_watch_sop_class", [], "", "Warning"),
            ("assoc_error", [], "", "Error"),
            ("assoc_success", [UID("1.2.840.10008.5.1.4.34.6.2")], "[Unified Procedure Step - Watch SOP Class]", "Success"),
        ]
    )
    @patch("tdwii_plus_examples.upswatchnactionscu.UPSWatchNActionSCU._send_upswatchnaction_request")
    def test_toggle_subscription_context_warning(
        self, name, accepted_sop_classes, expected_abstract_syntax, assoc_status, mock_send_upswatchnaction_request
    ):
        # Mock the association and response handling
        mock_assoc_instance = MagicMock()
        mock_assoc_instance.release.return_value = None

        # Initialize the base_scu instance
        self.upswatchnactionscu = UPSWatchNActionSCU()
        # Set up a memory handler for logging
        self.memory_handler = logging.handlers.MemoryHandler(capacity=10000, target=None)
        self.upswatchnactionscu.logger.addHandler(self.memory_handler)
        # Set the assoc attribute on the base_scu instance
        self.upswatchnactionscu.assoc = mock_assoc_instance

        mock_send_upswatchnaction_request.return_value = UPSWatchNActionSCU.PrimitiveResult(
            status_category="Success",
            status_code=0x0000,  # Example status code for success
            status_description="Request successful",
            dataset=None,
        )

        # Patch the _associate method with the appropriate result
        with patch(
            "tdwii_plus_examples.basescu.BaseSCU._associate",
            return_value=UPSWatchNActionSCU.AssociationResult(
                status=assoc_status,
                description="Some SOP classes were refused"
                if assoc_status == "Warning"
                else "Association error"
                if assoc_status == "Error"
                else "Association successful",
                accepted_sop_classes=accepted_sop_classes,
            ),
        ) as mock_associate:
            # Call the _toggle_subscription method
            result = self.upswatchnactionscu._toggle_subscription(action_type_id=1)

            # Check that the association was attempted
            mock_associate.assert_called_once()

            if assoc_status == "Error":
                self.assertEqual(result.status_category, "AssocFailure")
                self.assertEqual(result.status_code, 0xD000)
                self.assertEqual(result.status_description, "Association error")
                self.assertIsNone(result.dataset)
                mock_send_upswatchnaction_request.assert_not_called()
                mock_assoc_instance.release.assert_not_called()
            elif assoc_status == "Warning":
                if expected_abstract_syntax:
                    mock_send_upswatchnaction_request.assert_called_once()
                    mock_assoc_instance.release.assert_called_once()
                else:
                    mock_send_upswatchnaction_request.assert_not_called()
                    mock_assoc_instance.release.assert_called_once()

                    self.assertEqual(result.status_category, "AssocFailure")
                    self.assertEqual(result.status_code, 0xD001)
                    self.assertEqual(result.status_description, "Some SOP classes were refused")
                    self.assertIsNone(result.dataset)
            elif assoc_status == "Success":
                mock_send_upswatchnaction_request.assert_called_once()
                mock_assoc_instance.release.assert_called_once()

                self.assertEqual(result.status_category, "Success")
                self.assertEqual(result.status_code, 0x0000)
                self.assertEqual(result.status_description, "Request successful")
                self.assertIsNone(result.dataset)

            # Check the log messages in the memory handler
            self.memory_handler.flush()
            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            if assoc_status == "Warning":
                self.assertTrue(any("Some SOP classes were refused" in message for message in log_messages))
                self.assertTrue(
                    any(f"Accepted SOP Classes: {expected_abstract_syntax}" in message for message in log_messages)
                )


if __name__ == "__main__":
    unittest.main()

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
