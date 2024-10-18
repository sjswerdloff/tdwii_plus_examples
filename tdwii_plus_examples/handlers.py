"""Event handlers for upsscp.py"""
import copy
import logging
import os

# from io import BytesIO
from pathlib import Path

import pynetdicom

# from pynetdicom.dimse_primitives import N_ACTION
# from pynetdicom.dsutils import encode
import pynetdicom.events
from pydicom import Dataset, dcmread, dcmwrite

# from pydicom.dataset import FileMetaDataset
from pydicom.errors import InvalidDicomError
from pydicom.uid import ExplicitVRLittleEndian
from pynetdicom import AE, UnifiedProcedurePresentationContexts
from pynetdicom.dsutils import decode
from pynetdicom.sop_class import (
    UnifiedProcedureStepPull,
    UnifiedProcedureStepPush,
    UPSFilteredGlobalSubscriptionInstance,
    UPSGlobalSubscriptionInstance,
)

# from recursive_print_ds import print_ds
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tdwii_plus_examples import tdwii_config
from tdwii_plus_examples.upsdb import Instance, InvalidIdentifier, add_instance, search

_SERVICE_STATUS = {
    "SCHEDULED": {
        "SCHEDULED": 0xC303,
        "IN PROGRESS": 0x0000,
        "CANCELED": 0xC310,
        "COMPLETED": 0xC310,
    },
    "IN PROGRESS": {
        "SCHEDULED": 0xC303,
        "IN PROGRESS": 0xC302,
        "CANCELED": 0x0000,
        "COMPLETED": 0x0000,
    },
    "CANCELED": {
        "SCHEDULED": 0xC303,
        "IN PROGRESS": 0xC300,
        "CANCELED": 0xB304,
        "COMPLETED": 0xC300,
    },
    "COMPLETED": {
        "SCHEDULED": 0xC303,
        "IN PROGRESS": 0xC300,
        "CANCELED": 0xC300,
        "COMPLETED": 0xB306,
    },
}
_ups_instances = dict()

_global_subscribers = dict()  # AE Title and delete lock boolean "TRUE" or "FALSE" is the text representation
_filtered_subscribers = dict()  # AE Title and the Dataset acting as the query filter

REMOTE_AE_CONFIG_FILE = "ApplicationEntities.json"
tdwii_config.load_ae_config(REMOTE_AE_CONFIG_FILE)


def _add_global_subscriber(subscriber_ae_title: str, deletion_lock: bool = False, logger=None):
    if subscriber_ae_title not in _global_subscribers.keys():
        _global_subscribers[subscriber_ae_title] = deletion_lock
        if logger is not None:
            logger.debug(f"Receiving AE Title {subscriber_ae_title} is now subscribed globally")
    else:
        if logger is not None:
            logger.info(f"Receiving AE Title {subscriber_ae_title} is already subscribed globally")
    return


def _add_filtered_subscriber(subscriber_ae_title: str, query: Dataset, logger=None):
    if subscriber_ae_title not in _filtered_subscribers.keys():
        _filtered_subscribers[subscriber_ae_title] = query  # and you can get the deletion lock from the query
        if logger is not None:
            logger.debug(f"Receiving AE Title {subscriber_ae_title} is now subscribed using filter: {query}")
    else:
        if logger is not None:
            logger.info(
                f"Receiving AE Title {subscriber_ae_title} is already subscribed, \
                    only supporting one kind of filter per receiving AE"
            )
    return


def _remove_global_subscriber(subscriber_ae_title: str, deletion_lock: bool = False, logger=None):
    if subscriber_ae_title in _global_subscribers.keys():
        del _global_subscribers[subscriber_ae_title]
    else:
        if logger is not None:
            logger.info(f"Receiving AE Title {subscriber_ae_title} was not subscribed")
    return


