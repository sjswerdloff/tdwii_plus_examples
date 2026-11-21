"""
Command line options to secure the connections of a DICOM AE with TLS.

``--tls`` or ``--mtls`` selects the mode, and the ``--tls-*`` options provide
the files used by that mode.

    --tls       Use TLS
    --mtls      Use mutual TLS
    --tls-cert  PEM file with the certificate of the AE
    --tls-key   PEM file with the private key of the AE
    --tls-ca    PEM file with the CA certificates trusted to verify the remote AEs

Only the rules of an AE acting as an SCP (server) are implemented for now.

"""

import argparse
import os
from typing import Optional

from tdwii_plus_examples.tls_config import TLSConfig


def add_tls_arguments(parser: argparse.ArgumentParser) -> None:
    """Add the TLS options to the parser, in their own group."""
    group = parser.add_argument_group("TLS options")
    mode = group.add_mutually_exclusive_group()
    mode.add_argument("--tls", action="store_true", help="Use TLS, needs --tls-cert and --tls-key")
    mode.add_argument(
        "--mtls",
        action="store_true",
        help="Use mutual TLS, needs --tls-cert, --tls-key and --tls-ca",
    )
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

    # mtls must be explicitly selected when CA file option is present, to avoid client certificates not being verified
    if args.tls_ca and not args.mtls:
        raise ValueError("--tls-ca requires --mtls")

    _check_files_exist(args)


def tls_config_from_args(parser: argparse.ArgumentParser, args: argparse.Namespace) -> Optional[TLSConfig]:
    """
    Build the TLS configuration for a DICOM AE from the parsed arguments.

    Returns None when neither --tls nor --mtls is given. Reports an invalid
    combination of options with ``parser.error``, which exits the application.
    """
    try:
        mode = _selected_mode(args)
        if mode is None:
            return None
        _check_scp_options(mode, args)
    except ValueError as error:
        parser.error(str(error))

    return TLSConfig(cert_file=args.tls_cert, key_file=args.tls_key, ca_cert=args.tls_ca, require_mtls=args.mtls)
