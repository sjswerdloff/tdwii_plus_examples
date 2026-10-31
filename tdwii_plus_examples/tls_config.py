import ssl
from dataclasses import dataclass
from typing import Optional


@dataclass
class TLSConfig:
    """
    Configuration for TLS communication.

    Attributes:
        cert_file (str): Path to the certificate file.
        key_file (str): Path to the private key file.
        ca_cert (str, optional): Path to the CA certificate file for mTLS.
        require_mtls (bool): Whether to require mutual TLS (mTLS).
    """

    cert_file: str
    key_file: str
    ca_cert: Optional[str] = None
    require_mtls: bool = False

    def __post_init__(self):
        """Reject a configuration that requires client certificates without a CA to verify them."""
        if self.require_mtls and not self.ca_cert:
            raise ValueError("require_mtls=True needs ca_cert to verify client certificates")

    def create_ssl_context(self) -> ssl.SSLContext:
        """Creates an SSLContext based on the configuration."""
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=self.cert_file, keyfile=self.key_file)
        if self.ca_cert:
            context.load_verify_locations(cafile=self.ca_cert)
        if self.require_mtls:
            context.verify_mode = ssl.CERT_REQUIRED
        return context
