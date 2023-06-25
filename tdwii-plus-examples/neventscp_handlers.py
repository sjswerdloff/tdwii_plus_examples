"""Event handlers for neventscp.py"""
import os
from io import BytesIO
from pathlib import Path

from pydicom import Dataset, dcmread
from pynetdicom.dimse_primitives import N_ACTION
from pynetdicom.dsutils import encode
from pynetdicom.sop_class import (
    UnifiedProcedureStepPull,
    UnifiedProcedureStepPush,
    UPSFilteredGlobalSubscriptionInstance,
    UPSGlobalSubscriptionInstance,
)
from recursive_print_ds import print_ds
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_ups_instances = dict()

_global_subscribers = (
    dict()
)  # AE Title and delection lock boolean "TRUE" or "FALSE" is the text representation
_filtered_subscribers = dict()  # AE Title and the Dataset acting as the query filter


def _add_global_subscriber(
    subscriber_ae_title: str, deletion_lock: bool = False, logger=None
):
    if subscriber_ae_title not in _global_subscribers.keys():
        _global_subscribers[subscriber_ae_title] = deletion_lock
        if logger is not None:
            logger.debug(f"Receiving AE Title {subscriber_ae_title} is now subscribed")
    else:
        if logger is not None:
            logger.info(
                f"Receiving AE Title {subscriber_ae_title} is already subscribed"
            )
    return


def _add_filtered_subscriber(subscriber_ae_title: str, query: Dataset, logger=None):
    if subscriber_ae_title not in _filtered_subscribers.keys():
        _filtered_subscribers[
            subscriber_ae_title
        ] = query  # and you can get the deletion lock from the query
        if logger is not None:
            logger.debug(f"Receiving AE Title {subscriber_ae_title} is now subscribed")
    else:
        if logger is not None:
            logger.info(
                f"Receiving AE Title {subscriber_ae_title} is already subscribed, only supporting one kind of filter per receiving AE"
            )
    return


def _remove_global_subscriber(
    subscriber_ae_title: str, deletion_lock: bool = False, logger=None
):
    if subscriber_ae_title in _global_subscribers.keys():
        del _global_subscribers[subscriber_ae_title]
    else:
        if logger is not None:
            logger.info(f"Receiving AE Title {subscriber_ae_title} was not subscribed")
    return


def _remove_filtered_subscriber(
    subscriber_ae_title: str, query: Dataset = None, logger=None
):
    if subscriber_ae_title in _filtered_subscribers.keys():
        del _filtered_subscribers[subscriber_ae_title]
    else:
        if logger is not None:
            logger.info(f"Receiving AE Title {subscriber_ae_title} was not subscribed")
    return


def _add_ups_instance(ds: Dataset):
    sopInstanceUID = str(ds.SOPInstanceUID)
    if sopInstanceUID not in _ups_instances.keys():
        _ups_instances[sopInstanceUID] = ds


def _remove_ups_instance(ds: Dataset):
    sopInstanceUID = str(ds.SOPInstanceUID)
    if sopInstanceUID in _ups_instances.keys():
        del _ups_instances[sopInstanceUID]


def _ups_is_match_for_query(query: Dataset, ups: Dataset) -> bool:
    """Determine if a given UPS is a match for the query
    This would be much better done by having rows in a database and using a SQL query
    instead of iterating through each UPS
    But this is a reasonable approach for a simple test bed

    Args:
        query (Dataset): The UPS C-FIND-RQ
        ups (Dataset): The actual UPS (SCHEDULED or otherwise )

    Returns:
        bool: whether the UPS matched the query
    """
    if not machine_name_matches(query, ups):
        return False
    if not procedure_step_state_matches(query, ups):
        return False
    # TODO: add more checks.
    # DateTime Range is common.
    # So is ScheduledWorkitemCodeSequence[0].CodeValue e.g. 121726 in combination with CodingSchemeDesignator
    # (i.e. is this "RT Treatment With Internal Verification")
    """
        (0040,4018) SQ (Sequence with explicit length #=1)      #  82, 1 ScheduledWorkitemCodeSequence
        (fffe,e000) na (Item with explicit length #=3)          #  74, 1 Item
            (0008,0100) SH [121726]                                 #   6, 1 CodeValue
            (0008,0102) SH [DCM]                                    #   4, 1 CodingSchemeDesignator
            (0008,0104) LO [RT Treatment with Internal Verification] #  40, 1 CodeMeaning
        (fffe,e00d) na (ItemDelimitationItem for re-encoding)   #   0, 0 ItemDelimitationItem
        (fffe,e0dd) na (SequenceDelimitationItem for re-encod.) #   0, 0 SequenceDelimitationItem
    """
    return True


