# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
    QApplication,
    QCheckBox,
    QDateTimeEdit,
    QDoubleSpinBox,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QListView,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_MainBDIWidget(object):
    def setupUi(self, MainBDIWidget):
        if not MainBDIWidget.objectName():
            MainBDIWidget.setObjectName("MainBDIWidget")
        MainBDIWidget.resize(600, 600)
        self.verticalLayout_2 = QVBoxLayout(MainBDIWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.group_box_main = QGroupBox(MainBDIWidget)
        self.group_box_main.setObjectName("group_box_main")
        self.gridLayout_5 = QGridLayout(self.group_box_main)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_move_ae_title = QLabel(self.group_box_main)
        self.label_move_ae_title.setObjectName("label_move_ae_title")

        self.gridLayout_5.addWidget(self.label_move_ae_title, 0, 0, 1, 1)

        self.line_edit_move_scp_ae_title = QLineEdit(self.group_box_main)
        self.line_edit_move_scp_ae_title.setObjectName("line_edit_move_scp_ae_title")

        self.gridLayout_5.addWidget(self.line_edit_move_scp_ae_title, 0, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.group_box_main)

        self.group_box_plan_selection = QGroupBox(MainBDIWidget)
        self.group_box_plan_selection.setObjectName("group_box_plan_selection")
        self.gridLayout_4 = QGridLayout(self.group_box_plan_selection)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineedit_plan_selector = QLineEdit(self.group_box_plan_selection)
        self.lineedit_plan_selector.setObjectName("lineedit_plan_selector")

        self.gridLayout_4.addWidget(self.lineedit_plan_selector, 0, 1, 1, 1)

        self.label_plan_selector = QLabel(self.group_box_plan_selection)
        self.label_plan_selector.setObjectName("label_plan_selector")

        self.gridLayout_4.addWidget(self.label_plan_selector, 0, 0, 1, 1)

        self.push_button_plan_finder = QPushButton(self.group_box_plan_selection)
        self.push_button_plan_finder.setObjectName("push_button_plan_finder")

        self.gridLayout_4.addWidget(self.push_button_plan_finder, 0, 2, 1, 1)

        self.push_button_send_plan = QPushButton(self.group_box_plan_selection)
        self.push_button_send_plan.setObjectName("push_button_send_plan")

        self.gridLayout_4.addWidget(self.push_button_send_plan, 0, 3, 1, 1)

        self.verticalLayout_2.addWidget(self.group_box_plan_selection)

        self.group_box_bdi_variables = QGroupBox(MainBDIWidget)
        self.group_box_bdi_variables.setObjectName("group_box_bdi_variables")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_box_bdi_variables.sizePolicy().hasHeightForWidth())
        self.group_box_bdi_variables.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.group_box_bdi_variables)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.list_view_treatment_records = QListView(self.group_box_bdi_variables)
        self.list_view_treatment_records.setObjectName("list_view_treatment_records")

        self.gridLayout_3.addWidget(self.list_view_treatment_records, 1, 0, 1, 1)

        self.label_fraction_number = QLabel(self.group_box_bdi_variables)
        self.label_fraction_number.setObjectName("label_fraction_number")

        self.gridLayout_3.addWidget(self.label_fraction_number, 0, 0, 1, 1)

        self.push_button_load_treatment_records = QPushButton(self.group_box_bdi_variables)
        self.push_button_load_treatment_records.setObjectName("push_button_load_treatment_records")

        self.gridLayout_3.addWidget(self.push_button_load_treatment_records, 1, 1, 1, 1)

        self.double_spin_box_fraction_number = QDoubleSpinBox(self.group_box_bdi_variables)
        self.double_spin_box_fraction_number.setObjectName("double_spin_box_fraction_number")
        self.double_spin_box_fraction_number.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.double_spin_box_fraction_number.setDecimals(0)
        self.double_spin_box_fraction_number.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.double_spin_box_fraction_number, 0, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.group_box_bdi_variables)

        self.group_box_bdi_output = QGroupBox(MainBDIWidget)
        self.group_box_bdi_output.setObjectName("group_box_bdi_output")
        self.gridLayout_2 = QGridLayout(self.group_box_bdi_output)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_edit_bdi_filename = QLineEdit(self.group_box_bdi_output)
        self.line_edit_bdi_filename.setObjectName("line_edit_bdi_filename")

        self.gridLayout_2.addWidget(self.line_edit_bdi_filename, 1, 2, 1, 1)

        self.push_button_bdi_dir_finder = QPushButton(self.group_box_bdi_output)
        self.push_button_bdi_dir_finder.setObjectName("push_button_bdi_dir_finder")

        self.gridLayout_2.addWidget(self.push_button_bdi_dir_finder, 0, 3, 1, 1)

        self.lineedit_bdidir_selector = QLineEdit(self.group_box_bdi_output)
        self.lineedit_bdidir_selector.setObjectName("lineedit_bdidir_selector")

        self.gridLayout_2.addWidget(self.lineedit_bdidir_selector, 0, 1, 1, 2)

        self.label_bdi_output_dir = QLabel(self.group_box_bdi_output)
        self.label_bdi_output_dir.setObjectName("label_bdi_output_dir")

        self.gridLayout_2.addWidget(self.label_bdi_output_dir, 0, 0, 1, 1)

        self.checkbox_custom_bdi_filename = QCheckBox(self.group_box_bdi_output)
        self.checkbox_custom_bdi_filename.setObjectName("checkbox_custom_bdi_filename")

        self.gridLayout_2.addWidget(self.checkbox_custom_bdi_filename, 1, 0, 1, 2)

        self.push_button_export_bdi = QPushButton(self.group_box_bdi_output)
        self.push_button_export_bdi.setObjectName("push_button_export_bdi")

        self.gridLayout_2.addWidget(self.push_button_export_bdi, 2, 3, 1, 1)

        self.verticalLayout_2.addWidget(self.group_box_bdi_output)

        self.group_box_ups = QGroupBox(MainBDIWidget)
        self.group_box_ups.setObjectName("group_box_ups")
        self.gridLayout = QGridLayout(self.group_box_ups)
        self.gridLayout.setObjectName("gridLayout")
        self.datetime_edit_scheduled_datetime = QDateTimeEdit(self.group_box_ups)
        self.datetime_edit_scheduled_datetime.setObjectName("datetime_edit_scheduled_datetime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.datetime_edit_scheduled_datetime.sizePolicy().hasHeightForWidth())
        self.datetime_edit_scheduled_datetime.setSizePolicy(sizePolicy1)
        self.datetime_edit_scheduled_datetime.setDateTime(QDateTime(QDate(2023, 9, 1), QTime(0, 0, 0)))
        self.datetime_edit_scheduled_datetime.setCalendarPopup(True)

        self.gridLayout.addWidget(self.datetime_edit_scheduled_datetime, 1, 1, 1, 1)

        self.push_button_export_ups = QPushButton(self.group_box_ups)
        self.push_button_export_ups.setObjectName("push_button_export_ups")
        sizePolicy1.setHeightForWidth(self.push_button_export_ups.sizePolicy().hasHeightForWidth())
        self.push_button_export_ups.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.push_button_export_ups, 4, 2, 1, 1)

        self.label_tms_scp_ae_title = QLabel(self.group_box_ups)
        self.label_tms_scp_ae_title.setObjectName("label_tms_scp_ae_title")

        self.gridLayout.addWidget(self.label_tms_scp_ae_title, 4, 0, 1, 1)

        self.label_start_datetime = QLabel(self.group_box_ups)
        self.label_start_datetime.setObjectName("label_start_datetime")

        self.gridLayout.addWidget(self.label_start_datetime, 1, 0, 1, 1)

        self.checkbox_patient_photo = QCheckBox(self.group_box_ups)
        self.checkbox_patient_photo.setObjectName("checkbox_patient_photo")

        self.gridLayout.addWidget(self.checkbox_patient_photo, 1, 2, 1, 1)

        self.checkbox_setup_photos = QCheckBox(self.group_box_ups)
        self.checkbox_setup_photos.setObjectName("checkbox_setup_photos")
        self.checkbox_setup_photos.setEnabled(True)

        self.gridLayout.addWidget(self.checkbox_setup_photos, 2, 2, 1, 1)

        self.line_edit_tms_scp_ae_title = QLineEdit(self.group_box_ups)
        self.line_edit_tms_scp_ae_title.setObjectName("line_edit_tms_scp_ae_title")

        self.gridLayout.addWidget(self.line_edit_tms_scp_ae_title, 4, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.group_box_ups)

        self.retranslateUi(MainBDIWidget)

        QMetaObject.connectSlotsByName(MainBDIWidget)

    # setupUi

    def retranslateUi(self, MainBDIWidget):
        MainBDIWidget.setWindowTitle(
            QCoreApplication.translate("MainBDIWidget", "RT Beams Delivery Instruction and UPS Creator", None)
        )
        self.group_box_main.setTitle("")
        self.label_move_ae_title.setText(QCoreApplication.translate("MainBDIWidget", "Move/Retrieve AE Title", None))
        self.group_box_plan_selection.setTitle(QCoreApplication.translate("MainBDIWidget", "Plan Selection", None))
        self.label_plan_selector.setText(QCoreApplication.translate("MainBDIWidget", "RT (Ion) Plan", None))
        self.push_button_plan_finder.setText(QCoreApplication.translate("MainBDIWidget", "Find Plan", None))
        self.push_button_send_plan.setText(QCoreApplication.translate("MainBDIWidget", "Store Plan", None))
        self.group_box_bdi_variables.setTitle(QCoreApplication.translate("MainBDIWidget", "BDI Customization", None))
        self.label_fraction_number.setText(QCoreApplication.translate("MainBDIWidget", "Fraction #", None))
        # if QT_CONFIG(tooltip)
        self.push_button_load_treatment_records.setToolTip(
            QCoreApplication.translate(
                "MainBDIWidget",
                "<html><head/><body><p>Simulate a partially treated session.</p><p>The treatment records selected must reference the RT (Ion) Plan selected, and the Current Fraction Number in the RT (Ion) Beams Session records must match the Fraction # specified</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.push_button_load_treatment_records.setText(QCoreApplication.translate("MainBDIWidget", "Treatment Records", None))
        self.group_box_bdi_output.setTitle(QCoreApplication.translate("MainBDIWidget", "BDI Output", None))
        self.push_button_bdi_dir_finder.setText(QCoreApplication.translate("MainBDIWidget", "Choose BDI Dir", None))
        self.label_bdi_output_dir.setText(QCoreApplication.translate("MainBDIWidget", "BDI Output Dir", None))
        # if QT_CONFIG(tooltip)
        self.checkbox_custom_bdi_filename.setToolTip(
            QCoreApplication.translate(
                "MainBDIWidget",
                "<html><head/><body><p>When checked, the value entered will be used for the RT Beams Delivery Instruction file name.</p><p>If left unchecked, the file name for the RT Beams Delivery Instruction will be of the format RB_&lt;SOP Instance UID&gt;.dcm</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.checkbox_custom_bdi_filename.setText(QCoreApplication.translate("MainBDIWidget", "Custom BDI filename", None))
        self.push_button_export_bdi.setText(QCoreApplication.translate("MainBDIWidget", "Export BDI", None))
        self.group_box_ups.setTitle(QCoreApplication.translate("MainBDIWidget", "UPS Customization", None))
        self.datetime_edit_scheduled_datetime.setDisplayFormat(
            QCoreApplication.translate("MainBDIWidget", "dd/MM/yyyy h:mm AP", None)
        )
        self.push_button_export_ups.setText(QCoreApplication.translate("MainBDIWidget", "Export UPS", None))
        self.label_tms_scp_ae_title.setText(QCoreApplication.translate("MainBDIWidget", "TMS AE Title", None))
        self.label_start_datetime.setText(QCoreApplication.translate("MainBDIWidget", "Scheduled DateTime", None))
        self.checkbox_patient_photo.setText(QCoreApplication.translate("MainBDIWidget", "Patient Photo", None))
        self.checkbox_setup_photos.setText(QCoreApplication.translate("MainBDIWidget", "Setup Photos", None))

    # retranslateUi
