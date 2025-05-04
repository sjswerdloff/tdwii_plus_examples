import logging
import subprocess
import sys
import threading


def get_configured_logger(logger_name, level=logging.INFO, handler_class=logging.StreamHandler, capacity=None):
    """Returns a configured logger with a handler.

    Args:
        logger_name (str): The name of the logger.
        level (int): The logging level. Defaults to logging.INFO.
        handler_class (logging.Handler): The handler class to use. Defaults to logging.StreamHandler.
        capacity (int, optional): The capacity of the handler if it supports it (e.g., MemoryHandler).

    Returns:
        tuple[logging.Logger, logging.Handler]: A tuple containing the logger and the handler.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    handler = handler_class(capacity) if capacity else handler_class()
    logger.addHandler(handler)
    return logger, handler


def start_scp(command: list[str], logger, timeout: float = 1.0, success_message="SCP server started successfully") -> bool:
    """Starts an external SCP process and waits for a success message.

    Args:
        command (list[str]): The command to execute.
        logger: The logger to use for messages.
        timeout (float): Timeout in seconds.
        success_message (str): The message to watch on stdout that signals successful startup.

    Returns:
        True if the process started successfully, False otherwise.
    """
    python_executable = sys.executable
    try:
        process = subprocess.Popen(
            [python_executable] + command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    except Exception as e:
        logger.error(f"Error starting process: {e}")
        return False, None, None  # Return False and None for process and thread

    stdout_lines = []
    process_started_flag = [False]
    stdout_thread = threading.Thread(target=_read_stdout, args=(process, stdout_lines, process_started_flag, success_message))
    stdout_thread.output = None  # Will be set after join
    stdout_thread.start()
    stdout_thread.join(timeout=timeout)
    stdout_thread.output = "\n".join(stdout_lines)

    if not process_started_flag[0]:
        logger.error("Process did not start successfully.")
        for line in stdout_lines:
            logger.error(line)
        process.terminate()
        process.wait()
        return False, process, stdout_thread

    return True, process, stdout_thread


def _read_stdout(process, stdout_lines, process_started_flag, success_message):
    """Reads stdout from the process."""
    for line in iter(process.stdout.readline, b""):
        line = line.decode("utf-8").strip()
        if line:
            stdout_lines.append(line)
            if success_message in line:
                process_started_flag[0] = True
                break
