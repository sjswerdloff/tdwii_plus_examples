import contextlib
import io
import os
import tempfile
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

# Import the main function from storescu.py
from tdwii_plus_examples.cli.storescu import main
from tdwii_plus_examples.tls_config import TLSConfig, TLSUsage


class TestStoreSCU(unittest.TestCase):
    @patch("tdwii_plus_examples.cli.storescu.CStoreSCU")
    @patch("sys.argv", new=["storescu.py", "127.0.0.1", "11112", "test_path", "-e"])
    def test_echo_success(self, mock_scu):
        """Test Verification option (C-ECHO)."""
        mock_scu_instance = MagicMock()
        mock_scu.return_value = mock_scu_instance
        mock_scu_instance.verify.return_value.status_category = "Success"

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()

        self.assertIn("Verification (C-ECHO) successful", output)
        mock_scu_instance.verify.assert_called_once()

    @patch("tdwii_plus_examples.cli.storescu.CStoreSCU")
    @patch("sys.argv", new=["storescu.py", "127.0.0.1", "11112", "test_path", "-e"])
    def test_echo_failure(self, mock_scu):
        """Test Verification option (C-ECHO) failure path."""
        mock_scu_instance = MagicMock()
        mock_scu.return_value = mock_scu_instance
        mock_scu_instance.verify.return_value.status_category = "Failure"

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()

        self.assertIn("Verification (C-ECHO) failed", output)
        mock_scu_instance.verify.assert_called_once()

    @patch("tdwii_plus_examples.cli.storescu.CStoreSCU")
    @patch("tdwii_plus_examples.cli.storescu.get_files")
    @patch("tdwii_plus_examples.cli.storescu.get_contexts")
    @patch("tdwii_plus_examples.cli.storescu.dcmread")
    @patch("sys.argv", new=["storescu.py", "127.0.0.1", "11112", "test_path"])
    def test_store_instances(self, mock_dcmread, mock_get_contexts, mock_get_files, mock_scu):
        """Test storing SOP instances."""
        mock_scu_instance = MagicMock()
        mock_scu.return_value = mock_scu_instance
        mock_scu_instance.store_instances.return_value = 1  # Return an integer

        # Mock get_files to return one valid file path and one invalid file path
        mock_get_files.return_value = (["valid_file.dcm"], ["invalid_file.dcm"])

        # Mock get_contexts to return one valid file and a valid context dict
        mock_get_contexts.return_value = (["valid_file.dcm"], {"1.2.840.10008.5.1.4.1.1.4": ["1.2.840.10008.1.2.1"]})

        # Mock dcmread to return a valid dataset for the valid file
        mock_dcmread.return_value = MagicMock()

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()

        # Assert that the success message is printed
        self.assertIn("Storage successful", output)

        # Assert that store_instances is called once
        mock_scu_instance.store_instances.assert_called_once()

    @patch("tdwii_plus_examples.cli.storescu.get_files")
    @patch("sys.argv", new=["storescu.py", "127.0.0.1", "11112", "test_path"])
    def test_no_valid_files(self, mock_get_files):
        """Test error case where no valid DICOM files are found."""
        mock_get_files.return_value = ([], ["invalid_file.dcm"])

        with self.assertLogs("storescu", level="WARNING") as log:
            with self.assertRaises(SystemExit):
                main()

        # Assert that the warning message is in the logs
        self.assertIn("No suitable DICOM files found", log.output[-1])

    @patch("tdwii_plus_examples.cli.storescu.CStoreSCU")
    @patch("tdwii_plus_examples.cli.storescu.get_contexts")
    @patch("tdwii_plus_examples.cli.storescu.get_files")
    @patch("tdwii_plus_examples.cli.storescu.dcmread")
    @patch("sys.argv", new=["storescu.py", "127.0.0.1", "11112", "test_path"])
    def test_failed_dcmread(self, mock_dcmread, mock_get_files, mock_get_contexts, mock_scu):
        """Test error case where dcmread fails."""
        # Mock get_files to return one valid file
        mock_get_files.return_value = (["valid_file.dcm"], [])

        # Mock dcmread to raise an exception for the valid file
        mock_dcmread.side_effect = Exception("Failed to read file")

        mock_scu_instance = MagicMock()
        mock_scu.return_value = mock_scu_instance
        mock_scu_instance.store_instances.return_value = 1  # Return an integer

        mock_get_contexts.return_value = (["valid_file.dcm"], {"1.2.840.10008.5.1.4.1.1.4": ["1.2.840.10008.1.2.1"]})

        with self.assertLogs("storescu", level="ERROR") as log:
            main()

        # Assert that the error message is in the logs
        self.assertIn("Failed to read DICOM file valid_file.dcm", log.output[-1])


class TestStoreSCUWithTLS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create empty certificate, key and CA files, as only their existence is checked
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp_dir.cleanup)
        for name in ("cert", "key", "ca"):
            path = os.path.join(cls.temp_dir.name, f"{name}.pem")
            open(path, "w").close()
            setattr(cls, name, path)

    def run_main(self, *argv):
        with patch("sys.argv", ["storescu.py", "127.0.0.1", "11112", "-e", *argv]):
            main()

    @patch("tdwii_plus_examples.cli.storescu.CStoreSCU")
    def test_tls_options_are_forwarded(self, mock_scu):
        self.run_main("--tls", "--tls-ca", self.ca)

        tls_config = mock_scu.call_args.kwargs["tls_config"]
        self.assertEqual(tls_config, TLSConfig(ca_cert=self.ca, usage=TLSUsage.CLIENT_AUTH))

    @patch("tdwii_plus_examples.cli.storescu.CStoreSCU")
    def test_mtls_options_are_forwarded(self, mock_scu):
        self.run_main("--mtls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca)

        tls_config = mock_scu.call_args.kwargs["tls_config"]
        self.assertEqual(
            tls_config,
            TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True, usage=TLSUsage.CLIENT_AUTH),
        )

    @patch("tdwii_plus_examples.cli.storescu.CStoreSCU")
    def test_no_tls_options_means_no_tls(self, mock_scu):
        self.run_main()

        self.assertIsNone(mock_scu.call_args.kwargs["tls_config"])

    @patch("tdwii_plus_examples.cli.storescu.CStoreSCU")
    def test_invalid_tls_options_prevent_the_association(self, mock_scu):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as raised:
            self.run_main("--tls")

        self.assertEqual(raised.exception.code, 2)
        self.assertIn("--tls requires --tls-ca", stderr.getvalue())
        mock_scu.assert_not_called()


if __name__ == "__main__":
    unittest.main()
