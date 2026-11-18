"""
Command line options to secure the connections of a DICOM AE with TLS.

``--tls`` or ``--mtls`` selects the mode, and the ``--tls-*`` options provide
the files used by that mode.

    --tls       Use TLS
    --mtls      Use mutual TLS
    --tls-cert  PEM certificate of the application
    --tls-key   PEM private key of the application
    --tls-ca    PEM certificate authorities trusted to verify the peers

Only the rules of an AE acting as an SCP (server) are implemented for now.

"""

import argparse
import os
from typing import Optional

from tdwii_plus_examples.basescp import TLSConfig


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
    group.add_argument("--tls-cert", metavar="FILE", help="PEM certificate of the application")
    group.add_argument("--tls-key", metavar="FILE", help="PEM private key of the application")
    group.add_argument("--tls-ca", metavar="FILE", help="PEM certificate authorities trusted to verify the peers")


def _check_server_options(args: argparse.Namespace) -> None:
    """Raise a ValueError when the TLS options cannot configure a server."""
    options = {"--tls-cert": args.tls_cert, "--tls-key": args.tls_key, "--tls-ca": args.tls_ca}

    # tls or mtls must be explicitly selected when any of the file options is given
    if not (args.tls or args.mtls):
        tls_file_options = [name for name, path in options.items() if path]
        if tls_file_options:
            raise ValueError(f"{', '.join(tls_file_options)} requires --tls or --mtls")
        return

    # Cert and Key file options must be present for tls or mtls, and CA file option must be present for mtls
    mode = "--mtls" if args.mtls else "--tls"
    required = ["--tls-cert", "--tls-key"] + (["--tls-ca"] if args.mtls else [])
    missing = [name for name in required if not options[name]]
    if missing:
        raise ValueError(f"{mode} requires {', '.join(missing)}")

    # mtls must be explicitly selected when CA file option is present, to avoid client certificates not being verified
    if args.tls_ca and not args.mtls:
        raise ValueError("--tls-ca requires --mtls")

    # All file options must point to existing files
    for name, path in options.items():
        if path and not os.path.isfile(path):
            raise ValueError(f"{name}: file not found: {path}")


def tls_config_from_args(parser: argparse.ArgumentParser, args: argparse.Namespace) -> Optional[TLSConfig]:
    """
    Build the TLS configuration for a DICOM AE from the parsed arguments.

    Returns None when neither --tls nor --mtls is given. Reports an invalid
    combination of options with ``parser.error``, which exits the application.
    """
    try:
        _check_server_options(args)
    except ValueError as error:
        parser.error(str(error))

    if not (args.tls or args.mtls):
        return None
    return TLSConfig(cert_file=args.tls_cert, key_file=args.tls_key, ca_cert=args.tls_ca, require_mtls=args.mtls)
