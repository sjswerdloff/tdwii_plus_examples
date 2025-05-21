#!/usr/bin/env python

r"""
A DICOM UPS Worklist Manager application example.

This application starts an Application Entity (AE) server implementing
the Verification and Unified Procedure Step (UPS) Service Classes.
It supports the Verification, the UPS Push, UPS Pull, UPS Watch and
UPS Event SOP Classes as an SCP.
It listens for incoming DIMSE primitive requests and delegates the
processing to handlers to store UPS work items as DICOM Part 10 files
and manage them using a database.

Note: that for the UPS Event SOP Class, the SCP is not a receiver of the
N-EVENT-REPORT primitives but a sender of notifications about changes
in the states of the UPS it manages or its own state to any SCU that
has previously subscribed to receive such notifications using the UPS
Watch SOP Class.

If not specified in the command line, the configuration file is
tdwii_plus_examples\cli\upsscp\config\upsscp_default.ini

Usage:
    upsscp [options]

Options:
    -h, --help                  Show this help message and exit
    --version                   Print version information and exit
    -c, --config [f]ilename     Overridde configuration file
    -a, --ae_title              Override the Application Entity Title
    -b, --bind_address          Override the interface IP address or hostname
    -p, --port                  Override Port number
    -q, --quiet                 Quiet mode, print no warnings and errors
    -v, --verbose               Set log level to INFO
    -d, --debug                 Set log level to DEBUG
    -ll, --log-level [l]        Set level of logger (critical, error, warn,
                                info, debug)
    -ta, --acse-timeout [s]     Override the association messages timeout
    -td, --dimse-timeout [s]    Override the DIMSE messages timeout
    -tn, --network-timeout [s]  Override the network timeout
    -pdu, --max-pdu [n]         Override the maximum PDU size
    --database-location [f]     Override the database file path
    --instance-location [d]     Override the instance storage directory
    --clean                     Empty database and instance storage directory
"""

import argparse
import atexit
import os
import sys
import time
from configparser import ConfigParser

import pydicom.config
from pynetdicom import (
    ALL_TRANSFER_SYNTAXES,
    UnifiedProcedurePresentationContexts,
    _config,
    _handlers,
    evt,
)
from pynetdicom.apps.common import setup_logging
from pynetdicom.utils import set_ae
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tdwii_plus_examples.cechoscp import CEchoSCP
from tdwii_plus_examples.cli.upsscp import upsdb
from tdwii_plus_examples.cli.upsscp.handlers import (
    handle_find,
    handle_naction,
    handle_ncreate,
    handle_nget,
    handle_nset,
)

# Use `None` for empty values
pydicom.config.use_none_as_empty_text_VR_value = True
# Don't log identifiers
_config.LOG_RESPONSE_IDENTIFIERS = False


# Override the standard logging handlers
def _dont_log(event):
    pass


# _handlers._send_c_find_rsp = _dont_log
_handlers._send_c_get_rsp = _dont_log
_handlers._send_c_move_rsp = _dont_log
_handlers._send_c_store_rq = _dont_log
_handlers._recv_c_store_rsp = _dont_log


__version__ = "1.1.0"


def _log_config(config, logger):
    """Log the configuration settings.

    Parameters
    ----------
    logger: logging.Logger
        The application's logger.
    """
    logger.debug("Configuration settings")
    app = config["DEFAULT"]
    aet, port, pdu = app["ae_title"], app["port"], app["max_pdu"]
    logger.debug(f"  AE title: {aet}, Port: {port}, Max. PDU: {pdu}")
    logger.debug("  Timeouts:")
    acse, dimse = app["acse_timeout"], app["dimse_timeout"]
    network = app["network_timeout"]
    logger.debug(f"    ACSE: {acse}, DIMSE: {dimse}, Network: {network}")
    logger.debug(f"  Storage directory: {app['instance_location']}")
    logger.debug(f"  Database location: {app['database_location']}")

    if config.sections():
        logger.debug("  Move destinations: ")
    else:
        logger.debug("  Move destinations: none")

    for ae_title in config.sections():
        addr = config[ae_title]["address"]
        port = config[ae_title]["port"]
        logger.debug(f"    {ae_title}: ({addr}, {port})")

    logger.debug("")


