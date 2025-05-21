#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import List

if sys.version_info >= (3, 11):
    import tomllib as tomli
else:
    import tomli
from PySide6.QtCore import QDateTime, Qt, Slot  # pylint: disable=no-name-in-module
from PySide6.QtWidgets import (  # pylint: disable=no-name-in-module
    QApplication,
    QFileDialog,
    QMessageBox,
    QWidget,
)

from tdwii_plus_examples import tdwii_config
from tdwii_plus_examples.cstorescu import CStoreSCU
from tdwii_plus_examples.rtbdi_creator.rtbdi_factory import (
    create_rtbdi_from_rtion_plan,
    create_ups_from_plan_and_bdi,
    is_tx_record_for_bdi,
    is_tx_record_for_plan,
    load_plan,
    load_treatment_records,
    write_rtbdi,
    write_ups,
)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from tdwii_plus_examples.rtbdi_creator.ui_form import Ui_MainBDIWidget
from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU


class MainBDIWidget(QWidget):
    """Main UI for Creating an RT BDI based on an RT (Ion) Plan
    The UI provides a File Dialog to locate the RT (Ion) Plan
        A spinner for choosing which Fraction Number
        A File Dialog to specify the output directory
        A line edit(or) to enter the name of the RT BDI
        And an export button

    Args:
        QWidget (_type_): description
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainBDIWidget()
        self.ui.setupUi(self)
        self.ui.datetime_edit_scheduled_datetime.setDateTime(QDateTime.currentDateTime())

        self.ui.push_button_plan_finder.clicked.connect(self._plan_button_clicked)
        self.ui.push_button_bdi_dir_finder.clicked.connect(self._bdidir_button_clicked)
        self.ui.push_button_export_bdi.clicked.connect(self._bdi_export_button_clicked)
        self.ui.push_button_export_ups.clicked.connect(self._export_ups_button_clicked)
        self.ui.push_button_send_plan.clicked.connect(self._store_plan_button_clicked)

        self.logger = logging.getLogger(__name__)

        self.plan = None
        self.plan_path = Path("~/").expanduser()
        self.rtbdi = None
        self.export_path = Path("~/").expanduser()  # home for a default isn't the worst choice
        self.fraction_number = 1
        self.retrieve_ae_title = ""
        self.scheduled_datetime = datetime.now
        self.ae_title = "TMS"
        self.config_file = "rtbdi.toml"
        self._load_ae_config()

    def _load_ae_config(self):
        """Loads AE configuration from the TOML and JSON files."""
        try:
            with open(self.config_file, "rb") as f:
                toml_dict = tomli.load(f)
            if "DEFAULT" in toml_dict:
                default_dict = toml_dict["DEFAULT"]
                if "export_staging_directory" in default_dict:
                    export_staging_directory = Path(default_dict["export_staging_directory"]).expanduser()
                    self.ui.lineedit_bdidir_selector.setText(str(export_staging_directory))
                if "qr_ae_title" in default_dict:
                    self.ui.line_edit_move_scp_ae_title.setText(default_dict["qr_ae_title"])
                if "ae_title" in default_dict:
                    self.ae_title = default_dict["ae_title"]
                if "plan_path" in default_dict:
                    self.plan_path = str(Path(default_dict["plan_path"]).expanduser())
                if "ups_scp_ae_title" in default_dict:
                    self.ui.line_edit_tms_scp_ae_title.setText(default_dict["ups_scp_ae_title"])
            else:
                self.logger.warning("No [DEFAULT] section in toml config file")

            tdwii_config.load_ae_config()
            self.known_ae_ipaddr = tdwii_config.known_ae_ipaddr
            self.known_ae_port = tdwii_config.known_ae_port

        except OSError as config_file_error:
            self.logger.exception("Problem parsing config file: " + config_file_error)

    @Slot()
    def _plan_button_clicked(self):
        previous_path = self.plan_path
        file_name, ok = QFileDialog.getOpenFileName(self, "Open Plan", str(previous_path), "DICOM Plan Files (*.dcm)")
        if file_name:
            path = Path(file_name)
            self.ui.lineedit_plan_selector.setText(str(path))
            self.plan_path = path.parent
        # print("Plan Button Clicked")

    @Slot()
    def _store_plan_button_clicked(self):
        dest_ae_title = self.ui.line_edit_move_scp_ae_title.text()
        ip_addr, port = self._get_ae_config(dest_ae_title)
        if ip_addr is None or port is None:
            return
        store_scu = CStoreSCU(
            calling_ae_title=self.ae_title, called_ae_title=dest_ae_title, called_ip=ip_addr, called_port=port
        )
        # always re-load.  Not performant, but safe choice.
        # a more performant approach would be to force a re-load every time a plan is selected.
        # that's not really necessary unless the plan has to be (C-)stored
        plan = load_plan(self.ui.lineedit_plan_selector.text())
        iods = list()
        iods.append(plan)
        store_scu.set_contexts_from_files(iods)
        success = store_scu.store_instances(instances=iods)
        self._command_outcome_message(success=success, command_name="C-STORE")

        return

    @Slot()
    def _bdidir_button_clicked(self):
        dialog = QFileDialog(self, "BDI Export Dir")
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        dialog.setLabelText(QFileDialog.Accept, "Select")
        if dialog.exec() == QFileDialog.Accepted:
            file_name = dialog.selectedFiles()[0]
        if file_name:
            path = Path(file_name)
        self.ui.lineedit_bdidir_selector.setText(str(path))

    #     fraction_number = round(self.ui.double_spin_box_fraction_number.value())

    @Slot()
    def _bdi_export_button_clicked(self):
        fraction_number = round(self.ui.double_spin_box_fraction_number.value())
        scheduled_date = self.ui.datetime_edit_scheduled_datetime.date()
        scheduled_time = self.ui.datetime_edit_scheduled_datetime.time()
        print(f"Fraction Number: {fraction_number} Scheduled Date: {scheduled_date} Scheduled Time: {scheduled_time}")
        plan = load_plan(self.ui.lineedit_plan_selector.text())
        self.plan = plan
        fraction_number = round(self.ui.double_spin_box_fraction_number.value())
        self.fraction_number = fraction_number
        treatment_record_list = self._get_treatment_record_paths()
        rtbdi = create_rtbdi_from_rtion_plan(
            plan, fraction_number=fraction_number, treatment_record_list=treatment_record_list
        )
        self.rtbdi = rtbdi
        bdi_path = Path(self.ui.lineedit_bdidir_selector.text(), self.ui.line_edit_bdi_filename.text())
        write_rtbdi(rtbdi, bdi_path)
        self.export_path = bdi_path

        dest_ae_title = self.ui.line_edit_move_scp_ae_title.text()
        ip_addr, port = self._get_ae_config(dest_ae_title)
        if ip_addr is None or port is None:
            return

        store_scu = CStoreSCU(
            calling_ae_title=self.ae_title, called_ae_title=dest_ae_title, called_ip=ip_addr, called_port=port
        )
        iods = [rtbdi]
        store_scu.set_contexts_from_files(iods)
        success = store_scu.store_instances(instances=iods)
        self._command_outcome_message(success=success, command_name="C-STORE")

    def _get_ae_config(self, ae_title):
        """Retrieves AE configuration (IP and port).  Logs an error and returns None if config is missing."""
        ip_addr = self.known_ae_ipaddr.get(ae_title)
        port = self.known_ae_port.get(ae_title)
        if ip_addr is None or port is None:
            self.logger.error(f"Missing configuration for AE title: {ae_title}")
            return None, None  # Return None for both if config is missing
        return ip_addr, port

    @Slot()
    def _export_ups_button_clicked(self):
        self.retrieve_ae_title = self.ui.line_edit_move_scp_ae_title.text()
        self.scheduled_datetime = self.ui.datetime_edit_scheduled_datetime.dateTime().toPython()

        treatment_record_paths = self._get_treatment_record_paths()
        treatment_record_ds_list = load_treatment_records(treatment_record_paths)
        self._validate_treatment_records(treatment_record_ds_list)
        if self.rtbdi is None:
            self._bdi_export_button_clicked()

        ups = create_ups_from_plan_and_bdi(
            self.plan,
            self.rtbdi,
            self.retrieve_ae_title,
            self.scheduled_datetime,
            treatment_record_ds_list,
            enable_photo_ref=self.ui.checkbox_patient_photo.isChecked(),
            enable_setup_image_ref=self.ui.checkbox_setup_photos.isChecked(),
        )
        write_ups(ups, Path(self.ui.lineedit_bdidir_selector.text()))
        tms_ae_title = self.ui.line_edit_tms_scp_ae_title.text()
        if tms_ae_title is None or len(str(tms_ae_title.strip())) == 0:
            self.logger.warning("No TMS AE Title specified, will not attempt an N-CREATE")
        else:
            dest_ae_title = tms_ae_title.strip()
            ip_addr = self.known_ae_ipaddr.get(dest_ae_title)
            port = self.known_ae_port.get(dest_ae_title)
            if ip_addr is None or port is None:
                self.logger.error(f"AE title '{dest_ae_title}' not found in configuration.")
                return
            ncreate_scu = UPSPushNCreateSCU(
                logger=self.logger,
                calling_ae_title=self.ae_title,
                called_ip=ip_addr,
                called_port=port,
                called_ae_title=dest_ae_title,
            )
            ups_list = list()
            ups_list.append(ups)
            num_created_inst = ncreate_scu.create_ups_instances(ups_list)
            self._command_outcome_message(success=num_created_inst == len(ups_list), command_name="N-CREATE")

    def _command_outcome_message(self, success: bool, command_name: str, text: str = None):
        # apparently a known defect, see:
        # https://stackoverflow.com/questions/76869543/why-cant-i-change-the-window-icon-on-a-qmessagebox-with-seticon-in-pyside6
        app.setAttribute(Qt.ApplicationAttribute.AA_DontUseNativeDialogs, True)
        if not success:
            dlg = QMessageBox(self)
            dlg.setIcon(QMessageBox.Warning)
            if text is None:
                msg_text = " failed. Please check log for more information"
            else:
                msg_text = text
            dlg.setText(command_name + msg_text)
        else:
            dlg = QMessageBox(self)
            dlg.setIcon(QMessageBox.Information)
            if text is None:
                msg_text = " succeeded"
            else:
                msg_text = text
            dlg.setText(command_name + msg_text)
        dlg.exec()
        app.setAttribute(Qt.ApplicationAttribute.AA_DontUseNativeDialogs, False)

    def _validate_treatment_records(self, treatment_record_ds_list):
        """Confirms that the treatment records reference the plan
        and are for the correct fraction  number.  Modifies the input list
        by removing an invalid treatment records.  Presents a Message to the user
        if any of the treatment records aren't valid.

        Args:
            treatment_record_ds_list (_type_): _description_
        """
        mismatched_records = []
        if len(treatment_record_ds_list) != 0:
            for tx_record_ds in treatment_record_ds_list:
                if not is_tx_record_for_plan(tx_record_ds, self.plan):
                    treatment_record_ds_list.remove(tx_record_ds)
                    mismatched_records.append(tx_record_ds.SOPInstanceUID)
                else:
                    if not is_tx_record_for_bdi(tx_record_ds, self.rtbdi):
                        treatment_record_ds_list.remove(tx_record_ds)
                        mismatched_records.append(tx_record_ds.SOPInstanceUID)

        if len(mismatched_records) != 0:
            QMessageBox.show("<br>".join(mismatched_records))
        return

    def _get_treatment_record_paths(self) -> List[Path]:
        treatment_record_paths = []
        model = self.ui.list_view_treatment_records.model()
        if model is not None:
            for row in range(model.rowCount()):
                index = model.index(row, 0)
                item = model.data(index, Qt.ItemDataRole.DisplayRole)
                treatment_record_paths.append(Path(str(item)))
        return treatment_record_paths


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainBDIWidget()
    widget.show()
    sys.exit(app.exec())
