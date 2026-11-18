import argparse
import contextlib
import io
import logging
import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, Mock, patch

from tdwii_plus_examples.basescp import TLSConfig
from tdwii_plus_examples.cli.storescp import main


class TestMainFunction(unittest.TestCase):
    @patch("tdwii_plus_examples.cli.storescp.CStoreSCP")
    @patch("tdwii_plus_examples.cli.storescp.argparse.ArgumentParser.parse_args")
    def test_main(self, mock_parse_args, MockCStoreSCP):
        # Mock the arguments
        mock_parse_args.return_value = argparse.Namespace(
            ae_title="TEST_AE",
            bind_address="127.0.0.1",
            port=12345,
            sop_classes=["SecondaryCaptureImageStorage"],
            transfer_syntaxes=["ExplicitVRLittleEndian"],
            custom_handler="my_handler",
            output_directory="/var/tmp/output",
            verbose=False,
            debug=True,
            tls=False,
            mtls=False,
            tls_cert=None,
            tls_key=None,
            tls_ca=None,
        )

        # Mock the custom handler function
        mock_handler = Mock(name="my_handler")

        # Patch the place where the custom handler is used
        with patch("tdwii_plus_examples.cli.storescp.my_handler", mock_handler):
            # Mock the CStoreSCP instance
            mock_cstorescp_instance = MockCStoreSCP.return_value
            mock_cstorescp_instance.run = MagicMock()

            # Run the main function
            with patch.object(sys, "argv", ["storescp.py"]):
                with self.assertLogs("storescp", level="DEBUG") as log:
                    main(loop_forever=False)  # avoid the infinite loop

            # Check that CStoreSCP was initialized with the correct arguments
            MockCStoreSCP.assert_called_once_with(
                ae_title="TEST_AE",
                bind_address="127.0.0.1",
                port=12345,
                logger=logging.getLogger("storescp"),
                sop_classes=["SecondaryCaptureImageStorage"],
                transfer_syntaxes=["ExplicitVRLittleEndian"],
                custom_handler=mock_handler,  # Ensure this is the mock function
                store_directory="/var/tmp/output",
                tls_config=None,
            )

            # Check that the run method was called
            mock_cstorescp_instance.run.assert_called_once()

            # Check the log output
            self.assertIn("Starting up the DICOM Storage SCP...", log.output[0])


class TestMainFunctionTLS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Only the existence of the files is checked by the options, their content is not loaded
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp_dir.cleanup)
        for name in ("cert", "key", "ca"):
            path = os.path.join(cls.temp_dir.name, f"{name}.pem")
            open(path, "w").close()
            setattr(cls, name, path)

    def run_main(self, *argv):
        with patch.object(sys, "argv", ["storescp.py", *argv]):
            main(loop_forever=False)

    @patch("tdwii_plus_examples.cli.storescp.CStoreSCP")
    def test_tls_options_are_forwarded(self, MockCStoreSCP):
        self.run_main("--tls", "--tls-cert", self.cert, "--tls-key", self.key)

        tls_config = MockCStoreSCP.call_args.kwargs["tls_config"]
        self.assertEqual(tls_config, TLSConfig(cert_file=self.cert, key_file=self.key))

    @patch("tdwii_plus_examples.cli.storescp.CStoreSCP")
    def test_mtls_options_are_forwarded(self, MockCStoreSCP):
        self.run_main("--mtls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca)

        tls_config = MockCStoreSCP.call_args.kwargs["tls_config"]
        self.assertEqual(tls_config, TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True))

    @patch("tdwii_plus_examples.cli.storescp.CStoreSCP")
    def test_no_tls_options_means_no_tls(self, MockCStoreSCP):
        self.run_main()

        self.assertIsNone(MockCStoreSCP.call_args.kwargs["tls_config"])

    @patch("tdwii_plus_examples.cli.storescp.CStoreSCP")
    def test_invalid_tls_options_prevent_startup(self, MockCStoreSCP):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as raised:
            self.run_main("--tls", "--tls-cert", self.cert)

        self.assertEqual(raised.exception.code, 2)
        self.assertIn("--tls requires --tls-key", stderr.getvalue())
        MockCStoreSCP.assert_not_called()


if __name__ == "__main__":
    unittest.main()
