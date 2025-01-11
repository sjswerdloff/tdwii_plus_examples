from pydicom import Dataset, dcmread
from pynetdicom.status import Status

# Define some general Status Code values for the N-EVENT-REPORT Response
Status.add('ATTRIBUTE_LIST_ERROR', 0x0107)  # Failure to read event information
Status.add('PROCESSING_FAILURE', 0x0110)  # Failure to process the request
Status.add('NO_SUCH_EVENT_TYPE', 0x0113)  # Not a valid UPS Event Type
Status.add('REFUSED_SOP_CLASS_NOT_SUPPORTED', 0x0122)  # Not a valid SOP Class

UPS_EVENT_TYPES = {
    1: "UPS State Report",
    2: "UPS Cancel Requested",
    3: "UPS Progress Report",
    4: "SCP Status Change",
    5: "UPS Assigned",
}


def nevent_callback(upsinstance, upseventtype, upseventinfo, app_logger):
    app_logger.info(f"Processing Status Change for UPS Instance {upsinstance}")
    app_logger.info(f"UPS Event Type: {UPS_EVENT_TYPES[upseventtype]}")
    app_logger.info(f"UPS Event Information: \n{upseventinfo}")


def handle_nevent(event, ups_event_callback, app_logger):
    """Handler for evt.EVT_N_EVENT_REPORT.

    Parameters
    ----------
    event : pynetdicom.events.Event
        The UPS N-EVENT-REPORT request :class:`~pynetdicom.events.Event`.
    ups_event_callback : function
        The function to call when receiving the UPS N-EVENT-REPORT request.
    app_logger : logging.Logger
        The application's logger.

    Returns
    -------
    return_tuple: tuple[pydicom.dataset.Dataset or int,
                         pydicom.dataset.Dataset or None]
        A tuple containing two elements:
        - The status returned to the peer AE in the N-EVENT-REPORT response.
          Must be a valid N-EVENT-REPORT status value for the applicable Service
          Class as either an int or a Dataset object containing (at a minimum) a
          (0000,0900) Status element. If returning a Dataset object then it may
          also contain optional elements related to the Status (as in DICOM
          Standard, Part 7, Annex C).
        - If the status category is 'Success' or 'Warning' then a Dataset
          containing elements of the response's Event Reply conformant to the
          specifications in the corresponding Service Class may be returned.
          None otherwise.
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
    app_logger.info(
        f"Received N-EVENT-REPORT request from {addr}:{port} at {timestamp}")

    ups_sop_class = nevent_primitive.AffectedSOPClassUID
    ups_instance = nevent_primitive.AffectedSOPInstanceUID
    nevent_type_id = nevent_primitive.EventTypeID
    nevent_information = dcmread(nevent_primitive.EventInformation, force=True)

    # Create the response status assuming success
    # consistently using Dataset object with Status element (vs int)
    # Other N-EVENT-REPORT response parameters are set by pynetdicom
    # implementation of the UPS Event Service Class.
    status_ds = Dataset()
    status_ds.Status = Status.SUCCESS

    # Make sure the event SOP class is valid
    if ups_sop_class.keyword in ["UnifiedProcedureStepPush"]:
        app_logger.debug(
            f"UPS Event valid SOP Class UID: "
            f"{ups_sop_class}")
    else:
        app_logger.error(
            "UPS Event invalid SOP Class UID: "
            f"{ups_sop_class}")
        status_ds.Status = Status.REFUSED_SOP_CLASS_NOT_SUPPORTED
        return status_ds, None

    # Make sure the event type is valid
    if nevent_type_id in UPS_EVENT_TYPES:
        app_logger.debug(
            f"UPS Event valid Event Type ID: "
            f"{nevent_type_id} ({UPS_EVENT_TYPES[nevent_type_id]})")
    else:
        app_logger.error(
            "UPS Event invalid Event Type ID: "
            f"{nevent_type_id}")
        status_ds.Status = Status.NO_SUCH_EVENT_TYPE
        return status_ds, None

    # Make sure the event information is valid
    try:
        for elem in nevent_information:
            # Access the element's value to ensure it can be read
            _ = elem.value
    except Exception as e:
        app_logger.error(f"InvalidException encountered: {e}")
        status_ds.Status = Status.ATTRIBUTE_LIST_ERROR
        return status_ds, None
    app_logger.debug(f"UPS Event information: \n{nevent_information}")

    # Check if valid ups_event_callback function is provided
    app_logger.debug(
        f"UPS Event callback: {ups_event_callback} type is {type(ups_event_callback)}")
    if ups_event_callback is None:
        app_logger.warning("No ups_event_callback defined, "
                           "using default callback")
        ups_event_callback = nevent_callback
    elif not callable(ups_event_callback):
        app_logger.warning(f"{ups_event_callback} is not a known function, "
                           "using default callback")
        ups_event_callback = nevent_callback
    else:
        app_logger.debug(f"UPS Event callback: {ups_event_callback}")

    # Call the UPS Event callback
    try:
        ups_event_callback(upsinstance=ups_instance,
                           upseventtype=nevent_type_id,
                           upseventinfo=nevent_information,
                           app_logger=app_logger)
    except Exception as e:
        app_logger.error(f"Exception encountered in UPS Event callback: {e}")
        status_ds.Status = Status.PROCESSING_FAILURE
        return status_ds, None

    # Return Success status code and None as no Event Reply required
    return status_ds, None
