import logging
import unittest
from unittest.mock import Mock
from logging.handlers import MemoryHandler
from parameterized import parameterized
from pydicom import uid
from pynetdicom import UID, DEFAULT_TRANSFER_SYNTAXES
from pynetdicom.sop_class import Verification
from tdwii_plus_examples.upsneventreceiver import UPSNEventReceiver
from tdwii_plus_examples.upsneventhandler import nevent_callback
from tdwii_plus_examples._dicom_uids import (
    validate_transfer_syntaxes, UPS_SOP_CLASSES
)

# Define test lists of valid and invalid Transfer syntaxes to be used in the parameterized test cases.
XFER_SYNTAXES = [
    "ExplicitVRLittleEndian",  # valid transfer syntax Keyword
    "1.2.840.10008.1.2.2",     # valid transfer syntax UID
    "ImplicitLittleEndian",    # invalid transfer syntax Keyword
    "1.2.840.10008.5.2.1",     # invalid transfer syntax UID
]


class TestUPSNEventReceiver(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the logger for this test case to DEBUG level
        # with a stream handler to print the log messages to the console
        cls.test_logger = logging.getLogger('test_neventreceiver')
        cls.test_logger.setLevel(logging.INFO)
        cls.stream_handler = logging.StreamHandler()
        cls.test_logger.addHandler(cls.stream_handler)

        # Get the valid and invalid items of the test lists
        cls.valid_xfer_syntaxes, cls.invalid_xfer_syntaxes = \
            validate_transfer_syntaxes(XFER_SYNTAXES)

        # Get the list of default transfer syntaxes
        cls.default_transfer_syntaxes = DEFAULT_TRANSFER_SYNTAXES.copy()
        # Make ExplicitVRLittleEndian the preferred transfer syntax
        cls.default_transfer_syntaxes.remove(UID(uid.ExplicitVRLittleEndian))
        cls.default_transfer_syntaxes = [UID(uid.ExplicitVRLittleEndian)] + \
            cls.default_transfer_syntaxes
        cls.test_logger.debug(f"Default Transfer Syntaxes: "
                              f"{cls.default_transfer_syntaxes}")

    def setUp(self):
        # Set up the logger for the BaseSCP to DEBUG level
        # with a memory handler to store up to 100 log messages
        self.rcv_logger = logging.getLogger('neventreceiver')
        self.rcv_logger.setLevel(logging.INFO)
        self.memory_handler = MemoryHandler(100)
        self.rcv_logger.addHandler(self.memory_handler)

    def tearDown(self):
        self.rcv_logger.removeHandler(self.memory_handler)
        self.memory_handler.close()

    # Parameterized unit tests for the constructor parameters

    # Define test cases parameters
    @parameterized.expand([
        (XFER_SYNTAXES, None),
        (None, "custom_callback"),
        (None, ""),
    ])
    def test_init_params(self,
                         transfer_syntaxes,
                         ups_event_callback):
        # Custom callback should be a function defined in the global namespace
        # at the module level, so we use globals() to look it up.
        # This allows passing a function name as a string argument.
        if ups_event_callback:
            callback = Mock()
            self.test_logger.debug(f"Custom callback: {callback}")
        else:
            callback = None
        receiver = UPSNEventReceiver(
            logger=self.rcv_logger,
            transfer_syntaxes=transfer_syntaxes,
            ups_event_callback=callback,
        )
        self.memory_handler.flush()
        log_output = [record.getMessage()
                      for record in self.memory_handler.buffer]
        # Print the log messages
        self.test_logger.debug(f"{log_output}")

        if transfer_syntaxes:
            # get the valid Transfer Syntax UIDs passed to the constructor
            valid_xfer_stx_uids = list(
                self.valid_xfer_syntaxes.copy().values()
            )
            # add ImplicitVRLittleEndian to the list of valid Transfer Syntax
            # UIDs if it is not already present
            if uid.ImplicitVRLittleEndian not in valid_xfer_stx_uids:
                valid_xfer_stx_uids.append(uid.ImplicitVRLittleEndian)
            self.test_logger.debug(f"Expected Transfer Syntax UIDs: "
                                   f"{valid_xfer_stx_uids}")

            # get the list of Transfer Syntax UIDs supported by the AE
            ae_supported_xfer_stx_uids = [
                context.transfer_syntax
                for context in receiver.ae.supported_contexts
            ]

        # Check AE supports the UPSEventSOP and expected transfer syntaxes
        for context in receiver.ae.supported_contexts:
            if context.abstract_syntax != Verification:
                self.test_logger.debug(f"Supported Abstract Syntax UIDs: "
                                       f"{context.abstract_syntax}")
                self.assertEqual(
                    context.abstract_syntax,
                    UPS_SOP_CLASSES["UnifiedProcedureStepEvent"]
                )
            if not transfer_syntaxes:
                # Check default transfer syntaxes are supported
                if context.abstract_syntax == Verification:
                    pass  # skip as provided by parent class
                else:
                    self.test_logger.debug(f"Supported Transfer Syntax UIDs: "
                                           f"{context.transfer_syntax}")
                    self.assertCountEqual(
                        context.transfer_syntax,
                        self.default_transfer_syntaxes,
                        msg=f"Supported transfer syntaxes for "
                        f"{context.abstract_syntax} "
                        f"do not match the pynetdicom defaults "
                        f"({self.default_transfer_syntaxes})")
            else:
                # Check specified transfer syntaxes are supported
                if context.abstract_syntax == Verification:
                    pass  # skip as provided by parent class
                else:
                    self.test_logger.debug(f"Supported Transfer Syntax UIDs: "
                                           f"{context.transfer_syntax}")
                    self.assertCountEqual(
                        context.transfer_syntax, valid_xfer_stx_uids,
                        msg=f"Supported transfer syntaxes for "
                        f"{context.abstract_syntax} "
                        f"do not match the specified transfer syntaxes"
                        f"({valid_xfer_stx_uids})")

        if ups_event_callback:
            self.test_logger.debug("Asserting custom callback is set")
            self.assertEqual(receiver.ups_event_callback, callback)
        else:
            self.test_logger.debug("Asserting default callback is set")
            self.assertEqual(receiver.ups_event_callback, nevent_callback)
