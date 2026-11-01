import logging
import tempfile
import unittest

from tdwii_plus_examples.basescu import BaseSCU
from tdwii_plus_examples.cechoscp import CEchoSCP
from tdwii_plus_examples.tests.utils.certificates import create_ca_certificate, issue_certificate, write_pem_files
from tdwii_plus_examples.tls_config import TLSConfig, TLSUsage


class TestBaseSCUTLS(unittest.TestCase):
    # The SCP is addressed by IP address, while its certificate is issued for "localhost":
    # the SCU verifies the certificate chain, not the host name.
    ADDRESS = "127.0.0.1"
    PORT = 11120

    @classmethod
    def setUpClass(cls):
        # Generate the certificates for the tests:
        # - a CA that signs the server certificate and the client certificate
        # - a second CA that signs nothing, trusted by the SCU in the test that rejects the server
        # The temporary directory is removed at teardown, even if this setup fails.
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp_dir.cleanup)
        directory = cls.temp_dir.name

        ca_cert, ca_key = create_ca_certificate("Test CA")
        cls.ca_cert_path, _ = write_pem_files(directory, "ca", ca_cert, ca_key)

        server_cert, server_key = issue_certificate(ca_cert, ca_key, "localhost")
        cls.server_cert_path, cls.server_key_path = write_pem_files(directory, "server", server_cert, server_key)

        client_cert, client_key = issue_certificate(ca_cert, ca_key, "client")
        cls.client_cert_path, cls.client_key_path = write_pem_files(directory, "client", client_cert, client_key)

        other_ca_cert, other_ca_key = create_ca_certificate("Other Test CA")
        cls.other_ca_cert_path, _ = write_pem_files(directory, "other_ca", other_ca_cert, other_ca_key)

    def setUp(self):
        self.logger = logging.getLogger("test_basescu_tls")

    def _run_scp(self, tls_config=None):
        scp = CEchoSCP(bind_address=self.ADDRESS, port=self.PORT, logger=self.logger, tls_config=tls_config)
        scp.run()
        self.addCleanup(scp.stop)

    def _verify(self, tls_config=None):
        """Send a C-ECHO request with a BaseSCU configured as given and return its result."""
        scu = BaseSCU(
            logger=self.logger,
            calling_ae_title="ECHOSCU",
            called_ip=self.ADDRESS,
            called_port=self.PORT,
            called_ae_title="ECHO_SCP",
            tls_config=tls_config,
        )
        scu.ae.acse_timeout = 5
        scu.ae.network_timeout = 5
        return scu.verify()

    def _server_tls_config(self):
        return TLSConfig(cert_file=self.server_cert_path, key_file=self.server_key_path)

    def _server_mtls_config(self):
        return TLSConfig(
            cert_file=self.server_cert_path, key_file=self.server_key_path, ca_cert=self.ca_cert_path, require_mtls=True
        )

    def _client_tls_config(self, ca_cert=None):
        return TLSConfig(ca_cert=ca_cert or self.ca_cert_path, usage=TLSUsage.CLIENT_AUTH)

    def _client_mtls_config(self):
        return TLSConfig(
            cert_file=self.client_cert_path,
            key_file=self.client_key_path,
            ca_cert=self.ca_cert_path,
            require_mtls=True,
            usage=TLSUsage.CLIENT_AUTH,
        )

    def test_verify_without_tls(self):
        self._run_scp()

        result = self._verify()

        self.assertEqual(result.status_category, "Success")

    def test_verify_with_tls(self):
        self._run_scp(self._server_tls_config())

        result = self._verify(self._client_tls_config())

        self.assertEqual(result.status_category, "Success")

    def test_verify_with_mtls(self):
        self._run_scp(self._server_mtls_config())

        result = self._verify(self._client_mtls_config())

        self.assertEqual(result.status_category, "Success")

    def test_verify_fails_when_the_server_requires_a_client_certificate_and_the_scu_has_none(self):
        self._run_scp(self._server_mtls_config())

        result = self._verify(self._client_tls_config())

        self.assertEqual(result.status_category, "AssocFailure")

    def test_verify_fails_when_the_scu_does_not_trust_the_server_certificate(self):
        self._run_scp(self._server_tls_config())

        result = self._verify(self._client_tls_config(ca_cert=self.other_ca_cert_path))

        self.assertEqual(result.status_category, "AssocFailure")

    def test_verify_without_tls_fails_against_a_tls_server(self):
        self._run_scp(self._server_tls_config())

        result = self._verify()

        self.assertEqual(result.status_category, "AssocFailure")

    def test_verify_with_tls_fails_against_a_server_without_tls(self):
        self._run_scp()

        result = self._verify(self._client_tls_config())

        self.assertEqual(result.status_category, "AssocFailure")


if __name__ == "__main__":
    unittest.main()