def procedure_step_state_matches(query, ups):
    is_match = True  # until it's false?
    requested_step_status = get_procedure_step_state_from_ups(query)
    ups_step_status = get_procedure_step_state_from_ups(ups)
    if requested_step_status is not None and len(requested_step_status) > 0:
        if requested_step_status != ups_step_status:
            is_match = False
    return is_match


def machine_name_matches(query, ups):
    requested_machine_name = get_machine_name_from_ups(query)
    scheduled_machine_name = get_machine_name_from_ups(ups)
    if requested_machine_name is not None and len(requested_machine_name) > 0:
        if scheduled_machine_name != requested_machine_name:
            return False
    return True


def get_machine_name_from_ups(query):
    seq = query.ScheduledStationNameCodeSequence
    if seq is not None:
        for item_index in range(len(seq)):
            machine_name = seq[item_index].CodeValue
    return machine_name


def get_procedure_step_state_from_ups(query):
    step_status = query.ProcedureStepState
    return step_status


def _search_ups(query_as_ds: Dataset):
    # TODO:  actually try to match instead of sending everything back as a match
    for ups in _ups_instances.values():
        if _ups_is_match_for_query(query_as_ds, ups):
            yield ups


def _number_of_matching_ups(query_as_ds: Dataset):
    number_of_matches = 0
    for ups in _ups_instances.values():
        if _ups_is_match_for_query(query_as_ds, ups):
            number_of_matches += 1
    return number_of_matches


def handle_echo(event, cli_config, logger):
    """Handler for evt.EVT_C_ECHO.

    Parameters
    ----------
    event : events.Event
        The corresponding event.
    cli_config : dict
        A :class:`dict` containing configuration settings passed via CLI.
    logger : logging.Logger
        The application's logger.

    Returns
    -------
    int
        The status of the C-ECHO operation, always ``0x0000`` (Success).
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(f"Received C-ECHO request from {addr}:{port} at {timestamp}")

    return 0x0000


def handle_find(event, instance_dir, cli_config, logger):
    """Handler for evt.EVT_C_FIND.

    Parameters
    ----------
    event : pynetdicom.events.Event
        The C-FIND request :class:`~pynetdicom.events.Event`.
    db_path : str
        The database path to use with create_engine().
    cli_config : dict
        A :class:`dict` containing configuration settings passed via CLI.
    logger : logging.Logger
        The application's logger.

    Yields
    ------
    int or pydicom.dataset.Dataset, pydicom.dataset.Dataset or None
        The C-FIND response's *Status* and if the *Status* is pending then
        the dataset to be sent, otherwise ``None``.
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(f"Received C-FIND request from {addr}:{port} at {timestamp}")

    model = event.request.AffectedSOPClassUID
    db_path = None
    _reload_ups_instances(instance_dir, logger)

    if model.keyword in ("UnifiedProcedureStepPull",):
        query = (
            event.identifier
        )  # the identifier is not available through event multiple times.  so get it copied to a local variable
        matches = _search_ups(query)
        for response in matches:
            yield 0xFF00, response
        yield 0x0000, None
    else:
        engine = create_engine(db_path)
        with engine.connect() as conn:
            Session = sessionmaker(bind=engine)
            session = Session()
            # Search database using Identifier as the query
            try:
                matches = search(model, event.identifier, session)

            except InvalidIdentifier as exc:
                session.rollback()
                logger.error("Invalid C-FIND Identifier received")
                logger.error(str(exc))
                yield 0xA900, None
                return
            except Exception as exc:
                session.rollback()
                logger.error("Exception occurred while querying database")
                logger.exception(exc)
                yield 0xC320, None
                return
            finally:
                session.close()

        # Yield results
        for match in matches:
            if event.is_cancelled:
                yield 0xFE00, None
                return

            try:
                response = match.as_identifier(event.identifier, model)
                response.RetrieveAETitle = event.assoc.ae.ae_title
            except Exception as exc:
                logger.error("Error creating response Identifier")
                logger.exception(exc)
                yield 0xC322, None

            yield 0xFF00, response


