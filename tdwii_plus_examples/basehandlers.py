def handle_open(event, logger):
    """Handler for evt.EVT_CONN_OPEN

    Parameters
    ----------
    event : events.Event
        The corresponding event.
    logger : logging.Logger
        The application's logger.

    Returns
    -------
    int
        The status of possible processing of opened connection parameters,
        always ``0x0000`` (Success).
    """
    requestor = event.assoc.requestor
    addr, port = requestor.address, requestor.port
    logger.info(f"Succesful connection from {addr}:{port}")

    return 0x0000


def handle_close(event, logger):
    """Handler for evt.EVT_CONN_CLOSE

    Parameters
    ----------
    event : events.Event
        The corresponding event.
    logger : logging.Logger
        The application's logger.

    Returns
    -------
    int
        The status of possible processing of closed connection parameters,
        always ``0x0000`` (Success).
    """
    requestor = event.assoc.requestor
    aet, addr, port = requestor.ae_title, requestor.address, requestor.port
    logger.info(f"Closed connection with {aet}@{addr}:{port}")

    return 0x0000
