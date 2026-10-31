import ssl
import unittest
from unittest.mock import patch

from tdwii_plus_examples.tls_config import TLSConfig, TLSUsage


class TestTLSConfigValidation(unittest.TestCase):
    def test_default_usage_is_server_auth(self):
        tls_config = TLSConfig(cert_file="cert.pem", key_file="key.pem")
        self.assertEqual(tls_config.usage, TLSUsage.SERVER_AUTH)

    def test_usage_that_is_empty_or_not_a_tls_usage_raises(self):
        for usage in (TLSUsage(0), None, "serverAuth", ["serverAuth"]):
            with self.subTest(usage=usage):
                with self.assertRaisesRegex(ValueError, "usage must include serverAuth, clientAuth or both, got"):
                    TLSConfig(cert_file="cert.pem", key_file="key.pem", usage=usage)

    def test_server_auth_without_certificate_and_key_raises(self):
        with self.assertRaisesRegex(ValueError, "serverAuth usage needs cert_file and key_file"):
            TLSConfig()

    def test_server_auth_with_key_but_without_certificate_raises(self):
        with self.assertRaisesRegex(ValueError, "key_file needs cert_file"):
            TLSConfig(key_file="key.pem")

    def test_server_auth_with_certificate_but_without_key_raises(self):
        with self.assertRaisesRegex(ValueError, "cert_file needs key_file"):
            TLSConfig(cert_file="cert.pem")

    def test_certificate_without_key_raises(self):
        with self.assertRaisesRegex(ValueError, "cert_file needs key_file"):
            TLSConfig(cert_file="cert.pem", usage=TLSUsage.CLIENT_AUTH)

    def test_key_without_certificate_raises(self):
        with self.assertRaisesRegex(ValueError, "key_file needs cert_file"):
            TLSConfig(key_file="key.pem", usage=TLSUsage.CLIENT_AUTH)

    def test_client_auth_without_files_is_accepted(self):
        tls_config = TLSConfig(usage=TLSUsage.CLIENT_AUTH)
        self.assertIsNone(tls_config.cert_file)
        self.assertIsNone(tls_config.ca_cert)

    def test_client_auth_with_ca_only_is_accepted(self):
        tls_config = TLSConfig(ca_cert="ca.pem", usage=TLSUsage.CLIENT_AUTH)
        self.assertEqual(tls_config.ca_cert, "ca.pem")

    def test_client_auth_with_identity_is_accepted(self):
        tls_config = TLSConfig(cert_file="cert.pem", key_file="key.pem", usage=TLSUsage.CLIENT_AUTH)
        self.assertEqual(tls_config.cert_file, "cert.pem")

    def test_client_auth_with_mtls_needs_certificate_and_key(self):
        with self.assertRaisesRegex(ValueError, "require_mtls=True needs cert_file and key_file"):
            TLSConfig(ca_cert="ca.pem", require_mtls=True, usage=TLSUsage.CLIENT_AUTH)

    def test_client_auth_with_mtls_and_all_files_is_accepted(self):
        tls_config = TLSConfig(
            cert_file="cert.pem", key_file="key.pem", ca_cert="ca.pem", require_mtls=True, usage=TLSUsage.CLIENT_AUTH
        )
        self.assertTrue(tls_config.require_mtls)

    def test_both_usages_need_certificate_and_key(self):
        with self.assertRaisesRegex(ValueError, "serverAuth usage needs cert_file and key_file"):
            TLSConfig(usage=TLSUsage.SERVER_AUTH | TLSUsage.CLIENT_AUTH)

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


class TestTLSConfigServerContext(unittest.TestCase):
    def test_server_ssl_context_needs_server_auth(self):
        tls_config = TLSConfig(usage=TLSUsage.CLIENT_AUTH)
        with self.assertRaisesRegex(ValueError, "serverAuth"):
            tls_config.create_server_ssl_context()

    @patch("tdwii_plus_examples.tls_config.ssl.SSLContext")
    def test_create_server_ssl_context_loads_server_certificate_only(self, mock_ssl_context_class):
        mock_context = mock_ssl_context_class.return_value
        mock_context.verify_mode = ssl.CERT_NONE

        tls_config = TLSConfig(cert_file="cert.pem", key_file="key.pem")

        context = tls_config.create_server_ssl_context()

        mock_ssl_context_class.assert_called_once_with(ssl.PROTOCOL_TLS_SERVER)
        mock_context.load_cert_chain.assert_called_once_with(certfile="cert.pem", keyfile="key.pem")
        mock_context.load_verify_locations.assert_not_called()
        self.assertEqual(context.verify_mode, ssl.CERT_NONE)

    @patch("tdwii_plus_examples.tls_config.ssl.SSLContext")
    def test_create_server_ssl_context_loads_ca_without_requiring_client_certificate(self, mock_ssl_context_class):
        mock_context = mock_ssl_context_class.return_value
        mock_context.verify_mode = ssl.CERT_NONE

        tls_config = TLSConfig(cert_file="cert.pem", key_file="key.pem", ca_cert="ca.pem")

        context = tls_config.create_server_ssl_context()

        mock_context.load_verify_locations.assert_called_once_with(cafile="ca.pem")
        self.assertEqual(context.verify_mode, ssl.CERT_NONE)

    @patch("tdwii_plus_examples.tls_config.ssl.SSLContext")
    def test_create_server_ssl_context_requires_client_certificate_for_mtls(self, mock_ssl_context_class):
        mock_context = mock_ssl_context_class.return_value

        tls_config = TLSConfig(cert_file="cert.pem", key_file="key.pem", ca_cert="ca.pem", require_mtls=True)

        context = tls_config.create_server_ssl_context()

        mock_context.load_verify_locations.assert_called_once_with(cafile="ca.pem")
        self.assertEqual(context.verify_mode, ssl.CERT_REQUIRED)


if __name__ == "__main__":
    unittest.main()
