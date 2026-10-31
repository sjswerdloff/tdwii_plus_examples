import enum
import ssl
from dataclasses import dataclass
from typing import Optional


class TLSUsage(enum.Flag):
    """
    Usages of a TLS configuration, named after the extended key usages of X.509 certificates.

    The usages describe what the certificate of the configuration is used for, as the
    ``extendedKeyUsage`` of a certificate does.

    Usages are combined with ``|``: ``TLSUsage.SERVER_AUTH | TLSUsage.CLIENT_AUTH`` is for an
    application that is both a server and a client.

    Attributes:
        SERVER_AUTH (serverAuth): the configuration presents its certificate to the clients that connect to it.
        CLIENT_AUTH (clientAuth): the configuration connects to servers, and presents its certificate
            to them when mutual TLS is used.
    """

    SERVER_AUTH = enum.auto()
    CLIENT_AUTH = enum.auto()


@dataclass
class TLSConfig:
    """
    Configuration for TLS communication.

    Attributes:
        cert_file (str, optional): Path to the certificate file. Required for the serverAuth usage,
            optional for clientAuth, where it is the identity presented with mTLS.
        key_file (str, optional): Path to the private key file, given together with cert_file.
        ca_cert (str, optional): Path to the CA certificate file for mTLS.
        require_mtls (bool): Whether to require mutual TLS (mTLS), which needs ca_cert, cert_file and key_file.
        usage (TLSUsage): Whether the configuration is used as a server (serverAuth), as a client (clientAuth)
            or as both (the two usages combined with ``|``). Default: serverAuth.
    """

    cert_file: Optional[str] = None
    key_file: Optional[str] = None
    ca_cert: Optional[str] = None
    require_mtls: bool = False
    usage: TLSUsage = TLSUsage.SERVER_AUTH

    def __post_init__(self):
        """Reject a configuration that lacks what its usage and mTLS require."""
        if not isinstance(self.usage, TLSUsage) or not self.usage:
            raise ValueError(f"usage must include serverAuth, clientAuth or both, got {self.usage!r}")
        if self.cert_file and not self.key_file:
            raise ValueError("cert_file needs key_file")
        if self.key_file and not self.cert_file:
            raise ValueError("key_file needs cert_file")
        if TLSUsage.SERVER_AUTH in self.usage and not self.cert_file:
            raise ValueError("serverAuth usage needs cert_file and key_file")
        if self.require_mtls and not self.ca_cert:
            raise ValueError("require_mtls=True needs ca_cert to verify the certificates of the peers")
        if self.require_mtls and not self.cert_file:
            raise ValueError("require_mtls=True needs cert_file and key_file")

    def create_server_ssl_context(self) -> ssl.SSLContext:
        """Creates the SSLContext of a server based on the configuration."""
        if TLSUsage.SERVER_AUTH not in self.usage:
            raise ValueError("a server SSL context needs the serverAuth usage")
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=self.cert_file, keyfile=self.key_file)
        if self.ca_cert:
            context.load_verify_locations(cafile=self.ca_cert)
        if self.require_mtls:
            context.verify_mode = ssl.CERT_REQUIRED
        return context
