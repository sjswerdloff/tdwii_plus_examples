def validate_port(port, logger):
    """Validate the provided port number

    Parameters
    ----------
    port : int
        The port number to validate
    logger : logging.Logger
        Logger for diagnostic messages

    Returns
    -------
    int
        The validated port number

    Raises
    ------
    ValueError
        If the port number is invalid
    TypeError
        If the port is not an integer
    """
    if port is None:
        logger.info("Port not provided, using default: 11112")
        return 11112

    if not isinstance(port, int):
        raise TypeError("port must be an integer")

    if port < 0:
        raise ValueError("port must not be negative")
    elif 0 <= port <= 1023 and port != 104:
        raise ValueError("port must not be in the range (0-1023), except 104")
    elif port == 104:
        logger.warning("DICOM port 104 may need admin privileges")
        return port
    elif port in range(1024, 11111) or port in range(11161, 49151):
        logger.warning("Registered port (1024-49151) may be used by others")
        return port
    elif port > 65535:
        raise ValueError("port must not exceed 65535")

    return port
