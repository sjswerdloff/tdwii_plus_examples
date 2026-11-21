"""
Command line options to secure the connections of a DICOM AE with TLS.

``--tls`` or ``--mtls`` selects the mode, and the ``--tls-*`` options provide
the files used by that mode.

    --tls       Use TLS
    --mtls      Use mutual TLS
    --tls-cert  PEM file with the certificate of the AE
    --tls-key   PEM file with the private key of the AE
    --tls-ca    PEM file with the CA certificates trusted to verify the remote AEs

The files required by each mode depend on the role of the AE, which gives its TLS role:

- As an SCP (a TLS server), ``--tls`` requires ``--tls-cert`` and ``--tls-key``.
  ``--mtls`` also requires ``--tls-ca``, to verify the SCUs.
- As an SCU (a TLS client), ``--tls`` requires ``--tls-ca``, to verify the SCP.
  ``--mtls`` also requires ``--tls-cert`` and ``--tls-key``, the identity of the SCU.

These rules reflect the authentication requirements of the following specifications. They do not
claim conformance to either of them:

- DICOM PS3.15 B.12 and B.13, BCP 195 TLS Secure Transport Connection Profiles specifies that
  servers shall support mutual authentication and may be configured not to use it, and that
  clients are not required, but are encouraged, to use it.
  Hence an SCP accepts both ``--tls`` and ``--mtls``.
- IHE-ITI TF-1 9.4.1.2.2 and TF-2 3.19.6.1.1 ATNA profile specifies that the certificate
  authorities that are trusted must be configurable, and that common list of the certificate
  authorities like the ones for the browsers is not sufficient.
  Hence an SCU always needs ``--tls-ca``, and the system certificate authorities are never used.

"""

import argparse
import os
from typing import Optional

from tdwii_plus_examples.tls_config import TLSConfig, TLSUsage

# Define the help message for each TLS role depending on the selected mode (tls, mtls)
_MODE_HELP = {
    TLSUsage.SERVER_AUTH: (
        "Use TLS, needs --tls-cert and --tls-key",
        "Use mutual TLS, needs --tls-cert, --tls-key and --tls-ca",
    ),
    TLSUsage.CLIENT_AUTH: ("Use TLS, needs --tls-ca", "Use mutual TLS, needs --tls-ca, --tls-cert and --tls-key"),
}


def add_tls_arguments(parser: argparse.ArgumentParser, usage: TLSUsage) -> None:
    """
    Add the TLS options to the parser, in their own group.

    The ``usage`` is the TLS role of the AE, as for ``tls_config_from_args``, and selects the files
    that the help of ``--tls`` and ``--mtls`` states as required.

    Raises:
        ValueError: If ``usage`` is neither ``TLSUsage.SERVER_AUTH`` nor ``TLSUsage.CLIENT_AUTH``.
    """
    if usage not in _MODE_HELP:
        raise ValueError(f"unsupported usage: {usage!r}")
    tls_help, mtls_help = _MODE_HELP[usage]
    group = parser.add_argument_group("TLS options")
    mode = group.add_mutually_exclusive_group()
    mode.add_argument("--tls", action="store_true", help=tls_help)
    mode.add_argument("--mtls", action="store_true", help=mtls_help)
    group.add_argument("--tls-cert", metavar="FILE", help="PEM file with the certificate of the AE")
    group.add_argument("--tls-key", metavar="FILE", help="PEM file with the private key of the AE")
    group.add_argument("--tls-ca", metavar="FILE", help="PEM file with the CA certificates trusted to verify the remote AEs")


def _tls_file_options(args: argparse.Namespace) -> dict:
    """Return the file options by name."""
    return {"--tls-cert": args.tls_cert, "--tls-key": args.tls_key, "--tls-ca": args.tls_ca}


