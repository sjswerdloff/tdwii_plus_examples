# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QDoubleSpinBox,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QListView, QPushButton, QSizePolicy, QWidget)

class Ui_MainBDIWidget(object):
    def setupUi(self, MainBDIWidget):
        if not MainBDIWidget.objectName():
            MainBDIWidget.setObjectName(u"MainBDIWidget")
        MainBDIWidget.resize(800, 600)
        self.group_box_bdi_variables = QGroupBox(MainBDIWidget)
        self.group_box_bdi_variables.setObjectName(u"group_box_bdi_variables")
        self.group_box_bdi_variables.setGeometry(QRect(40, 110, 491, 121))
        self.gridLayout_3 = QGridLayout(self.group_box_bdi_variables)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.double_spin_box_fraction_number = QDoubleSpinBox(self.group_box_bdi_variables)
        self.double_spin_box_fraction_number.setObjectName(u"double_spin_box_fraction_number")
        self.double_spin_box_fraction_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.double_spin_box_fraction_number.setDecimals(0)

        self.gridLayout_3.addWidget(self.double_spin_box_fraction_number, 0, 1, 1, 1)

        self.label_fraction_number = QLabel(self.group_box_bdi_variables)
        self.label_fraction_number.setObjectName(u"label_fraction_number")

        self.gridLayout_3.addWidget(self.label_fraction_number, 0, 0, 1, 1)

        self.list_view_treatment_records = QListView(self.group_box_bdi_variables)
        self.list_view_treatment_records.setObjectName(u"list_view_treatment_records")

        self.gridLayout_3.addWidget(self.list_view_treatment_records, 1, 0, 1, 1)

        self.push_button_load_treatment_records = QPushButton(self.group_box_bdi_variables)
        self.push_button_load_treatment_records.setObjectName(u"push_button_load_treatment_records")

        self.gridLayout_3.addWidget(self.push_button_load_treatment_records, 1, 1, 1, 1)

        self.group_box_plan_selection = QGroupBox(MainBDIWidget)
        self.group_box_plan_selection.setObjectName(u"group_box_plan_selection")
        self.group_box_plan_selection.setGeometry(QRect(40, 20, 581, 70))
        self.gridLayout_4 = QGridLayout(self.group_box_plan_selection)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_plan_selector = QLabel(self.group_box_plan_selection)
        self.label_plan_selector.setObjectName(u"label_plan_selector")

        self.gridLayout_4.addWidget(self.label_plan_selector, 0, 0, 1, 1)

        self.lineedit_plan_selector = QLineEdit(self.group_box_plan_selection)
        self.lineedit_plan_selector.setObjectName(u"lineedit_plan_selector")

        self.gridLayout_4.addWidget(self.lineedit_plan_selector, 0, 1, 1, 1)

        self.push_button_plan_finder = QPushButton(self.group_box_plan_selection)
        self.push_button_plan_finder.setObjectName(u"push_button_plan_finder")

        self.gridLayout_4.addWidget(self.push_button_plan_finder, 0, 2, 1, 1)

        self.group_box_bdi_output = QGroupBox(MainBDIWidget)
        self.group_box_bdi_output.setObjectName(u"group_box_bdi_output")
        self.group_box_bdi_output.setGeometry(QRect(40, 230, 591, 193))
        self.gridLayout_2 = QGridLayout(self.group_box_bdi_output)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_bdi_output_dir = QLabel(self.group_box_bdi_output)
        self.label_bdi_output_dir.setObjectName(u"label_bdi_output_dir")

        self.gridLayout_2.addWidget(self.label_bdi_output_dir, 0, 0, 1, 1)

        self.lineedit_bdidir_selector = QLineEdit(self.group_box_bdi_output)
        self.lineedit_bdidir_selector.setObjectName(u"lineedit_bdidir_selector")

        self.gridLayout_2.addWidget(self.lineedit_bdidir_selector, 0, 1, 1, 2)

        self.push_button_bdi_dir_finder = QPushButton(self.group_box_bdi_output)
        self.push_button_bdi_dir_finder.setObjectName(u"push_button_bdi_dir_finder")

        self.gridLayout_2.addWidget(self.push_button_bdi_dir_finder, 0, 3, 1, 1)

        self.checkbox_custom_bdi_filename = QCheckBox(self.group_box_bdi_output)
        self.checkbox_custom_bdi_filename.setObjectName(u"checkbox_custom_bdi_filename")

        self.gridLayout_2.addWidget(self.checkbox_custom_bdi_filename, 1, 0, 1, 2)

        self.line_edit_bdi_filename = QLineEdit(self.group_box_bdi_output)
        self.line_edit_bdi_filename.setObjectName(u"line_edit_bdi_filename")

        self.gridLayout_2.addWidget(self.line_edit_bdi_filename, 1, 2, 1, 1)

        self.push_button_export_bdi = QPushButton(self.group_box_bdi_output)
        self.push_button_export_bdi.setObjectName(u"push_button_export_bdi")

        self.gridLayout_2.addWidget(self.push_button_export_bdi, 3, 3, 1, 1)

        self.group_box_ups = QGroupBox(MainBDIWidget)
        self.group_box_ups.setObjectName(u"group_box_ups")
        self.group_box_ups.setGeometry(QRect(40, 430, 359, 151))
        self.gridLayout = QGridLayout(self.group_box_ups)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_start_datetime = QLabel(self.group_box_ups)
        self.label_start_datetime.setObjectName(u"label_start_datetime")

        self.gridLayout.addWidget(self.label_start_datetime, 1, 0, 1, 1)

        self.datetime_edit_scheduled_datetime = QDateTimeEdit(self.group_box_ups)
        self.datetime_edit_scheduled_datetime.setObjectName(u"datetime_edit_scheduled_datetime")
        self.datetime_edit_scheduled_datetime.setDateTime(QDateTime(QDate(2023, 9, 1), QTime(0, 0, 0)))
        self.datetime_edit_scheduled_datetime.setCalendarPopup(True)

        self.gridLayout.addWidget(self.datetime_edit_scheduled_datetime, 1, 1, 1, 1)

        self.label_move_ae_title = QLabel(self.group_box_ups)
        self.label_move_ae_title.setObjectName(u"label_move_ae_title")

        self.gridLayout.addWidget(self.label_move_ae_title, 0, 0, 1, 1)

        self.line_edit_move_scp_ae_title = QLineEdit(self.group_box_ups)
        self.line_edit_move_scp_ae_title.setObjectName(u"line_edit_move_scp_ae_title")
        self.line_edit_move_scp_ae_title.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.line_edit_move_scp_ae_title, 0, 1, 1, 1)

        self.push_button_export_ups = QPushButton(self.group_box_ups)
        self.push_button_export_ups.setObjectName(u"push_button_export_ups")

        self.gridLayout.addWidget(self.push_button_export_ups, 2, 1, 1, 1)


        self.retranslateUi(MainBDIWidget)

        QMetaObject.connectSlotsByName(MainBDIWidget)
    # setupUi

    def retranslateUi(self, MainBDIWidget):
        MainBDIWidget.setWindowTitle(QCoreApplication.translate("MainBDIWidget", u"RT Beams Delivery Instruction and UPS Creator", None))
