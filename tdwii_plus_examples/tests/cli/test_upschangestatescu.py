import sys
import unittest
from unittest import mock

import tdwii_plus_examples.cli.upschangestatescu as upschangestatescu


class TestUPSChangeStateSCUCLI(unittest.TestCase):
    def setUp(self):
        self.scu_patch = mock.patch("tdwii_plus_examples.cli.upschangestatescu.UPSPullNActionSCU")
        self.mock_scu_class = self.scu_patch.start()
        self.mock_scu = self.mock_scu_class.return_value

    def tearDown(self):
        self.scu_patch.stop()

    def run_main_with_args(self, args):
        with mock.patch.object(sys, "argv", args):
            try:
                upschangestatescu.main()
            except SystemExit as e:
                return e.code
            return 0

    def test_claim_ups_success(self):
        self.mock_scu.claim_ups.return_value = "1.2.3.4"
        exit_code = self.run_main_with_args(["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "IN PROGRESS"])
        self.mock_scu.claim_ups.assert_called_once_with("1.2.3.4.5")
        self.assertEqual(exit_code, 0)

    def test_cancel_ups_success(self):
        self.mock_scu.cancel_ups.return_value = True
        exit_code = self.run_main_with_args(["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "CANCELED", "2.3.4.5.6"])
        self.mock_scu.cancel_ups.assert_called_once_with("1.2.3.4.5", "2.3.4.5.6")
        self.assertEqual(exit_code, 0)

    def test_complete_ups_success(self):
        self.mock_scu.complete_ups.return_value = True
        exit_code = self.run_main_with_args(["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "COMPLETED", "2.3.4.5.6"])
        self.mock_scu.complete_ups.assert_called_once_with("1.2.3.4.5", "2.3.4.5.6")
        self.assertEqual(exit_code, 0)

    def test_missing_transaction_uid_for_cancel(self):
        with mock.patch.object(sys, "argv", ["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "CANCELED"]):
            with self.assertRaises(SystemExit) as cm:
                upschangestatescu.main()
            self.assertNotEqual(cm.exception.code, 0)

    def test_transaction_uid_given_for_in_progress(self):
        with mock.patch.object(
            sys, "argv", ["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "IN PROGRESS", "2.3.4.5.6"]
        ):
            with self.assertRaises(SystemExit) as cm:
                upschangestatescu.main()
            self.assertNotEqual(cm.exception.code, 0)

    def test_echo_success(self):
        self.mock_scu.verify.return_value = mock.Mock(status_category="Success")
        exit_code = self.run_main_with_args(["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "--echo"])
        self.mock_scu.verify.assert_called_once()
        self.assertEqual(exit_code, 0)

    def test_echo_failure(self):
        self.mock_scu.verify.return_value = mock.Mock(status_category="Failure", status_description="Failed")
        exit_code = self.run_main_with_args(["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "--echo"])
        self.mock_scu.verify.assert_called_once()
        self.assertEqual(exit_code, 0)