def clean(db_path, instance_path, logger):
    """Remove all entries from the database and delete the corresponding
    stored instances.

    Parameters
    ----------
    db_path : str
        The database path to use with create_engine().
    instance_path : str
        The instance storage path.
    logger : logging.Logger
        The application logger.

    Returns
    -------
    bool
        ``True`` if the storage directory and database were both cleaned
        successfully, ``False`` otherwise.
    """
    engine = create_engine(db_path)
    with engine.connect() as conn:  # noqa: F841
        Session = sessionmaker(bind=engine)
        session = Session()
        query_success = True
        try:
            fpaths = [ii.filename for ii in session.query(upsdb.Instance).all()]
        except Exception as exc:
            logger.error("Exception raised while querying the database")
            logger.exception(exc)
            session.rollback()
            query_success = False
        finally:
            session.close()

        if not query_success:
            return False

        storage_cleaned = True
        for fpath in fpaths:
            try:
                os.remove(os.path.join(instance_path, fpath))
            except Exception as exc:
                logger.error(f"Unable to delete the instance at '{fpath}'")
                logger.exception(exc)
                storage_cleaned = False

        if storage_cleaned:
            logger.info("Storage directory cleaned successfully")
        else:
            logger.error("Failed to clean storage directory")

        database_cleaned = False
        try:
            upsdb.clear(session)
            database_cleaned = True
            logger.info("Database cleaned successfully")
        except Exception as exc:
            logger.error("Failed to clean the database")
            logger.exception(exc)
            session.rollback()
        finally:
            session.close()

        return database_cleaned and storage_cleaned


def _setup_argparser():
    """Setup the command line arguments"""
    # Description
    parser = argparse.ArgumentParser(
        description=(
            "The upsscp application implements a Service Class Provider (SCP) "
            "for the Verification and Unified Procedure Step (UPS) Service "
            "Classes."
        ),
        usage="upsscp [options]",
    )

    # General Options
    gen_opts = parser.add_argument_group("General Options")
    gen_opts.add_argument("--version", help="print version information and exit", action="store_true")
    output = gen_opts.add_mutually_exclusive_group()
    output.add_argument(
        "-q",
        "--quiet",
        help="quiet mode, print no warnings and errors",
        action="store_const",
        dest="log_type",
        const="q",
    )
    output.add_argument(
        "-v",
        "--verbose",
        help="verbose mode, print processing details",
        action="store_const",
        dest="log_type",
        const="v",
    )
    output.add_argument(
        "-d",
        "--debug",
        help="debug mode, print debug information",
        action="store_const",
        dest="log_type",
        const="d",
    )
    gen_opts.add_argument(
        "-ll",
        "--log-level",
        metavar="[l]",
        help=("use level l for the logger (critical, error, warn, info, debug)"),
        type=str,
        choices=["critical", "error", "warn", "info", "debug"],
    )
    fdir = os.path.abspath(os.path.dirname(__file__))
    fpath = os.path.join(fdir, "./config/upsscp_default.ini")
    internal_fpath = fpath
    if not os.path.exists(fdir) or not os.path.exists(fpath):
        fdir = os.path.abspath(os.path.dirname(sys.executable))
        fpath = os.path.join(fdir, "./config/upsscp_default.ini")

    if not os.path.exists(fdir) or not os.path.exists(fpath):
        raise FileExistsError(f"Cannot find config file in {fpath} or {internal_fpath}")

    fabspath = os.path.abspath(fpath)
    gen_opts.add_argument(
        "-c",
        "--config",
        metavar="[f]ilename",
        help="use configuration file f",
        default=fabspath,
    )

    net_opts = parser.add_argument_group("Networking Options")
    net_opts.add_argument(
        "-p",
        "--port",
        help="override the configured TCP/IP listen port number",
    )
    net_opts.add_argument(
        "-a",
        "--ae-title",
        metavar="[a]etitle",
        help="override the configured AE title",
    )
    net_opts.add_argument(
        "-ta",
        "--acse-timeout",
        metavar="[s]econds",
        help="override the configured timeout for ACSE messages",
    )
    net_opts.add_argument(
        "-td",
        "--dimse-timeout",
        metavar="[s]econds",
        help="override the configured timeout for DIMSE messages",
    )
    net_opts.add_argument(
        "-tn",
        "--network-timeout",
        metavar="[s]econds",
        help="override the configured timeout for the network",
    )
    net_opts.add_argument(
        "-pdu",
        "--max-pdu",
        metavar="[n]umber of bytes",
        help="override the configured max receive pdu to n bytes",
    )
    net_opts.add_argument(
        "-b",
        "--bind-address",
        metavar="[a]ddress",
        help="override the configured address of the network interface to listen on",
    )

    db_opts = parser.add_argument_group("Database Options")
    db_opts.add_argument(
        "--database-location",
        metavar="[f]ile",
        help="override the location of the database using file f",
        type=str,
    )
    db_opts.add_argument(
        "--instance-location",
        metavar="[d]irectory",
        help=("override the configured instance storage location to directory d"),
        type=str,
    )
    db_opts.add_argument(
        "--clean",
        help=("remove all entries from the database and delete the corresponding stored instances"),
        action="store_true",
    )

    return parser.parse_args()


