import logging
import re
import unittest
from unittest.mock import Mock
from logging.handlers import MemoryHandler
from parameterized import parameterized
from pydicom import uid
from pynetdicom import UID, DEFAULT_TRANSFER_SYNTAXES
from pynetdicom.sop_class import Verification
from tdwii_plus_examples.cstorescp import CStoreSCP

# Define dictionaries of valid and invalid SOP Classes and Transfer syntaxes
SOP_CLASSES = {
    "CTImageStorage": True,                 # valid Storage SOP Class Keyword
    "MRStorage": False,                     # invalid Storage SOP Class Keyword
    "RTIonPlanStorage": True,               # valid Storage SOP Class Keyword
    "1.2.840.10008.5.1.4.1.1.481.9": True,  # valid Storage SOP Class UID
    "1.2.840.10008.1.2": False,             # invalid Storage SOP Class UID
    "Verification": False                   # invalid Storage SOP Class UID
}

XFER_SYNTAXES = {
    "ExplicitVRLittleEndian": True,  # valid transfer syntax Keyword
    "1.2.840.10008.1.2.2": True,     # valid transfer syntax UID
    "ImplicitLittleEndian": False,   # invalid transfer syntax Keyword
    "1.2.840.10008.5.2.1": False,     # invalid transfer syntax UID
}


class TestCStoreSCP(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the logger for this test case to DEBUG level
        # with a stream handler to print the log messages to the console
        cls.test_logger = logging.getLogger('test_cstorescp')
        cls.test_logger.setLevel(logging.INFO)
        cls.stream_handler = logging.StreamHandler()
        cls.test_logger.addHandler(cls.stream_handler)

        # Create lists of valid and invalid values from the dictionaries
        cls.valid_sop_classes = [
            sop for sop, is_valid in SOP_CLASSES.items() if is_valid]
        cls.invalid_sop_classes = [
            sop for sop, is_valid in SOP_CLASSES.items() if not is_valid]

        cls.valid_xfer_syntaxes = [
            xfer for xfer, is_valid in XFER_SYNTAXES.items() if is_valid]
        cls.invalid_xfer_syntaxes = [
            xfer for xfer, is_valid in XFER_SYNTAXES.items() if not is_valid]
        
        # Create the list of default transfer syntaxes
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
        self.scp_logger = logging.getLogger('cstorescp')
        self.scp_logger.setLevel(logging.INFO)
        self.memory_handler = MemoryHandler(100)
        self.scp_logger.addHandler(self.memory_handler)

    def tearDown(self):
        self.scp_logger.removeHandler(self.memory_handler)
        self.memory_handler.close()

    # Parameterized unit tests for the constructor parameters

    # Define test cases parameters

    @parameterized.expand([
        (list(SOP_CLASSES.keys()), None, None, None),
        (None, list(XFER_SYNTAXES.keys()), None, None),
        (list(SOP_CLASSES.keys()), list(XFER_SYNTAXES.keys()), None, None),
        (None, None, "custom_handler", None),
        (None, None, "", None),
        (None, None, None, "/path/to/store"),
    ])
    def test_init_params(self,
                         sop_classes,
                         transfer_syntaxes,
                         custom_handler,
                         store_directory):
        # Custom handler should be a function defined in the global namespace
        # at the module level, so we use globals() to look it up.
        # This allows passing a function name as a string argument.
        if custom_handler:
            handler = Mock()
            self.test_logger.debug(f"Custom handler: {handler}")
        else:
            handler = None
        self.test_logger.debug(f"transfer_syntaxes: {transfer_syntaxes}")
        scp = CStoreSCP(
            logger=self.scp_logger,
            sop_classes=sop_classes,
            transfer_syntaxes=transfer_syntaxes,
            custom_handler=handler,
            store_directory=store_directory
        )

        self.memory_handler.flush()
        log_output = [record.getMessage()
                      for record in self.memory_handler.buffer]
        # Print the log messages
        self.test_logger.debug(f"{log_output}")

        if transfer_syntaxes:
            # get the valid Transfer Syntax UIDs passed to the constructor
            valid_xfer_stx_uids = []
            for xfer_stx in self.valid_xfer_syntaxes:
                if not re.match(uid.RE_VALID_UID, xfer_stx):
                    valid_xfer_stx_uids.append(getattr(uid, xfer_stx))
                else:
                    valid_xfer_stx_uids.append(xfer_stx)
            # add DICOM default Transfer Syntax if not present
            if uid.ImplicitVRLittleEndian not in valid_xfer_stx_uids:
                valid_xfer_stx_uids.append(uid.ImplicitVRLittleEndian)
            self.test_logger.debug(f"Transfer Syntax UIDs: "
                                   f"{valid_xfer_stx_uids}")

        if sop_classes:
            # get the valid SOP Class UIDs passed to the constructor
            valid_sop_classes_uids = []
            for sop_class in self.valid_sop_classes:
                if not re.match(uid.RE_VALID_UID, sop_class):
                    valid_sop_classes_uids.append(getattr(uid, sop_class))
                else:
                    valid_sop_classes_uids.append(sop_class)

            # get the list of Storage SOP Classes UIDs supported by the AE
            ae_supported_sop_classes_uids = [
                context.abstract_syntax
                for context in scp.ae.supported_contexts
                if context.abstract_syntax.keyword != 'Verification'
            ]

            # The set of SOP Classes supported by the AE should be the same
            # as the set of valid SOP Classes passed to the constructor.
            # We use assertCountEqual to check that the same elements are
            # present in both lists, regardless of order.
            self.assertCountEqual(
                ae_supported_sop_classes_uids, valid_sop_classes_uids,
                msg=f"Supported SOP Classes in AE "
                    f"({ae_supported_sop_classes_uids}) "
                    f"do not match valid SOP Classes passed to constructor "
                    f"({valid_sop_classes_uids})")

            # Check transfer syntaxes
            for context in scp.ae.supported_contexts:
                if not transfer_syntaxes:
                    # Check default transfer syntaxes are supported
                    if context.abstract_syntax == Verification:
                        pass  # skip as provided by parent class
                    else:
                        self.assertCountEqual(
                            context.transfer_syntax,
                            self.default_transfer_syntaxes,
                            msg=f"Supported transfer syntaxes for "
                            f"{context.abstract_syntax} "
                            f"do not match the pynetdicom defaults "
                            f"({self.default_transfer_syntaxes})")
                else:
                    # Check specified transfer syntaxes are supported
                    if context.abstract_syntax == '1.2.840.10008.1.1':
                        pass  # skip as provided by parent class
                    else:
                        self.assertCountEqual(
                            context.transfer_syntax, valid_xfer_stx_uids,
                            msg=f"Supported transfer syntaxes for "
                            f"{context.abstract_syntax} "
                            f"do not match the specified transfer syntaxes"
                            f"({valid_xfer_stx_uids})")

        elif transfer_syntaxes:
            # Check transfer syntaxes passed to the constructor are supported
            # by pynetdicom default SOP Classes
            for context in scp.ae.supported_contexts:
                # Check default transfer syntaxes are supported
                if context.abstract_syntax == '1.2.840.10008.1.1':
                    pass  # skip as provided by parent class
                else:
                    self.assertCountEqual(
                        context.transfer_syntax, valid_xfer_stx_uids,
                        msg=f"Supported transfer syntaxes for "
                        f"{context.abstract_syntax} "
                        f"do not match the specified transfer syntaxes"
                        f"({valid_xfer_stx_uids})")
        elif custom_handler:
            self.assertEqual(scp.handle_store, handler)
        elif store_directory:
            self.assertEqual(scp.store_directory, store_directory)

