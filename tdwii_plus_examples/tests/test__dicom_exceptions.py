import unittest

from pydicom.uid import UID

from tdwii_plus_examples._dicom_exceptions import (
    AssociationError,
    ContextWarning,
    ResponseCancel,
    ResponseError,
    ResponsePending,
    ResponseUnknown,
    ResponseWarning,
)


class TestDicomExceptions(unittest.TestCase):
    def test_association_error(self):
        with self.assertRaises(AssociationError):
            raise AssociationError("Association failed")

    def test_context_warning(self):
        accepted_sop_classes = [UID("1.2.840.10008.1.1")]
        refused_sop_classes = [UID("1.2.840.10008.5.1.4.34.6.2")]
        message = "SOP classes not accepted"
        exception = ContextWarning(message, accepted_sop_classes, refused_sop_classes)
        self.assertIn("SOP classes not accepted: [Unified Procedure Step - Watch SOP Class]", str(exception))
        self.assertEqual(exception.accepted_sop_classes, accepted_sop_classes)
        self.assertEqual(exception.refused_sop_classes, refused_sop_classes)

    def test_response_error(self):
        status_code = 0xA700
        message = "Refused: Out of resources"
        exception = ResponseError(status_code, message)
        self.assertEqual(str(exception), "Refused: Out of resources (Status Code: 0xA700)")
        self.assertEqual(exception.status_code, status_code)
        self.assertEqual(exception.message, message)

    def test_response_warning(self):
        status_code = 0xB000
        message = "Sub-operations completed, one or more failures"
        exception = ResponseWarning(status_code, message)
        self.assertEqual(str(exception), "Sub-operations completed, one or more failures (Status Code: 0xB000)")
        self.assertEqual(exception.status_code, status_code)
        self.assertEqual(exception.message, message)

    def test_response_cancel(self):
        status_code = 0xFE00
        message = "Operation canceled"
        exception = ResponseCancel(status_code, message)
        self.assertEqual(str(exception), "Operation canceled (Status Code: 0xFE00)")
        self.assertEqual(exception.status_code, status_code)
        self.assertEqual(exception.message, message)

    def test_response_pending(self):
        status_code = 0xFF00
        message = "Sub-operations are continuing"
        exception = ResponsePending(status_code, message)
        self.assertEqual(str(exception), "Sub-operations are continuing (Status Code: 0xFF00)")
        self.assertEqual(exception.status_code, status_code)
        self.assertEqual(exception.message, message)

    def test_response_unknown(self):
        status_code = 0xFFFF
        message = "Unknown status code"
        exception = ResponseUnknown(status_code, message)
        self.assertEqual(str(exception), "Unknown status code (Status Code: 0xFFFF)")
        self.assertEqual(exception.status_code, status_code)
        self.assertEqual(exception.message, message)


if __name__ == "__main__":
    unittest.main()
