import unittest
from unittest.mock import MagicMock, patch
from tdwii_plus_examples.cechohandler import handle_cecho


class TestHandleCEchoEvent(unittest.TestCase):
    @patch('logging.Logger')
    def test_handle_cecho(self, MockLogger):
        # Create a mock event
        mock_event = MagicMock()
        mock_event.assoc.requestor.ae_title = 'TEST_AET'
        mock_event.assoc.requestor.address = '127.0.0.1'
        mock_event.assoc.requestor.port = 104
        mock_event.timestamp.strftime.return_value = '2024-12-28 11:00:00'

        # Create a mock logger
        mock_logger = MockLogger()

        # Call the function
        status = handle_cecho(mock_event, mock_logger)

        # Check the status
        self.assertEqual(status, 0x0000)

        # Check that the logger was called with the correct message
        mock_logger.info.assert_called_once_with(
            'Received C-ECHO request from TEST_AET@127.0.0.1:104 at '
            '2024-12-28 11:00:00'
        )


if __name__ == '__main__':
    unittest.main()