def main(args=None, loop_forever=True):  # Add a parameter to control the loop
    """Run the application."""

    # parse the arguments from the command line or from the calling function
    if args is not None:
        sys.argv = args

    args = _setup_argparser()

    if args.version:
        print(f"upsscp.py v{__version__}")
        sys.exit()

    # Setup logging
    APP_LOGGER = setup_logging(args, "upsscp")
    APP_LOGGER.debug(f"upsscp.py v{__version__}")
    APP_LOGGER.debug("")

    # Load the configuration file settings
    APP_LOGGER.debug("Using configuration from:")
    APP_LOGGER.debug(f"  {args.config}")
    APP_LOGGER.debug("")
    config = ConfigParser()
    config.read(args.config)

    # Override configuration file settings with command line settings
    if args.ae_title:
        config["DEFAULT"]["ae_title"] = args.ae_title
    if args.port:
        config["DEFAULT"]["port"] = args.port
    if args.max_pdu:
        config["DEFAULT"]["max_pdu"] = args.max_pdu
    if args.acse_timeout:
        config["DEFAULT"]["acse_timeout"] = args.acse_timeout
    if args.dimse_timeout:
        config["DEFAULT"]["dimse_timeout"] = args.dimse_timeout
    if args.network_timeout:
        config["DEFAULT"]["network_timeout"] = args.network_timeout
    if args.bind_address:
        config["DEFAULT"]["bind_address"] = args.bind_address
    if args.database_location:
        config["DEFAULT"]["database_location"] = args.database_location
    if args.instance_location:
        config["DEFAULT"]["instance_location"] = args.instance_location

    # Log the configuration settings
    _log_config(config, APP_LOGGER)

    # Get our Application Entity settings
    app_config = config["DEFAULT"]

    # Get other Application Entities settings
    dests = {}
    for ae_title in config.sections():
        dest = config[ae_title]
        # Convert to bytes and validate the AE title
        ae_title = set_ae(ae_title, "ae_title", False, False)
        dests[ae_title] = (dest["address"], dest.getint("port"))

    # Set the instance storage and database directories to current directory
    # if setting is not an absolute path
    current_dir = os.path.abspath(os.path.dirname(__file__))
    instance_dir = os.path.join(current_dir, app_config["instance_location"])
    instance_dir_path = os.path.abspath(instance_dir)
    if not os.path.exists(instance_dir_path):
        os.makedirs(instance_dir_path, exist_ok=True)
    APP_LOGGER.info(f"Configured for instance_dir = {instance_dir_path}")

    db_path = os.path.join(current_dir, app_config["database_location"])
    db_path = f"sqlite:///{db_path}"

    # Create the database if it doesn't exist
    upsdb.create(db_path)

    # Clean up the database and storage directory if requested
    if args.clean:
        response = input(
            "This will delete all instances from both the storage directory "
            "and the database. Are you sure you wish to continue? [yes/no]: "
        )
        if response != "yes":
            sys.exit()

        if clean(db_path, instance_dir, APP_LOGGER):
            sys.exit()
        else:
            sys.exit(1)

    # Create the instance storage directory if it doesn't exist
    os.makedirs(instance_dir, exist_ok=True)

    # Create our Application Entity
    upsscp = CEchoSCP(
        ae_title=app_config["ae_title"],
        bind_address=app_config["bind_address"],
        port=app_config.getint("port"),
        logger=APP_LOGGER,
    )

    ae = upsscp.ae
    ae.maximum_pdu_size = app_config.getint("max_pdu")
    ae.acse_timeout = app_config.getfloat("acse_timeout")
    ae.dimse_timeout = app_config.getfloat("dimse_timeout")
    ae.network_timeout = app_config.getfloat("network_timeout")

    # Unified Procedure Step SCP
    for cx in UnifiedProcedurePresentationContexts:
        if cx.abstract_syntax.keyword not in ("UnifiedProcedureStepEvent", "UnifiedProcedureStepQuery"):
            ae.add_supported_context(cx.abstract_syntax, ALL_TRANSFER_SYNTAXES, scp_role=True, scu_role=False)

    # Set our handler bindings
    upsscp.handlers.append((evt.EVT_C_FIND, handle_find, [instance_dir, db_path, args, APP_LOGGER]))
    upsscp.handlers.append((evt.EVT_N_GET, handle_nget, [db_path, args, APP_LOGGER]))
    upsscp.handlers.append((evt.EVT_N_ACTION, handle_naction, [instance_dir, db_path, args, APP_LOGGER]))
    upsscp.handlers.append((evt.EVT_N_CREATE, handle_ncreate, [instance_dir, db_path, args, APP_LOGGER]))
    upsscp.handlers.append((evt.EVT_N_SET, handle_nset, [db_path, args, APP_LOGGER]))

    # Listen for incoming association requests
    upsscp.run()
    # Ensure that the SCP gets shut down when the application exits.
    atexit.register(upsscp.stop)
    # Keep the main application running
    try:
        while loop_forever:
            time.sleep(1)  # Sleep to prevent high CPU usage
    except KeyboardInterrupt:
        APP_LOGGER.info("Shutting down the DICOM Verification + UPS SCP...")
        loop_forever = False


if __name__ == "__main__":
    main()
