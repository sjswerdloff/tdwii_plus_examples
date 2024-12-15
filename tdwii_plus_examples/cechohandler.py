def handle_cecho(event, logger):
    """Handler for evt.EVT_C_ECHO.
    Parameters
    ----------
    event : events.Event
        The corresponding event.
    logger : logging.Logger
        The application's logger.

    Returns
    -------
    int
        The status of the C-ECHO operation, always ``0x0000`` (Success).
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    aet, addr, port = requestor.ae_title, requestor.address, requestor.port
    logger.info(
        f"Received C-ECHO request from {aet}@{addr}:{port} at {timestamp}"
    )

    return 0x0000
