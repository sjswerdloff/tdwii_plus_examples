import logging
import os
import re
import ssl
import subprocess
import sys
import tempfile
import time
import unittest
from datetime import datetime, timedelta, timezone
from logging.handlers import MemoryHandler

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from pynetdicom import AE
from pynetdicom.sop_class import Verification

from tdwii_plus_examples.basescp import BaseSCP, TLSConfig


class CEchoSCP(BaseSCP):
    def __init__(self, bind_address, port=11112, logger=None, tls_config=None):
        super().__init__(bind_address=bind_address, port=port, logger=logger, tls_config=tls_config)

    def _add_contexts(self):
        super()._add_contexts()
        self.ae.add_supported_context(Verification, "1.2.840.10008.1.2")


class TestBaseSCP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Generate self-signed cert for TLS tests
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.cert_path = os.path.join(cls.temp_dir.name, "cert.pem")
        cls.key_path = os.path.join(cls.temp_dir.name, "key.pem")

        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "localhost")])
        now = datetime.now(timezone.utc)
        cert = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now)
            .not_valid_after(now + timedelta(days=1))
            .add_extension(x509.SubjectAlternativeName([x509.DNSName("localhost")]), critical=False)
            .sign(key, hashes.SHA256())
        )

        with open(cls.key_path, "wb") as f:
            f.write(
                key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )

        with open(cls.cert_path, "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()

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

    def test_run_and_check_log(self):
        # Run the SCP
        self.scp.run()

        # Ensure the correct Python interpreter is used for the subprocess call
        python_executable = sys.executable

        # Send an echo request using pynetdicom's echoscu.py
        subprocess.check_call(
            [python_executable, "-m", "pynetdicom", "echoscu", "localhost", "11112", "-aet", "ECHOSCU", "-aec", "BASE_SCP"]
        )

        # Wait for 1 second to ensure the logs are generated
        time.sleep(1)

        # Get the log messages
        log_messages = [record.getMessage() for record in self.memory_handler.buffer]

        # Check the EVT_CONN_OPEN event log message
        self.test_logger.info("Searching for EVT_CONN_OPEN event log message")
        pattern = r"^Successful connection from " + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):([\w]{3,5})"
        matching_message = None
        for message in log_messages:
            if re.search(pattern, message):
                matching_message = message
                break
        self.test_logger.info(f"EVT_CONN_OPEN event log message found: {matching_message}")
        self.assertIsNotNone(matching_message, "EVT_CONN_OPEN event log message not found")
        # Stop the SCP
        self.scp.stop()

        # Check the EVT_CONN_CLOSE event log message
        self.test_logger.info("Searching for EVT_CONN_CLOSE event log message")
        pattern = r"^Closed connection with " + r"([\w]+)@" + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):([\w]{3,5})"
        matching_message = None
        for message in log_messages:
            if re.search(pattern, message):
                matching_message = message
                break
        self.test_logger.info(f"EVT_CONN_CLOSE event log message found: {matching_message}")
        self.assertIsNotNone(matching_message, "EVT_CONN_CLOSE event log message not found")

    def test_run_with_tls(self):
        """
        Verify that passing a TLSConfig correctly configures the server
        for real TLS communication.
        """
        # 1. Setup the SCP with TLS enabled
        tls_config = TLSConfig(cert_file=self.cert_path, key_file=self.key_path)
        scp = CEchoSCP(bind_address="localhost", port=11113, logger=self.scp_logger, tls_config=tls_config)
        scp.run()

        try:
            # 2. Setup the SCU (Client) with TLS using pynetdicom AE
            ae = AE(ae_title="ECHOSCU")
            ae.add_requested_context(Verification, "1.2.840.10008.1.2")

            # Client SSL context that trusts the self-signed certificate
            client_ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            client_ssl_context.load_verify_locations(cafile=self.cert_path)

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


if __name__ == "__main__":
    unittest.main()
