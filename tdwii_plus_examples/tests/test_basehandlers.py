import ssl
import unittest
from unittest.mock import MagicMock, call, patch

from tdwii_plus_examples.basehandlers import describe_tls_session, handle_close, handle_open


def make_tls_event(client_certificate=None, cipher=("TLS_AES_256_GCM_SHA384", "TLSv1.3", 256)):
    """Create a mock connection event whose socket is a TLS socket."""
    tls_socket = MagicMock(spec=ssl.SSLSocket)
    tls_socket.version.return_value = "TLSv1.3"
    tls_socket.cipher.return_value = cipher
    tls_socket.getpeercert.return_value = client_certificate

    event = MagicMock()
    event.assoc.requestor.address = "127.0.0.1"
    event.assoc.requestor.port = 104
    event.assoc.dul.socket.socket = tls_socket
    return event


class TestHandleConnectionsEvents(unittest.TestCase):
    @patch("logging.Logger")
    def test_handle_open(self, MockLogger):
        # Create a mock event
        mock_event = MagicMock()
        mock_event.assoc.requestor.address = "127.0.0.1"
        mock_event.assoc.requestor.port = 104

        # Create a mock logger
        mock_logger = MockLogger()

        # Call the function
        status = handle_open(mock_event, mock_logger)

        # Check the status
        self.assertEqual(status, 0x0000)

        # Check that the logger was called with the correct message
        mock_logger.info.assert_called_once_with("Successful connection from 127.0.0.1:104")

    @patch("logging.Logger")
    def test_handle_close(self, MockLogger):
        # Create a mock event
        mock_event = MagicMock()
        mock_event.assoc.requestor.ae_title = "TEST_AET"
        mock_event.assoc.requestor.address = "127.0.0.1"
        mock_event.assoc.requestor.port = 104

        # Create a mock logger
        mock_logger = MockLogger()

        # Call the function
        status = handle_close(mock_event, mock_logger)

        # Check the status
        self.assertEqual(status, 0x0000)

        # Check that the logger was called with the correct message
        mock_logger.info.assert_called_once_with("Closed connection with TEST_AET@127.0.0.1:104")

    def test_handle_open_logs_tls_session(self):
        mock_logger = MagicMock()

        status = handle_open(make_tls_event(), mock_logger)

        self.assertEqual(status, 0x0000)
        self.assertEqual(
            mock_logger.info.call_args_list,
            [
                call("Successful connection from 127.0.0.1:104"),
                call("TLS session with 127.0.0.1:104: TLSv1.3, TLS_AES_256_GCM_SHA384"),
            ],
        )

    def test_handle_open_logs_client_certificate_subject_of_tls_session(self):
        mock_logger = MagicMock()
        client_certificate = {"subject": ((("commonName", "client"),),)}

        handle_open(make_tls_event(client_certificate), mock_logger)

        mock_logger.info.assert_called_with(
            "TLS session with 127.0.0.1:104: TLSv1.3, TLS_AES_256_GCM_SHA384, client certificate subject: commonName=client"
        )


class TestDescribeTlsSession(unittest.TestCase):
    def test_connection_without_tls_is_not_described(self):
        self.assertIsNone(describe_tls_session(MagicMock()))

    def test_event_without_socket_is_not_described(self):
        event = MagicMock()
        event.assoc.dul = None

        self.assertIsNone(describe_tls_session(event))

    def test_tls_session_without_client_certificate(self):
        self.assertEqual(describe_tls_session(make_tls_event()), "TLSv1.3, TLS_AES_256_GCM_SHA384")

    def test_tls_session_with_client_certificate_subject(self):
        client_certificate = {"subject": ((("countryName", "FR"),), (("commonName", "client"),))}

        description = describe_tls_session(make_tls_event(client_certificate))

        self.assertEqual(
            description, "TLSv1.3, TLS_AES_256_GCM_SHA384, client certificate subject: countryName=FR, commonName=client"
        )

    def test_tls_session_without_cipher(self):
        self.assertEqual(describe_tls_session(make_tls_event(cipher=None)), "TLSv1.3, unknown cipher")

    def test_client_certificate_subject_cannot_forge_log_records(self):
        # A subject chosen by a client to forge a log record: a carriage return and a line feed, then text imitating
        # a connection record, ended with a Unicode line separator
        hostile_value = "client\r\nSuccessful connection from 6.6.6.6:104\u2028"
        client_certificate = {"subject": ((("commonName", hostile_value),),)}

        description = describe_tls_session(make_tls_event(client_certificate))

        # The description stays on a single line: the carriage return, the line feed and the line separator are
        # replaced by their visible escape sequences, and the imitated record remains inside the subject text
        self.assertTrue(description.isprintable())
        self.assertIn(r"commonName=client\r\nSuccessful connection from 6.6.6.6:104\u2028", description)

    def test_client_certificate_subject_keeps_printable_characters(self):
        # A subject with a printable non-ASCII character, as found in the names of organizations
        client_certificate = {"subject": ((("organizationName", "Hôpital Pitié Salpêtrière"),),)}

        description = describe_tls_session(make_tls_event(client_certificate))

        # Printable characters are logged as they are: only the non-printable ones are escaped
        self.assertIn("organizationName=Hôpital Pitié Salpêtrière", description)


if __name__ == "__main__":
    unittest.main()
