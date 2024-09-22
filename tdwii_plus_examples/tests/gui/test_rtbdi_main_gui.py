import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QFileDialog  # , QMessageBox
from pytestqt.qtbot import QtBot

from tdwii_plus_examples.rtbdi_creator.mainbdiwidget import MainBDIWidget

PATH_TO_PLAN = "/Users/stuartswerdloff/Downloads/Breast_ProNova/RP1.2.752.243.1.1.20240618125727890.2330.42704_ims_pvt.dcm"
PATH_TO_BDI_DIR = "/Users/stuartswerdloff/BDIFolder"
MOVE_SCP_TITLE = "OST"
BDI_FILE_NAME = "test_bdi.dcm"


@pytest.fixture(scope="session")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app
    app.quit()


@pytest.fixture
def main_window(qtbot: QtBot, qapp):
    """Fixture to create and return the main window."""
    window = MainBDIWidget()
    qtbot.addWidget(window)
    return window


def test_initial_state(main_window):
    """Test the initial state of the main window."""
    assert main_window.ui.lineedit_plan_selector.text() == ""
    assert main_window.ui.lineedit_bdidir_selector.text() != ""  # Should have a default value
    assert main_window.ui.double_spin_box_fraction_number.value() == 1


def test_plan_button_click(main_window, qtbot, mocker):
    """Test the plan finder button click."""
    # Mock the QFileDialog
    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(PATH_TO_PLAN, ""))

    # Click the plan finder button
    qtbot.mouseClick(main_window.ui.push_button_plan_finder, Qt.LeftButton)

    # Check if the line edit was updated
    assert main_window.ui.lineedit_plan_selector.text() == PATH_TO_PLAN


def test_bdi_dir_button_click(main_window, qtbot, mocker):
    """Test the BDI directory finder button click."""
    # Mock the QFileDialog
    mocker.patch.object(QFileDialog, "exec", return_value=QFileDialog.Accepted)
    mocker.patch.object(QFileDialog, "selectedFiles", return_value=[PATH_TO_BDI_DIR])

    # Click the BDI directory finder button
    qtbot.mouseClick(main_window.ui.push_button_bdi_dir_finder, Qt.LeftButton)

    # Check if the line edit was updated
    assert main_window.ui.lineedit_bdidir_selector.text() == PATH_TO_BDI_DIR


def test_fraction_number_change(main_window, qtbot):
    """Test changing the fraction number."""
    # Click on the spin box to focus it
    qtbot.mouseClick(main_window.ui.double_spin_box_fraction_number, Qt.LeftButton)

    # Clear existing value
    qtbot.keyClick(main_window.ui.double_spin_box_fraction_number, Qt.Key_Delete)

    # Type new value
    qtbot.keyClicks(main_window.ui.double_spin_box_fraction_number, "2")

    # Press enter to ensure value is committed
    qtbot.keyClick(main_window.ui.double_spin_box_fraction_number, Qt.Key_Enter)

    # Check the value
    assert main_window.ui.double_spin_box_fraction_number.value() == 2


def test_export_bdi_button_click(main_window, qtbot, mocker):
    """Test the export BDI button click."""
    # Mock the imported functions
    mock_load_plan = mocker.patch("tdwii_plus_examples.rtbdi_creator.mainbdiwidget.load_plan")
    mock_create_rtbdi = mocker.patch("tdwii_plus_examples.rtbdi_creator.mainbdiwidget.create_rtbdi_from_rtion_plan")
    mock_write_rtbdi = mocker.patch("tdwii_plus_examples.rtbdi_creator.mainbdiwidget.write_rtbdi")
    mock_store_scu = mocker.patch("tdwii_plus_examples.rtbdi_creator.mainbdiwidget.StoreSCU")

    # Mock the _get_treatment_record_paths method
    mocker.patch.object(main_window, "_get_treatment_record_paths", return_value=[])

    # Mock the _command_outcome_message method
    mocker.patch.object(main_window, "_command_outcome_message")

    # Set up return values
    mock_load_plan.return_value = mocker.MagicMock()
    mock_create_rtbdi.return_value = mocker.MagicMock()
    mock_store_scu.return_value.store.return_value = True

    # Set up the necessary inputs
    main_window.ui.lineedit_plan_selector.setText(PATH_TO_PLAN)
    main_window.ui.lineedit_bdidir_selector.setText(PATH_TO_BDI_DIR)
    main_window.ui.line_edit_move_scp_ae_title.setText(MOVE_SCP_TITLE)
    main_window.ui.line_edit_bdi_filename.setText(BDI_FILE_NAME)
    main_window.ui.double_spin_box_fraction_number.setValue(2)

    # Click the export BDI button
    qtbot.mouseClick(main_window.ui.push_button_export_bdi, Qt.LeftButton)

    # Check if the necessary functions were called
    mock_load_plan.assert_called_once_with(PATH_TO_PLAN)
    mock_create_rtbdi.assert_called_once()
    mock_write_rtbdi.assert_called_once()
    mock_store_scu.assert_called_once()
    mock_store_scu.return_value.store.assert_called_once()

    # Check if _command_outcome_message was called
    main_window._command_outcome_message.assert_called_once_with(success=True, command_name="C-STORE")
