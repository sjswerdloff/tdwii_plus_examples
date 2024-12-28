import unittest
from unittest.mock import MagicMock, patch
from tdwii_plus_examples.basehandlers import handle_open, handle_close


class TestHandleConnectionsEvents(unittest.TestCase):
    @patch('logging.Logger')
    def test_handle_open(self, MockLogger):
        # Create a mock event
        mock_event = MagicMock()
        mock_event.assoc.requestor.address = '127.0.0.1'
        mock_event.assoc.requestor.port = 104

        # Create a mock logger
        mock_logger = MockLogger()

        # Call the function
        status = handle_open(mock_event, mock_logger)

        # Check the status
        self.assertEqual(status, 0x0000)

        # Check that the logger was called with the correct message
        mock_logger.info.assert_called_once_with(
            'Succesful connection from 127.0.0.1:104'
        )

    @patch('logging.Logger')
    def test_handle_close(self, MockLogger):
        # Create a mock event
        mock_event = MagicMock()
        mock_event.assoc.requestor.ae_title = 'TEST_AET'
        mock_event.assoc.requestor.address = '127.0.0.1'
        mock_event.assoc.requestor.port = 104

        # Create a mock logger
        mock_logger = MockLogger()

        # Call the function
        status = handle_close(mock_event, mock_logger)

        # Check the status
        self.assertEqual(status, 0x0000)

        # Check that the logger was called with the correct message
        mock_logger.info.assert_called_once_with(
            'Closed connection with TEST_AET@127.0.0.1:104'
        )


if __name__ == '__main__':
    unittest.main()
