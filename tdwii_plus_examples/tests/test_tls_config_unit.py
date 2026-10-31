import ssl
import unittest
from unittest.mock import patch

from tdwii_plus_examples.tls_config import TLSConfig


class TestTLSConfig(unittest.TestCase):
    def test_require_mtls_without_ca_cert_raises(self):
        with self.assertRaisesRegex(ValueError, "require_mtls=True needs ca_cert"):
            TLSConfig(cert_file="cert.pem", key_file="key.pem", require_mtls=True)

    def test_require_mtls_with_ca_cert_is_accepted(self):
        tls_config = TLSConfig(cert_file="cert.pem", key_file="key.pem", ca_cert="ca.pem", require_mtls=True)
        self.assertTrue(tls_config.require_mtls)
        self.assertEqual(tls_config.ca_cert, "ca.pem")

    def test_default_config_without_ca_cert_is_accepted(self):
        tls_config = TLSConfig(cert_file="cert.pem", key_file="key.pem")
        self.assertFalse(tls_config.require_mtls)
        self.assertIsNone(tls_config.ca_cert)

    @patch("tdwii_plus_examples.tls_config.ssl.SSLContext")
    def test_create_ssl_context_loads_server_certificate_only(self, mock_ssl_context_class):
        mock_context = mock_ssl_context_class.return_value
        mock_context.verify_mode = ssl.CERT_NONE

        tls_config = TLSConfig(cert_file="cert.pem", key_file="key.pem")

        context = tls_config.create_ssl_context()

        mock_ssl_context_class.assert_called_once_with(ssl.PROTOCOL_TLS_SERVER)
        mock_context.load_cert_chain.assert_called_once_with(certfile="cert.pem", keyfile="key.pem")
        mock_context.load_verify_locations.assert_not_called()
        self.assertEqual(context.verify_mode, ssl.CERT_NONE)

    @patch("tdwii_plus_examples.tls_config.ssl.SSLContext")
    def test_create_ssl_context_loads_ca_without_requiring_client_certificate(self, mock_ssl_context_class):
        mock_context = mock_ssl_context_class.return_value
        mock_context.verify_mode = ssl.CERT_NONE

        tls_config = TLSConfig(cert_file="cert.pem", key_file="key.pem", ca_cert="ca.pem")

        context = tls_config.create_ssl_context()

        mock_context.load_verify_locations.assert_called_once_with(cafile="ca.pem")
        self.assertEqual(context.verify_mode, ssl.CERT_NONE)

    @patch("tdwii_plus_examples.tls_config.ssl.SSLContext")
    def test_create_ssl_context_requires_client_certificate_for_mtls(self, mock_ssl_context_class):
        mock_context = mock_ssl_context_class.return_value

        tls_config = TLSConfig(cert_file="cert.pem", key_file="key.pem", ca_cert="ca.pem", require_mtls=True)

        context = tls_config.create_ssl_context()

        mock_context.load_verify_locations.assert_called_once_with(cafile="ca.pem")
        self.assertEqual(context.verify_mode, ssl.CERT_REQUIRED)


if __name__ == "__main__":
    unittest.main()
