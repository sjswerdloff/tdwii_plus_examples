import logging
from argparse import Namespace

from pynetdicom.apps.common import setup_logging


def init_logger(logger, default_name, class_name):
    """Initialize and validate logger

    Parameters
    ----------
    logger : logging.Logger or None
        The logger instance or None to create a default logger
    default_name : str
        The name to use for the default logger if one is not provided
    class_name : str
        The name of the class initializing the logger for better log messages

    Returns
    -------
    logging.Logger
        The initialized logger

    Raises
    ------
    TypeError
        If logger is not an instance of logging.Logger
    """
    if logger is None:
        new_logger = setup_logging(Namespace(log_type=None, log_level="debug"), default_name)
        new_logger.info("Logger not provided, using default logger with level %s", logging.getLevelName(new_logger.level))
    elif isinstance(logger, logging.Logger):
        new_logger = logger
        new_logger.debug("Logger set to %s with level %s", logger.name, logging.getLevelName(logger.getEffectiveLevel()))
    else:
        raise TypeError("logger must be an instance of logging.Logger")
    new_logger.debug(f"{class_name}.__init__")
    return new_logger
