"""Event handlers for nevent_receiver.py"""

from pydicom import dcmread


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
        event_response_cb(type_id=nevent_type_id, information_ds=nevent_information, logger=logger)
    else:
        logger.warning(f"Received model.keyword = {model.keyword} with AffectedSOPClassUID = {model}")
        logger.warning("Not a UPS Event")

    logger.info("Finished Processing N-EVENT-REPORT-RQ")
    yield 0  # Number of suboperations remaining
    #  If a rsp dataset of None is provided below, the underlying handler and dimse primitive in pynetdicom raises an error
    yield 0  # Status
