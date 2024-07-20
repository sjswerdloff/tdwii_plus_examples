#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import logging
import sys
from pathlib import Path

import tomli
from pydicom import DataElement, Dataset, dcmread, uid
from pydicom.valuerep import VR
from pynetdicom.presentation import build_context
from PySide6.QtCore import QDateTime, Qt, Slot  # pylint: disable=no-name-in-module
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QTreeWidget,
    QTreeWidgetItem,
    QWidget,
)

from tdwii_plus_examples import cmove_inputs, tdwii_config

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from tdwii_plus_examples.tdd.ui_tdd import Ui_MainTDDWidget
from tdwii_plus_examples.TDWII_PPVS_subscriber.ppvsscp import PPVS_SCP
from tdwii_plus_examples.TDWII_PPVS_subscriber.upsfindscu import (
    create_ups_query,
    get_ups,
    response_content_to_dict,
)
from tdwii_plus_examples.TDWII_PPVS_subscriber.watchscu import WatchSCU


class TDD_Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainTDDWidget()
        self.ui.setupUi(self)
        self.ui.scrollArea.setWidgetResizable(True)

        self.ui.import_staging_directory_push_button.clicked.connect(self._import_staging_dir_clicked)
        self.ui.tdd_restart_push_button.clicked.connect(self._restart_scp)
        self.ui.push_button_get_ups.clicked.connect(self._get_ups)
        self.ui.get_listed_inputs_push_button.clicked.connect(self._get_input_information)
        self.ui.get_rtss_and_ct_push_button.clicked.connect(self._get_referenced_rtss_and_volumetric_images)
        self.ui.ups_response_tree_widget.setColumnCount(5)
        self.tdd_scp = None
        self.ui.soonest_date_time_edit.setDateTime(QDateTime.currentDateTime().addSecs(-3600))
        self.ui.latest_date_time_edit.setDateTime(QDateTime.currentDateTime().addSecs(3600))
        self.ui.step_status_combo_box.addItems(["SCHEDULED", "IN PROGRESS", "CANCELED", "COMPLETED", "ANY"])
        self.ui.subscribe_ups_checkbox.toggled.connect(self._toggle_subscription)
        self.watch_scu = None
        config_file = "tdd.toml"
        # TODO: command line argument specifying a different config file
        try:
            with open(config_file, "rb") as f:
                toml_dict = tomli.load(f)
            if "DEFAULT" in toml_dict:
                default_dict = toml_dict["DEFAULT"]

            try:
                if "ups_ae_title" in default_dict:
                    self.ui.ups_ae_line_edit.setText(default_dict["ups_ae_title"])
                    logging.debug("parsed ups_ae_title")
                if "qr_ae_title" in default_dict:
                    self.ui.qr_ae_line_edit.setText(default_dict["qr_ae_title"])
                if "ae_title" in default_dict:
                    self.ui.tdd_ae_line_edit.setText(default_dict["ae_title"])
                if "import_staging_directory" in default_dict:
                    raw_staging_dir = default_dict["import_staging_directory"]
                    expanded_staging_dir = str(Path(raw_staging_dir).expanduser())
                    self.ui.import_staging_dir_line_edit.setText(expanded_staging_dir)
                if "machine" in default_dict:
                    machine_name = default_dict["machine"]
                    self.ui.machine_name_line_edit.setText(machine_name)
                logging.warning("Completed Parsing of " + config_file)
            except Exception:
                warning_msg = f"Difficulty parsing config file {config_file}"
                logging.warning(warning_msg)
        except OSError as config_file_error:
            logging.exception("Problem parsing config file: " + config_file_error)
        self.ups_dataset_dict = dict()
        try:
            if "ae_title" in default_dict and "import_staging_directory" in default_dict:
                self._restart_scp()
        except Exception:
            logging.error(
                "Unable to start SCP for this Emulator, check AE Title in defaults configuration and ApplicationEntities.json"
            )

    @Slot()
    def _get_input_information(self):
        fallback_retrieve_ae_title = self.ui.qr_ae_line_edit.text()
        for ups_uid, ups_ds in self.ups_dataset_dict.items():
            debug_message = f"Retrieving inputs for UPS with UID: {ups_uid}"
            logging.debug(debug_message)
            # retrieve AE title for OST is embedded in the input information sequence
            # provide the import staging/cache directory so cmove_inputs can skip instances already present.
            cmove_inputs.cmove_inputs(
                ups_ds,
                self.ui.tdd_ae_line_edit.text(),
                self.ui.import_staging_dir_line_edit.text(),
                fallback_retrieve_ae_title=fallback_retrieve_ae_title,
            )

    @Slot()
    def _get_referenced_rtss_and_volumetric_images(self):
        cache_path = Path(self.ui.import_staging_dir_line_edit.text())
        retrieve_ae_title = self.ui.qr_ae_line_edit.text()
        dest_ae_title = self.ui.tdd_ae_line_edit.text()
        for ups_uid, ups_ds in self.ups_dataset_dict.items():
            debug_message = f"Searching inputs for plan in UPS with UID: {ups_uid}"
            logging.debug(debug_message)
            sop_dict = sop_references_in_input_info(ups_ds)
            for sop_uid, sop_class in sop_dict.items():
                if sop_class == uid.RTPlanStorage or sop_class == uid.RTIonPlanStorage:
                    if iod_in_staging_directory(sop_uid, cache_path):
                        plan_path = list(cache_path.glob(f"**/*.{sop_uid}.dcm"))[0]
                        plan_ds = dcmread(plan_path, force=True)
                        patient_id = plan_ds.PatientID
                        study_uid = plan_ds.StudyInstanceUID
                        series_uid = plan_ds.SeriesInstanceUID
                        try:
                            referenced_rtss_seq = plan_ds.ReferencedStructureSetSequence
                            referenced_rtss_seq_item = referenced_rtss_seq[0]
                            rtss_sop_instance_uid = referenced_rtss_seq_item.ReferencedSOPInstanceUID
                            if not iod_in_staging_directory(rtss_sop_instance_uid, ""):
                                cmove_inputs.cmove_specific_input(
                                    retrieve_ae_title=retrieve_ae_title,
                                    dest_ae_title=dest_ae_title,
                                    patient_id=patient_id,
                                    study_uid=study_uid,
                                    series_uid=series_uid,
                                    instance_uid=rtss_sop_instance_uid,
                                )
                            path_list = list(cache_path.glob(f"**/*.{rtss_sop_instance_uid}.dcm"))
                            if len(path_list) == 0:
                                warning_message = f"Unable to find RT SS {rtss_sop_instance_uid} in cache {cache_path}"
                                logging.warning(warning_message)
                                return

                            rt_ss_path = path_list[0]

                            rtss_ds = dcmread(rt_ss_path, force=True)
                            warning_message = f"No RT Referenced Series in RT SS {rtss_sop_instance_uid}"
                            if "ReferencedFrameOfReference" in rtss_ds:
                                for referenced_frame_of_reference_sequence_item in rtss_ds.ReferencedFrameOfReferenceSequence:
                                    if "RTReferencedStudySequence" in referenced_frame_of_reference_sequence_item:
                                        for (
                                            rt_referenced_study_seq_item
                                        ) in referenced_frame_of_reference_sequence_item.RTReferencedStudySequence:
                                            for (
                                                rt_referenced_series_seq_item
                                            ) in rt_referenced_study_seq_item.RTReferencedSeriesSequence:
                                                series_uid = rt_referenced_series_seq_item.SeriesInstanceUID
                                                study_uid = study_uid_for_series_from_common_instance_reference(
                                                    rtss_ds, series_uid
                                                )
                                                cmove_inputs.cmove_specific_input(
                                                    retrieve_ae_title=retrieve_ae_title,
                                                    dest_ae_title=dest_ae_title,
                                                    patient_id=patient_id,
                                                    study_uid=study_uid,
                                                    series_uid=series_uid,
                                                    instance_uid=None,
                                                )
                                    else:
                                        logging.warning(warning_message)
                            else:
                                logging.warning(warning_message)

                        except AttributeError | IndexError:
                            warning_message = f"No RT SS for Plan {sop_uid}"
                            logging.warning(warning_message)

        pass

    @Slot()
    def _import_staging_dir_clicked(self):
        dialog = QFileDialog(self, "Import Staging Dir")
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        dialog.setLabelText(QFileDialog.Accept, "Select")
        if dialog.exec_() == QFileDialog.Accepted:
            file_name = dialog.selectedFiles()[0]
        if file_name:
            path = Path(file_name)
        self.ui.import_staging_dir_line_edit.setText(str(path))

    @Slot()
    def _toggle_subscription(self):
        if self.ui.subscribe_ups_checkbox.checkState() == Qt.Checked:
            self._subscribe_to_ups()
        else:
            self._unsubscribe_from_ups()

    @Slot()
    def _restart_scp(self):
        tdd_scp_ae_title = self.ui.tdd_ae_line_edit.text()
        staging_dir = self.ui.import_staging_dir_line_edit.text()
        print(f"TDD AE Title: {tdd_scp_ae_title} using {staging_dir} for caching data")
        # TDD_SCP combines the NEVENT SCP and C-STORE SCP
        self.tdd_scp = PPVS_SCP(nevent_callback=self._nevent_callback, ae_title=tdd_scp_ae_title, store_directory=staging_dir)
        self.tdd_scp.run()
        self.watch_scu = WatchSCU(self.ui.tdd_ae_line_edit.text())
        upsscp_ae_title = self.ui.ups_ae_line_edit.text()
        ip_addr = tdwii_config.known_ae_ipaddr[upsscp_ae_title]
        port = tdwii_config.known_ae_port[upsscp_ae_title]
        self.watch_scu.set_subscription_ae(upsscp_ae_title, ip_addr=ip_addr, port=port)

    @Slot()
    def _get_ups(self, ups_uid: str = ""):
        # do C-FIND-RQ
        my_ae_title = self.ui.tdd_ae_line_edit.text()
        upsscp_ae_title = self.ui.ups_ae_line_edit.text()
        machine_name = self.ui.machine_name_line_edit.text()
        soonest_datetime_widget = self.ui.soonest_date_time_edit
        procedure_step_state = self.ui.step_status_combo_box.currentText()
        if procedure_step_state == "ANY":
            procedure_step_state = ""

        query_ds = create_ups_query(
            ups_uid=ups_uid,
            machine_name=machine_name,
            procedure_step_state=procedure_step_state,
            scheduled_no_sooner_than=soonest_datetime_widget.dateTime().toString("yyyyMMddhhmm"),
            scheduled_no_later_than=self.ui.latest_date_time_edit.dateTime().toString("yyyyMMddhhmm"),
        )
        responses = get_ups(query_ds, my_ae_title, upsscp_ae_title)

        self.ui.ups_response_tree_widget.clear()
        self.ups_dataset_dict.clear()
        if responses is None:
            logging.warning("No responses, nothing matched query")
            return
        for response_content in responses:
            ups_item = QTreeWidgetItem(self.ui.ups_response_tree_widget)
            context = build_context(response_content.SOPClassUID)
            abstract_syntax = str(context).splitlines()[0].split(sep=":")[1]
            ups_item.setText(0, abstract_syntax)
            ups_item.setText(1, str(response_content.PatientName))
            ups_item.setText(2, response_content.PatientID)
            ups_item.setText(3, response_content.ScheduledProcedureStepStartDateTime)
            ups_item.setText(4, response_content.WorklistLabel)
            self.ups_dataset_dict[str(response_content.SOPInstanceUID)] = response_content
            self._populate_tree_widget_item_from_dataset(ups_item, response_content)

        return

    def _subscribe_to_ups(self, match_on_step_state=False, match_on_beam_number=False) -> bool:
        if self.watch_scu is None:
            my_ae_title = self.ui.ppvs_ae_line_edit.text()
            watch_scu = WatchSCU(my_ae_title)
            upsscp_ae_title = self.ui.ups_ae_line_edit.text()
            ip_addr = tdwii_config.known_ae_ipaddr[upsscp_ae_title]
            port = tdwii_config.known_ae_port[upsscp_ae_title]
            watch_scu.set_subscription_ae(upsscp_ae_title, ip_addr=ip_addr, port=port)
        else:
            watch_scu = self.watch_scu

        matching_keys = None
        if match_on_beam_number or match_on_step_state:
            matching_keys = watch_scu.create_data_set(
                match_on_beam_number=match_on_beam_number, match_on_step_state=match_on_step_state
            )
        success = watch_scu.subscribe(matching_keys=matching_keys)
        if success and self.watch_scu is None:
            self.watch_scu = watch_scu
        return success

    def _unsubscribe_from_ups(self):
        if self.watch_scu is None:
            my_ae_title = self.ui.ppvs_ae_line_edit.text()
            watch_scu = WatchSCU(my_ae_title)
            upsscp_ae_title = self.ui.ups_ae_line_edit.text()
            ip_addr = tdwii_config.known_ae_ipaddr[upsscp_ae_title]
            port = tdwii_config.known_ae_port[upsscp_ae_title]

            watch_scu.set_subscription_ae(upsscp_ae_title, ip_addr=ip_addr, port=port)
        else:
            watch_scu = self.watch_scu

        matching_keys = None
        success = watch_scu.unsubscribe(matching_keys=matching_keys)
        if success and self.watch_scu is None:
            self.watch_scu = watch_scu
        return success

    def _nevent_callback(self, **kwargs):
        logger = None
        ups_uid = ""
        if "logger" in kwargs.keys():
            logger = kwargs["logger"]
        if logger:
            logger.info("nevent_cb invoked")
        event_type_id = 0  # not a valid type ID
        if logger:
            logger.info("TODO: Invoke application response appropriate to content of N-EVENT-REPORT-RQ")
        if "type_id" in kwargs.keys():
            event_type_id = kwargs["type_id"]
            if logger:
                logger.info(f"Event Type ID is: {event_type_id}")
        if "information_ds" in kwargs.keys():
            information_ds = kwargs["information_ds"]
            if logger:
                logger.info("Dataset in N-EVENT-REPORT-RQ: ")
                logger.info(f"{information_ds}")
            if "SOPInstanceUID" in information_ds:
                ups_uid = information_ds.SOPInstanceUID
        # TODO: replace if/elif with dict of {event_type_id,application_response_functions}
        if event_type_id == 1:
            if logger:
                logger.info("UPS State Report")
                logger.info("Probably time to do a C-FIND-RQ")
                self._get_ups(ups_uid=str(ups_uid))
        elif event_type_id == 2:
            if logger:
                logger.info("UPS Cancel Request")
                self.ui.ups_response_tree_widget.clear()
        elif event_type_id == 3:
            if logger:
                logger.info("UPS Progress Report")
                logger.info("Probably time to see if the Beam (number) changed, or if adaptation is taking or took place")
                self._get_ups(ups_uid=str(ups_uid))
        elif event_type_id == 4:
            if logger:
                logger.info("SCP Status Change")
                logger.info(
                    "Probably a good time to check if this is a Cold Start and then re-subscribe \
                        for specific UPS instances if this application has/had instance specific subscriptions"
                )
        elif event_type_id == 5:
            if logger:
                logger.info("UPS Assigned")
                logger.info(
                    "Not too interesting for TDW-II, UPS are typically assigned at the time of scheduling, \
                        but a matching class of machines might make for a different approach"
                )
        else:
            if logger:
                logger.warning(f"Unknown Event Type ID: {event_type_id}")

    def _populate_tree_widget_item_from_element(self, parent: QTreeWidgetItem | QTreeWidget, elem: DataElement):
        if elem.VR != VR.SQ:
            tree_child_item = QTreeWidgetItem(parent)
            tree_child_item.setFlags(Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            tree_child_item.setText(0, str(elem.tag))
            tree_child_item.setText(1, elem.name)
            if elem.VR not in [VR.OB, VR.OW, VR.OB_OW, VR.OD, VR.OF]:
                if elem.value is None:
                    tree_child_item.setText(2, "")
                else:
                    tree_child_item.setText(2, str(elem.value))
            else:
                logging.warning("Need to stash away OB/OW type values")
            tree_child_item.setText(3, str(elem.VR))
            tree_child_item.setText(4, elem.keyword)
        else:
            tree_child_item = QTreeWidgetItem(parent)
            tree_child_item.setText(0, str(elem.tag))
            tree_child_item.setText(1, elem.name)
            tree_child_item.setText(3, str(elem.VR))
            tree_child_item.setText(4, elem.keyword)
            seq_item_count = 0
            for seq_item in elem:
                seq_item_count += 1
                seq_child_item = QTreeWidgetItem(tree_child_item)
                seq_child_item.setText(0, str(elem.tag))
                seq_child_item.setText(1, elem.name)
                seq_child_item.setText(2, str(seq_item_count))
                seq_child_item.setText(3, str(elem.VR))
                seq_child_item.setText(4, elem.keyword)
                self._populate_tree_widget_item_from_dataset(seq_child_item, seq_item)

    def _populate_tree_widget_item_from_dataset(self, parent: QTreeWidgetItem | QTreeWidget, ds: Dataset):
        for elem in ds:
            if elem.VR != VR.SQ:
                tree_child_item = QTreeWidgetItem(parent)
                tree_child_item.setFlags(Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                tree_child_item.setText(0, str(elem.tag))
                tree_child_item.setText(1, elem.name)
                if elem.VR not in [VR.OB, VR.OW, VR.OB_OW, VR.OD, VR.OF]:
                    if elem.value is None:
                        tree_child_item.setText(2, "")
                    else:
                        tree_child_item.setText(2, str(elem.value))
                else:
                    logging.warning("Need to stash away OB/OW type values")
                tree_child_item.setText(3, str(elem.VR))
                tree_child_item.setText(4, elem.keyword)
            else:
                tree_child_item = QTreeWidgetItem(parent)
                tree_child_item.setText(0, str(elem.tag))
                tree_child_item.setText(1, elem.name)
                tree_child_item.setText(3, str(elem.VR))
                tree_child_item.setText(4, elem.keyword)
                seq_item_count = 0
                for seq_item in elem:
                    seq_item_count += 1
                    seq_child_item = QTreeWidgetItem(tree_child_item)
                    seq_child_item.setText(0, str(elem.tag))
                    seq_child_item.setText(1, elem.name)
                    seq_child_item.setText(2, str(seq_item_count))
                    seq_child_item.setText(3, str(elem.VR))
                    seq_child_item.setText(4, elem.keyword)
                    self._populate_tree_widget_item_from_dataset(seq_child_item, seq_item)


def iod_in_staging_directory(sop_instance_uid: str, staging_directory: Path | str) -> bool:
    """Search the staging directory for a file that matches the SOP Instance UID
    Will do a recursive search.

    Args:
        sop_instance_uid (str): _description_
        staging_directory (Path | str): _description_

    Returns:
        bool: _description_
    """
    search_path = Path(staging_directory)
    search_pattern = f"**/*.{sop_instance_uid}.dcm"
    found_instances = list(search_path.glob(search_pattern))
    if found_instances is not None and len(found_instances) > 0:
        return True
    return False


def sop_references_in_input_info(ups_ds: Dataset) -> dict[uid.UID | str, uid.UID | str]:
    sop_ref_dict = dict()
    iis = ups_ds.InputInformationSequence
    for iis_index in range(len(iis)):
        iis_item = iis[iis_index]
        ref_instance_seq = iis_item.ReferencedSOPSequence
        for ref_instance_index in range(len(ref_instance_seq)):
            instance_uid = ref_instance_seq[ref_instance_index].ReferencedSOPInstanceUID
            class_uid = ref_instance_seq[ref_instance_index].ReferencedSOPClassUID
            sop_ref_dict[instance_uid] = class_uid
    return sop_ref_dict


def study_uid_for_series_from_common_instance_reference(iod_ds: Dataset, series_uid: uid.UID | str) -> uid.UID | None:
    iod_study_uid = iod_ds.StudyInstanceUID
    if "ReferencedSeriesSequence" in iod_ds:
        if series_uid in [x.SeriesInstanceUID for x in iod_ds.ReferencedSeriesSequence]:
            return iod_study_uid
    if "StudiesContainingOtherReferencedInstancesSequence" in iod_ds:
        for other_study in iod_ds.StudiesContainingOtherReferencedInstancesSequence:
            if series_uid in [x.SeriesInstanceUID for x in other_study]:
                other_study_uid = other_study.StudyInstanceUID
                return other_study_uid
    return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tdwii_config.load_ae_config()
    widget = TDD_Widget()

    widget.show()
    sys.exit(app.exec())
