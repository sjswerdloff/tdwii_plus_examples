# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tdd.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QApplication,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHeaderView,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QTreeWidget,
    QTreeWidgetItem,
    QWidget,
)


class Ui_MainTDDWidget(object):
    def setupUi(self, MainTDDWidget):
        if not MainTDDWidget.objectName():
            MainTDDWidget.setObjectName("MainTDDWidget")
        MainTDDWidget.resize(786, 642)
        self.formLayout = QFormLayout(MainTDDWidget)
        self.formLayout.setObjectName("formLayout")
        self.group_box_aes_and_machine = QGroupBox(MainTDDWidget)
        self.group_box_aes_and_machine.setObjectName("group_box_aes_and_machine")
        self.gridLayout = QGridLayout(self.group_box_aes_and_machine)
        self.gridLayout.setObjectName("gridLayout")
        self.machine_name_label = QLabel(self.group_box_aes_and_machine)
        self.machine_name_label.setObjectName("machine_name_label")

        self.gridLayout.addWidget(self.machine_name_label, 0, 4, 1, 1)

        self.machine_name_line_edit = QLineEdit(self.group_box_aes_and_machine)
        self.machine_name_line_edit.setObjectName("machine_name_line_edit")

        self.gridLayout.addWidget(self.machine_name_line_edit, 0, 5, 1, 1)

        self.qr_ae_label = QLabel(self.group_box_aes_and_machine)
        self.qr_ae_label.setObjectName("qr_ae_label")

        self.gridLayout.addWidget(self.qr_ae_label, 0, 2, 1, 1)

        self.qr_ae_line_edit = QLineEdit(self.group_box_aes_and_machine)
        self.qr_ae_line_edit.setObjectName("qr_ae_line_edit")

        self.gridLayout.addWidget(self.qr_ae_line_edit, 0, 3, 1, 1)

        self.ups_ae_line_edit = QLineEdit(self.group_box_aes_and_machine)
        self.ups_ae_line_edit.setObjectName("ups_ae_line_edit")

        self.gridLayout.addWidget(self.ups_ae_line_edit, 0, 1, 1, 1)

        self.ups_ae_label = QLabel(self.group_box_aes_and_machine)
        self.ups_ae_label.setObjectName("ups_ae_label")

        self.gridLayout.addWidget(self.ups_ae_label, 0, 0, 1, 1)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.group_box_aes_and_machine)

        self.group_box_tdd_scp = QGroupBox(MainTDDWidget)
        self.group_box_tdd_scp.setObjectName("group_box_tdd_scp")
        self.gridLayout_2 = QGridLayout(self.group_box_tdd_scp)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QLabel(self.group_box_tdd_scp)
        self.label.setObjectName("label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.tdd_ae_line_edit = QLineEdit(self.group_box_tdd_scp)
        self.tdd_ae_line_edit.setObjectName("tdd_ae_line_edit")

        self.gridLayout_2.addWidget(self.tdd_ae_line_edit, 0, 2, 1, 1)

        self.import_staging_dir_line_edit = QLineEdit(self.group_box_tdd_scp)
        self.import_staging_dir_line_edit.setObjectName("import_staging_dir_line_edit")

        self.gridLayout_2.addWidget(self.import_staging_dir_line_edit, 2, 0, 1, 4)

        self.tdd_ae_label = QLabel(self.group_box_tdd_scp)
        self.tdd_ae_label.setObjectName("tdd_ae_label")

        self.gridLayout_2.addWidget(self.tdd_ae_label, 0, 0, 1, 1)

        self.tdd_restart_push_button = QPushButton(self.group_box_tdd_scp)
        self.tdd_restart_push_button.setObjectName("tdd_restart_push_button")

        self.gridLayout_2.addWidget(self.tdd_restart_push_button, 3, 3, 1, 1)

        self.import_staging_directory_push_button = QPushButton(self.group_box_tdd_scp)
        self.import_staging_directory_push_button.setObjectName("import_staging_directory_push_button")

        self.gridLayout_2.addWidget(self.import_staging_directory_push_button, 1, 2, 1, 1)

        self.subscribe_ups_checkbox = QCheckBox(self.group_box_tdd_scp)
        self.subscribe_ups_checkbox.setObjectName("subscribe_ups_checkbox")

        self.gridLayout_2.addWidget(self.subscribe_ups_checkbox, 3, 0, 1, 1)

        self.auto_download_checkbox = QCheckBox(self.group_box_tdd_scp)
        self.auto_download_checkbox.setObjectName("auto_download_checkbox")

        self.gridLayout_2.addWidget(self.auto_download_checkbox, 3, 1, 1, 2)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.group_box_tdd_scp)

        self.group_box_cfind_request_and_response = QGroupBox(MainTDDWidget)
        self.group_box_cfind_request_and_response.setObjectName("group_box_cfind_request_and_response")
        self.gridLayout_3 = QGridLayout(self.group_box_cfind_request_and_response)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scheduled_date_label = QLabel(self.group_box_cfind_request_and_response)
        self.scheduled_date_label.setObjectName("scheduled_date_label")

        self.gridLayout_3.addWidget(self.scheduled_date_label, 0, 0, 1, 1)

        self.soonest_date_time_edit = QDateTimeEdit(self.group_box_cfind_request_and_response)
        self.soonest_date_time_edit.setObjectName("soonest_date_time_edit")
        self.soonest_date_time_edit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.soonest_date_time_edit, 1, 0, 1, 1)

        self.latest_date_time_edit = QDateTimeEdit(self.group_box_cfind_request_and_response)
        self.latest_date_time_edit.setObjectName("latest_date_time_edit")
        self.latest_date_time_edit.setEnabled(True)
        self.latest_date_time_edit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.latest_date_time_edit, 3, 0, 1, 1)

        self.push_button_get_ups = QPushButton(self.group_box_cfind_request_and_response)
        self.push_button_get_ups.setObjectName("push_button_get_ups")

        self.gridLayout_3.addWidget(self.push_button_get_ups, 6, 0, 1, 1)

        self.step_status_combo_box = QComboBox(self.group_box_cfind_request_and_response)
        self.step_status_combo_box.setObjectName("step_status_combo_box")
        self.step_status_combo_box.setMaxVisibleItems(6)
        self.step_status_combo_box.setMaxCount(6)

        self.gridLayout_3.addWidget(self.step_status_combo_box, 5, 0, 1, 1)

        self.step_status_label = QLabel(self.group_box_cfind_request_and_response)
        self.step_status_label.setObjectName("step_status_label")

        self.gridLayout_3.addWidget(self.step_status_label, 4, 0, 1, 1)

        self.schedule_to_label = QLabel(self.group_box_cfind_request_and_response)
        self.schedule_to_label.setObjectName("schedule_to_label")

        self.gridLayout_3.addWidget(self.schedule_to_label, 2, 0, 1, 1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.group_box_cfind_request_and_response)

        self.scrollArea = QScrollArea(MainTDDWidget)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(500, 300))
        self.scrollArea.setLayoutDirection(Qt.RightToLeft)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 538, 306))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ups_response_tree_widget = QTreeWidget(self.scrollAreaWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, "Tag")
        self.ups_response_tree_widget.setHeaderItem(__qtreewidgetitem)
        self.ups_response_tree_widget.setObjectName("ups_response_tree_widget")
        self.ups_response_tree_widget.setLayoutDirection(Qt.LeftToRight)
        self.ups_response_tree_widget.setAlternatingRowColors(True)
        self.ups_response_tree_widget.setSortingEnabled(False)
        self.ups_response_tree_widget.setWordWrap(False)
        self.ups_response_tree_widget.setColumnCount(5)
        self.ups_response_tree_widget.header().setProperty("showSortIndicator", False)
        self.ups_response_tree_widget.header().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.ups_response_tree_widget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.scrollArea)

        self.groupBox = QGroupBox(MainTDDWidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.get_listed_inputs_push_button = QPushButton(self.groupBox)
        self.get_listed_inputs_push_button.setObjectName("get_listed_inputs_push_button")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.get_listed_inputs_push_button)

        self.get_rtss_and_ct_push_button = QPushButton(self.groupBox)
        self.get_rtss_and_ct_push_button.setObjectName("get_rtss_and_ct_push_button")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.get_rtss_and_ct_push_button)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.groupBox)

        self.retranslateUi(MainTDDWidget)

        QMetaObject.connectSlotsByName(MainTDDWidget)

    # setupUi

    def retranslateUi(self, MainTDDWidget):
        MainTDDWidget.setWindowTitle(QCoreApplication.translate("MainTDDWidget", "Treatment Delivery Device Emulator", None))
        self.group_box_aes_and_machine.setTitle(
            QCoreApplication.translate("MainTDDWidget", "Remote System Configuration", None)
        )
        self.machine_name_label.setText(QCoreApplication.translate("MainTDDWidget", "Machine Name", None))
        self.qr_ae_label.setText(QCoreApplication.translate("MainTDDWidget", "QR AE", None))
        self.ups_ae_label.setText(QCoreApplication.translate("MainTDDWidget", "UPS AE", None))
        self.group_box_tdd_scp.setTitle(QCoreApplication.translate("MainTDDWidget", "PPVS Configuration", None))
        self.label.setText(QCoreApplication.translate("MainTDDWidget", "Import Staging Directory:", None))
        self.tdd_ae_label.setText(QCoreApplication.translate("MainTDDWidget", "TDD Event and Store SCP AE", None))
        self.tdd_restart_push_button.setText(QCoreApplication.translate("MainTDDWidget", "Restart SCP", None))
        self.import_staging_directory_push_button.setText(
            QCoreApplication.translate("MainTDDWidget", "Choose Staging Directory", None)
        )
        self.subscribe_ups_checkbox.setText(QCoreApplication.translate("MainTDDWidget", "Subscribe to UPS", None))
        self.auto_download_checkbox.setText(QCoreApplication.translate("MainTDDWidget", "Auto Download", None))
        self.group_box_cfind_request_and_response.setTitle(
            QCoreApplication.translate("MainTDDWidget", "UPS Query Specification", None)
        )
        self.scheduled_date_label.setText(QCoreApplication.translate("MainTDDWidget", "scheduled date range", None))
        self.push_button_get_ups.setText(QCoreApplication.translate("MainTDDWidget", "Get UPS", None))
        self.step_status_label.setText(QCoreApplication.translate("MainTDDWidget", "Procedure Step Status", None))
        self.schedule_to_label.setText(QCoreApplication.translate("MainTDDWidget", "to", None))
        ___qtreewidgetitem = self.ups_response_tree_widget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainTDDWidget", "Keyword", None))
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainTDDWidget", "VR", None))
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainTDDWidget", "Value", None))
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainTDDWidget", "Name", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainTDDWidget", "Reference Data Retrieval", None))
        self.get_listed_inputs_push_button.setText(QCoreApplication.translate("MainTDDWidget", "Get Listed Inputs", None))
        self.get_rtss_and_ct_push_button.setText(QCoreApplication.translate("MainTDDWidget", "Get RTSS and CT", None))

    # retranslateUi
