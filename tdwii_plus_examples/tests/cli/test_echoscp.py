import argparse
import contextlib
import io
import logging
import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from tdwii_plus_examples.basescp import TLSConfig
from tdwii_plus_examples.cli.echoscp import main


class TestMainFunction(unittest.TestCase):
    @patch("tdwii_plus_examples.cli.echoscp.CEchoSCP")
    @patch("tdwii_plus_examples.cli.echoscp.argparse.ArgumentParser.parse_args")
    def test_main(self, mock_parse_args, MockCEchoSCP):
        # Mock the arguments
        mock_parse_args.return_value = argparse.Namespace(
            ae_title="TEST_AE",
            bind_address="127.0.0.1",
            port=12345,
            verbose=False,
            debug=True,
            tls=False,
            mtls=False,
            tls_cert=None,
            tls_key=None,
            tls_ca=None,
        )

        # Mock the CEchoSCP instance
        mock_cechoscp_instance = MockCEchoSCP.return_value
        mock_cechoscp_instance.run = MagicMock()

        # Run the main function
        with patch.object(sys, "argv", ["echoscp.py"]):
            with self.assertLogs("echoscp", level="DEBUG") as log:
                main(loop_forever=False)  # avoid the infinite loop

        # Check that CEchoSCP was initialized with the correct arguments
        MockCEchoSCP.assert_called_once_with(
            ae_title="TEST_AE", bind_address="127.0.0.1", port=12345, logger=logging.getLogger("echoscp"), tls_config=None
        )

        # Check that the run method was called
        mock_cechoscp_instance.run.assert_called_once()

        # Check the log output
        self.assertIn("Starting up the DICOM Verification SCP...", log.output[0])


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
        with patch.object(sys, "argv", ["echoscp.py", *argv]):
            main(loop_forever=False)

    @patch("tdwii_plus_examples.cli.echoscp.CEchoSCP")
    def test_tls_options_are_forwarded(self, MockCEchoSCP):
        self.run_main("--tls", "--tls-cert", self.cert, "--tls-key", self.key)

        tls_config = MockCEchoSCP.call_args.kwargs["tls_config"]
        self.assertEqual(tls_config, TLSConfig(cert_file=self.cert, key_file=self.key))

    @patch("tdwii_plus_examples.cli.echoscp.CEchoSCP")
    def test_mtls_options_are_forwarded(self, MockCEchoSCP):
        self.run_main("--mtls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca)

        tls_config = MockCEchoSCP.call_args.kwargs["tls_config"]
        self.assertEqual(tls_config, TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True))

    @patch("tdwii_plus_examples.cli.echoscp.CEchoSCP")
    def test_no_tls_options_means_no_tls(self, MockCEchoSCP):
        self.run_main()

        self.assertIsNone(MockCEchoSCP.call_args.kwargs["tls_config"])

    @patch("tdwii_plus_examples.cli.echoscp.CEchoSCP")
    def test_invalid_tls_options_prevent_startup(self, MockCEchoSCP):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as raised:
            self.run_main("--tls", "--tls-cert", self.cert)

        self.assertEqual(raised.exception.code, 2)
        self.assertIn("--tls requires --tls-key", stderr.getvalue())
        MockCEchoSCP.assert_not_called()


if __name__ == "__main__":
    unittest.main()
