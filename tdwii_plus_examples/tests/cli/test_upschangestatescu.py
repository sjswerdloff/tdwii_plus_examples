import contextlib
import io
import os
import sys
import tempfile
import unittest
from io import StringIO
from unittest import mock

import tdwii_plus_examples.cli.upschangestatescu as upschangestatescu
from tdwii_plus_examples.tls_config import TLSConfig, TLSUsage


class TestUPSChangeStateSCUCLI(unittest.TestCase):
    def setUp(self):
        self.scu_patch = mock.patch("tdwii_plus_examples.cli.upschangestatescu.UPSPullNActionSCU")
        self.mock_scu_class = self.scu_patch.start()
        self.mock_scu = self.mock_scu_class.return_value

    def tearDown(self):
        self.scu_patch.stop()

    def run_main_with_args(self, args):
        with mock.patch.object(sys, "argv", args), mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            try:
                upschangestatescu.main()
            except SystemExit as e:
                return e.code, mock_stdout.getvalue()
            return 0, mock_stdout.getvalue()

    def test_claim_ups_success(self):
        self.mock_scu.claim_ups.return_value = "1.2.3.4"
        exit_code, output = self.run_main_with_args(["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "IN PROGRESS"])
        self.mock_scu.claim_ups.assert_called_once_with("1.2.3.4.5")
        self.assertEqual(exit_code, 0)
        self.assertIn("Transaction UID: 1.2.3.4", output)

    def test_cancel_ups_success(self):
        self.mock_scu.cancel_ups.return_value = True
        exit_code, output = self.run_main_with_args(
            ["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "CANCELED", "2.3.4.5.6"]
        )
        self.mock_scu.cancel_ups.assert_called_once_with("1.2.3.4.5", "2.3.4.5.6")
        self.assertEqual(exit_code, 0)

    def test_complete_ups_success(self):
        self.mock_scu.complete_ups.return_value = True
        exit_code, output = self.run_main_with_args(
            ["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "COMPLETED", "2.3.4.5.6"]
        )
        self.mock_scu.complete_ups.assert_called_once_with("1.2.3.4.5", "2.3.4.5.6")
        self.assertEqual(exit_code, 0)

    def test_missing_transaction_uid_for_cancel(self):
        with mock.patch.object(sys, "argv", ["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "CANCELED"]):
            with self.assertRaises(SystemExit) as cm:
                upschangestatescu.main()
            self.assertEqual(cm.exception.code, 2)  # parser error code value

    def test_transaction_uid_given_for_in_progress(self):
        with mock.patch.object(
            sys, "argv", ["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "IN PROGRESS", "2.3.4.5.6"]
        ):
            with self.assertRaises(SystemExit) as cm:
                upschangestatescu.main()
            self.assertEqual(cm.exception.code, 2)  # parser error code value

    def test_echo_success(self):
        self.mock_scu.verify.return_value = mock.Mock(status_category="Success")
        exit_code, output = self.run_main_with_args(["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "--echo"])
        self.mock_scu.verify.assert_called_once()
        self.assertEqual(exit_code, 0)

    def test_echo_failure(self):
        self.mock_scu.verify.return_value = mock.Mock(status_category="Failure", status_description="Failed")
        exit_code, output = self.run_main_with_args(["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "--echo"])
        self.mock_scu.verify.assert_called_once()
        self.assertEqual(exit_code, 1)


class TestUPSChangeStateSCUCLIWithTLS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp_dir.cleanup)
        # Create empty certificate, key and CA files, as only their existence is checked
        for name in ("cert", "key", "ca"):
            path = os.path.join(cls.temp_dir.name, f"{name}.pem")
            open(path, "w").close()
            setattr(cls, name, path)

    def setUp(self):
        scu_patch = mock.patch("tdwii_plus_examples.cli.upschangestatescu.UPSPullNActionSCU")
        self.mock_scu_class = scu_patch.start()
        self.addCleanup(scu_patch.stop)
        self.mock_scu_class.return_value.verify.return_value = mock.Mock(status_category="Success")

    def run_main(self, *argv):
        with mock.patch.object(sys, "argv", ["upschangestatescu", "127.0.0.1", "11114", "1.2.3.4.5", "--echo", *argv]):
            upschangestatescu.main()

    def test_tls_options_are_forwarded(self):
        self.run_main("--tls", "--tls-ca", self.ca)

        tls_config = self.mock_scu_class.call_args.kwargs["tls_config"]
        self.assertEqual(tls_config, TLSConfig(ca_cert=self.ca, usage=TLSUsage.CLIENT_AUTH))

    def test_mtls_options_are_forwarded(self):
        self.run_main("--mtls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca)

        tls_config = self.mock_scu_class.call_args.kwargs["tls_config"]
        self.assertEqual(
            tls_config,
            TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True, usage=TLSUsage.CLIENT_AUTH),
        )

    def test_no_tls_options_means_no_tls(self):
        self.run_main()

        self.assertIsNone(self.mock_scu_class.call_args.kwargs["tls_config"])

    def test_invalid_tls_options_prevent_the_association(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as raised:
            self.run_main("--tls")

        self.assertEqual(raised.exception.code, 2)
        self.assertIn("--tls requires --tls-ca", stderr.getvalue())
        self.mock_scu_class.assert_not_called()
