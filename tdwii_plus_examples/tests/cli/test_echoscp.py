import argparse
import logging
import sys
import unittest
from unittest.mock import MagicMock, patch

from tdwii_plus_examples.cli.echoscp import main


class TestMainFunction(unittest.TestCase):
    @patch("tdwii_plus_examples.cli.echoscp.CEchoSCP")
    @patch("tdwii_plus_examples.cli.echoscp.argparse.ArgumentParser.parse_args")
    def test_main(self, mock_parse_args, MockCEchoSCP):
        # Mock the arguments
        mock_parse_args.return_value = argparse.Namespace(
            ae_title="TEST_AE", bind_address="127.0.0.1", port=12345, verbose=False, debug=True
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
            ae_title="TEST_AE", bind_address="127.0.0.1", port=12345, logger=logging.getLogger("echoscp")
        )

        # Check that the run method was called
        mock_cechoscp_instance.run.assert_called_once()

        # Check the log output
        self.assertIn("Starting up the DICOM Verification SCP...", log.output[0])


if __name__ == "__main__":
    unittest.main()
