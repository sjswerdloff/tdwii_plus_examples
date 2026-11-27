"""Helpers generating the certificates used by the TLS tests."""

import ipaddress
import os
from datetime import datetime, timedelta, timezone

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID


def _new_private_key():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def create_ca_certificate(common_name):
    """Create a self-signed certificate authority (CA) certificate.

    Returns the certificate and its private key.
    """
    key = _new_private_key()
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, common_name)])
    now = datetime.now(timezone.utc)
    cert = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now)
        .not_valid_after(now + timedelta(days=1))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .add_extension(
            x509.KeyUsage(
                digital_signature=False,
                content_commitment=False,
                key_encipherment=False,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=True,
                crl_sign=True,
                encipher_only=False,
                decipher_only=False,
            ),
            critical=True,
        )
        .add_extension(x509.SubjectKeyIdentifier.from_public_key(key.public_key()), critical=False)
        .sign(key, hashes.SHA256())
    )
    return cert, key


def _subject_alternative_name(hosts):
    """Return the subjectAltName entries of hosts: an IPAddress for an IP address, a DNSName otherwise."""
    names = []
    for host in hosts:
        try:
            names.append(x509.IPAddress(ipaddress.ip_address(host)))
        except ValueError:
            names.append(x509.DNSName(host))
    return x509.SubjectAlternativeName(names)


def issue_certificate(ca_cert, ca_key, common_name, hosts=None):
    """Issue a certificate signed by the given CA.

    common_name is the Common Name (CN) of the subject of the certificate, a label that no host check reads.

    hosts is the list of host names and IP addresses written in the subjectAltName (SAN) of the certificate,
    such as ["localhost", "127.0.0.1"]: the hosts the certificate is issued for. Without hosts, the certificate
    has no SAN, as a client certificate usually does.

    Returns the certificate and its private key.
    """
    key = _new_private_key()
    now = datetime.now(timezone.utc)
    builder = (
        x509.CertificateBuilder()
        .subject_name(x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, common_name)]))
        .issuer_name(ca_cert.subject)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now)
        .not_valid_after(now + timedelta(days=1))
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .add_extension(
            x509.KeyUsage(
                digital_signature=True,
                content_commitment=False,
                key_encipherment=True,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=False,
                crl_sign=False,
                encipher_only=False,
                decipher_only=False,
            ),
            critical=True,
        )
        .add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_cert.public_key()), critical=False)
    )
    if hosts:
        builder = builder.add_extension(_subject_alternative_name(hosts), critical=False)
    cert = builder.sign(ca_key, hashes.SHA256())
    return cert, key


def write_pem_files(directory, name, cert, key):
    """Write a certificate and its private key as PEM files.

    Returns the paths of the certificate file and of the key file.
    """
    cert_path = os.path.join(directory, f"{name}_cert.pem")
    key_path = os.path.join(directory, f"{name}_key.pem")

    with open(key_path, "wb") as f:
        f.write(
            key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )

    with open(cert_path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

    return cert_path, key_path
