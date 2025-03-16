import logging
import unittest
from logging.handlers import MemoryHandler
from unittest.mock import Mock

from parameterized import parameterized
from pydicom import uid
from pynetdicom import DEFAULT_TRANSFER_SYNTAXES, UID
from pynetdicom.sop_class import Verification

from tdwii_plus_examples._dicom_uids import validate_sop_classes, validate_transfer_syntaxes
from tdwii_plus_examples.cstorescp import CStoreSCP

# Define test lists of valid and invalid SOP Classes and Transfer syntaxes
# to be used in the parameterized test cases.
SOP_CLASSES = [
    "CTImageStorage",  # valid Storage SOP Class Keyword
    "MRStorage",  # invalid Storage SOP Class Keyword
    "RTIonPlanStorage",  # valid Storage SOP Class Keyword
    "1.2.840.10008.5.1.4.1.1.481.9",  # valid Storage SOP Class UID
    "1.2.840.10008.1.2",  # invalid Storage SOP Class UID
    "Verification",  # invalid Storage SOP Class UID
]

XFER_SYNTAXES = [
    "ExplicitVRLittleEndian",  # valid transfer syntax Keyword
    "1.2.840.10008.1.2.2",  # valid transfer syntax UID
    "ImplicitLittleEndian",  # invalid transfer syntax Keyword
    "1.2.840.10008.5.2.1",  # invalid transfer syntax UID
]


class TestCStoreSCP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the logger for this test case to DEBUG level
        # with a stream handler to print the log messages to the console
        cls.test_logger = logging.getLogger("test_cstorescp")
        cls.test_logger.setLevel(logging.INFO)
        cls.stream_handler = logging.StreamHandler()
        cls.test_logger.addHandler(cls.stream_handler)

        # Get the valid and invalid items of the test lists
        cls.valid_sop_classes, cls.invalid_sop_classes = validate_sop_classes(SOP_CLASSES)

        cls.valid_xfer_syntaxes, cls.invalid_xfer_syntaxes = validate_transfer_syntaxes(XFER_SYNTAXES)

        # Get the list of default transfer syntaxes
        cls.default_transfer_syntaxes = DEFAULT_TRANSFER_SYNTAXES.copy()
        # Make ExplicitVRLittleEndian the preferred transfer syntax
        cls.default_transfer_syntaxes.remove(UID(uid.ExplicitVRLittleEndian))
        cls.default_transfer_syntaxes = [UID(uid.ExplicitVRLittleEndian)] + cls.default_transfer_syntaxes
        cls.test_logger.debug(f"Default Transfer Syntaxes: {cls.default_transfer_syntaxes}")

    def setUp(self):
        # Set up the logger for the BaseSCP to DEBUG level
        # with a memory handler to store up to 100 log messages
        self.scp_logger = logging.getLogger("cstorescp")
        self.scp_logger.setLevel(logging.INFO)
        self.memory_handler = MemoryHandler(100)
        self.scp_logger.addHandler(self.memory_handler)

    def tearDown(self):
        self.scp_logger.removeHandler(self.memory_handler)
        self.memory_handler.close()

    # Parameterized unit tests for the constructor parameters

    # Define test cases parameters
    @parameterized.expand(
        [
            (SOP_CLASSES, None, None, None),
            (None, XFER_SYNTAXES, None, None),
            (SOP_CLASSES, XFER_SYNTAXES, None, None),
            (None, None, "custom_handler", None),
            (None, None, "", None),
            (None, None, None, "/path/to/store"),
        ]
    )
    def test_init_params(self, sop_classes, transfer_syntaxes, custom_handler, store_directory):
        # Custom handler should be a function defined in the global namespace
        # at the module level, so we use globals() to look it up.
        # This allows passing a function name as a string argument.
        if custom_handler:
            handler = Mock()
            self.test_logger.debug(f"Custom handler: {handler}")
        else:
            handler = None
        scp = CStoreSCP(
            logger=self.scp_logger,
            sop_classes=sop_classes,
            transfer_syntaxes=transfer_syntaxes,
            custom_handler=handler,
            store_directory=store_directory,
        )
        self.memory_handler.flush()
        log_output = [record.getMessage() for record in self.memory_handler.buffer]
        # Print the log messages
        self.test_logger.debug(f"{log_output}")

        if transfer_syntaxes:
            # get the valid Transfer Syntax UIDs passed to the constructor
            valid_xfer_stx_uids = list(self.valid_xfer_syntaxes.copy().values())
            # add ImplicitVRLittleEndian to the list of valid Transfer Syntax
            # UIDs if it is not already present
            if uid.ImplicitVRLittleEndian not in valid_xfer_stx_uids:
                valid_xfer_stx_uids.append(uid.ImplicitVRLittleEndian)
            self.test_logger.debug(f"Expected Transfer Syntax UIDs: {valid_xfer_stx_uids}")

            # get the list of Transfer Syntax UIDs supported by the AE
            ae_supported_xfer_stx_uids = [
                context.transfer_syntax for context in scp.ae.supported_contexts if context.abstract_syntax != Verification
            ]
            self.test_logger.debug(f"Supported Transfer Syntax UIDs: {ae_supported_xfer_stx_uids[0]}")

        if sop_classes:
            # get the valid SOP Class UIDs passed to the constructor
            valid_sop_classes_uids = list(self.valid_sop_classes.copy().values())

            # get the list of Storage SOP Classes UIDs supported by the AE
            ae_supported_sop_classes_uids = [
                context.abstract_syntax
                for context in scp.ae.supported_contexts
                if context.abstract_syntax.keyword != "Verification"
            ]

            # The set of SOP Classes supported by the AE should be the same
            # as the set of valid SOP Classes passed to the constructor.
            # We use assertCountEqual to check that the same elements are
            # present in both lists, regardless of order.
            self.assertCountEqual(
                ae_supported_sop_classes_uids,
                valid_sop_classes_uids,
                msg=f"Supported SOP Classes in AE "
                f"({ae_supported_sop_classes_uids}) "
                f"do not match valid SOP Classes passed to constructor "
                f"({valid_sop_classes_uids})",
            )

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
                            f"({self.default_transfer_syntaxes})",
                        )
                else:
                    # Check specified transfer syntaxes are supported
                    if context.abstract_syntax == "1.2.840.10008.1.1":
                        pass  # skip as provided by parent class
                    else:
                        self.assertCountEqual(
                            context.transfer_syntax,
                            valid_xfer_stx_uids,
                            msg=f"Supported transfer syntaxes for "
                            f"{context.abstract_syntax} "
                            f"do not match the specified transfer syntaxes"
                            f"({valid_xfer_stx_uids})",
                        )

        elif transfer_syntaxes:
            # Check transfer syntaxes passed to the constructor are supported
            # by pynetdicom default SOP Classes
            for context in scp.ae.supported_contexts:
                # Check default transfer syntaxes are supported
                if context.abstract_syntax == "1.2.840.10008.1.1":
                    pass  # skip as provided by parent class
                else:
                    self.assertCountEqual(
                        context.transfer_syntax,
                        valid_xfer_stx_uids,
                        msg=f"Supported transfer syntaxes for "
                        f"{context.abstract_syntax} "
                        f"do not match the specified transfer syntaxes"
                        f"({valid_xfer_stx_uids})",
                    )
        elif custom_handler:
            self.assertEqual(scp.handle_store, handler)
        elif store_directory:
            self.assertEqual(scp.store_directory, store_directory)
