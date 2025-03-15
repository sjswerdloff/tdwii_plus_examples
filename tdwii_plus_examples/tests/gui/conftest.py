#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Debug version of conftest.py with extensive logging for screenshot troubleshooting.
"""

import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

import pytest
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget

from tdwii_plus_examples import tdwii_config

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("pytest_debug.log")],
)
logger = logging.getLogger("pytest_screenshot")
logger.info("Loading conftest.py for test run")


# Ensure the application is only initialized once
@pytest.fixture(scope="session")
def qapp():
    """Create QApplication once per session."""
    logger.info("Setting up QApplication")
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        logger.info("Created new QApplication")
    else:
        logger.info("Using existing QApplication")
    yield app


# Ensure the screenshot directory exists
@pytest.fixture(scope="session", autouse=True)
def create_screenshot_dir():
    """Create screenshot directory if it doesn't exist."""
    screenshot_dir = Path("test_screenshots")
    try:
        screenshot_dir.mkdir(exist_ok=True)
        logger.info(f"Created or verified screenshot directory: {screenshot_dir.absolute()}")

        # Verify we can write to the directory
        test_file = screenshot_dir / "write_test.txt"
        test_file.write_text("Test write permission")
        test_file.unlink()  # Delete the test file
        logger.info("Successfully verified write permission to screenshot directory")
    except Exception as e:
        logger.error(f"Error setting up screenshot directory: {e}")

    return screenshot_dir


@pytest.fixture(scope="session", autouse=True)
def setup_tdwii_config():
    """
    Setup the tdwii_config with test values.
    This is crucial to avoid KeyErrors when initializing components.
    """
    logger.info("Setting up tdwii_config for testing")
    # Backup original state if needed for restoration
    original_ipaddr = tdwii_config.known_ae_ipaddr.copy() if hasattr(tdwii_config, "known_ae_ipaddr") else {}
    original_port = tdwii_config.known_ae_port.copy() if hasattr(tdwii_config, "known_ae_port") else {}
    logger.debug(f"setting aside original ip {original_ipaddr}")
    logger.debug(f"setting aside original port {original_port}")
    # Set up test configuration
    tdwii_config.known_ae_ipaddr = {
        "UPS_TEST_AE": "127.0.0.1",
        "QR_TEST_AE": "127.0.0.1",
        "PPVS_SCP": "127.0.0.1",
        "TEST_AE": "127.0.0.1",
    }

    tdwii_config.known_ae_port = {"UPS_TEST_AE": 11112, "QR_TEST_AE": 11114, "PPVS_SCP": 11113, "TEST_AE": 11115}

    logger.info(f"tdwii_config setup complete. known_ae_port: {tdwii_config.known_ae_port}")

    yield

    # Restore original configuration if needed
    # Uncomment if you want to restore the original state
    # tdwii_config.known_ae_ipaddr = original_ipaddr
    # tdwii_config.known_ae_port = original_port


@pytest.fixture
def create_test_directories():
    """Create test directories for storing files."""
    test_staging_dir = Path.home() / "test_staging_dir"

    # Create directory
    os.makedirs(test_staging_dir, exist_ok=True)
    logger.info(f"Created test staging directory: {test_staging_dir}")

    yield {"staging_dir": str(test_staging_dir)}


