import argparse
import logging
import sys
import unittest
from unittest.mock import MagicMock, Mock, patch

from tdwii_plus_examples.cli.upseventreceiver import main


class TestMainFunction(unittest.TestCase):
    @patch("tdwii_plus_examples.cli.upseventreceiver.UPSNEventReceiver")
    @patch("tdwii_plus_examples.cli.upseventreceiver.argparse.ArgumentParser.parse_args")
    def test_main(self, mock_parse_args, MockUPSNEventReceiver):
        # Mock the arguments
        mock_parse_args.return_value = argparse.Namespace(
            ae_title="TEST_AE",
            bind_address="127.0.0.1",
            port=12345,
            transfer_syntaxes=["ExplicitVRLittleEndian"],
            callback="my_upsevent_callback",
            verbose=False,
            debug=True,
        )

        # Mock the custom callback function
        mock_callback = Mock(name="my_upsevent_callback")

        # Patch the place where the custom callback is used
        with patch("tdwii_plus_examples.cli.upseventreceiver.my_upsevent_callback", mock_callback):
            # Mock the UPSNEventReceiver instance
            mock_upseventreceiver_instance = MockUPSNEventReceiver.return_value
            mock_upseventreceiver_instance.run = MagicMock()

            # Run the main function
            with patch.object(sys, "argv", ["upseventreceiver.py"]):
                with self.assertLogs("upseventreceiver", level="DEBUG") as log:
                    main(loop_forever=False)  # avoid the infinite loop

            # Check that UPSNEventReceiver was initialized with the
            # correct arguments
            MockUPSNEventReceiver.assert_called_once_with(
                ae_title="TEST_AE",
                bind_address="127.0.0.1",
                port=12345,
                logger=logging.getLogger("upseventreceiver"),
                transfer_syntaxes=["ExplicitVRLittleEndian"],
                ups_event_callback=mock_callback,
            )

            # Check that the run method was called
            mock_upseventreceiver_instance.run.assert_called_once()

            # Check the log output
            self.assertIn("Starting up the DICOM UPS Event Receiver (SCU) ...", log.output[0])


if __name__ == "__main__":
    unittest.main()
