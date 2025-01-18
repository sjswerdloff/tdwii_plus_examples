import unittest
from parameterized import parameterized
from tdwii_plus_examples._dicom_uids import (
    validate_sop_classes,
    validate_transfer_syntaxes,
)


class TestValidateSOPClasses(unittest.TestCase):
    EXPECTED_SOP_CLASS_UID = "1.2.840.10008.5.1.4.1.1.2"
    EXPECTED_TRANSFER_SYNTAX_UID = "1.2.840.10008.1.2.1"

    # Define test lists of valid and invalid SOP Classes
    # to be used in the parameterized test cases.
    VALID_UID = "1.2.840.10008.5.1.4.1.1.2"
    VALID_NAME = "CT Image Storage"
    VALID_KEYWORD = "CTImageStorage"
    INVALID_NAME = "CT Storage"

    @parameterized.expand([
        ([VALID_UID], []),
        ([VALID_NAME], []),
        ([VALID_KEYWORD], []),
        ([], [INVALID_NAME]),
        ([], []),
        ([VALID_UID, f"  {VALID_NAME}", VALID_KEYWORD], []),
        ([VALID_UID, f"  {VALID_NAME}"], [VALID_NAME.replace(" ", "", 1)]),
        ([], [INVALID_NAME, ""]),
        ([VALID_UID, VALID_NAME], [INVALID_NAME]),
    ])
    def test_validate_sop_classes(self,
                                  valid_sop_classes,
                                  invalid_sop_classes
                                  ):
        sop_classes = valid_sop_classes + invalid_sop_classes
        valid, invalid = validate_sop_classes(sop_classes)
        valid_expected = {}
        for sop_class in valid_sop_classes:
            valid_expected[sop_class.strip()] = self.EXPECTED_SOP_CLASS_UID
        invalid_expected = {}
        for sop_class in invalid_sop_classes:
            invalid_expected[sop_class] = None
        self.assertEqual(valid, valid_expected)
        self.assertEqual(invalid, invalid_expected)

    @parameterized.expand([
        (["1.2.840.10008.1.2.1"], []),
        (["ExplicitVRLittleEndian"], []),
        (["Explicit VR Little Endian"], []),
        ([], ["Invalid UID"]),
        ([], []),
        (["1.2.840.10008.1.2.1", "  Explicit VR Little Endian",
         "ExplicitVRLittleEndian"], []),
        (["ExplicitVRLittleEndian", "1.2.840.10008.1.2.1"],
         ["Explicit VRLittleEndian"]),
        ([], ["Invalid UID", ""]),
        (["1.2.840.10008.1.2.1", "ExplicitVRLittleEndian"], ["Explicit"]),
    ])
    def test_validate_transfer_syntaxes(self,
                                        valid_transfer_syntaxes,
                                        invalid_transfer_syntaxes
                                        ):
        transfer_syntaxes = (
            valid_transfer_syntaxes + invalid_transfer_syntaxes
        )
        valid, invalid = validate_transfer_syntaxes(
            transfer_syntaxes)
        valid_expected = {}
        for syntax in valid_transfer_syntaxes:
            valid_expected[syntax.strip()] = self.EXPECTED_TRANSFER_SYNTAX_UID
        invalid_expected = {}
        for syntax in invalid_transfer_syntaxes:
            invalid_expected[syntax] = None
        self.assertEqual(valid, valid_expected)
        self.assertEqual(invalid, invalid_expected)


if __name__ == '__main__':
    unittest.main()