def _remove_filtered_subscriber(subscriber_ae_title: str, query: Dataset = None, logger=None):
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
        (0xfffe,e000) na (Item with explicit length #=3)          #  74, 1 Item
            (0008,0100) SH [121726]                                 #   6, 1 CodeValue
            (0008,0102) SH [DCM]                                    #   4, 1 CodingSchemeDesignator
            (0008,0104) LO [RT Treatment with Internal Verification] #  40, 1 CodeMeaning
        (0xfffe,e00d) na (ItemDelimitationItem for re-encoding)   #   0, 0 ItemDelimitationItem
        (0xfffe,e0dd) na (SequenceDelimitationItem for re-encoding) #   0, 0 SequenceDelimitationItem
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


def handle_find(event, instance_dir, db_path, cli_config, logger):
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

    # _reload_ups_instances(instance_dir, logger)
    logger.info(f"model: {model}")
    if model in [UnifiedProcedureStepPull, UnifiedProcedureStepPush]:
        #     query = (
        #         event.identifier
        #     )  # the identifier is not available through event multiple times.  so get it copied to a local variable
        #     matches = _search_ups(query)
        #     for response in matches:
        #         yield 0xFF00, response
        #     yield 0x0000, None
        # else:
        engine = create_engine(db_path)
        with engine.connect() as conn:  # noqa:  F841
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
                logger.info(f"match: {match} with SOP Instance UID: {match.sop_instance_uid}")
                response = dcmread(Path(instance_dir).joinpath(str(match.sop_instance_uid)), force=True)
                logger.info(f"response: {response}")
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
        except (FileNotFoundError, InvalidDicomError, TypeError):
            logger.warn(f"Unable to load UPS from {filename}")

    for ups in ups_instance_list:
        _add_ups_instance(ups)
    logger.info(f"# UPS Instances loaded from {instance_dir} = {len(_ups_instances)}")


def handle_nget(event, db_path, cli_config, logger):
    """Handler for evt.EVT_N_GET.
    #TODO This is just copied from C-GET and is probably very wrong
    Parameters
    ----------
    event : pynetdicom.events.Event
        The N-GET request :class:`~pynetdicom.events.Event`.
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
        The N-GET response's *Status* and if the *Status* is pending then
        the dataset to be sent, otherwise ``None``.
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(f"Received N-GET request from {addr}:{port} at {timestamp}")

    model = event.request.RequestedSOPClassUID
    if len(model) == 0:
        print("Requested SOP Class UID not provided")
    # need to manipulate the content of the request
    # also need to validate the content and reject if it's not DICOM conformant and IHE-RO
    # TDW-II profile adherent
    ds_from_request = Dataset()
    # decode(event.request.ModificationList, True, True)
    ds_from_request.SOPInstanceUID = event.request.RequestedSOPInstanceUID
    if ds_from_request.SOPInstanceUID is None or len(ds_from_request.SOPInstanceUID) == 0:
        print("Requested SOP Instance UID is empty")

    engine = create_engine(db_path)
    with engine.connect() as conn:  # noqa:  F841
        Session = sessionmaker(bind=engine)
        session = Session()
        # Search database using Identifier as the query
        try:
            matches = search(model, ds_from_request, session)
        except InvalidIdentifier as exc:
            session.rollback()
            logger.error("Invalid N-GET Identifier received")
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
    # yield len(matches)

    # Yield results
    for match in matches:
        if event.is_cancelled:
            yield 0xFE00, None
            return

        try:
            print(f"N-GET handler: matched on {match.filename}")
            ds = dcmread(match.filename)
            print(ds)
            ds.is_implicit_VR = False
            ds.ensure_file_meta()
            ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
            ds.fix_meta_info()
            ds.Status = 0x0000
        except Exception as exc:
            logger.error(f"Error reading file: {match.filename}")
            logger.exception(exc)
            yield 0xC421, None

        yield 0x0000
        yield ds


def handle_naction(event, instance_dir, db_path, cli_config, logger):
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
    r"""
    +------------------------------------------+---------+----------+
    | Parameter                                | Req/ind | Rsp/conf |
    +==========================================+=========+==========+
    | Message ID                               | M       | \-       | # noqa: W605
    +------------------------------------------+---------+----------+
    | Message ID Being Responded To            | \-      | M        | # noqa: W605
    +------------------------------------------+---------+----------+
    | Requested SOP Class UID                  | M       | \-       | # noqa: W605
    +------------------------------------------+---------+----------+
    | Requested SOP Instance UID               | M       | \-       | # noqa: W605
    +------------------------------------------+---------+----------+
    | Action Type ID                           | M       | C(=)     |
    +------------------------------------------+---------+----------+
    | Action Information                       | U       | \-       | # noqa: W605
    +------------------------------------------+---------+----------+
    | Affected SOP Class UID                   | \-      | U        | # noqa: W605
    +------------------------------------------+---------+----------+
    | Affected SOP Instance UID                | \-      | U        | # noqa: W605
    +------------------------------------------+---------+----------+
    | Action Reply                             | \-      | C        | # noqa: W605
    +------------------------------------------+---------+----------+
    | Status                                   | \-      | M        | # noqa: W605
    +------------------------------------------+---------+----------+
    """
    action_type_id = naction_primitive.ActionTypeID
    action_information = dcmread(naction_primitive.ActionInformation, force=True)
    service_status = 0x0000
    # sub_operations_remaining = 0
    # in case things go wrong
    error_response = Dataset()
    error_response.is_little_endian = True
    error_response.is_implicit_VR = True

    happy_response = Dataset()
    happy_response.Status = service_status  # change this if things go wrong
    # happy_response.update(action_information) # apparently not all elements get to go back in a status dataset

    if action_type_id != 1:
        subscribing_ae_title = None
        deletion_lock = False
        if action_information is not None:
            try:
                logger.info("Action Information:")

                subscribing_ae_title = action_information.ReceivingAE
                deletion_lock = action_information.DeletionLock == "TRUE"
                logger.info(f"{action_information}")
            except AttributeError as exc:
                logger.error(f"Error in decoding subscriber information: {exc}")
                # TODO... service_status = some error code
        else:
            logger.warn("No action information available!")
            # TODO... service_status = some error code

        # TODO:  use action_type_id to determine if this is subscribe or unsubscribe
        if naction_primitive.RequestedSOPInstanceUID == UPSGlobalSubscriptionInstance:
            logger.info("Request was for Subscribing to (unfiltered) Global UPS")
            if action_type_id == 3:
                _add_global_subscriber(subscribing_ae_title, deletion_lock=deletion_lock, logger=logger)
            elif action_type_id == 4:
                _remove_global_subscriber(subscribing_ae_title, logger=logger)
        elif naction_primitive.RequestedSOPInstanceUID == UPSFilteredGlobalSubscriptionInstance:
            logger.info("Request was for Subscribing to Filtered Global UPS")
            if action_type_id == 3:
                _add_filtered_subscriber(subscribing_ae_title, action_information)
            elif action_type_id == 4:
                _remove_filtered_subscriber(subscribing_ae_title)
        yield happy_response
        yield None
        return
    # yield action_information
    else:
        # This is a ProcedureStepState change request...
        engine = create_engine(db_path)
        service_status = 0x0000
        with engine.connect() as conn:  # noqa:  F841
            Session = sessionmaker(bind=engine)
            session = Session()
            model = None
            # Search database using Identifier as the query
            print(f"naction_primitive = {naction_primitive}")
            print(f"action information = {action_information}")

            if model is None:
                try:
                    model = naction_primitive.RequestedSOPClassUID
                except AttributeError:
                    try:
                        model = naction_primitive.AffectedSOPClassUID
                    except AttributeError:
                        raise

            if action_information is not None:
                try:
                    logger.info(f"{action_information}")
                except Exception as exc:
                    logger.info(f"Unable to decode action information: {exc}")
            else:
                logger.info("No action information")

            try:
                search_ds = Dataset()  # (action_information)
                transaction_uid = action_information.TransactionUID
                requested_step_state = action_information.ProcedureStepState
                if "RequestedSOPInstanceUID" in action_information:
                    search_ds.SOPInstanceUID = action_information.RequestedSOPInstanceUID
                else:
                    search_ds.SOPInstanceUID = naction_primitive.RequestedSOPInstanceUID
                # search_ds.SOPClassUID = action_information.RequestedSOPClassUID
                matches = search(model, search_ds, session)
                if matches is None or (len(matches) < 1):
                    error_str = f"No Matching SOP Instance UID: {search_ds.SOPInstanceUID}"
                    logger.error(error_str)
                    session.close()
                    error_response.ErrorComment = error_str[0:59] + " ..."
                    error_response.Status = 0xC307
                    yield error_response
                    yield None
                    return
                if len(matches) > 1:
                    logger.error("Internal Error: More than one match for the given SOP Instance UID")
                match = matches[0]
                current_step_state = match.procedure_step_state
                stored_transaction_uid = match.transaction_uid
                service_status = _SERVICE_STATUS[current_step_state][requested_step_state]

                if transaction_uid is None and current_step_state != "SCHEDULED":
                    logging.error("Transaction UID is None, and current step state is not SCHEDULED")
                elif len(transaction_uid) == 0 and current_step_state != "SCHEDULED":
                    logging.error("Transaction UID is zero length, and current step state is not SCHEDULED")
                elif current_step_state != "SCHEDULED" and str(transaction_uid) != str(stored_transaction_uid):
                    logging.error("Current Step state is not SCHEDULED, but transaction uids don't match")
                    error_message = (
                        f"Provided Transaction UID {transaction_uid}, vs. Stored Transaction UID {stored_transaction_uid}"
                    )
                    logging.error(error_message)

                if (
                    (transaction_uid is None)
                    or (len(transaction_uid) == 0)  # noqa: W503,W504
                    or (current_step_state != "SCHEDULED" and transaction_uid != stored_transaction_uid)  # noqa: W503,W504
                ):
                    service_status = 0xC301
                    error_str = "Transaction UID is missing, zero length, or not valid"
                    error_response.ErrorComment = error_str[:63]
                    logger.error(f"Service Status: 0x{service_status:X}")
                    logger.error(error_str)
                    error_response.Status = service_status
                    # yield service_status
                    yield error_response
                    yield None
                    return

                if service_status != 0x0000:
                    error_response.ErrorComment = f"Current Step State {current_step_state}, \
                        requested Step State {requested_step_state}"
                    logger.error(f"Service Status: 0x{service_status:X}")
                    error_response.Status = service_status
                    # yield service_status
                    yield error_response
                    yield None
                    return
                logger.info(f"Matching instance: {match}")
                logger.info(f"Stored Procedure Step State: {current_step_state}")
                logger.info(f"Requested Procedure Step State: {requested_step_state}")
                response = dcmread(Path(instance_dir).joinpath(str(match.sop_instance_uid)), force=True)
                response.ProcedureStepState = requested_step_state
                response.is_little_endian = True
                response.is_implicit_VR = True
                # Updates to content of database below for next state change request
                match.procedure_step_state = requested_step_state
                match.transaction_uid = transaction_uid
                session.commit()
                # Update to the blob/dicom file.  Probably not as important here, but will be important for N-SET
                dcmwrite(
                    Path(instance_dir).joinpath(str(match.sop_instance_uid)),
                    response,
                    write_like_original=True,
                )
                response.TransactionUID = transaction_uid
                response.Status = service_status
                print(f"response content: {response}")
                yield service_status
                yield response

            except InvalidIdentifier as exc:
                session.rollback()
                logger.error("Invalid N-Action Identifier received")
                logger.error(str(exc))
                yield 0
                yield 0xA900

            except Exception as exc:
                session.rollback()
                logger.error("Exception occurred while querying database")
                logger.exception(exc)
                yield 0
                yield 0xC320

            finally:
                session.close()

    logger.info(f"Requested SOP Class UID: {naction_primitive.RequestedSOPClassUID}")
    logger.info(f"Request dump: {naction_primitive}")

    return


def handle_nset(event: pynetdicom.events.Event, db_path: Path | str, cli_config, logger: logging.Logger):
    """Handler for evt.EVT_N_SET.

    Parameters
    ----------
    event : pynetdicom.events.Event
        The N-SET request :class:`~pynetdicom.events.Event`.
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
        The N-SET response's *Status* and if the *Status* is pending then
        the dataset to be sent, otherwise ``None``.
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(f"Received N-SET request from {addr}:{port} at {timestamp}")
    response_ds = None
    # need to manipulate the content of the request
    # also need to validate the content and reject if it's not DICOM conformant and IHE-RO
    # TDW-II profile adherent
    ds_from_request = decode(event.request.ModificationList, True, True)
    deep_copy_of_request = copy.deepcopy(ds_from_request)
    model = None
    try:
        model = event.request.AffectedSOPClassUID
    except AttributeError:
        error_message = "Unable to get AffectedSOPClassUID from request (pynetdicom event.request)"
        print(error_message)

        logger.error(error_message)
        try:
            model = ds_from_request.AffectedSOPClassUID
        except AttributeError:
            error_message = "Unable to get AffectedSOPClassUID from Modification List"
            print(error_message)
            logger.error(error_message)
    print(f"model={model} when looking at AffectedSOPClassUID")

    if model is None:
        try:
            model = event.request.RequestedSOPClassUID
        except AttributeError:
            error_message = "Unable to get RequestedSOPClass from request (pynetdicom event.request)"
            print(error_message)
            logger.error(error_message)

    print(f"model={model} when looking at RequestedSOPClassUID")

    if model is None:
        model = UnifiedProcedureStepPush
        print(f"Forcing model to {UnifiedProcedureStepPush}")

    logger.info(str(ds_from_request))
    progress_info_seq = None
    ups_performed_procedure_sequence = None

    try:
        progress_info_seq = ds_from_request.ProcedureStepProgressInformationSequence
        ups_performed_procedure_sequence = ds_from_request.UnifiedProcedureStepPerformedProcedureSequence
    except AttributeError:
        print(
            "Could not access either ProcedureStepProgressInformationSequence \
                or UnifiedProcedureStepPerformedProcedureSequence"
        )
    # identifier = event.request.Identifier
    # if identifier is not None:
    #     logger.info(str(identifier))
    # else:
    #     logger.warning("No Identifier in N-SET-REQUEST")

    if "TransactionUID" not in ds_from_request:
        logger.warning("TransactionUID is missing")
        yield 0xC301, None
    elif "SOPInstanceUID" in ds_from_request:
        # the SCU isn't supposed to specify the SOP Instance UID, it's supposed to identify the Affected one
        logger.warning("SOP Instance UID is not supposed to be in N-SET, use Affected SOP Instance UID")
        yield 0xC3FF, None
        return
    elif "PatientID" in ds_from_request:
        logger.warning("Patient ID is not supposed to be in N-SET-RQ")
        yield 0xC3FE, None
        return
    elif "PatientName" in ds_from_request:
        logger.warning("Patient Name is not supposed to be in N-SET-RQ")
        yield 0x3CFD, None
        return
    else:
        # the internal search needs to match on SOP Instance UID
        ds_from_request.SOPInstanceUID = event.request.RequestedSOPInstanceUID

    engine = create_engine(db_path)
    with engine.connect() as conn:  # noqa:  F841
        Session = sessionmaker(bind=engine)
        session = Session()
        # Search database using subset of ds in the N-SET-RQ as the query
        try:
            matches = search(model, ds_from_request, session)
        except InvalidIdentifier as exc:
            session.rollback()
            logger.error("Invalid N-SET Identifier received")
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

    if len(matches) == 0:
        # no SOP Instance UID that matches the Affected SOP Instance UID in the request
        yield 0xC307, None
        return

    if len(matches) > 1:
        logger.error(f"More than one matching UPS entry for {ds_from_request.AffectedSOPInstanceUID}")

    # Yield results
    for match in matches:
        if event.is_cancelled:
            yield 0xFE00, None
            return

        try:
            ds = dcmread(match.filename, force=True)
            if "ProcedureStepState" not in ds or ds["ProcedureStepState"].value != "IN PROGRESS":
                logger.warning("Procedure Step State is not IN PROGRESS")
                yield 0x3C10
                yield None
                return

            if "UnifiedProcedureStepPerformedProcedureSequence" not in ds:
                if "UnifiedProcedureStepPerformedProcedureSequence" in deep_copy_of_request:
                    ds.UnifiedProcedureStepPerformedProcedureSequence = (
                        deep_copy_of_request.UnifiedProcedureStepPerformedProcedureSequence
                    )
                else:
                    print("UnifiedProcedureStepPerformedProcedureSequence not found in the N-SET-RQ or stored UPS")
                    if ups_performed_procedure_sequence is not None:
                        print("But earlier access found it")
                        ds.UnifiedProcedureStepPerformedProcedureSequence = ups_performed_procedure_sequence
            else:
                if "UnifiedProcedureStepPerformedProcedureSequence" in deep_copy_of_request:
                    for item in deep_copy_of_request.UnifiedProcedureStepPerformedProcedureSequence:
                        ds.UnifiedProcedureStepPerformedProcedureSequence.append(item)
                else:
                    print("UnifiedProcedureStepPerformedProcedureSequence not found in the N-SET-RQ")
                    if ups_performed_procedure_sequence is not None:
                        print("But earlier access found it")
                        for item in ups_performed_procedure_sequence:
                            ds.UnifiedProcedureStepPerformedProcedureSequence.append(item)

            if "ProcedureStepProgressInformationSequence" in deep_copy_of_request:
                ds.ProcedureStepProgressInformationSequence = deep_copy_of_request.ProcedureStepProgressInformationSequence
            else:
                print("ProcedureStepProgressInformationSequence not found in the N-SET-RQ")
                if progress_info_seq is not None:
                    print("But earlier access found it")
                    ds.ProcedureStepProgressInformationSequence = progress_info_seq

            # clear out elements that we shouldn't use to *update* the UPS.  They probably match already.
            deep_copy_of_request.pop("SOPInstanceUID", None)
            deep_copy_of_request.pop("TransactionUID", None)
            deep_copy_of_request.pop("SOPClassUID", None)
            deep_copy_of_request.pop("AffectedSOPClassUID", None)
            # ProcedureStepProgressInformationSequence

            ds.update(deep_copy_of_request)
            print("Contents of Dataset after update from N-SET:")
            print(ds)
            ds.is_implicit_VR = False
            ds.ensure_file_meta()
            ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
            ds.fix_meta_info()
            dcmwrite(match.filename, ds, write_like_original=False)
            ds.Status = 0xFF00
            response_ds = ds
        except InvalidDicomError or TypeError as exc:
            logger.error(f"Error reading file: {match.filename}")
            logger.exception(exc)
            yield 0xC421, None
        except AttributeError or ValueError as write_error:
            logger.error(f"Error updating file: {match.filename}")
            logger.exception(write_error)
            yield 0xC421, None

        yield 0xFF00
        yield response_ds
        return


def handle_ncreate(event, storage_dir, db_path, cli_config, logger):
    """Handler for evt.EVT_N_CREATE.

    Parameters
    ----------
    event : pynetdicom.events.Event
        The N-CREATE request :class:`~pynetdicom.events.Event`.
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
        The N-CREATE response's *Status*. If the creation operation is successful
        but the dataset couldn't be added to the database then the *Status*
        will still be ``0x0000`` (Success).
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    logger.info(f"Received N-CREATE request from {addr}:{port} at {timestamp}")

    try:
        req = event.request
        attr_list = event.attribute_list
        ds = Dataset()

        # Add the SOP Common module elements (Annex C.12.1)
        ds.SOPClassUID = UnifiedProcedureStepPush
        ds.SOPInstanceUID = req.AffectedSOPInstanceUID

        # Update with the requested attributes
        ds.update(attr_list)

        # Remove any Group 0x0002 elements that may have been included
        # ds = ds[0x00030000:]
        sop_instance = ds.SOPInstanceUID
    except Exception as exc:
        logger.error("Unable to decode the dataset")
        logger.exception(exc)
        # Unable to decode dataset
        return 0xC210

    # Check attributes satisfy CC.2.5.1.3 UPS Attribute Service Requirements
    if not (("ProcedureStepState" in ds) and ("InputReadinessState" in ds)):
        logger.error("UPS is missing required attributes")
        return 0x0120, None  # Missing Attribute
    elif not ds.ProcedureStepState == "SCHEDULED":
        logger.error("UPS State not SCHEDULED")
        return 0xC309, None  # The provided value of UPS State was not "SCHEDULED"
    elif ds.InputReadinessState not in ("INCOMPLETE", "UNAVAILABLE", "READY"):
        logger.error("Input Readiness State not valid")
        return 0x0106, None  # Invalid Attribute Value
    # More requirements need check from Table CC.2.5-3 and TDW-II
    #  Transaction UID present and empty
    #  Scheduled Procedure Step Priority present and not empty
    #  Procedure Step Label present and not empty
    #  Worklist Label present and assign default value if empty
    #  Scheduled Processing Parameters Sequence present
    # ...

    # Add the file meta information elements - must be before adding to DB
    #   ds.file_meta = event.file_meta
    # file_meta = FileMetaDataset()
    # file_meta.ensure_file_meta()
    # file_meta.is_implicit_VR = True
    # file_meta.is_little_endian = True
    # ds.file_meta = file_meta
    ds.is_little_endian = True
    ds.is_implicit_VR = False  # need this for reading in later on.

    ds.ensure_file_meta()
    ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
    ds.fix_meta_info()
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
    with engine.connect() as conn:  # noqa:  F841
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # Path is relative to the database file
            matches = session.query(Instance).filter(Instance.sop_instance_uid == ds.SOPInstanceUID).all()
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

    # Database successfully updated, notify any globally subscribed AE
    # Get AET of UPS Event SCP (which is the AET of the UPS Watch SCP)
    acceptor = event.assoc.acceptor

    # Set event information and type
    event_info = Dataset()
    event_info.ProcedureStepState = ds.ProcedureStepState
    event_info.InputReadinessState = ds.InputReadinessState

    # UPS Assigned when Scheduled Station Name or Scheduled Human Performers is defined
    # Only Scheduled Station Name is relevant for assignment to TDD in TDW-II
    # As the SCP may choose to not send duplicate messages to an AE, only UPS State Report events
    # could maybe be sent and properly documented in conformance statement
    if "ScheduledStationNameCodeSequence" in ds:
        event_type = 5
        event_info.ScheduledStationNameCodeSequence = ds.ScheduledStationNameCodeSequence
        if "ScheduledHumanPerformersSequence" in ds:
            event_info.ScheduledHumanPerformersSequence = ds.ScheduledHumanPerformersSequence
        if "HumanPerformerOrganization" in ds:
            event_info.HumanPerformerOrganization = ds.HumanPerformerOrganization
        logger.info(
            f"Send UPS Assigned event from {acceptor.ae_title} to subscribed AEs "
            f"(assigned to {ds.ScheduledStationNameCodeSequence[0].CodeValue})"
        )
    else:
        # UPS State Report otherwise
        event_type = 1
        logger.info(f"Send UPS State Report event from {acceptor.ae_title} to subscribed AEs")

    for globalsubscriber in _global_subscribers:
        # Request association with subscriber
        ae = AE(ae_title=acceptor.ae_title)
        if globalsubscriber not in tdwii_config.known_ae_ipaddr:
            logger.error(f"{globalsubscriber} missing IP Address configuration in {REMOTE_AE_CONFIG_FILE}")
            continue

        if globalsubscriber not in tdwii_config.known_ae_port:
            logger.error(f"{globalsubscriber} missing Port configuration in {REMOTE_AE_CONFIG_FILE}")
            continue

        subscriber_ip_addr = tdwii_config.known_ae_ipaddr[globalsubscriber]
        subscriber_port = tdwii_config.known_ae_port[globalsubscriber]
        assoc = ae.associate(
            subscriber_ip_addr,
            subscriber_port,
            contexts=UnifiedProcedurePresentationContexts,
            ae_title=globalsubscriber,
            max_pdu=16382,
        )

        if assoc.is_established:
            message_id = 0
            try:
                if event_type == 1:
                    logger.info(f"Sending UPS State Report: {ds.SOPInstanceUID}, {ds.ProcedureStepState}")
                    message_id += 1
                    assoc.send_n_event_report(event_info, event_type, UnifiedProcedureStepPush, ds.SOPInstanceUID, message_id)
                elif event_type == 5:  # The assignment took place at the time of creation
                    # notify of creation first, i.e. event type == 1
                    logger.info(f"Sending UPS State Report: {ds.SOPInstanceUID}, {ds.ProcedureStepState}")
                    message_id += 1
                    assoc.send_n_event_report(event_info, 1, UnifiedProcedureStepPush, ds.SOPInstanceUID, message_id)
                    # if the assignment happened after the creation (e.g. via N-SET or internal change in a TMS)
                    # then *only* send an N-EVENT-REPORT regarding the UPS Assignment
                    logger.info(f"Sending UPS Assignment: {ds.ScheduledStationNameCodeSequence}")
                    message_id += 1
                    assoc.send_n_event_report(event_info, event_type, UnifiedProcedureStepPush, ds.SOPInstanceUID, message_id)

                logger.info(f"Notified global subscriber: {globalsubscriber}")
            except InvalidDicomError:
                logger.error("Bad DICOM: ")
            except Exception as exc:
                logger.error("UPS State Report as Event Notification (N-EVENT-REPORT-RQ) failed")
                logger.exception(exc)

            assoc.release()

        else:
            logger.error(f"Failed to establish association with subscriber: {globalsubscriber}")

    return 0x0000, ds