def _selected_mode(args: argparse.Namespace) -> Optional[str]:
    """
    Return the selected mode, "--tls" or "--mtls", or None when neither is selected.

    Raise a ValueError when a file option is present without a mode.
    """
    if args.mtls:
        return "--mtls"
    if args.tls:
        return "--tls"
    tls_file_options = [name for name, path in _tls_file_options(args).items() if path]
    if tls_file_options:
        raise ValueError(f"{', '.join(tls_file_options)} requires --tls or --mtls")
    return None


def _check_required_options(mode: str, args: argparse.Namespace, required: list) -> None:
    """Raise a ValueError when a file option required by the mode is missing."""
    options = _tls_file_options(args)
    missing = [name for name in required if not options[name]]
    if missing:
        raise ValueError(f"{mode} requires {', '.join(missing)}")


def _check_files_exist(args: argparse.Namespace) -> None:
    """Raise a ValueError when a file option does not point to an existing file."""
    for name, path in _tls_file_options(args).items():
        if path and not os.path.isfile(path):
            raise ValueError(f"{name}: file not found: {path}")


def _check_scp_options(mode: str, args: argparse.Namespace) -> None:
    """Raise a ValueError when the TLS options are not valid for an SCP."""
    # Cert and Key file options must be present for tls or mtls, and CA file option must be present for mtls
    _check_required_options(mode, args, ["--tls-cert", "--tls-key"] + (["--tls-ca"] if args.mtls else []))

    # mtls must be explicitly selected when CA file option is present, to avoid the certificates of the SCUs not being verified
    if args.tls_ca and not args.mtls:
        raise ValueError("--tls-ca requires --mtls")

    _check_files_exist(args)


def _check_scu_options(mode: str, args: argparse.Namespace) -> None:
    """Raise a ValueError when the TLS options are not valid for an SCU."""
    # CA file option must be present for tls or mtls, so that the system certificate authorities are never used,
    # and Cert and Key file options must be present for mtls
    _check_required_options(mode, args, ["--tls-ca"] + (["--tls-cert", "--tls-key"] if args.mtls else []))

    # The client identity options (certificate and key) are only valid with mtls, so that the SCU configuration
    # states what it expects of the server: with tls, a server that asks for a client certificate is refused
    # and not silently satisfied
    options = _tls_file_options(args)
    identity_options = [name for name in ("--tls-cert", "--tls-key") if options[name]]
    if identity_options and not args.mtls:
        raise ValueError(f"{', '.join(identity_options)} requires --mtls")

    _check_files_exist(args)


def tls_config_from_args(parser: argparse.ArgumentParser, args: argparse.Namespace, usage: TLSUsage) -> Optional[TLSConfig]:
    """
    Build the TLS configuration for a DICOM AE from the parsed arguments.

    The ``usage`` is the TLS role of the AE and selects the rules applied to the options:
    ``TLSUsage.SERVER_AUTH`` for an SCP app, which accepts the connections, or
    ``TLSUsage.CLIENT_AUTH`` for an SCU app, which initiates them.

    Returns:
        Optional[TLSConfig]: The configuration, or None when neither --tls nor --mtls is selected.

    Raises:
        SystemExit: If the options are invalid, after ``parser.error`` printed the usage and the error.
        ValueError: If ``usage`` is neither ``TLSUsage.SERVER_AUTH`` nor ``TLSUsage.CLIENT_AUTH``.
    """
    if usage not in (TLSUsage.SERVER_AUTH, TLSUsage.CLIENT_AUTH):
        raise ValueError(f"unsupported usage: {usage!r}")
    try:
        mode = _selected_mode(args)
        if mode is None:
            return None
        if usage == TLSUsage.SERVER_AUTH:
            _check_scp_options(mode, args)
        else:
            _check_scu_options(mode, args)
    except ValueError as error:
        parser.error(str(error))

    return TLSConfig(cert_file=args.tls_cert, key_file=args.tls_key, ca_cert=args.tls_ca, require_mtls=args.mtls, usage=usage)