#if QT_CONFIG(tooltip)
        MainBDIWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.group_box_bdi_variables.setTitle(QCoreApplication.translate("MainBDIWidget", u"BDI Customization", None))
        self.label_fraction_number.setText(QCoreApplication.translate("MainBDIWidget", u"Fraction #", None))
#if QT_CONFIG(tooltip)
        self.push_button_load_treatment_records.setToolTip(QCoreApplication.translate("MainBDIWidget", u"<html><head/><body><p>Simulate a partially treated session.</p><p>The treatment records selected must reference the RT (Ion) Plan selected, and the Current Fraction Number in the RT (Ion) Beams Session records must match the Fraction # specified</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.push_button_load_treatment_records.setText(QCoreApplication.translate("MainBDIWidget", u"Treatment Records", None))
        self.group_box_plan_selection.setTitle(QCoreApplication.translate("MainBDIWidget", u"Plan Selection", None))
        self.label_plan_selector.setText(QCoreApplication.translate("MainBDIWidget", u"RT (Ion) Plan", None))
        self.push_button_plan_finder.setText(QCoreApplication.translate("MainBDIWidget", u"Find Plan", None))
        self.group_box_bdi_output.setTitle(QCoreApplication.translate("MainBDIWidget", u"BDI Output", None))
        self.label_bdi_output_dir.setText(QCoreApplication.translate("MainBDIWidget", u"BDI Output Dir", None))
        self.push_button_bdi_dir_finder.setText(QCoreApplication.translate("MainBDIWidget", u"Choose BDI Dir", None))
#if QT_CONFIG(tooltip)
        self.checkbox_custom_bdi_filename.setToolTip(QCoreApplication.translate("MainBDIWidget", u"<html><head/><body><p>When checked, the value entered will be used for the RT Beams Delivery Instruction file name.</p><p>If left unchecked, the file name for the RT Beams Delivery Instruction will be of the format RB_&lt;SOP Instance UID&gt;.dcm</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkbox_custom_bdi_filename.setText(QCoreApplication.translate("MainBDIWidget", u"Custom BDI filename", None))
        self.push_button_export_bdi.setText(QCoreApplication.translate("MainBDIWidget", u"Export BDI", None))
        self.group_box_ups.setTitle(QCoreApplication.translate("MainBDIWidget", u"UPS Customization", None))
        self.label_start_datetime.setText(QCoreApplication.translate("MainBDIWidget", u"Scheduled DateTime", None))
        self.datetime_edit_scheduled_datetime.setDisplayFormat(QCoreApplication.translate("MainBDIWidget", u"dd/MM/yyyy h:mm AP", None))
        self.label_move_ae_title.setText(QCoreApplication.translate("MainBDIWidget", u"Move/Retrieve AE Title", None))
        self.push_button_export_ups.setText(QCoreApplication.translate("MainBDIWidget", u"Export UPS", None))
    # retranslateUi

