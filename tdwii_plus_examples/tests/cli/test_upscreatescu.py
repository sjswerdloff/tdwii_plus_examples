import contextlib
import io
import os
import tempfile
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

# Import the main function from upscreatescu.py
from tdwii_plus_examples.cli.upscreatescu import main
from tdwii_plus_examples.tls_config import TLSConfig, TLSUsage


class TestUPSCreateSCU(unittest.TestCase):
    @patch("tdwii_plus_examples.cli.upscreatescu.UPSPushNCreateSCU")
    @patch("sys.argv", new=["upscreatescu.py", "127.0.0.1", "104", "test_path", "-e"])
    def test_echo_success(self, mock_scu):
        """Test Verification option"""
        mock_scu_instance = MagicMock()
        mock_scu.return_value = mock_scu_instance
        mock_scu_instance.verify.return_value.status_category = "Success"

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()

        self.assertIn("Verification (C-ECHO) successful", output)
        mock_scu_instance.verify.assert_called_once()

    @patch("tdwii_plus_examples.cli.upscreatescu.UPSPushNCreateSCU")
    @patch("tdwii_plus_examples.cli.upscreatescu.get_files")
    @patch("tdwii_plus_examples.cli.upscreatescu.dcmread")
    @patch("sys.argv", new=["upscreatescu.py", "127.0.0.1", "104", "test_path"])
    def test_create_ups_instances(self, mock_dcmread, mock_get_files, mock_scu):
        """Test UPS Push creation of UPS instances."""
        mock_scu_instance = MagicMock()
        mock_scu.return_value = mock_scu_instance
        mock_scu_instance.create_ups_instances.return_value = 1

        # Mock get_files to return exactly one valid file and one invalid file
        mock_get_files.return_value = (["valid_file.dcm"], ["invalid_file.dcm"])

        # Mock dcmread to return a valid dataset for the valid file
        mock_dcmread.return_value = MagicMock()

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()

        # Assert that the success message is printed
        self.assertIn("UPS creation successful", output)

        # Assert that create_ups_instances is called once
        mock_scu_instance.create_ups_instances.assert_called_once()

    @patch("tdwii_plus_examples.cli.upscreatescu.get_files")
    @patch("tdwii_plus_examples.cli.upscreatescu.dcmread")
    @patch("sys.argv", new=["upscreatescu.py", "127.0.0.1", "11114", "test_path"])
    def test_no_valid_files(self, mock_dcmread, mock_get_files):
        """Test error case where no valid DICOM files are found."""
        mock_get_files.return_value = ([], ["invalid_file.dcm"])

        with self.assertLogs("upspushncreatescu", level="WARNING") as log:
            with self.assertRaises(SystemExit):
                main()

        # Assert that the warning message is in the logs
        self.assertIn("No suitable DICOM files found", log.output[-1])
        mock_dcmread.assert_not_called()

    @patch("tdwii_plus_examples.cli.upscreatescu.get_files")
    @patch("tdwii_plus_examples.cli.upscreatescu.get_contexts")
    @patch("tdwii_plus_examples.cli.upscreatescu.dcmread")
    @patch("sys.argv", new=["upscreatescu.py", "127.0.0.1", "11114", "test_path"])
    def test_failed_dcmread(self, mock_dcmread, mock_get_contexts, mock_get_files):
        """Test error case where DICOM file reading fails."""
        # Mock get_files to return one valid file
        mock_get_files.return_value = (["valid_file.dcm"], [])

        # Mock get_contexts to return the valid file and contexts
        mock_get_contexts.return_value = (["valid_file.dcm"], MagicMock())

        # Mock dcmread to raise an exception for the valid file
        mock_dcmread.side_effect = Exception("Failed to read file")

        with self.assertLogs("upspushncreatescu", level="ERROR") as log:
            main()

        # Assert that the error message is in the logs
        self.assertIn("Failed to read DICOM file valid_file.dcm", log.output[-1])


class TestUPSCreateSCUWithTLS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp_dir.cleanup)
        # Create empty certificate, key and CA files, as only their existence is checked
        for name in ("cert", "key", "ca"):
            path = os.path.join(cls.temp_dir.name, f"{name}.pem")
            open(path, "w").close()
            setattr(cls, name, path)

    def run_main(self, *argv):
        with patch("sys.argv", ["upscreatescu.py", "127.0.0.1", "104", "test_path", "-e", *argv]):
            main()

    @patch("tdwii_plus_examples.cli.upscreatescu.UPSPushNCreateSCU")
    def test_tls_options_are_forwarded(self, mock_scu):
        self.run_main("--tls", "--tls-ca", self.ca)

        tls_config = mock_scu.call_args.kwargs["tls_config"]
        self.assertEqual(tls_config, TLSConfig(ca_cert=self.ca, usage=TLSUsage.CLIENT_AUTH))

    @patch("tdwii_plus_examples.cli.upscreatescu.UPSPushNCreateSCU")
    def test_mtls_options_are_forwarded(self, mock_scu):
        self.run_main("--mtls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca)

        tls_config = mock_scu.call_args.kwargs["tls_config"]
        self.assertEqual(
            tls_config,
            TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True, usage=TLSUsage.CLIENT_AUTH),
        )

    @patch("tdwii_plus_examples.cli.upscreatescu.UPSPushNCreateSCU")
    def test_no_tls_options_means_no_tls(self, mock_scu):
        self.run_main()

        self.assertIsNone(mock_scu.call_args.kwargs["tls_config"])

    @patch("tdwii_plus_examples.cli.upscreatescu.UPSPushNCreateSCU")
    def test_invalid_tls_options_prevent_the_association(self, mock_scu):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as raised:
            self.run_main("--tls")

        self.assertEqual(raised.exception.code, 2)
        self.assertIn("--tls requires --tls-ca", stderr.getvalue())
        mock_scu.assert_not_called()


if __name__ == "__main__":
    unittest.main()
