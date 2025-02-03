import argparse
import sys
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

from parameterized import parameterized
from pydicom import Dataset
from pydicom.uid import UID

from tdwii_plus_examples.cli import upswatchscu


class TestUPSWatchSCU(unittest.TestCase):
    @parameterized.expand(
        [
            ("Echo", True, None, False, None, False, False),
            ("Global w/o Lock", False, None, False, None, False, False),
            ("Global w Lock", False, None, True, None, False, False),
            ("Filtered Global w/o Lock", False, None, False, "FX1", False, False),
            ("Filtered Global w Lock", False, None, True, "FX1", False, False),
            ("Single w Lock", False, "1.2.3.4", True, None, False, False),
            ("Single w/o Lock", False, "1.2.3.4", False, None, False, False),
            ("Unsubscribe Global", False, None, False, None, True, False),
            ("Unsubscribe Single", False, "1.2.3.4", False, None, True, False),
            ("Suspend Global", False, None, False, None, False, True),
            ("Failure", False, None, False, None, False, False),
        ]
    )
    @patch("tdwii_plus_examples.cli.upswatchscu.argparse.ArgumentParser.parse_args")
    @patch("tdwii_plus_examples.basescu.BaseSCU", autospec=True)
    @patch("tdwii_plus_examples.upswatchnactionscu.UPSWatchNActionSCU", autospec=True)
    @patch("pynetdicom.AE.associate", return_value=MagicMock())
    def test_main(
        self,
        name,
        echo,
        uid,
        lock,
        machine,
        unsubscribe,
        suspend,
        mock_associate,
        MockUPSWatchNActionSCU,
        MockBaseSCU,
        mock_parse_args,
    ):
        # Mock the command line arguments
        mock_parse_args.return_value = argparse.Namespace(
            ip="127.0.0.1",
            port=104,
            uid=uid,
            ae_title="WATCHSCU",
            called_ae_title="ANYSCP",
            lock=lock,
            machine=machine,
            unsubscribe=unsubscribe,
            suspend=suspend,
            echo=echo,
            verbose=False,
            debug=False,
            quiet=False,
        )

        # Mock the association object and its methods
        mock_association = mock_associate.return_value

        # Fill assoc.accepted_contexts list with Verification and UPS Watch SOP Class
        verification_context = MagicMock()
        verification_context.abstract_syntax = "1.2.840.10008.1.1"  # Verification SOP Class UI
        upswatch_context = MagicMock()
        upswatch_context.abstract_syntax = UID("1.2.840.10008.5.1.4.34.6.2")  # UPS Watch SOP Class UID
        mock_association.accepted_contexts = [verification_context, upswatch_context]

        # Mock the send_c_echo and send_n_action methods to return a valid status response
        status_response = Dataset()
        if name == "Failure":
            status_response.Status = 0x0211  # Unrecognised Operation status code
        else:
            status_response.Status = 0x0000  # Success status code

        action_reply = Dataset()
        action_reply = None
        mock_association.send_c_echo.return_value = status_response
        mock_association.send_n_action.return_value = status_response, action_reply

        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the main function
        upswatchscu.main()

        # Reset redirect.
        sys.stdout = sys.__stdout__
        # print(captured_output.getvalue())

        # Assert the expected print statements
        if name == "Failure":
            self.assertIn("Unrecognised Operation", captured_output.getvalue())
        elif echo:
            self.assertIn("Verification (C-ECHO) successful", captured_output.getvalue())
        elif uid is None:
            if not unsubscribe and not suspend:
                if machine is None:
                    self.assertIn("Global Subscription successful", captured_output.getvalue())
                else:
                    self.assertIn("Filtered Global Subscription successful", captured_output.getvalue())
            else:
                if unsubscribe:
                    self.assertIn("Global Unsubscription successful", captured_output.getvalue())
                else:
                    self.assertIn("Suspend successful", captured_output.getvalue())
        else:
            if not unsubscribe:
                self.assertIn("Single UPS Subscription successful", captured_output.getvalue())
            else:
                self.assertIn("Single UPS Unsubscription successful", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()
