import ssl


def describe_tls_session(event):
    """Describe the TLS session of the connection of an event.

    Parameters
    ----------
    event : pynetdicom.event.event
        The event corresponding to a TCP connection.

    Returns
    -------
    str or None
        The TLS protocol version and cipher, followed by the subject of the client certificate
        if the client presented one, or ``None`` if the connection is not secured with TLS.
    """
    try:
        # The connection socket is reached through pynetdicom's association, which is not a documented public API
        connection_socket = event.assoc.dul.socket.socket
    except AttributeError:
        return None

    if not isinstance(connection_socket, ssl.SSLSocket):
        return None

    cipher = connection_socket.cipher()
    description = f"{connection_socket.version()}, {cipher[0] if cipher else 'unknown cipher'}"

    client_certificate = connection_socket.getpeercert()
    if client_certificate:
        subject = ", ".join(f"{name}={value}" for rdn in client_certificate["subject"] for name, value in rdn)
        description += f", client certificate subject: {subject}"

    return description


def handle_open(event, logger):
    """Handler for evt.EVT_CONN_OPEN

    Parameters
    ----------
    event : pynetdicom.event.event
        The event corresponding to the opening of a TCP connection.
    app_logger : logging.Logger
        The application's logger.

    Returns
    -------
    int
        The status of possible processing of opened connection parameters,
        always ``0x0000`` (Success).
    """
    requestor = event.assoc.requestor
    addr, port = requestor.address, requestor.port
    logger.info(f"Successful connection from {addr}:{port}")

    tls_session = describe_tls_session(event)
    if tls_session:
        logger.info(f"TLS session with {addr}:{port}: {tls_session}")

    return 0x0000


def handle_close(event, logger):
    """Handler for evt.EVT_CONN_CLOSE

    Parameters
    ----------
    event : pynetdicom.event.event
        The event corresponding to the closing of a TCP connection.
    app_logger : logging.Logger
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
