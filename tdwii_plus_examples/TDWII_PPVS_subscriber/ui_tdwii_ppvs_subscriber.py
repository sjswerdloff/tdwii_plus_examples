# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tdwii_ppvs_subscriber.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_MainPPVSSubscriberWidget(object):
    def setupUi(self, MainPPVSSubscriberWidget):
        if not MainPPVSSubscriberWidget.objectName():
            MainPPVSSubscriberWidget.setObjectName(u"MainPPVSSubscriberWidget")
        MainPPVSSubscriberWidget.resize(800, 659)
        self.group_box_aes_and_machine = QGroupBox(MainPPVSSubscriberWidget)
        self.group_box_aes_and_machine.setObjectName(u"group_box_aes_and_machine")
        self.group_box_aes_and_machine.setGeometry(QRect(30, 30, 622, 70))
        self.gridLayout = QGridLayout(self.group_box_aes_and_machine)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ups_ae_label = QLabel(self.group_box_aes_and_machine)
        self.ups_ae_label.setObjectName(u"ups_ae_label")

        self.gridLayout.addWidget(self.ups_ae_label, 0, 0, 1, 1)

        self.ups_ae_line_edit = QLineEdit(self.group_box_aes_and_machine)
        self.ups_ae_line_edit.setObjectName(u"ups_ae_line_edit")

        self.gridLayout.addWidget(self.ups_ae_line_edit, 0, 1, 1, 1)

        self.qr_ae_label = QLabel(self.group_box_aes_and_machine)
        self.qr_ae_label.setObjectName(u"qr_ae_label")

        self.gridLayout.addWidget(self.qr_ae_label, 0, 2, 1, 1)

        self.qr_ae_line_edit = QLineEdit(self.group_box_aes_and_machine)
        self.qr_ae_line_edit.setObjectName(u"qr_ae_line_edit")

        self.gridLayout.addWidget(self.qr_ae_line_edit, 0, 3, 1, 1)

        self.machine_name_label = QLabel(self.group_box_aes_and_machine)
        self.machine_name_label.setObjectName(u"machine_name_label")

        self.gridLayout.addWidget(self.machine_name_label, 0, 4, 1, 1)

        self.machine_name_line_edit = QLineEdit(self.group_box_aes_and_machine)
        self.machine_name_line_edit.setObjectName(u"machine_name_line_edit")

        self.gridLayout.addWidget(self.machine_name_line_edit, 0, 5, 1, 1)

        self.group_box_ppvs_scp = QGroupBox(MainPPVSSubscriberWidget)
        self.group_box_ppvs_scp.setObjectName(u"group_box_ppvs_scp")
        self.group_box_ppvs_scp.setGeometry(QRect(20, 120, 496, 171))
        self.gridLayout_2 = QGridLayout(self.group_box_ppvs_scp)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.group_box_ppvs_scp)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.ppvs_ae_line_edit = QLineEdit(self.group_box_ppvs_scp)
        self.ppvs_ae_line_edit.setObjectName(u"ppvs_ae_line_edit")

        self.gridLayout_2.addWidget(self.ppvs_ae_line_edit, 0, 2, 1, 1)

        self.import_staging_dir_line_edit = QLineEdit(self.group_box_ppvs_scp)
        self.import_staging_dir_line_edit.setObjectName(u"import_staging_dir_line_edit")

        self.gridLayout_2.addWidget(self.import_staging_dir_line_edit, 2, 0, 1, 4)

        self.ppvs_ae_label = QLabel(self.group_box_ppvs_scp)
        self.ppvs_ae_label.setObjectName(u"ppvs_ae_label")

        self.gridLayout_2.addWidget(self.ppvs_ae_label, 0, 0, 1, 1)

        self.ppvs_restart_push_button = QPushButton(self.group_box_ppvs_scp)
        self.ppvs_restart_push_button.setObjectName(u"ppvs_restart_push_button")

        self.gridLayout_2.addWidget(self.ppvs_restart_push_button, 3, 3, 1, 1)

        self.import_staging_directory_push_button = QPushButton(self.group_box_ppvs_scp)
        self.import_staging_directory_push_button.setObjectName(u"import_staging_directory_push_button")

        self.gridLayout_2.addWidget(self.import_staging_directory_push_button, 1, 2, 1, 1)

        self.subscribe_ups_checkbox = QCheckBox(self.group_box_ppvs_scp)
        self.subscribe_ups_checkbox.setObjectName(u"subscribe_ups_checkbox")

        self.gridLayout_2.addWidget(self.subscribe_ups_checkbox, 3, 0, 1, 1)

        self.auto_download_checkbox = QCheckBox(self.group_box_ppvs_scp)
        self.auto_download_checkbox.setObjectName(u"auto_download_checkbox")

        self.gridLayout_2.addWidget(self.auto_download_checkbox, 3, 1, 1, 2)

        self.group_box_cfind_request_and_response = QGroupBox(MainPPVSSubscriberWidget)
        self.group_box_cfind_request_and_response.setObjectName(u"group_box_cfind_request_and_response")
        self.group_box_cfind_request_and_response.setGeometry(QRect(20, 300, 751, 243))
        self.gridLayout_3 = QGridLayout(self.group_box_cfind_request_and_response)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scheduled_date_label = QLabel(self.group_box_cfind_request_and_response)
        self.scheduled_date_label.setObjectName(u"scheduled_date_label")

        self.gridLayout_3.addWidget(self.scheduled_date_label, 0, 0, 1, 1)

        self.ups_response_tree_widget = QTreeWidget(self.group_box_cfind_request_and_response)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.ups_response_tree_widget.setHeaderItem(__qtreewidgetitem)
        self.ups_response_tree_widget.setObjectName(u"ups_response_tree_widget")

        self.gridLayout_3.addWidget(self.ups_response_tree_widget, 0, 1, 7, 1)

        self.soonest_date_time_edit = QDateTimeEdit(self.group_box_cfind_request_and_response)
        self.soonest_date_time_edit.setObjectName(u"soonest_date_time_edit")
        self.soonest_date_time_edit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.soonest_date_time_edit, 1, 0, 1, 1)

        self.schedule_to_label = QLabel(self.group_box_cfind_request_and_response)
        self.schedule_to_label.setObjectName(u"schedule_to_label")

        self.gridLayout_3.addWidget(self.schedule_to_label, 2, 0, 1, 1)

        self.latest_date_time_edit = QDateTimeEdit(self.group_box_cfind_request_and_response)
        self.latest_date_time_edit.setObjectName(u"latest_date_time_edit")
        self.latest_date_time_edit.setEnabled(True)
        self.latest_date_time_edit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.latest_date_time_edit, 3, 0, 1, 1)

        self.step_status_label = QLabel(self.group_box_cfind_request_and_response)
        self.step_status_label.setObjectName(u"step_status_label")

        self.gridLayout_3.addWidget(self.step_status_label, 4, 0, 1, 1)

        self.step_status_combo_box = QComboBox(self.group_box_cfind_request_and_response)
        self.step_status_combo_box.setObjectName(u"step_status_combo_box")
        self.step_status_combo_box.setMaxVisibleItems(6)
        self.step_status_combo_box.setMaxCount(6)

        self.gridLayout_3.addWidget(self.step_status_combo_box, 5, 0, 1, 1)

        self.push_button_get_ups = QPushButton(self.group_box_cfind_request_and_response)
        self.push_button_get_ups.setObjectName(u"push_button_get_ups")

        self.gridLayout_3.addWidget(self.push_button_get_ups, 6, 0, 1, 1)

        self.groupBox = QGroupBox(MainPPVSSubscriberWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 550, 361, 80))
        self.get_listed_inputs_push_button = QPushButton(self.groupBox)
        self.get_listed_inputs_push_button.setObjectName(u"get_listed_inputs_push_button")
        self.get_listed_inputs_push_button.setGeometry(QRect(30, 30, 131, 32))
        self.get_rtss_and_ct_push_button = QPushButton(self.groupBox)
        self.get_rtss_and_ct_push_button.setObjectName(u"get_rtss_and_ct_push_button")
        self.get_rtss_and_ct_push_button.setGeometry(QRect(170, 30, 161, 32))

        self.retranslateUi(MainPPVSSubscriberWidget)

        QMetaObject.connectSlotsByName(MainPPVSSubscriberWidget)
    # setupUi

    def retranslateUi(self, MainPPVSSubscriberWidget):
        MainPPVSSubscriberWidget.setWindowTitle(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Widget", None))
        self.group_box_aes_and_machine.setTitle(QCoreApplication.translate("MainPPVSSubscriberWidget", u"group_box_aes_and_machine_name", None))
        self.ups_ae_label.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"UPS AE", None))
        self.qr_ae_label.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"QR AE", None))
        self.machine_name_label.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Machine Name", None))
        self.group_box_ppvs_scp.setTitle(QCoreApplication.translate("MainPPVSSubscriberWidget", u"ppvs_scp_group_box", None))
        self.label.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Import Staging Directory:", None))
        self.ppvs_ae_label.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Event and Store SCP AE", None))
        self.ppvs_restart_push_button.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Restart SCP", None))
        self.import_staging_directory_push_button.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Choose Staging Directory", None))
        self.subscribe_ups_checkbox.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Subscribe to UPS", None))
        self.auto_download_checkbox.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Auto Download", None))
        self.group_box_cfind_request_and_response.setTitle(QCoreApplication.translate("MainPPVSSubscriberWidget", u"group_box_cfind_request_and_response", None))
        self.scheduled_date_label.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"scheduled date range", None))
        self.schedule_to_label.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"to", None))
        self.step_status_label.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Procedure Step Status", None))
        self.push_button_get_ups.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Get UPS", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainPPVSSubscriberWidget", u"group_box_get_reference_data", None))
        self.get_listed_inputs_push_button.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Get Listed Inputs", None))
        self.get_rtss_and_ct_push_button.setText(QCoreApplication.translate("MainPPVSSubscriberWidget", u"Get RTSS and CT", None))
    # retranslateUi

