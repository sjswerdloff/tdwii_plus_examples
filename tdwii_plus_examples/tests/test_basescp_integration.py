import logging
import re
import ssl
import subprocess
import sys
import tempfile
import time
import unittest
from logging.handlers import MemoryHandler

from pynetdicom import AE
from pynetdicom.sop_class import Verification

from tdwii_plus_examples.basescp import BaseSCP, TLSConfig
from tdwii_plus_examples.tests.utils.certificates import create_ca_certificate, issue_certificate, write_pem_files


class CEchoSCP(BaseSCP):
    def __init__(self, bind_address, port=11112, logger=None, tls_config=None):
        super().__init__(bind_address=bind_address, port=port, logger=logger, tls_config=tls_config)

    def _add_contexts(self):
        super()._add_contexts()
        self.ae.add_supported_context(Verification, "1.2.840.10008.1.2")


class TestBaseSCP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Generate the certificates for the TLS tests: a self-signed CA that signs the server certificate
        # and the client certificate (mTLS), and a client certificate signed by another CA, which is not trusted.
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
        untrusted_cert, untrusted_key = issue_certificate(other_ca_cert, other_ca_key, "untrusted")
        cls.untrusted_cert_path, cls.untrusted_key_path = write_pem_files(
            directory, "untrusted", untrusted_cert, untrusted_key
        )

    def setUp(self):
        # Set up the logger for the BaseSCP to DEBUG level
        # with a memory handler to store up to 100 log messages
        self.scp_logger = logging.getLogger("basescp")
        self.scp_logger.setLevel(logging.DEBUG)
        self.memory_handler = MemoryHandler(100)
        self.scp_logger.addHandler(self.memory_handler)

        # Set up the logger for this test to DEBUG level
        # with a stream handler to print the log messages to the console
        self.test_logger = logging.getLogger("test_basescp")
        self.test_logger.setLevel(logging.DEBUG)
        self.stream_handler = logging.StreamHandler()
        self.test_logger.addHandler(self.stream_handler)

        # Create a subclass of BaseSCP with only 1 presentation context:
        # the required Verification presentation context with the
        # default DICOM transfer syntax (Implicit VR Little Endian)
        self.scp = CEchoSCP(bind_address="localhost", logger=self.scp_logger)

    # Connection events logged by the SCP (EVT_CONN_OPEN and EVT_CONN_CLOSE)
    CONN_OPEN_PATTERN = r"^Successful connection from " + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):([\w]{3,5})"
    CONN_CLOSE_PATTERN = r"^Closed connection with " + r"([\w]+)@" + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):([\w]{3,5})"
    # TLS session logged when a connection is opened over TLS
    TLS_SESSION_PATTERN = r"^TLS session with \S+: TLSv[\d.]+, \w+"

    def _logged_messages(self, pattern):
        """Return the SCP log messages matching the pattern."""
        messages = [record.getMessage() for record in self.memory_handler.buffer]
        return [message for message in messages if re.search(pattern, message)]

    def _wait_for_logged_messages(self, pattern, timeout=5.0):
        """Wait until the SCP has logged a message matching the pattern, as events are logged by its own threads."""
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            messages = self._logged_messages(pattern)
            if messages:
                return messages
            time.sleep(0.05)
        return []

    def test_run_and_check_log(self):
        # Run the SCP
        self.scp.run()

        # Ensure the correct Python interpreter is used for the subprocess call
        python_executable = sys.executable

        # Send an echo request using pynetdicom's echoscu.py
        subprocess.check_call(
            [python_executable, "-m", "pynetdicom", "echoscu", "localhost", "11112", "-aet", "ECHOSCU", "-aec", "BASE_SCP"]
        )

        # Check the EVT_CONN_OPEN event log message, waiting for the logs to be generated
        self.test_logger.info("Searching for EVT_CONN_OPEN event log message")
        matching_messages = self._wait_for_logged_messages(self.CONN_OPEN_PATTERN)
        self.test_logger.info(f"EVT_CONN_OPEN event log message found: {matching_messages}")
        self.assertTrue(matching_messages, "EVT_CONN_OPEN event log message not found")
        # A connection that is not secured with TLS does not log any TLS session
        self.assertEqual(self._logged_messages(self.TLS_SESSION_PATTERN), [])
        # Stop the SCP
        self.scp.stop()

        # Check the EVT_CONN_CLOSE event log message
        self.test_logger.info("Searching for EVT_CONN_CLOSE event log message")
        matching_messages = self._wait_for_logged_messages(self.CONN_CLOSE_PATTERN)
        self.test_logger.info(f"EVT_CONN_CLOSE event log message found: {matching_messages}")
        self.assertTrue(matching_messages, "EVT_CONN_CLOSE event log message not found")

    def test_run_with_tls(self):
        """
        Verify that passing a TLSConfig correctly configures the server
        for real TLS communication.
        """
        # 1. Setup the SCP with TLS enabled
        tls_config = TLSConfig(cert_file=self.server_cert_path, key_file=self.server_key_path)
        scp = CEchoSCP(bind_address="localhost", port=11113, logger=self.scp_logger, tls_config=tls_config)
        scp.run()

        try:
            # 2. Setup the SCU (Client) with TLS using pynetdicom AE
            ae = AE(ae_title="ECHOSCU")
            ae.add_requested_context(Verification, "1.2.840.10008.1.2")

            # Client SSL context that trusts the CA which signed the server certificate
            client_ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            client_ssl_context.load_verify_locations(cafile=self.ca_cert_path)

            # Require the remote hostname to match "localhost" as embedded in cert
            client_ssl_context.check_hostname = True

            # 3. Associate with TLS parameters
            assoc = ae.associate("localhost", 11113, tls_args=(client_ssl_context, "localhost"))

            self.assertTrue(assoc.is_established, "Failed to establish TLS association with SCP")

            if assoc.is_established:
                status = assoc.send_c_echo()
                self.assertIsNotNone(status, "Did not receive a response to C-ECHO over TLS")
                self.assertEqual(status.Status, 0x0000, "C-ECHO status was not SUCCESS")
                assoc.release()

            time.sleep(1)

        finally:
            scp.stop()
            # print the logs to debug if it fails
            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            print("\nLOGS:", log_messages)

        # Check that TLS was configured
        self.assertIn("Configuring TLS for SCP server", log_messages)

        # Check that the SCP logged the connection events
        self.assertTrue(self._wait_for_logged_messages(self.CONN_OPEN_PATTERN), "EVT_CONN_OPEN event log message not found")
        self.assertTrue(self._wait_for_logged_messages(self.CONN_CLOSE_PATTERN), "EVT_CONN_CLOSE event log message not found")

        # Check that the TLS session was logged, without client certificate as the client did not present one
        tls_sessions = self._wait_for_logged_messages(self.TLS_SESSION_PATTERN)
        self.assertTrue(tls_sessions, "TLS session log message not found")
        self.assertNotIn("client certificate", tls_sessions[0])

    # mTLS: the server requires a client certificate signed by the configured CA

    MTLS_PORT = 11116

    def _run_scp_with_mtls(self):
        """Start an SCP that requires a client certificate trusted through the client CA."""
        tls_config = TLSConfig(
            cert_file=self.server_cert_path, key_file=self.server_key_path, ca_cert=self.ca_cert_path, require_mtls=True
        )
        scp = CEchoSCP(bind_address="localhost", port=self.MTLS_PORT, logger=self.scp_logger, tls_config=tls_config)
        scp.run()
        return scp

    def _associate_with_tls(self, client_certificate=None):
        """Associate over TLS, trusting the server certificate and optionally presenting a client certificate."""
        ae = AE(ae_title="ECHOSCU")
        ae.add_requested_context(Verification, "1.2.840.10008.1.2")
        ae.acse_timeout = 5
        ae.network_timeout = 5

        client_ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        client_ssl_context.load_verify_locations(cafile=self.ca_cert_path)
        if client_certificate:
            cert_file, key_file = client_certificate
            client_ssl_context.load_cert_chain(certfile=cert_file, keyfile=key_file)

        return ae.associate("localhost", self.MTLS_PORT, tls_args=(client_ssl_context, "localhost"))

    def test_run_with_mtls_accepts_trusted_client_certificate(self):
        scp = self._run_scp_with_mtls()
        assoc = None
        try:
            assoc = self._associate_with_tls(client_certificate=(self.client_cert_path, self.client_key_path))

            self.assertTrue(assoc.is_established, "Trusted client certificate was not accepted")
            status = assoc.send_c_echo()
            self.assertIsNotNone(status, "Did not receive a response to C-ECHO over mTLS")
            self.assertEqual(status.Status, 0x0000, "C-ECHO status was not SUCCESS")
            assoc.release()

            # The SCP logged the connection events for the accepted client
            self.assertTrue(self._wait_for_logged_messages(self.CONN_OPEN_PATTERN), "EVT_CONN_OPEN not logged")
            self.assertTrue(self._wait_for_logged_messages(self.CONN_CLOSE_PATTERN), "EVT_CONN_CLOSE not logged")

            # The TLS session logged identifies the client through its certificate
            tls_sessions = self._wait_for_logged_messages(self.TLS_SESSION_PATTERN)
            self.assertTrue(tls_sessions, "TLS session not logged")
            self.assertIn("client certificate subject: commonName=client", tls_sessions[0])
        finally:
            if assoc is not None and assoc.is_established:
                assoc.release()
            scp.stop()

    def test_run_with_mtls_rejects_client_without_certificate(self):
        scp = self._run_scp_with_mtls()
        assoc = None
        try:
            assoc = self._associate_with_tls()

            self.assertFalse(assoc.is_established, "Client without a certificate was accepted")
            # The client is rejected during the TLS handshake: the SCP does not log any connection
            self.assertEqual(self._logged_messages(self.CONN_OPEN_PATTERN), [])
        finally:
            if assoc is not None and assoc.is_established:
                assoc.release()
            scp.stop()

    def test_run_with_mtls_rejects_untrusted_client_certificate(self):
        scp = self._run_scp_with_mtls()
        assoc = None
        try:
            assoc = self._associate_with_tls(client_certificate=(self.untrusted_cert_path, self.untrusted_key_path))

            self.assertFalse(assoc.is_established, "Untrusted client certificate was accepted")
            # The client is rejected during the TLS handshake: the SCP does not log any connection
            self.assertEqual(self._logged_messages(self.CONN_OPEN_PATTERN), [])
        finally:
            if assoc is not None and assoc.is_established:
                assoc.release()
            scp.stop()


if __name__ == "__main__":
    unittest.main()
