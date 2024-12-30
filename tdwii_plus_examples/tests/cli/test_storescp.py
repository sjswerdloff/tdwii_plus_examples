import unittest
from unittest.mock import patch, MagicMock, Mock
import argparse
import sys
import logging

from tdwii_plus_examples.cli.storescp import main


class TestMainFunction(unittest.TestCase):

    @patch('tdwii_plus_examples.cli.storescp.CStoreSCP')
    @patch('tdwii_plus_examples.cli.storescp.argparse.ArgumentParser.parse_args')
    def test_main(self, mock_parse_args, MockCStoreSCP):
        # Mock the arguments
        mock_parse_args.return_value = argparse.Namespace(
            ae_title='TEST_AE',
            bind_address='127.0.0.1',
            port=12345,
            sop_classes=['SecondaryCaptureImageStorage'],
            transfer_syntaxes=['ImplicitVRLittleEndian'],
            custom_handler='my_handler',
            output_directory='/var/tmp/output',
            verbose=False,
            debug=True
        )

        # Mock the custom handler function
        mock_handler = Mock(name='my_handler')

        # Patch the place where the custom handler is used
        with patch('tdwii_plus_examples.cli.storescp.my_handler', mock_handler):
            # Mock the CStoreSCP instance
            mock_cstorescp_instance = MockCStoreSCP.return_value
            mock_cstorescp_instance.run = MagicMock()

            # Run the main function
            with patch.object(sys, 'argv', ['storescp.py']):
                with self.assertLogs('storescp', level='DEBUG') as log:
                    main(loop_forever=False)  # avoid the infinite loop

            # Check that CStoreSCP was initialized with the correct arguments
            MockCStoreSCP.assert_called_once_with(
                ae_title='TEST_AE',
                bind_address='127.0.0.1',
                port=12345,
                logger=logging.getLogger('storescp'),
                sop_classes=['SecondaryCaptureImageStorage'],
                transfer_syntaxes=['ImplicitVRLittleEndian'],
                custom_handler=mock_handler,  # Ensure this is the mock function
                store_directory='/var/tmp/output'
            )

            # Check that the run method was called
            mock_cstorescp_instance.run.assert_called_once()

            # Check the log output
            self.assertIn(
                'Starting up the DICOM Storage SCP...', log.output[0])


if __name__ == '__main__':
    unittest.main()
