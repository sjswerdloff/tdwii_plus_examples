#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime
from pathlib import Path
from typing import List

from PySide6.QtCore import QDateTime, Qt, Slot  # pylint: disable=no-name-in-module
from PySide6.QtWidgets import (  # pylint: disable=no-name-in-module
    QApplication,
    QFileDialog,
    QMessageBox,
    QWidget,
)
from rtbdi_factory import (
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
from ui_form import Ui_MainBDIWidget


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
        self.plan = None
        self.rtbdi = None
        self.export_path = Path("~/")  # home for a default isn't the worst choice
        self.fraction_number = 1
        self.retrieve_ae_title = ""
        self.scheduled_datetime = datetime.now

    @Slot()
    def _plan_button_clicked(self):
        file_name, ok = QFileDialog.getOpenFileName(self, "Open Plan", "~/", "Image Files (*.dcm)")
        if file_name:
            path = Path(file_name)
        self.ui.lineedit_plan_selector.insert(str(path))
        # print("Plan Button Clicked")

    @Slot()
    def _bdidir_button_clicked(self):
        dialog = QFileDialog(self, "BDI Export Dir")
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        dialog.setLabelText(QFileDialog.Accept, "Select")
        if dialog.exec_() == QFileDialog.Accepted:
            file_name = dialog.selectedFiles()[0]
        if file_name:
            path = Path(file_name)
        self.ui.lineedit_bdidir_selector.insert(str(path))

    #     fraction_number = round(self.ui.double_spin_box_fraction_number.value())

    @Slot()
    def _bdi_export_button_clicked(self):
        fraction_number = round(self.ui.double_spin_box_fraction_number.value())
        scheduled_date = self.ui.datetime_edit_scheduled_datetime.date()
        scheduled_time = self.ui.datetime_edit_scheduled_datetime.time()
        print(f"Fraction Number: {fraction_number} " f"Scheduled Date: {scheduled_date} " f"Scheduled Time: {scheduled_time}")
        plan = load_plan(self.ui.lineedit_plan_selector.text())
        self.plan = plan
        fraction_number = round(self.ui.double_spin_box_fraction_number.value())
        self.fraction_number = fraction_number
        treatment_record_list = self._get_treatment_record_paths()
        rtbdi = create_rtbdi_from_rtion_plan(plan, fraction_number=fraction_number)
        self.rtbdi = rtbdi
        bdi_path = Path(self.ui.lineedit_bdidir_selector.text(), self.ui.line_edit_bdi_filename.text())
        write_rtbdi(rtbdi, bdi_path)
        self.export_path = bdi_path

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
            self.plan, self.rtbdi, self.retrieve_ae_title, self.scheduled_datetime, treatment_record_ds_list
        )
        write_ups(ups, Path(self.ui.lineedit_bdidir_selector.text()))

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
