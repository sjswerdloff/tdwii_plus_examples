#!/usr/bin/env python
"""A Verification SCP and N_EVENT_REPORT receiver application."""

import argparse
import os
import sys
from configparser import ConfigParser

import pydicom.config
from pynetdicom import (
    AE,
    ALL_TRANSFER_SYNTAXES,
    UnifiedProcedurePresentationContexts,
    _config,
    _handlers,
    evt,
)
from pynetdicom.apps.common import setup_logging
from pynetdicom.sop_class import Verification
from pynetdicom.utils import set_ae

from nevent_receiver_handlers import handle_echo, handle_nevent

# Use `None` for empty values
pydicom.config.use_none_as_empty_text_VR_value = True
# Don't log identifiers
_config.LOG_RESPONSE_IDENTIFIERS = False


# Override the standard logging handlers
def _dont_log(event):
    pass


_handlers._send_c_find_rsp = _dont_log
_handlers._send_c_get_rsp = _dont_log
_handlers._send_c_move_rsp = _dont_log
_handlers._send_c_store_rq = _dont_log
_handlers._recv_c_store_rsp = _dont_log


__version__ = "0.1.0"


def _log_config(config, logger):
    """Log the configuration settings.

    Parameters
    ----------
    logger : logging.Logger
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


def _setup_argparser():
    """Setup the command line arguments"""
    # Description
    parser = argparse.ArgumentParser(
        description=(
            "The nevent_receiver application implements a Service Class Provider (SCP) "
            "for the Verification and Unified Procedure Step Service "
            "Classes."
        ),
        usage="nevent_receiver [options]",
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
    fpath = os.path.join(fdir, "nevent_receiver_default.ini")
    gen_opts.add_argument(
        "-c",
        "--config",
        metavar="[f]ilename",
        help="use configuration file f",
        default=fpath,
    )

    net_opts = parser.add_argument_group("Networking Options")
    net_opts.add_argument(
        "--port",
        help="override the configured TCP/IP listen port number",
    )
    net_opts.add_argument(
        "-aet",
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
        "-ba",
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
        help=("remove all entries from the database and delete the " "corresponding stored instances"),
        action="store_true",
    )

    return parser.parse_args()


def nevent_cb(**kwargs):
    logger = None
    if "logger" in kwargs.keys():
        logger = kwargs["logger"]
    if logger:
        logger.info("nevent_cb invoked")
    event_type_id = 0  # not a valid type ID
    if logger:
        logger.info("TODO: Invoke application response appropriate to content of N-EVENT-REPORT-RQ")
    if "type_id" in kwargs.keys():
        event_type_id = kwargs["type_id"]
        if logger:
            logger.info(f"Event Type ID is: {event_type_id}")
    if "information_ds" in kwargs.keys():
        information_ds = kwargs["information_ds"]
        if logger:
            logger.info("Dataset in N-EVENT-REPORT-RQ: ")
            logger.info(f"{information_ds}")
    # TODO: replace if/elif with dict of {event_type_id,application_response_functions}
    if event_type_id == 1:
        if logger:
            logger.info("UPS State Report")
            logger.info("Probably time to do a C-FIND-RQ")
    elif event_type_id == 2:
        if logger:
            logger.info("UPS Cancel Request")
    elif event_type_id == 3:
        if logger:
            logger.info("UPS Progress Report")
            logger.info("Probably time to see if the Beam (number) changed, or if adaptation is taking or took place")
    elif event_type_id == 4:
        if logger:
            logger.info("SCP Status Change")
            logger.info(
                "Probably a good time to check if this is a Cold Start and then re-subscribe \
                    for specific UPS instances if this application has/had instance specific subscriptions"
            )
    elif event_type_id == 5:
        if logger:
            logger.info("UPS Assigned")
            logger.info(
                "Not too interesting for TDW-II, UPS are typically assigned at the time of scheduling, \
                    but a matching class of machines might make for a different approach"
            )
    else:
        if logger:
            logger.warning(f"Unknown Event Type ID: {event_type_id}")


def main(args=None):
    """Run the application."""
    if args is not None:
        sys.argv = args

    args = _setup_argparser()

    if args.version:
        print(f"nevent_receiver.py v{__version__}")
        sys.exit()

    APP_LOGGER = setup_logging(args, "nevent_receiver")
    APP_LOGGER.debug(f"nevent_receiver.py v{__version__}")
    APP_LOGGER.debug("")

    APP_LOGGER.debug("Using configuration from:")
    APP_LOGGER.debug(f"  {args.config}")
    APP_LOGGER.debug("")
    config = ConfigParser()
    config.read(args.config)

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

    # Log configuration settings
    _log_config(config, APP_LOGGER)
    app_config = config["DEFAULT"]

    dests = {}
    for ae_title in config.sections():
        dest = config[ae_title]
        # Convert to bytes and validate the AE title
        ae_title = set_ae(ae_title, "ae_title", False, False)
        dests[ae_title] = (dest["address"], dest.getint("port"))

    # Use default or specified configuration file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    instance_dir = os.path.join(current_dir, app_config["instance_location"])
    # db_path = os.path.join(current_dir, app_config["database_location"])

    # Clean up the database and storage directory
    if args.clean:
        response = input(
            "This will delete all instances from both the storage directory "
            "and the database. Are you sure you wish to continue? [yes/no]: "
        )
        if response != "yes":
            sys.exit()

        # if clean(db_path, instance_dir, APP_LOGGER):
        #     sys.exit()
        # else:
        #     sys.exit(1)

    # Try to create the instance storage directory
    os.makedirs(instance_dir, exist_ok=True)

    ae = AE(app_config["ae_title"])
    ae.maximum_pdu_size = app_config.getint("max_pdu")
    ae.acse_timeout = app_config.getfloat("acse_timeout")
    ae.dimse_timeout = app_config.getfloat("dimse_timeout")
    ae.network_timeout = app_config.getfloat("network_timeout")

    # Add supported presentation contexts
    # Verification SCP
    ae.add_supported_context(Verification, ALL_TRANSFER_SYNTAXES)

    # # Storage SCP - support all transfer syntaxes
    # for cx in AllStoragePresentationContexts:
    #     ae.add_supported_context(
    #         cx.abstract_syntax, ALL_TRANSFER_SYNTAXES, scp_role=True, scu_role=False
    #     )

    # # Query/Retrieve SCP
    # ae.add_supported_context(PatientRootQueryRetrieveInformationModelFind)
    # ae.add_supported_context(PatientRootQueryRetrieveInformationModelMove)
    # ae.add_supported_context(PatientRootQueryRetrieveInformationModelGet)
    # ae.add_supported_context(StudyRootQueryRetrieveInformationModelFind)
    # ae.add_supported_context(StudyRootQueryRetrieveInformationModelMove)
    # ae.add_supported_context(StudyRootQueryRetrieveInformationModelGet)

    # Unified Procedure Step SCP
    for cx in UnifiedProcedurePresentationContexts:
        ae.add_supported_context(cx.abstract_syntax, ALL_TRANSFER_SYNTAXES, scp_role=True, scu_role=False)

    APP_LOGGER.info(f"Configured for instance_dir = {instance_dir}")
    # Set our handler bindings
    handlers = [
        (evt.EVT_C_ECHO, handle_echo, [args, APP_LOGGER]),
        # (evt.EVT_C_FIND, handle_find, [instance_dir, args, APP_LOGGER]),
        # (evt.EVT_C_GET, handle_get, [db_path, args, APP_LOGGER]),
        # (evt.EVT_C_MOVE, handle_move, [dests, db_path, args, APP_LOGGER]),
        # (evt.EVT_C_STORE, handle_store, [instance_dir, db_path, args, APP_LOGGER]),
        # (evt.EVT_N_GET, handle_nget, [db_path, args, APP_LOGGER]),
        # (evt.EVT_N_ACTION, handle_naction, [db_path, args, APP_LOGGER]),
        (evt.EVT_N_EVENT_REPORT, handle_nevent, [nevent_cb, args, APP_LOGGER]),
        # (evt.EVT_N_SET, handle_nset, [db_path, args, APP_LOGGER]),
    ]

    # Listen for incoming association requests
    ae.start_server((app_config["bind_address"], app_config.getint("port")), evt_handlers=handlers)


if __name__ == "__main__":
    main()