def _reload_ups_instances(instance_dir, logger):
    # TODO: Find a more elegant way to handle these UPS instances
    #       and maybe allow reload if updated
    #       right now, it's just loading the first time through, and done.
    ups_instance_list = []
    logger.info(f"# UPS Instances currently loaded = {len(_ups_instances)}")
    if len(_ups_instances) == 0:
        p = Path(instance_dir)
        list_of_dcm_ups = [x for x in p.glob("UPS_*.dcm")]

        try:
            for filename in list_of_dcm_ups:
                ups = dcmread(filename, force=True)
                ups_instance_list.append(ups)
                logger.info(f"Loaded UPS from {filename}")
        except:
            logger.warn(f"Unable to load UPS from {filename}")

    for ups in ups_instance_list:
        _add_ups_instance(ups)
    logger.info(f"# UPS Instances loaded from {instance_dir} = {len(_ups_instances)}")


def handle_get(event, db_path, cli_config, logger):
    """Handler for evt.EVT_C_GET.

    Parameters
    ----------
    event : pynetdicom.events.Event
        The C-GET request :class:`~pynetdicom.events.Event`.
    db_path : str
        The database path to use with create_engine().
    cli_config : dict
        A :class:`dict` containing configuration settings passed via CLI.
    logger : logging.Logger
        The application's logger.

    Yields
    ------
    int
        The number of sub-operations required to complete the request.
    int or pydicom.dataset.Dataset, pydicom.dataset.Dataset or None
        The C-GET response's *Status* and if the *Status* is pending then
        the dataset to be sent, otherwise ``None``.
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(f"Received C-GET request from {addr}:{port} at {timestamp}")

    model = event.request.AffectedSOPClassUID

    engine = create_engine(db_path)
    with engine.connect() as conn:
        Session = sessionmaker(bind=engine)
        session = Session()
        # Search database using Identifier as the query
        try:
            matches = search(model, event.identifier, session)
        except InvalidIdentifier as exc:
            session.rollback()
            logger.error("Invalid C-GET Identifier received")
            logger.error(str(exc))
            yield 0xA900, None
            return
        except Exception as exc:
            session.rollback()
            logger.error("Exception occurred while querying database")
            logger.exception(exc)
            yield 0xC420, None
            return
        finally:
            session.close()

    # Yield number of sub-operations
    yield len(matches)

    # Yield results
    for match in matches:
        if event.is_cancelled:
            yield 0xFE00, None
            return

        try:
            ds = dcmread(match.filename)
        except Exception as exc:
            logger.error(f"Error reading file: {match.filename}")
            logger.exception(exc)
            yield 0xC421, None

        yield 0xFF00, ds


def handle_move(event, destinations, db_path, cli_config, logger):
    """Handler for evt.EVT_C_MOVE.

    Parameters
    ----------
    event : pynetdicom.events.Event
        The C-MOVE request :class:`~pynetdicom.events.Event`.
    destinations : dict
        A :class:`dict` containing know move destinations as
        ``{b'AE_TITLE: (addr, port)}``
    db_path : str
        The database path to use with create_engine().
    cli_config : dict
        A :class:`dict` containing configuration settings passed via CLI.
    logger : logging.Logger
        The application's logger.

    Yields
    ------
    (str, int) or (None, None)
        The (IP address, port) of the *Move Destination* (if known).
    int
        The number of sub-operations required to complete the request.
    int or pydicom.dataset.Dataset, pydicom.dataset.Dataset or None
        The C-MOVE response's *Status* and if the *Status* is pending then
        the dataset to be sent, otherwise ``None``.
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(
        f"Received C-MOVE request from {addr}:{port} at {timestamp} "
        f"with move destination {event.move_destination}"
    )

    # Unknown `Move Destination`
    try:
        addr, port = destinations[event.move_destination]
    except KeyError:
        logger.info("No matching move destination in the configuration")
        yield None, None
        return

    model = event.request.AffectedSOPClassUID
    engine = create_engine(db_path)
    with engine.connect() as conn:
        Session = sessionmaker(bind=engine)
        session = Session()
        # Search database using Identifier as the query
        try:
            matches = search(model, event.identifier, session)
        except InvalidIdentifier as exc:
            session.rollback()
            logger.error("Invalid C-MOVE Identifier received")
            logger.error(str(exc))
            yield 0xA900, None
            return
        except Exception as exc:
            session.rollback()
            logger.error("Exception occurred while querying database")
            logger.exception(exc)
            yield 0xC520, None
            return
        finally:
            session.close()

    # Yield `Move Destination` IP and port, plus required contexts
    # We should be able to reduce the number of contexts by using the
    # implicit context conversion between:
    #   implicit VR <-> explicit VR <-> deflated transfer syntaxes
    contexts = list(set([ii.context for ii in matches]))
    yield addr, port, {"contexts": contexts[:128]}

    # Yield number of sub-operations
    yield len(matches)

    # Yield results
    for match in matches:
        if event.is_cancelled:
            yield 0xFE00, None
            return

        try:
            ds = dcmread(match.filename)
        except Exception as exc:
            logger.error(f"Error reading file: {match.filename}")
            logger.exception(exc)
            yield 0xC521, None

        yield 0xFF00, ds


def handle_store(event, storage_dir, db_path, cli_config, logger):
    """Handler for evt.EVT_C_STORE.

    Parameters
    ----------
    event : pynetdicom.events.Event
        The C-STORE request :class:`~pynetdicom.events.Event`.
    storage_dir : str
        The path to the directory where instances will be stored.
    db_path : str
        The database path to use with create_engine().
    cli_config : dict
        A :class:`dict` containing configuration settings passed via CLI.
    logger : logging.Logger
        The application's logger.

    Returns
    -------
    int or pydicom.dataset.Dataset
        The C-STORE response's *Status*. If the storage operation is successful
        but the dataset couldn't be added to the database then the *Status*
        will still be ``0x0000`` (Success).
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(f"Received C-STORE request from {addr}:{port} at {timestamp}")

    try:
        ds = event.dataset
        # Remove any Group 0x0002 elements that may have been included
        ds = ds[0x00030000:]
        sop_instance = ds.SOPInstanceUID
    except Exception as exc:
        logger.error("Unable to decode the dataset")
        logger.exception(exc)
        # Unable to decode dataset
        return 0xC210

    # Add the file meta information elements - must be before adding to DB
    ds.file_meta = event.file_meta

    logger.info(f"SOP Instance UID '{sop_instance}'")

    # Try and add the instance to the database
    #   If we fail then don't even try to store
    fpath = os.path.join(storage_dir, sop_instance)

    if os.path.exists(fpath):
        logger.warning("Instance already exists in storage directory, overwriting")

    try:
        ds.save_as(fpath, write_like_original=False)
    except Exception as exc:
        logger.error("Failed writing instance to storage directory")
        logger.exception(exc)
        # Failed - Out of Resources
        return 0xA700

    logger.info("Instance written to storage directory")

    # Dataset successfully written, try to add to/update database
    engine = create_engine(db_path)
    with engine.connect() as conn:
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # Path is relative to the database file
            matches = (
                session.query(Instance)
                .filter(Instance.sop_instance_uid == ds.SOPInstanceUID)
                .all()
            )
            add_instance(ds, session, os.path.abspath(fpath))
            if not matches:
                logger.info("Instance added to database")
            else:
                logger.info("Database entry for instance updated")
        except Exception as exc:
            session.rollback()
            logger.error("Unable to add instance to the database")
            logger.exception(exc)
        finally:
            session.close()

    return 0x0000


def handle_nget(event, db_path, cli_config, logger):
    """Handler for evt.EVT_C_GET.

    Parameters
    ----------
    event : pynetdicom.events.Event
        The C-GET request :class:`~pynetdicom.events.Event`.
    db_path : str
        The database path to use with create_engine().
    cli_config : dict
        A :class:`dict` containing configuration settings passed via CLI.
    logger : logging.Logger
        The application's logger.

    Yields
    ------
    int
        The number of sub-operations required to complete the request.
    int or pydicom.dataset.Dataset, pydicom.dataset.Dataset or None
        The C-GET response's *Status* and if the *Status* is pending then
        the dataset to be sent, otherwise ``None``.
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(f"Received C-GET request from {addr}:{port} at {timestamp}")

    model = event.request.AffectedSOPClassUID

    engine = create_engine(db_path)
    with engine.connect() as conn:
        Session = sessionmaker(bind=engine)
        session = Session()
        # Search database using Identifier as the query
        try:
            matches = search(model, event.identifier, session)
        except InvalidIdentifier as exc:
            session.rollback()
            logger.error("Invalid C-GET Identifier received")
            logger.error(str(exc))
            yield 0xA900, None
            return
        except Exception as exc:
            session.rollback()
            logger.error("Exception occurred while querying database")
            logger.exception(exc)
            yield 0xC420, None
            return
        finally:
            session.close()

    # Yield number of sub-operations
    yield len(matches)

    # Yield results
    for match in matches:
        if event.is_cancelled:
            yield 0xFE00, None
            return

        try:
            ds = dcmread(match.filename)
        except Exception as exc:
            logger.error(f"Error reading file: {match.filename}")
            logger.exception(exc)
            yield 0xC421, None

        yield 0xFF00, ds


def handle_naction(event, db_path, cli_config, logger):
    """Handler for evt.EVT_N_ACTION

    Parameters
    ----------
    event : pynetdicom.events.Event
        The N-ACTION request :class:`~pynetdicom.events.Event`.
    db_path : str
        The database path to use with create_engine().
    cli_config : dict
        A :class:`dict` containing configuration settings passed via CLI.
    logger : logging.Logger
        The application's logger.

    Yields
    ------
    int
        The number of sub-operations required to complete the request.
    int or pydicom.dataset.Dataset, pydicom.dataset.Dataset or None
        The C-GET response's *Status* and if the *Status* is pending then
        the dataset to be sent, otherwise ``None``.
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(f"Received N-ACTION request from {addr}:{port} at {timestamp}")

    # model = event.request.AffectedSOPClassUID
    # logger.info(f"Model = {model}")
    # logger.info(f"Event = {event}")
    # logger.info(f"Action Information:")
    # logger.info(f"{event.action_information}")

    naction_primitive = event.request
    # pynetdicom.dimse_primitives.N_ACTION
    """"
    +------------------------------------------+---------+----------+
    | Parameter                                | Req/ind | Rsp/conf |
    +==========================================+=========+==========+
    | Message ID                               | M       | \-       |
    +------------------------------------------+---------+----------+
    | Message ID Being Responded To            | \-      | M        |
    +------------------------------------------+---------+----------+
    | Requested SOP Class UID                  | M       | \-       |
    +------------------------------------------+---------+----------+
    | Requested SOP Instance UID               | M       | \-       |
    +------------------------------------------+---------+----------+
    | Action Type ID                           | M       | C(=)     |
    +------------------------------------------+---------+----------+
    | Action Information                       | U       | \-       |
    +------------------------------------------+---------+----------+
    | Affected SOP Class UID                   | \-      | U        |
    +------------------------------------------+---------+----------+
    | Affected SOP Instance UID                | \-      | U        |
    +------------------------------------------+---------+----------+
    | Action Reply                             | \-      | C        |
    +------------------------------------------+---------+----------+
    | Status                                   | \-      | M        |
    +------------------------------------------+---------+----------+
    """
    action_type_id = naction_primitive.ActionTypeID
    action_information = dcmread(naction_primitive.ActionInformation, force=True)

    if action_information is not None:
        try:
            logger.info(f"{action_information}")
            subscribing_ae_title = action_information.ReceivingAE
            deletion_lock = action_information.DeletionLock == "TRUE"
        except AttributeError as exc:
            logger.error(f"Error in decoding subscriber information: {exc}")
        finally:
            subscribing_ae_title = None
            deletion_lock = False

    # TODO:  use action_type_id to determine if this is subscribe or unsubscribe
    if naction_primitive.RequestedSOPInstanceUID == UPSGlobalSubscriptionInstance:
        logger.info("Request was for Subscribing to (unfiltered) Global UPS")
        if action_type_id == 3:
            _add_global_subscriber(
                subscribing_ae_title, deletion_lock=deletion_lock, logger=logger
            )
        elif action_type_id == 4:
            _remove_global_subscriber(subscribing_ae_title, logger=logger)
    elif (
        naction_primitive.RequestedSOPInstanceUID
        == UPSFilteredGlobalSubscriptionInstance
    ):
        logger.info("Request was for Subscribing to Filtered Global UPS")
        if action_type_id == 3:
            _add_filtered_subscriber(subscribing_ae_title, action_information)
        elif action_type_id == 4:
            _remove_filtered_subscriber(subscribing_ae_title)

    logger.info(f"Requested SOP Class UID: {naction_primitive.RequestedSOPClassUID}")
    logger.info(f"Request dump: {naction_primitive}")

    response = Dataset()
    # rsp = N_ACTION()
    # rsp.AffectedSOPClassUID = naction_primitive.RequestedSOPClassUID
    # rsp.AffectedSOPInstanceUID = naction_primitive.RequestedSOPInstanceUID
    # rsp.RequestedSOPClassUID = naction_primitive.RequestedSOPClassUID
    # rsp.RequestedSOPInstanceUID = naction_primitive.RequestedSOPInstanceUID

    response.AffectedSOPClassUID = naction_primitive.RequestedSOPClassUID
    response.AffectedSOPInstanceUID = naction_primitive.RequestedSOPInstanceUID
    response.RequestedSOPClassUID = naction_primitive.RequestedSOPClassUID
    response.RequestedSOPInstanceUID = naction_primitive.RequestedSOPInstanceUID
    response.action_type = event.action_type
    response.action_information = None
    response.action_reply = None
    response.status = 0x0000
    response.is_little_endian = True
    response.is_implicit_VR = True
    response.is_decompressed = False

    # bytestream = encode(
    #             rsp,
    #             True,
    #             True,
    #             False
    #         )
    # response.action_reply = BytesIO(bytestream)

    # matches = [response]
    # yield len(matches)

    # # Yield results
    # for match in matches:
    #     if event.is_cancelled:
    #         yield 0xFE00, None
    #         return

    #     try:
    #         ds = dcmread(match.filename)
    #     except Exception as exc:
    #         logger.error(f"Error reading file: {match.filename}")
    #         logger.exception(exc)
    #         yield 0xC421, None

    return 0x0000, response


def handle_nevent(event, event_response_cb, cli_config, logger):
    """Handler for evt.EVT_N_EVENT.

    Parameters
    ----------
    event : pynetdicom.events.Event
        The N-EVENT request :class:`~pynetdicom.events.Event`.
    event_response_cb : function
        The function to call when receiving an Event (that is a UPS Event).
    cli_config : dict
        A :class:`dict` containing configuration settings passed via CLI.
    logger : logging.Logger
        The application's logger.

    Yields
    ------
    int
        The number of sub-operations required to complete the request.
    int or pydicom.dataset.Dataset, pydicom.dataset.Dataset or None
        The C-GET response's *Status* and if the *Status* is pending then
        the dataset to be sent, otherwise ``None``.
    """

    nevent_primitive = event.request
    r"""Represents a N-EVENT-REPORT primitive.

    +------------------------------------------+---------+----------+
    | Parameter                                | Req/ind | Rsp/conf |
    +==========================================+=========+==========+
    | Message ID                               | M       | \-       |
    +------------------------------------------+---------+----------+
    | Message ID Being Responded To            | \-      | M        |
    +------------------------------------------+---------+----------+
    | Affected SOP Class UID                   | M       | U(=)     |
    +------------------------------------------+---------+----------+
    | Affected SOP Instance UID                | M       | U(=)     |
    +------------------------------------------+---------+----------+
    | Event Type ID                            | M       | C(=)     |
    +------------------------------------------+---------+----------+
    | Event Information                        | U       | \-       |
    +------------------------------------------+---------+----------+
    | Event Reply                              | \-      | C        |
    +------------------------------------------+---------+----------+
    | Status                                   | \-      | M        |
    +------------------------------------------+---------+----------+

    | (=) - The value of the parameter is equal to the value of the parameter
      in the column to the left
    | C - The parameter is conditional.
    | M - Mandatory
    | MF - Mandatory with a fixed value
    | U - The use of this parameter is a DIMSE service user option
    | UF - User option with a fixed value

    Attributes
    ----------
    MessageID : int
        Identifies the operation and is used to distinguish this
        operation from other notifications or operations that may be in
        progress. No two identical values for the Message ID shall be used for
        outstanding operations.
    MessageIDBeingRespondedTo : int
        The Message ID of the operation request/indication to which this
        response/confirmation applies.
    AffectedSOPClassUID : pydicom.uid.UID, bytes or str
        For the request/indication this specifies the SOP Class for
        storage. If included in the response/confirmation, it shall be equal
        to the value in the request/indication
    Status : int
        The error or success notification of the operation.
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(f"Received N-EVENT request from {addr}:{port} at {timestamp}")

    model = event.request.AffectedSOPClassUID
    nevent_type_id = nevent_primitive.EventTypeID
    nevent_information = dcmread(nevent_primitive.EventInformation, force=True)
    nevent_rsp_primitive = nevent_primitive
    nevent_rsp_primitive.Status = 0x0000

    logger.info(f"Event Information: {nevent_information}")

    if model.keyword in ["UnifiedProcedureStepPush"]:
        event_response_cb(
            type_id=nevent_type_id, information_ds=nevent_information, logger=logger
        )
    else:
        logger.warning(
            f"Received model.keyword = {model.keyword} with AffectedSOPClassUID = {model}"
        )
        logger.warning(f"Not a UPS Event")

    logger.info(f"Finished Processing N-EVENT-REPORT-RQ")
    yield 0  # Number of suboperations remaining
    yield 0  # Status.  If a rsp dataset of None is provided, the underlying handler and dimse primitive in pynetdicom raises an error


def handle_nset(event, db_path, cli_config, logger):
    """Handler for evt.EVT_C_GET.

    Parameters
    ----------
    event : pynetdicom.events.Event
        The C-GET request :class:`~pynetdicom.events.Event`.
    db_path : str
        The database path to use with create_engine().
    cli_config : dict
        A :class:`dict` containing configuration settings passed via CLI.
    logger : logging.Logger
        The application's logger.

    Yields
    ------
    int
        The number of sub-operations required to complete the request.
    int or pydicom.dataset.Dataset, pydicom.dataset.Dataset or None
        The C-GET response's *Status* and if the *Status* is pending then
        the dataset to be sent, otherwise ``None``.
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(f"Received C-GET request from {addr}:{port} at {timestamp}")

    model = event.request.AffectedSOPClassUID

    engine = create_engine(db_path)
    with engine.connect() as conn:
        Session = sessionmaker(bind=engine)
        session = Session()
        # Search database using Identifier as the query
        try:
            matches = search(model, event.identifier, session)
        except InvalidIdentifier as exc:
            session.rollback()
            logger.error("Invalid C-GET Identifier received")
            logger.error(str(exc))
            yield 0xA900, None
            return
        except Exception as exc:
            session.rollback()
            logger.error("Exception occurred while querying database")
            logger.exception(exc)
            yield 0xC420, None
            return
        finally:
            session.close()

    # Yield number of sub-operations
    yield len(matches)

    # Yield results
    for match in matches:
        if event.is_cancelled:
            yield 0xFE00, None
            return

        try:
            ds = dcmread(match.filename)
        except Exception as exc:
            logger.error(f"Error reading file: {match.filename}")
            logger.exception(exc)
            yield 0xC421, None

        yield 0xFF00, ds