# This is the key hook that will take screenshots on test failures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Make test result information available for screenshot capture.
    """
    # Execute the test
    outcome = yield
    rep = outcome.get_result()

    # Set report attributes for each phase (setup, call, teardown)
    setattr(item, f"rep_{rep.when}", rep)

    # Log all test phases
    logger.info(f"Test {item.name} phase {rep.when} - {'PASSED' if rep.passed else 'FAILED' if rep.failed else 'SKIPPED'}")

    # Take screenshots when tests fail in any phase
    if rep.failed:
        logger.info(f"Test {item.name} failed in phase {rep.when} - attempting to capture screenshots")
        try:
            # Get widgets to screenshot from the qtbot fixture
            qtbot = item.funcargs.get("qtbot", None)
            if qtbot and hasattr(qtbot, "_widgets"):
                logger.info(f"Found qtbot with {len(qtbot._widgets)} registered widgets")

                # Get test name and timestamp
                test_name = item.name
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

                # Create screenshot directory
                screenshot_dir = Path("test_screenshots")
                screenshot_dir.mkdir(exist_ok=True)

                # Try to capture all registered widgets
                registered_widget_captured = False
                for i, widget in enumerate(qtbot._widgets):
                    visibility_string = "N/A"
                    if hasattr(widget, "isVisible"):
                        visibility_string = widget.isVisible()
                    logger.info(f"Processing widget {i}: {widget}, visible={visibility_string}")

                    if isinstance(widget, QWidget) and widget.isVisible():
                        try:
                            filename = f"{screenshot_dir}/{test_name}_{timestamp}_widget_{i}.png"
                            logger.info(f"Attempting to capture widget to {filename}")

                            # Process events to ensure widget is rendered
                            QApplication.processEvents()

                            # Take the screenshot
                            pixmap = widget.grab()
                            result = pixmap.save(filename)

                            if result:
                                logger.info(f"Successfully saved screenshot to {filename}")
                                registered_widget_captured = True
                            else:
                                logger.error(f"Failed to save screenshot to {filename}")
                        except Exception as e:
                            logger.error(f"Error capturing widget {i}: {e}")

                if not registered_widget_captured:
                    logger.warning("No registered widgets were captured. Attempting to capture top-level widgets.")
            else:
                logger.warning("qtbot not found or has no widgets registered")
        except Exception as e:
            logger.error(f"Error in screenshot capture hook: {e}")


# Add this fixture to automatically capture screenshots for all tests
@pytest.fixture(autouse=True)
def auto_screenshot_on_failure(request, qapp, create_screenshot_dir):
    """
    Automatically capture screenshots on test failure.
    This works independently of qtbot and captures all visible windows.
    """
    # Allow test to run
    yield

    # Check if the test failed
    failed = False
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        failed = True
    elif hasattr(request.node, "rep_setup") and request.node.rep_setup.failed:
        failed = True
    elif hasattr(request.node, "rep_teardown") and request.node.rep_teardown.failed:
        failed = True

    if failed:
        logger.info(f"Test {request.node.name} failed - attempting to capture top-level widgets")
        try:
            # Get all top-level widgets
            widgets = QApplication.topLevelWidgets()
            logger.info(f"Found {len(widgets)} top-level widgets")

            # Get test name and timestamp
            test_name = request.node.name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Take screenshots
            screenshot_dir = create_screenshot_dir

            # Process events to ensure widgets are rendered
            QApplication.processEvents()

            toplevel_captured = False
            for i, widget in enumerate(widgets):
                visibility_string = "N/A"
                if hasattr(widget, "isVisible"):
                    visibility_string = widget.isVisible()
                logger.info(f"Processing widget {i}: {widget}, visible={visibility_string}")

                if hasattr(widget, "isVisible") and widget.isVisible() and not isinstance(widget, QMessageBox):
                    try:
                        filename = f"{screenshot_dir}/{test_name}_{timestamp}_toplevel_{i}.png"
                        logger.info(f"Attempting to capture top-level widget to {filename}")

                        # Ensure the widget is active
                        widget.activateWindow()
                        widget.raise_()
                        QApplication.processEvents()

                        # Add a slight delay to ensure rendering
                        time.sleep(0.1)
                        QApplication.processEvents()

                        # Take the screenshot
                        pixmap = widget.grab()
                        result = pixmap.save(filename)

                        if result:
                            logger.info(f"Successfully saved top-level screenshot to {filename}")
                            toplevel_captured = True
                        else:
                            logger.error(f"Failed to save top-level screenshot to {filename}")
                    except Exception as e:
                        logger.error(f"Error capturing top-level widget {i}: {e}")

            if not toplevel_captured:
                logger.warning("No top-level widgets were captured.")

                # Try a whole screen capture as last resort
                try:
                    screen = QApplication.primaryScreen()
                    if screen:
                        filename = f"{screenshot_dir}/{test_name}_{timestamp}_screen.png"
                        logger.info(f"Attempting to capture entire screen to {filename}")

                        pixmap = screen.grabWindow(0)  # 0 means entire screen
                        result = pixmap.save(filename)

                        if result:
                            logger.info(f"Successfully saved screen capture to {filename}")
                        else:
                            logger.error(f"Failed to save screen capture to {filename}")
                except Exception as e:
                    logger.error(f"Error capturing screen: {e}")

        except Exception as e:
            logger.error(f"Error in auto_screenshot_on_failure fixture: {e}")


@pytest.fixture
def manual_screenshot():
    """
    Fixture that allows manually taking screenshots during tests.
    Usage: screenshot = manual_screenshot(); screenshot("my_filename")
    """

    def _take_screenshot(name="manual_capture"):
        """Take a screenshot of all visible widgets."""
        try:
            logger.info(f"Taking manual screenshot: {name}")
            screenshot_dir = Path("test_screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{screenshot_dir}/{name}_{timestamp}.png"

            screen = QApplication.primaryScreen()
            if screen:
                pixmap = screen.grabWindow(0)  # 0 means entire screen
                result = pixmap.save(filename)

                if result:
                    logger.info(f"Successfully saved manual screenshot to {filename}")
                    return filename
                else:
                    logger.error(f"Failed to save manual screenshot to {filename}")
                    return None

        except Exception as e:
            logger.error(f"Error taking manual screenshot: {e}")
            return None

    return _take_screenshot


@pytest.fixture
def close_all_message_boxes(qapp):
    """Close any message boxes that might appear during testing."""
    yield

    # After test, find and close any message boxes
    for widget in qapp.topLevelWidgets():
        if isinstance(widget, QMessageBox):
            logger.info(f"Closing message box: {widget.text()}")
            QTimer.singleShot(0, widget.close)
            qapp.processEvents()


@pytest.fixture
def mock_ppvs_scp():
    """Fixture to patch the PPVS_SCP class."""
    with patch("tdwii_plus_examples.TDWII_PPVS_subscriber.ppvsscp.PPVS_SCP") as mock_class:
        logger.info("Mocked PPVS_SCP class")
        yield mock_class


# Add this if you want to temporarily pause for inspection during testing
@pytest.fixture
def pause_for_inspection():
    """
    Pause the test execution for manual inspection.
    Usage: add 'pause_for_inspection' to your test function parameters.
    """

    def _pause(seconds=2):
        logger.info(f"Pausing for {seconds} seconds for inspection...")
        QApplication.processEvents()
        time.sleep(seconds)
        QApplication.processEvents()

    return _pause
