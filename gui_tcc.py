# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_tcc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout_27.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.tabWidget = QtWidgets.QTabWidget(self.central_widget)
        self.tabWidget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(238, 238, 236);")
        self.tabWidget.setObjectName("tabWidget")
        self.globalsettings_tab = QtWidgets.QWidget()
        self.globalsettings_tab.setObjectName("globalsettings_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.globalsettings_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_file_frame = QtWidgets.QFrame(self.globalsettings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_file_frame.sizePolicy().hasHeightForWidth())
        self.open_file_frame.setSizePolicy(sizePolicy)
        self.open_file_frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.open_file_frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.open_file_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.open_file_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.open_file_frame.setObjectName("open_file_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.open_file_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.open_file_label = QtWidgets.QLabel(self.open_file_frame)
        self.open_file_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.open_file_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.open_file_label.setObjectName("open_file_label")
        self.gridLayout.addWidget(self.open_file_label, 0, 0, 1, 1)
        self.open_button = QtWidgets.QPushButton(self.open_file_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.open_button.setObjectName("open_button")
        self.gridLayout.addWidget(self.open_button, 1, 1, 1, 1)
        self.open_file_field = QtWidgets.QLineEdit(self.open_file_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_file_field.sizePolicy().hasHeightForWidth())
        self.open_file_field.setSizePolicy(sizePolicy)
        self.open_file_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.open_file_field.setText("")
        self.open_file_field.setObjectName("open_file_field")
        self.gridLayout.addWidget(self.open_file_field, 1, 0, 1, 1)
        self.global_settings_frame = QtWidgets.QFrame(self.open_file_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.global_settings_frame.sizePolicy().hasHeightForWidth())
        self.global_settings_frame.setSizePolicy(sizePolicy)
        self.global_settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.global_settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.global_settings_frame.setObjectName("global_settings_frame")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.global_settings_frame)
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_29.setSpacing(2)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.dayindex_field = QtWidgets.QLineEdit(self.global_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dayindex_field.sizePolicy().hasHeightForWidth())
        self.dayindex_field.setSizePolicy(sizePolicy)
        self.dayindex_field.setMinimumSize(QtCore.QSize(70, 0))
        self.dayindex_field.setMaximumSize(QtCore.QSize(100, 16777215))
        self.dayindex_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.dayindex_field.setObjectName("dayindex_field")
        self.gridLayout_29.addWidget(self.dayindex_field, 0, 1, 1, 1)
        self.prediction_field = QtWidgets.QLineEdit(self.global_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prediction_field.sizePolicy().hasHeightForWidth())
        self.prediction_field.setSizePolicy(sizePolicy)
        self.prediction_field.setMinimumSize(QtCore.QSize(70, 0))
        self.prediction_field.setMaximumSize(QtCore.QSize(100, 16777215))
        self.prediction_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.prediction_field.setObjectName("prediction_field")
        self.gridLayout_29.addWidget(self.prediction_field, 1, 1, 1, 1)
        self.number_test_samples_field = QtWidgets.QLineEdit(self.global_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_test_samples_field.sizePolicy().hasHeightForWidth())
        self.number_test_samples_field.setSizePolicy(sizePolicy)
        self.number_test_samples_field.setMinimumSize(QtCore.QSize(70, 0))
        self.number_test_samples_field.setMaximumSize(QtCore.QSize(100, 16777215))
        self.number_test_samples_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.number_test_samples_field.setObjectName("number_test_samples_field")
        self.gridLayout_29.addWidget(self.number_test_samples_field, 3, 1, 1, 1)
        self.number_test_samples_label = QtWidgets.QLabel(self.global_settings_frame)
        self.number_test_samples_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.number_test_samples_label.setObjectName("number_test_samples_label")
        self.gridLayout_29.addWidget(self.number_test_samples_label, 3, 0, 1, 1)
        self.prediction_label = QtWidgets.QLabel(self.global_settings_frame)
        self.prediction_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.prediction_label.setObjectName("prediction_label")
        self.gridLayout_29.addWidget(self.prediction_label, 1, 0, 1, 1)
        self.dayindex_label = QtWidgets.QLabel(self.global_settings_frame)
        self.dayindex_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dayindex_label.setObjectName("dayindex_label")
        self.gridLayout_29.addWidget(self.dayindex_label, 0, 0, 1, 1)
        self.dayoftheweek_field = QtWidgets.QLineEdit(self.global_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dayoftheweek_field.sizePolicy().hasHeightForWidth())
        self.dayoftheweek_field.setSizePolicy(sizePolicy)
        self.dayoftheweek_field.setMinimumSize(QtCore.QSize(70, 0))
        self.dayoftheweek_field.setMaximumSize(QtCore.QSize(100, 16777215))
        self.dayoftheweek_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.dayoftheweek_field.setObjectName("dayoftheweek_field")
        self.gridLayout_29.addWidget(self.dayoftheweek_field, 2, 1, 1, 1)
        self.dayoftheweek_label = QtWidgets.QLabel(self.global_settings_frame)
        self.dayoftheweek_label.setObjectName("dayoftheweek_label")
        self.gridLayout_29.addWidget(self.dayoftheweek_label, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.global_settings_frame, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self.open_file_frame)
        self.exec_method_groupbox = QtWidgets.QGroupBox(self.globalsettings_tab)
        self.exec_method_groupbox.setObjectName("exec_method_groupbox")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.exec_method_groupbox)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.exec_method_radiobutton = QtWidgets.QRadioButton(self.exec_method_groupbox)
        self.exec_method_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.exec_method_radiobutton.setChecked(True)
        self.exec_method_radiobutton.setObjectName("exec_method_radiobutton")
        self.verticalLayout_18.addWidget(self.exec_method_radiobutton)
        self.debug_method_radiobutton = QtWidgets.QRadioButton(self.exec_method_groupbox)
        self.debug_method_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.debug_method_radiobutton.setObjectName("debug_method_radiobutton")
        self.verticalLayout_18.addWidget(self.debug_method_radiobutton)
        self.verticalLayout.addWidget(self.exec_method_groupbox)
        self.label = QtWidgets.QLabel(self.globalsettings_tab)
        self.label.setMaximumSize(QtCore.QSize(950, 350))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./images/LICON.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget.addTab(self.globalsettings_tab, "")
        self.ga_tab = QtWidgets.QWidget()
        self.ga_tab.setObjectName("ga_tab")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.ga_tab)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.ga_settings_frame = QtWidgets.QFrame(self.ga_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ga_settings_frame.sizePolicy().hasHeightForWidth())
        self.ga_settings_frame.setSizePolicy(sizePolicy)
        self.ga_settings_frame.setMinimumSize(QtCore.QSize(0, 200))
        self.ga_settings_frame.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.ga_settings_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ga_settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_settings_frame.setObjectName("ga_settings_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ga_settings_frame)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ga_settings = QtWidgets.QGroupBox(self.ga_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ga_settings.sizePolicy().hasHeightForWidth())
        self.ga_settings.setSizePolicy(sizePolicy)
        self.ga_settings.setMinimumSize(QtCore.QSize(0, 0))
        self.ga_settings.setMaximumSize(QtCore.QSize(600, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.ga_settings.setPalette(palette)
        self.ga_settings.setStyleSheet("")
        self.ga_settings.setObjectName("ga_settings")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.ga_settings)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ga_settings_1 = QtWidgets.QFrame(self.ga_settings)
        self.ga_settings_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ga_settings_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_settings_1.setObjectName("ga_settings_1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ga_settings_1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ga_settings_labels_frame = QtWidgets.QFrame(self.ga_settings_1)
        self.ga_settings_labels_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ga_settings_labels_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_settings_labels_frame.setObjectName("ga_settings_labels_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ga_settings_labels_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ga_population_label = QtWidgets.QLabel(self.ga_settings_labels_frame)
        self.ga_population_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ga_population_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.ga_population_label.setObjectName("ga_population_label")
        self.verticalLayout_3.addWidget(self.ga_population_label)
        self.ga_generations_label = QtWidgets.QLabel(self.ga_settings_labels_frame)
        self.ga_generations_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ga_generations_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.ga_generations_label.setObjectName("ga_generations_label")
        self.verticalLayout_3.addWidget(self.ga_generations_label)
        self.ga_executions_label = QtWidgets.QLabel(self.ga_settings_labels_frame)
        self.ga_executions_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ga_executions_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.ga_executions_label.setObjectName("ga_executions_label")
        self.verticalLayout_3.addWidget(self.ga_executions_label)
        self.horizontalLayout_3.addWidget(self.ga_settings_labels_frame)
        self.ga_settings_fields_frame = QtWidgets.QFrame(self.ga_settings_1)
        self.ga_settings_fields_frame.setMinimumSize(QtCore.QSize(70, 0))
        self.ga_settings_fields_frame.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ga_settings_fields_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ga_settings_fields_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_settings_fields_frame.setObjectName("ga_settings_fields_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.ga_settings_fields_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ga_population_field = QtWidgets.QLineEdit(self.ga_settings_fields_frame)
        self.ga_population_field.setMinimumSize(QtCore.QSize(0, 0))
        self.ga_population_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.ga_population_field.setObjectName("ga_population_field")
        self.verticalLayout_4.addWidget(self.ga_population_field)
        self.ga_gerations_field = QtWidgets.QLineEdit(self.ga_settings_fields_frame)
        self.ga_gerations_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.ga_gerations_field.setObjectName("ga_gerations_field")
        self.verticalLayout_4.addWidget(self.ga_gerations_field)
        self.ga_executions_field = QtWidgets.QLineEdit(self.ga_settings_fields_frame)
        self.ga_executions_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.ga_executions_field.setObjectName("ga_executions_field")
        self.verticalLayout_4.addWidget(self.ga_executions_field)
        self.horizontalLayout_3.addWidget(self.ga_settings_fields_frame)
        self.verticalLayout_6.addWidget(self.ga_settings_1)
        self.horizontalLayout_2.addWidget(self.ga_settings)
        self.ga_selection = QtWidgets.QGroupBox(self.ga_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ga_selection.sizePolicy().hasHeightForWidth())
        self.ga_selection.setSizePolicy(sizePolicy)
        self.ga_selection.setMinimumSize(QtCore.QSize(200, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.ga_selection.setPalette(palette)
        self.ga_selection.setObjectName("ga_selection")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.ga_selection)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.roulette_radiobutton = QtWidgets.QRadioButton(self.ga_selection)
        self.roulette_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.roulette_radiobutton.setChecked(True)
        self.roulette_radiobutton.setObjectName("roulette_radiobutton")
        self.verticalLayout_7.addWidget(self.roulette_radiobutton)
        self.roulette_sus_radiobutton = QtWidgets.QRadioButton(self.ga_selection)
        self.roulette_sus_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.roulette_sus_radiobutton.setObjectName("roulette_sus_radiobutton")
        self.verticalLayout_7.addWidget(self.roulette_sus_radiobutton)
        self.single_tournament_radiobutton = QtWidgets.QRadioButton(self.ga_selection)
        self.single_tournament_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.single_tournament_radiobutton.setObjectName("single_tournament_radiobutton")
        self.verticalLayout_7.addWidget(self.single_tournament_radiobutton)
        self.death_tournament_radiobutton = QtWidgets.QRadioButton(self.ga_selection)
        self.death_tournament_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.death_tournament_radiobutton.setObjectName("death_tournament_radiobutton")
        self.verticalLayout_7.addWidget(self.death_tournament_radiobutton)
        self.local_search_label = QtWidgets.QLabel(self.ga_selection)
        self.local_search_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.local_search_label.setObjectName("local_search_label")
        self.verticalLayout_7.addWidget(self.local_search_label)
        self.local_search_frame = QtWidgets.QFrame(self.ga_selection)
        self.local_search_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.local_search_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.local_search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.local_search_frame.setObjectName("local_search_frame")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.local_search_frame)
        self.horizontalLayout_16.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.local_search_scrollbar = QtWidgets.QScrollBar(self.local_search_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.local_search_scrollbar.sizePolicy().hasHeightForWidth())
        self.local_search_scrollbar.setSizePolicy(sizePolicy)
        self.local_search_scrollbar.setMinimumSize(QtCore.QSize(0, 0))
        self.local_search_scrollbar.setMaximum(100)
        self.local_search_scrollbar.setSingleStep(1)
        self.local_search_scrollbar.setPageStep(10)
        self.local_search_scrollbar.setProperty("value", 10)
        self.local_search_scrollbar.setOrientation(QtCore.Qt.Horizontal)
        self.local_search_scrollbar.setObjectName("local_search_scrollbar")
        self.horizontalLayout_16.addWidget(self.local_search_scrollbar)
        self.local_search_spinbox = QtWidgets.QSpinBox(self.local_search_frame)
        self.local_search_spinbox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.local_search_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.local_search_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.local_search_spinbox.setMaximum(100)
        self.local_search_spinbox.setProperty("value", 10)
        self.local_search_spinbox.setObjectName("local_search_spinbox")
        self.horizontalLayout_16.addWidget(self.local_search_spinbox)
        self.verticalLayout_7.addWidget(self.local_search_frame)
        self.horizontalLayout_2.addWidget(self.ga_selection)
        self.ga_cost = QtWidgets.QGroupBox(self.ga_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ga_cost.sizePolicy().hasHeightForWidth())
        self.ga_cost.setSizePolicy(sizePolicy)
        self.ga_cost.setObjectName("ga_cost")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.ga_cost)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ga_mse_radiobutton = QtWidgets.QRadioButton(self.ga_cost)
        self.ga_mse_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.ga_mse_radiobutton.setChecked(True)
        self.ga_mse_radiobutton.setObjectName("ga_mse_radiobutton")
        self.verticalLayout_5.addWidget(self.ga_mse_radiobutton)
        self.ga_ae_radiobutton = QtWidgets.QRadioButton(self.ga_cost)
        self.ga_ae_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.ga_ae_radiobutton.setObjectName("ga_ae_radiobutton")
        self.verticalLayout_5.addWidget(self.ga_ae_radiobutton)
        self.horizontalLayout_2.addWidget(self.ga_cost)
        self.ga_crossover = QtWidgets.QGroupBox(self.ga_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ga_crossover.sizePolicy().hasHeightForWidth())
        self.ga_crossover.setSizePolicy(sizePolicy)
        self.ga_crossover.setMinimumSize(QtCore.QSize(210, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.ga_crossover.setPalette(palette)
        self.ga_crossover.setObjectName("ga_crossover")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.ga_crossover)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.point_radiobutton = QtWidgets.QRadioButton(self.ga_crossover)
        self.point_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.point_radiobutton.setChecked(True)
        self.point_radiobutton.setObjectName("point_radiobutton")
        self.verticalLayout_8.addWidget(self.point_radiobutton)
        self.arithmetic_radiobutton = QtWidgets.QRadioButton(self.ga_crossover)
        self.arithmetic_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.arithmetic_radiobutton.setObjectName("arithmetic_radiobutton")
        self.verticalLayout_8.addWidget(self.arithmetic_radiobutton)
        self.sbx_radiobutton = QtWidgets.QRadioButton(self.ga_crossover)
        self.sbx_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.sbx_radiobutton.setObjectName("sbx_radiobutton")
        self.verticalLayout_8.addWidget(self.sbx_radiobutton)
        self.sbx_frame = QtWidgets.QFrame(self.ga_crossover)
        self.sbx_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.sbx_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sbx_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sbx_frame.setObjectName("sbx_frame")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.sbx_frame)
        self.horizontalLayout_17.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.sbx_ScrollBar = QtWidgets.QScrollBar(self.sbx_frame)
        self.sbx_ScrollBar.setMinimum(5)
        self.sbx_ScrollBar.setMaximum(200)
        self.sbx_ScrollBar.setSingleStep(1)
        self.sbx_ScrollBar.setPageStep(10)
        self.sbx_ScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.sbx_ScrollBar.setObjectName("sbx_ScrollBar")
        self.horizontalLayout_17.addWidget(self.sbx_ScrollBar)
        self.sbx_spinBox = QtWidgets.QSpinBox(self.sbx_frame)
        self.sbx_spinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.sbx_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.sbx_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sbx_spinBox.setMinimum(5)
        self.sbx_spinBox.setMaximum(200)
        self.sbx_spinBox.setObjectName("sbx_spinBox")
        self.horizontalLayout_17.addWidget(self.sbx_spinBox)
        self.verticalLayout_8.addWidget(self.sbx_frame)
        self.crossover_rate_frame = QtWidgets.QFrame(self.ga_crossover)
        self.crossover_rate_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.crossover_rate_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.crossover_rate_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.crossover_rate_frame.setObjectName("crossover_rate_frame")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.crossover_rate_frame)
        self.horizontalLayout_18.setContentsMargins(1, 1, -1, 1)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.crossover_rate_label = QtWidgets.QLabel(self.crossover_rate_frame)
        self.crossover_rate_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.crossover_rate_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.crossover_rate_label.setObjectName("crossover_rate_label")
        self.horizontalLayout_18.addWidget(self.crossover_rate_label)
        self.crossover_rate_spinbox = QtWidgets.QDoubleSpinBox(self.crossover_rate_frame)
        self.crossover_rate_spinbox.setMinimumSize(QtCore.QSize(60, 0))
        self.crossover_rate_spinbox.setMaximumSize(QtCore.QSize(60, 100))
        self.crossover_rate_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.crossover_rate_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.crossover_rate_spinbox.setMaximum(1.0)
        self.crossover_rate_spinbox.setSingleStep(0.05)
        self.crossover_rate_spinbox.setProperty("value", 0.7)
        self.crossover_rate_spinbox.setObjectName("crossover_rate_spinbox")
        self.horizontalLayout_18.addWidget(self.crossover_rate_spinbox)
        self.verticalLayout_8.addWidget(self.crossover_rate_frame)
        self.horizontalLayout_2.addWidget(self.ga_crossover)
        self.ga_mutation = QtWidgets.QGroupBox(self.ga_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ga_mutation.sizePolicy().hasHeightForWidth())
        self.ga_mutation.setSizePolicy(sizePolicy)
        self.ga_mutation.setMinimumSize(QtCore.QSize(200, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.ga_mutation.setPalette(palette)
        self.ga_mutation.setObjectName("ga_mutation")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.ga_mutation)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.fixed_mutation_radiobutton = QtWidgets.QRadioButton(self.ga_mutation)
        self.fixed_mutation_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.fixed_mutation_radiobutton.setChecked(True)
        self.fixed_mutation_radiobutton.setObjectName("fixed_mutation_radiobutton")
        self.verticalLayout_9.addWidget(self.fixed_mutation_radiobutton)
        self.dyn_mutation_radiobutton = QtWidgets.QRadioButton(self.ga_mutation)
        self.dyn_mutation_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.dyn_mutation_radiobutton.setObjectName("dyn_mutation_radiobutton")
        self.verticalLayout_9.addWidget(self.dyn_mutation_radiobutton)
        self.mutation_rate_frame = QtWidgets.QFrame(self.ga_mutation)
        self.mutation_rate_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.mutation_rate_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mutation_rate_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mutation_rate_frame.setObjectName("mutation_rate_frame")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.mutation_rate_frame)
        self.horizontalLayout_19.setContentsMargins(1, 1, -1, 1)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.mutation_rate_label = QtWidgets.QLabel(self.mutation_rate_frame)
        self.mutation_rate_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.mutation_rate_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.mutation_rate_label.setObjectName("mutation_rate_label")
        self.horizontalLayout_19.addWidget(self.mutation_rate_label)
        self.mutation_rate_SpinBox = QtWidgets.QDoubleSpinBox(self.mutation_rate_frame)
        self.mutation_rate_SpinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.mutation_rate_SpinBox.setMaximumSize(QtCore.QSize(60, 100))
        self.mutation_rate_SpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.mutation_rate_SpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.mutation_rate_SpinBox.setMaximum(1.0)
        self.mutation_rate_SpinBox.setSingleStep(0.05)
        self.mutation_rate_SpinBox.setProperty("value", 0.1)
        self.mutation_rate_SpinBox.setObjectName("mutation_rate_SpinBox")
        self.horizontalLayout_19.addWidget(self.mutation_rate_SpinBox)
        self.verticalLayout_9.addWidget(self.mutation_rate_frame)
        self.horizontalLayout_2.addWidget(self.ga_mutation)
        self.verticalLayout_19.addWidget(self.ga_settings_frame)
        self.ga_upper_frame = QtWidgets.QFrame(self.ga_tab)
        self.ga_upper_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ga_upper_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_upper_frame.setObjectName("ga_upper_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ga_upper_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ga_frame_lag_0 = QtWidgets.QFrame(self.ga_upper_frame)
        self.ga_frame_lag_0.setStyleSheet("color: rgb(238, 238, 236);")
        self.ga_frame_lag_0.setFrameShape(QtWidgets.QFrame.Box)
        self.ga_frame_lag_0.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ga_frame_lag_0.setLineWidth(0)
        self.ga_frame_lag_0.setObjectName("ga_frame_lag_0")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ga_frame_lag_0)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_lag_ga_0 = QtWidgets.QLabel(self.ga_frame_lag_0)
        self.label_lag_ga_0.setObjectName("label_lag_ga_0")
        self.gridLayout_2.addWidget(self.label_lag_ga_0, 0, 0, 1, 1)
        self.start_ga_0 = QtWidgets.QPushButton(self.ga_frame_lag_0)
        self.start_ga_0.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_ga_0.setObjectName("start_ga_0")
        self.gridLayout_2.addWidget(self.start_ga_0, 0, 1, 1, 1)
        self.stop_ga_0 = QtWidgets.QPushButton(self.ga_frame_lag_0)
        self.stop_ga_0.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_ga_0.setObjectName("stop_ga_0")
        self.gridLayout_2.addWidget(self.stop_ga_0, 0, 2, 1, 1)
        self.label_ga_0 = QtWidgets.QLabel(self.ga_frame_lag_0)
        self.label_ga_0.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_ga_0.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ga_0.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_ga_0.setLineWidth(1)
        self.label_ga_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ga_0.setObjectName("label_ga_0")
        self.gridLayout_2.addWidget(self.label_ga_0, 1, 0, 1, 3)
        self.horizontalLayout.addWidget(self.ga_frame_lag_0)
        self.ga_frame_lag_1 = QtWidgets.QFrame(self.ga_upper_frame)
        self.ga_frame_lag_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ga_frame_lag_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_frame_lag_1.setObjectName("ga_frame_lag_1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.ga_frame_lag_1)
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_lag_ga_1 = QtWidgets.QLabel(self.ga_frame_lag_1)
        self.label_lag_ga_1.setObjectName("label_lag_ga_1")
        self.gridLayout_5.addWidget(self.label_lag_ga_1, 0, 0, 1, 1)
        self.start_ga_1 = QtWidgets.QPushButton(self.ga_frame_lag_1)
        self.start_ga_1.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_ga_1.setObjectName("start_ga_1")
        self.gridLayout_5.addWidget(self.start_ga_1, 0, 1, 1, 1)
        self.stop_ga_1 = QtWidgets.QPushButton(self.ga_frame_lag_1)
        self.stop_ga_1.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_ga_1.setObjectName("stop_ga_1")
        self.gridLayout_5.addWidget(self.stop_ga_1, 0, 2, 1, 1)
        self.label_ga_1 = QtWidgets.QLabel(self.ga_frame_lag_1)
        self.label_ga_1.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_ga_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ga_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ga_1.setObjectName("label_ga_1")
        self.gridLayout_5.addWidget(self.label_ga_1, 1, 0, 1, 3)
        self.horizontalLayout.addWidget(self.ga_frame_lag_1)
        self.ga_frame_lag_2 = QtWidgets.QFrame(self.ga_upper_frame)
        self.ga_frame_lag_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ga_frame_lag_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_frame_lag_2.setObjectName("ga_frame_lag_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ga_frame_lag_2)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_lag_ga_2 = QtWidgets.QLabel(self.ga_frame_lag_2)
        self.label_lag_ga_2.setObjectName("label_lag_ga_2")
        self.gridLayout_4.addWidget(self.label_lag_ga_2, 0, 0, 1, 1)
        self.start_ga_2 = QtWidgets.QPushButton(self.ga_frame_lag_2)
        self.start_ga_2.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_ga_2.setObjectName("start_ga_2")
        self.gridLayout_4.addWidget(self.start_ga_2, 0, 1, 1, 1)
        self.stop_ga_2 = QtWidgets.QPushButton(self.ga_frame_lag_2)
        self.stop_ga_2.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_ga_2.setObjectName("stop_ga_2")
        self.gridLayout_4.addWidget(self.stop_ga_2, 0, 2, 1, 1)
        self.label_ga_2 = QtWidgets.QLabel(self.ga_frame_lag_2)
        self.label_ga_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_ga_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ga_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ga_2.setObjectName("label_ga_2")
        self.gridLayout_4.addWidget(self.label_ga_2, 1, 0, 1, 3)
        self.horizontalLayout.addWidget(self.ga_frame_lag_2)
        self.ga_frame_lag_3 = QtWidgets.QFrame(self.ga_upper_frame)
        self.ga_frame_lag_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ga_frame_lag_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_frame_lag_3.setObjectName("ga_frame_lag_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ga_frame_lag_3)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_lag_ga_3 = QtWidgets.QLabel(self.ga_frame_lag_3)
        self.label_lag_ga_3.setObjectName("label_lag_ga_3")
        self.gridLayout_3.addWidget(self.label_lag_ga_3, 0, 1, 1, 1)
        self.start_ga_3 = QtWidgets.QPushButton(self.ga_frame_lag_3)
        self.start_ga_3.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_ga_3.setObjectName("start_ga_3")
        self.gridLayout_3.addWidget(self.start_ga_3, 0, 2, 1, 1)
        self.stop_ga_3 = QtWidgets.QPushButton(self.ga_frame_lag_3)
        self.stop_ga_3.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_ga_3.setObjectName("stop_ga_3")
        self.gridLayout_3.addWidget(self.stop_ga_3, 0, 3, 1, 1)
        self.label_ga_3 = QtWidgets.QLabel(self.ga_frame_lag_3)
        self.label_ga_3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_ga_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ga_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ga_3.setObjectName("label_ga_3")
        self.gridLayout_3.addWidget(self.label_ga_3, 1, 1, 1, 3)
        self.horizontalLayout.addWidget(self.ga_frame_lag_3)
        self.verticalLayout_19.addWidget(self.ga_upper_frame)
        self.ga_bottom_frame = QtWidgets.QFrame(self.ga_tab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.ga_bottom_frame.setPalette(palette)
        self.ga_bottom_frame.setStyleSheet("")
        self.ga_bottom_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ga_bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_bottom_frame.setObjectName("ga_bottom_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ga_bottom_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ga_frame_lag_4 = QtWidgets.QFrame(self.ga_bottom_frame)
        self.ga_frame_lag_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ga_frame_lag_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_frame_lag_4.setObjectName("ga_frame_lag_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.ga_frame_lag_4)
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_lag_ga_4 = QtWidgets.QLabel(self.ga_frame_lag_4)
        self.label_lag_ga_4.setObjectName("label_lag_ga_4")
        self.gridLayout_6.addWidget(self.label_lag_ga_4, 0, 0, 1, 1)
        self.start_ga_4 = QtWidgets.QPushButton(self.ga_frame_lag_4)
        self.start_ga_4.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_ga_4.setObjectName("start_ga_4")
        self.gridLayout_6.addWidget(self.start_ga_4, 0, 1, 1, 1)
        self.stop_ga_4 = QtWidgets.QPushButton(self.ga_frame_lag_4)
        self.stop_ga_4.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_ga_4.setObjectName("stop_ga_4")
        self.gridLayout_6.addWidget(self.stop_ga_4, 0, 2, 1, 1)
        self.label_ga_4 = QtWidgets.QLabel(self.ga_frame_lag_4)
        self.label_ga_4.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_ga_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ga_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ga_4.setObjectName("label_ga_4")
        self.gridLayout_6.addWidget(self.label_ga_4, 1, 0, 1, 3)
        self.horizontalLayout_4.addWidget(self.ga_frame_lag_4)
        self.ga_frame_lag_5 = QtWidgets.QFrame(self.ga_bottom_frame)
        self.ga_frame_lag_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ga_frame_lag_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_frame_lag_5.setObjectName("ga_frame_lag_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.ga_frame_lag_5)
        self.gridLayout_7.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_lag_ga_5 = QtWidgets.QLabel(self.ga_frame_lag_5)
        self.label_lag_ga_5.setObjectName("label_lag_ga_5")
        self.gridLayout_7.addWidget(self.label_lag_ga_5, 0, 0, 1, 1)
        self.start_ga_5 = QtWidgets.QPushButton(self.ga_frame_lag_5)
        self.start_ga_5.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_ga_5.setObjectName("start_ga_5")
        self.gridLayout_7.addWidget(self.start_ga_5, 0, 1, 1, 1)
        self.stop_ga_5 = QtWidgets.QPushButton(self.ga_frame_lag_5)
        self.stop_ga_5.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_ga_5.setObjectName("stop_ga_5")
        self.gridLayout_7.addWidget(self.stop_ga_5, 0, 2, 1, 1)
        self.label_ga_5 = QtWidgets.QLabel(self.ga_frame_lag_5)
        self.label_ga_5.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_ga_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ga_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ga_5.setObjectName("label_ga_5")
        self.gridLayout_7.addWidget(self.label_ga_5, 1, 0, 1, 3)
        self.horizontalLayout_4.addWidget(self.ga_frame_lag_5)
        self.ga_frame_lag_6 = QtWidgets.QFrame(self.ga_bottom_frame)
        self.ga_frame_lag_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ga_frame_lag_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_frame_lag_6.setObjectName("ga_frame_lag_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.ga_frame_lag_6)
        self.gridLayout_8.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_lag_ga_6 = QtWidgets.QLabel(self.ga_frame_lag_6)
        self.label_lag_ga_6.setObjectName("label_lag_ga_6")
        self.gridLayout_8.addWidget(self.label_lag_ga_6, 0, 0, 1, 1)
        self.start_ga_6 = QtWidgets.QPushButton(self.ga_frame_lag_6)
        self.start_ga_6.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_ga_6.setObjectName("start_ga_6")
        self.gridLayout_8.addWidget(self.start_ga_6, 0, 1, 1, 1)
        self.stop_ga_6 = QtWidgets.QPushButton(self.ga_frame_lag_6)
        self.stop_ga_6.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_ga_6.setObjectName("stop_ga_6")
        self.gridLayout_8.addWidget(self.stop_ga_6, 0, 2, 1, 1)
        self.label_ga_6 = QtWidgets.QLabel(self.ga_frame_lag_6)
        self.label_ga_6.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_ga_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ga_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ga_6.setObjectName("label_ga_6")
        self.gridLayout_8.addWidget(self.label_ga_6, 1, 0, 1, 3)
        self.horizontalLayout_4.addWidget(self.ga_frame_lag_6)
        self.ga_frame_lag_7 = QtWidgets.QFrame(self.ga_bottom_frame)
        self.ga_frame_lag_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ga_frame_lag_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ga_frame_lag_7.setObjectName("ga_frame_lag_7")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.ga_frame_lag_7)
        self.gridLayout_9.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_9.setSpacing(5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_lag_ga_7 = QtWidgets.QLabel(self.ga_frame_lag_7)
        self.label_lag_ga_7.setObjectName("label_lag_ga_7")
        self.gridLayout_9.addWidget(self.label_lag_ga_7, 0, 0, 1, 1)
        self.start_ga_7 = QtWidgets.QPushButton(self.ga_frame_lag_7)
        self.start_ga_7.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_ga_7.setObjectName("start_ga_7")
        self.gridLayout_9.addWidget(self.start_ga_7, 0, 1, 1, 1)
        self.stop_ga_7 = QtWidgets.QPushButton(self.ga_frame_lag_7)
        self.stop_ga_7.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_ga_7.setObjectName("stop_ga_7")
        self.gridLayout_9.addWidget(self.stop_ga_7, 0, 2, 1, 1)
        self.label_ga_7 = QtWidgets.QLabel(self.ga_frame_lag_7)
        self.label_ga_7.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_ga_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ga_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ga_7.setObjectName("label_ga_7")
        self.gridLayout_9.addWidget(self.label_ga_7, 1, 0, 1, 3)
        self.horizontalLayout_4.addWidget(self.ga_frame_lag_7)
        self.verticalLayout_19.addWidget(self.ga_bottom_frame)
        self.tabWidget.addTab(self.ga_tab, "")
        self.de_tab = QtWidgets.QWidget()
        self.de_tab.setObjectName("de_tab")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.de_tab)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.de_settings_frame = QtWidgets.QFrame(self.de_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.de_settings_frame.sizePolicy().hasHeightForWidth())
        self.de_settings_frame.setSizePolicy(sizePolicy)
        self.de_settings_frame.setMaximumSize(QtCore.QSize(16777215, 230))
        self.de_settings_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.de_settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_settings_frame.setObjectName("de_settings_frame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.de_settings_frame)
        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_13.setSpacing(9)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.de_settings = QtWidgets.QGroupBox(self.de_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.de_settings.sizePolicy().hasHeightForWidth())
        self.de_settings.setSizePolicy(sizePolicy)
        self.de_settings.setMinimumSize(QtCore.QSize(200, 0))
        self.de_settings.setMaximumSize(QtCore.QSize(600, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.de_settings.setPalette(palette)
        self.de_settings.setObjectName("de_settings")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.de_settings)
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.de_settings_1 = QtWidgets.QFrame(self.de_settings)
        self.de_settings_1.setMinimumSize(QtCore.QSize(200, 0))
        self.de_settings_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.de_settings_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_settings_1.setObjectName("de_settings_1")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.de_settings_1)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.de_settings_labels_frame = QtWidgets.QFrame(self.de_settings_1)
        self.de_settings_labels_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.de_settings_labels_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_settings_labels_frame.setObjectName("de_settings_labels_frame")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.de_settings_labels_frame)
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.de_population_label = QtWidgets.QLabel(self.de_settings_labels_frame)
        self.de_population_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.de_population_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.de_population_label.setObjectName("de_population_label")
        self.verticalLayout_43.addWidget(self.de_population_label)
        self.de_generations_label = QtWidgets.QLabel(self.de_settings_labels_frame)
        self.de_generations_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.de_generations_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.de_generations_label.setObjectName("de_generations_label")
        self.verticalLayout_43.addWidget(self.de_generations_label)
        self.de_executions_label = QtWidgets.QLabel(self.de_settings_labels_frame)
        self.de_executions_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.de_executions_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.de_executions_label.setObjectName("de_executions_label")
        self.verticalLayout_43.addWidget(self.de_executions_label)
        self.horizontalLayout_14.addWidget(self.de_settings_labels_frame)
        self.de_settings_fields_frame = QtWidgets.QFrame(self.de_settings_1)
        self.de_settings_fields_frame.setMinimumSize(QtCore.QSize(70, 0))
        self.de_settings_fields_frame.setMaximumSize(QtCore.QSize(100, 16777215))
        self.de_settings_fields_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.de_settings_fields_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_settings_fields_frame.setObjectName("de_settings_fields_frame")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.de_settings_fields_frame)
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.de_population_field = QtWidgets.QLineEdit(self.de_settings_fields_frame)
        self.de_population_field.setMinimumSize(QtCore.QSize(0, 0))
        self.de_population_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.de_population_field.setObjectName("de_population_field")
        self.verticalLayout_44.addWidget(self.de_population_field)
        self.de_gerations_field = QtWidgets.QLineEdit(self.de_settings_fields_frame)
        self.de_gerations_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.de_gerations_field.setObjectName("de_gerations_field")
        self.verticalLayout_44.addWidget(self.de_gerations_field)
        self.de_executions_field = QtWidgets.QLineEdit(self.de_settings_fields_frame)
        self.de_executions_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.de_executions_field.setObjectName("de_executions_field")
        self.verticalLayout_44.addWidget(self.de_executions_field)
        self.horizontalLayout_14.addWidget(self.de_settings_fields_frame)
        self.verticalLayout_42.addWidget(self.de_settings_1)
        self.horizontalLayout_13.addWidget(self.de_settings)
        self.de_selection = QtWidgets.QGroupBox(self.de_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.de_selection.sizePolicy().hasHeightForWidth())
        self.de_selection.setSizePolicy(sizePolicy)
        self.de_selection.setMinimumSize(QtCore.QSize(200, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.de_selection.setPalette(palette)
        self.de_selection.setObjectName("de_selection")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.de_selection)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.greedy_radiobutton = QtWidgets.QRadioButton(self.de_selection)
        self.greedy_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.greedy_radiobutton.setChecked(True)
        self.greedy_radiobutton.setObjectName("greedy_radiobutton")
        self.verticalLayout_46.addWidget(self.greedy_radiobutton)
        self.number_f_frame = QtWidgets.QFrame(self.de_selection)
        self.number_f_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.number_f_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.number_f_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.number_f_frame.setObjectName("number_f_frame")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.number_f_frame)
        self.horizontalLayout_42.setContentsMargins(-1, 1, 1, 1)
        self.horizontalLayout_42.setSpacing(5)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.number_f_label = QtWidgets.QLabel(self.number_f_frame)
        self.number_f_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.number_f_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.number_f_label.setObjectName("number_f_label")
        self.horizontalLayout_42.addWidget(self.number_f_label)
        self.number_f_spinbox = QtWidgets.QDoubleSpinBox(self.number_f_frame)
        self.number_f_spinbox.setMinimumSize(QtCore.QSize(60, 0))
        self.number_f_spinbox.setMaximumSize(QtCore.QSize(60, 100))
        self.number_f_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.number_f_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.number_f_spinbox.setDecimals(1)
        self.number_f_spinbox.setMaximum(2.0)
        self.number_f_spinbox.setSingleStep(0.1)
        self.number_f_spinbox.setProperty("value", 0.2)
        self.number_f_spinbox.setObjectName("number_f_spinbox")
        self.horizontalLayout_42.addWidget(self.number_f_spinbox)
        self.verticalLayout_46.addWidget(self.number_f_frame)
        self.horizontalLayout_13.addWidget(self.de_selection)
        self.de_cost = QtWidgets.QGroupBox(self.de_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.de_cost.sizePolicy().hasHeightForWidth())
        self.de_cost.setSizePolicy(sizePolicy)
        self.de_cost.setObjectName("de_cost")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.de_cost)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.de_mse_radiobutton = QtWidgets.QRadioButton(self.de_cost)
        self.de_mse_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.de_mse_radiobutton.setChecked(True)
        self.de_mse_radiobutton.setObjectName("de_mse_radiobutton")
        self.verticalLayout_14.addWidget(self.de_mse_radiobutton)
        self.de_ae_radiobutton = QtWidgets.QRadioButton(self.de_cost)
        self.de_ae_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.de_ae_radiobutton.setObjectName("de_ae_radiobutton")
        self.verticalLayout_14.addWidget(self.de_ae_radiobutton)
        self.horizontalLayout_13.addWidget(self.de_cost)
        self.de_crossover = QtWidgets.QGroupBox(self.de_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.de_crossover.sizePolicy().hasHeightForWidth())
        self.de_crossover.setSizePolicy(sizePolicy)
        self.de_crossover.setMinimumSize(QtCore.QSize(210, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.de_crossover.setPalette(palette)
        self.de_crossover.setObjectName("de_crossover")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.de_crossover)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.exponential_radiobutton = QtWidgets.QRadioButton(self.de_crossover)
        self.exponential_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.exponential_radiobutton.setChecked(True)
        self.exponential_radiobutton.setObjectName("exponential_radiobutton")
        self.verticalLayout_47.addWidget(self.exponential_radiobutton)
        self.binary_radiobutton = QtWidgets.QRadioButton(self.de_crossover)
        self.binary_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.binary_radiobutton.setObjectName("binary_radiobutton")
        self.verticalLayout_47.addWidget(self.binary_radiobutton)
        self.crossover_rate_frame_2 = QtWidgets.QFrame(self.de_crossover)
        self.crossover_rate_frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.crossover_rate_frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.crossover_rate_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.crossover_rate_frame_2.setObjectName("crossover_rate_frame_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.crossover_rate_frame_2)
        self.horizontalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.crossover_rate_label_2 = QtWidgets.QLabel(self.crossover_rate_frame_2)
        self.crossover_rate_label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.crossover_rate_label_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.crossover_rate_label_2.setObjectName("crossover_rate_label_2")
        self.horizontalLayout_12.addWidget(self.crossover_rate_label_2)
        self.crossover_rate_spinbox_2 = QtWidgets.QDoubleSpinBox(self.crossover_rate_frame_2)
        self.crossover_rate_spinbox_2.setMinimumSize(QtCore.QSize(60, 0))
        self.crossover_rate_spinbox_2.setMaximumSize(QtCore.QSize(60, 100))
        self.crossover_rate_spinbox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.crossover_rate_spinbox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.crossover_rate_spinbox_2.setMaximum(1.0)
        self.crossover_rate_spinbox_2.setSingleStep(0.05)
        self.crossover_rate_spinbox_2.setProperty("value", 0.2)
        self.crossover_rate_spinbox_2.setObjectName("crossover_rate_spinbox_2")
        self.horizontalLayout_12.addWidget(self.crossover_rate_spinbox_2)
        self.verticalLayout_47.addWidget(self.crossover_rate_frame_2)
        self.horizontalLayout_13.addWidget(self.de_crossover)
        self.de_mutation = QtWidgets.QGroupBox(self.de_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.de_mutation.sizePolicy().hasHeightForWidth())
        self.de_mutation.setSizePolicy(sizePolicy)
        self.de_mutation.setMinimumSize(QtCore.QSize(200, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.de_mutation.setPalette(palette)
        self.de_mutation.setObjectName("de_mutation")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.de_mutation)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.rand_radiobutton = QtWidgets.QRadioButton(self.de_mutation)
        self.rand_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.rand_radiobutton.setChecked(True)
        self.rand_radiobutton.setObjectName("rand_radiobutton")
        self.verticalLayout_48.addWidget(self.rand_radiobutton)
        self.rand2dp_radiobutton = QtWidgets.QRadioButton(self.de_mutation)
        self.rand2dp_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.rand2dp_radiobutton.setObjectName("rand2dp_radiobutton")
        self.verticalLayout_48.addWidget(self.rand2dp_radiobutton)
        self.best_radiobutton = QtWidgets.QRadioButton(self.de_mutation)
        self.best_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.best_radiobutton.setObjectName("best_radiobutton")
        self.verticalLayout_48.addWidget(self.best_radiobutton)
        self.best2dp_radiobutton = QtWidgets.QRadioButton(self.de_mutation)
        self.best2dp_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.best2dp_radiobutton.setObjectName("best2dp_radiobutton")
        self.verticalLayout_48.addWidget(self.best2dp_radiobutton)
        self.target_to_best_radiobutton = QtWidgets.QRadioButton(self.de_mutation)
        self.target_to_best_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.target_to_best_radiobutton.setObjectName("target_to_best_radiobutton")
        self.verticalLayout_48.addWidget(self.target_to_best_radiobutton)
        self.mutation_rate_frame_2 = QtWidgets.QFrame(self.de_mutation)
        self.mutation_rate_frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.mutation_rate_frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mutation_rate_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mutation_rate_frame_2.setObjectName("mutation_rate_frame_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.mutation_rate_frame_2)
        self.horizontalLayout_15.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.mutation_rate_label_2 = QtWidgets.QLabel(self.mutation_rate_frame_2)
        self.mutation_rate_label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.mutation_rate_label_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.mutation_rate_label_2.setObjectName("mutation_rate_label_2")
        self.horizontalLayout_15.addWidget(self.mutation_rate_label_2)
        self.mutation_rate_spinbox = QtWidgets.QDoubleSpinBox(self.mutation_rate_frame_2)
        self.mutation_rate_spinbox.setMinimumSize(QtCore.QSize(60, 0))
        self.mutation_rate_spinbox.setMaximumSize(QtCore.QSize(60, 100))
        self.mutation_rate_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.mutation_rate_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.mutation_rate_spinbox.setMaximum(1.0)
        self.mutation_rate_spinbox.setSingleStep(0.05)
        self.mutation_rate_spinbox.setProperty("value", 0.2)
        self.mutation_rate_spinbox.setObjectName("mutation_rate_spinbox")
        self.horizontalLayout_15.addWidget(self.mutation_rate_spinbox)
        self.verticalLayout_48.addWidget(self.mutation_rate_frame_2)
        self.horizontalLayout_13.addWidget(self.de_mutation)
        self.verticalLayout_20.addWidget(self.de_settings_frame)
        self.de_upper_frame = QtWidgets.QFrame(self.de_tab)
        self.de_upper_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.de_upper_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_upper_frame.setObjectName("de_upper_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.de_upper_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.de_frame_lag_0 = QtWidgets.QFrame(self.de_upper_frame)
        self.de_frame_lag_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.de_frame_lag_0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_frame_lag_0.setObjectName("de_frame_lag_0")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.de_frame_lag_0)
        self.gridLayout_10.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_10.setSpacing(5)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_lag_de_0 = QtWidgets.QLabel(self.de_frame_lag_0)
        self.label_lag_de_0.setObjectName("label_lag_de_0")
        self.gridLayout_10.addWidget(self.label_lag_de_0, 0, 0, 1, 1)
        self.start_de_0 = QtWidgets.QPushButton(self.de_frame_lag_0)
        self.start_de_0.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_de_0.setObjectName("start_de_0")
        self.gridLayout_10.addWidget(self.start_de_0, 0, 1, 1, 1)
        self.stop_de_0 = QtWidgets.QPushButton(self.de_frame_lag_0)
        self.stop_de_0.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_de_0.setObjectName("stop_de_0")
        self.gridLayout_10.addWidget(self.stop_de_0, 0, 2, 1, 1)
        self.label_de_0 = QtWidgets.QLabel(self.de_frame_lag_0)
        self.label_de_0.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_de_0.setFrameShape(QtWidgets.QFrame.Box)
        self.label_de_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_de_0.setObjectName("label_de_0")
        self.gridLayout_10.addWidget(self.label_de_0, 1, 0, 1, 3)
        self.horizontalLayout_5.addWidget(self.de_frame_lag_0)
        self.de_frame_lag_1 = QtWidgets.QFrame(self.de_upper_frame)
        self.de_frame_lag_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.de_frame_lag_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_frame_lag_1.setObjectName("de_frame_lag_1")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.de_frame_lag_1)
        self.gridLayout_11.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_11.setSpacing(5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_lag_de_1 = QtWidgets.QLabel(self.de_frame_lag_1)
        self.label_lag_de_1.setObjectName("label_lag_de_1")
        self.gridLayout_11.addWidget(self.label_lag_de_1, 0, 0, 1, 1)
        self.start_de_1 = QtWidgets.QPushButton(self.de_frame_lag_1)
        self.start_de_1.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_de_1.setObjectName("start_de_1")
        self.gridLayout_11.addWidget(self.start_de_1, 0, 1, 1, 1)
        self.stop_de_1 = QtWidgets.QPushButton(self.de_frame_lag_1)
        self.stop_de_1.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_de_1.setObjectName("stop_de_1")
        self.gridLayout_11.addWidget(self.stop_de_1, 0, 2, 1, 1)
        self.label_de_1 = QtWidgets.QLabel(self.de_frame_lag_1)
        self.label_de_1.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_de_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_de_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_de_1.setObjectName("label_de_1")
        self.gridLayout_11.addWidget(self.label_de_1, 1, 0, 1, 3)
        self.horizontalLayout_5.addWidget(self.de_frame_lag_1)
        self.de_frame_lag_2 = QtWidgets.QFrame(self.de_upper_frame)
        self.de_frame_lag_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.de_frame_lag_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_frame_lag_2.setObjectName("de_frame_lag_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.de_frame_lag_2)
        self.gridLayout_12.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_12.setSpacing(5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_lag_de_2 = QtWidgets.QLabel(self.de_frame_lag_2)
        self.label_lag_de_2.setObjectName("label_lag_de_2")
        self.gridLayout_12.addWidget(self.label_lag_de_2, 0, 0, 1, 1)
        self.start_de_2 = QtWidgets.QPushButton(self.de_frame_lag_2)
        self.start_de_2.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_de_2.setObjectName("start_de_2")
        self.gridLayout_12.addWidget(self.start_de_2, 0, 1, 1, 1)
        self.stop_de_2 = QtWidgets.QPushButton(self.de_frame_lag_2)
        self.stop_de_2.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_de_2.setObjectName("stop_de_2")
        self.gridLayout_12.addWidget(self.stop_de_2, 0, 2, 1, 1)
        self.label_de_2 = QtWidgets.QLabel(self.de_frame_lag_2)
        self.label_de_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_de_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_de_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_de_2.setObjectName("label_de_2")
        self.gridLayout_12.addWidget(self.label_de_2, 1, 0, 1, 3)
        self.horizontalLayout_5.addWidget(self.de_frame_lag_2)
        self.de_frame_lag_3 = QtWidgets.QFrame(self.de_upper_frame)
        self.de_frame_lag_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.de_frame_lag_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_frame_lag_3.setObjectName("de_frame_lag_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.de_frame_lag_3)
        self.gridLayout_13.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_13.setSpacing(5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_lag_de_3 = QtWidgets.QLabel(self.de_frame_lag_3)
        self.label_lag_de_3.setObjectName("label_lag_de_3")
        self.gridLayout_13.addWidget(self.label_lag_de_3, 0, 0, 1, 1)
        self.start_de_3 = QtWidgets.QPushButton(self.de_frame_lag_3)
        self.start_de_3.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_de_3.setObjectName("start_de_3")
        self.gridLayout_13.addWidget(self.start_de_3, 0, 1, 1, 1)
        self.stop_de_3 = QtWidgets.QPushButton(self.de_frame_lag_3)
        self.stop_de_3.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_de_3.setObjectName("stop_de_3")
        self.gridLayout_13.addWidget(self.stop_de_3, 0, 2, 1, 1)
        self.label_de_3 = QtWidgets.QLabel(self.de_frame_lag_3)
        self.label_de_3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_de_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_de_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_de_3.setObjectName("label_de_3")
        self.gridLayout_13.addWidget(self.label_de_3, 1, 0, 1, 3)
        self.horizontalLayout_5.addWidget(self.de_frame_lag_3)
        self.verticalLayout_20.addWidget(self.de_upper_frame)
        self.de_bottom_frame = QtWidgets.QFrame(self.de_tab)
        self.de_bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.de_bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_bottom_frame.setObjectName("de_bottom_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.de_bottom_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.de_frame_lag_4 = QtWidgets.QFrame(self.de_bottom_frame)
        self.de_frame_lag_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.de_frame_lag_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_frame_lag_4.setObjectName("de_frame_lag_4")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.de_frame_lag_4)
        self.gridLayout_14.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_14.setSpacing(5)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_lag_de_4 = QtWidgets.QLabel(self.de_frame_lag_4)
        self.label_lag_de_4.setObjectName("label_lag_de_4")
        self.gridLayout_14.addWidget(self.label_lag_de_4, 0, 0, 1, 1)
        self.start_de_4 = QtWidgets.QPushButton(self.de_frame_lag_4)
        self.start_de_4.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_de_4.setObjectName("start_de_4")
        self.gridLayout_14.addWidget(self.start_de_4, 0, 1, 1, 1)
        self.stop_de_4 = QtWidgets.QPushButton(self.de_frame_lag_4)
        self.stop_de_4.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_de_4.setObjectName("stop_de_4")
        self.gridLayout_14.addWidget(self.stop_de_4, 0, 2, 1, 1)
        self.label_de_4 = QtWidgets.QLabel(self.de_frame_lag_4)
        self.label_de_4.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_de_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_de_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_de_4.setObjectName("label_de_4")
        self.gridLayout_14.addWidget(self.label_de_4, 1, 0, 1, 3)
        self.horizontalLayout_6.addWidget(self.de_frame_lag_4)
        self.de_frame_lag_5 = QtWidgets.QFrame(self.de_bottom_frame)
        self.de_frame_lag_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.de_frame_lag_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_frame_lag_5.setObjectName("de_frame_lag_5")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.de_frame_lag_5)
        self.gridLayout_15.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_15.setSpacing(5)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_lag_de_5 = QtWidgets.QLabel(self.de_frame_lag_5)
        self.label_lag_de_5.setObjectName("label_lag_de_5")
        self.gridLayout_15.addWidget(self.label_lag_de_5, 0, 0, 1, 1)
        self.start_de_5 = QtWidgets.QPushButton(self.de_frame_lag_5)
        self.start_de_5.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_de_5.setObjectName("start_de_5")
        self.gridLayout_15.addWidget(self.start_de_5, 0, 1, 1, 1)
        self.stop_de_5 = QtWidgets.QPushButton(self.de_frame_lag_5)
        self.stop_de_5.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_de_5.setObjectName("stop_de_5")
        self.gridLayout_15.addWidget(self.stop_de_5, 0, 2, 1, 1)
        self.label_de_5 = QtWidgets.QLabel(self.de_frame_lag_5)
        self.label_de_5.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_de_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_de_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_de_5.setObjectName("label_de_5")
        self.gridLayout_15.addWidget(self.label_de_5, 1, 0, 1, 3)
        self.horizontalLayout_6.addWidget(self.de_frame_lag_5)
        self.de_frame_lag_6 = QtWidgets.QFrame(self.de_bottom_frame)
        self.de_frame_lag_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.de_frame_lag_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_frame_lag_6.setObjectName("de_frame_lag_6")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.de_frame_lag_6)
        self.gridLayout_16.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_16.setSpacing(5)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_lag_de_6 = QtWidgets.QLabel(self.de_frame_lag_6)
        self.label_lag_de_6.setObjectName("label_lag_de_6")
        self.gridLayout_16.addWidget(self.label_lag_de_6, 0, 0, 1, 1)
        self.start_de_6 = QtWidgets.QPushButton(self.de_frame_lag_6)
        self.start_de_6.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_de_6.setObjectName("start_de_6")
        self.gridLayout_16.addWidget(self.start_de_6, 0, 1, 1, 1)
        self.stop_de_6 = QtWidgets.QPushButton(self.de_frame_lag_6)
        self.stop_de_6.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_de_6.setObjectName("stop_de_6")
        self.gridLayout_16.addWidget(self.stop_de_6, 0, 2, 1, 1)
        self.label_de_6 = QtWidgets.QLabel(self.de_frame_lag_6)
        self.label_de_6.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_de_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_de_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_de_6.setObjectName("label_de_6")
        self.gridLayout_16.addWidget(self.label_de_6, 1, 0, 1, 3)
        self.horizontalLayout_6.addWidget(self.de_frame_lag_6)
        self.de_frame_lag_7 = QtWidgets.QFrame(self.de_bottom_frame)
        self.de_frame_lag_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.de_frame_lag_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.de_frame_lag_7.setObjectName("de_frame_lag_7")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.de_frame_lag_7)
        self.gridLayout_17.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_17.setSpacing(5)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_lag_de_7 = QtWidgets.QLabel(self.de_frame_lag_7)
        self.label_lag_de_7.setObjectName("label_lag_de_7")
        self.gridLayout_17.addWidget(self.label_lag_de_7, 0, 0, 1, 1)
        self.start_de_7 = QtWidgets.QPushButton(self.de_frame_lag_7)
        self.start_de_7.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_de_7.setObjectName("start_de_7")
        self.gridLayout_17.addWidget(self.start_de_7, 0, 1, 1, 1)
        self.stop_de_7 = QtWidgets.QPushButton(self.de_frame_lag_7)
        self.stop_de_7.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_de_7.setObjectName("stop_de_7")
        self.gridLayout_17.addWidget(self.stop_de_7, 0, 2, 1, 1)
        self.label_de_7 = QtWidgets.QLabel(self.de_frame_lag_7)
        self.label_de_7.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_de_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_de_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_de_7.setObjectName("label_de_7")
        self.gridLayout_17.addWidget(self.label_de_7, 1, 0, 1, 3)
        self.horizontalLayout_6.addWidget(self.de_frame_lag_7)
        self.verticalLayout_20.addWidget(self.de_bottom_frame)
        self.tabWidget.addTab(self.de_tab, "")
        self.pso_tab = QtWidgets.QWidget()
        self.pso_tab.setObjectName("pso_tab")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.pso_tab)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.pso_settings_frame = QtWidgets.QFrame(self.pso_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pso_settings_frame.sizePolicy().hasHeightForWidth())
        self.pso_settings_frame.setSizePolicy(sizePolicy)
        self.pso_settings_frame.setMaximumSize(QtCore.QSize(16777215, 230))
        self.pso_settings_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pso_settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_settings_frame.setObjectName("pso_settings_frame")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.pso_settings_frame)
        self.horizontalLayout_20.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_20.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_20.setSpacing(9)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pso_settings = QtWidgets.QGroupBox(self.pso_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pso_settings.sizePolicy().hasHeightForWidth())
        self.pso_settings.setSizePolicy(sizePolicy)
        self.pso_settings.setMinimumSize(QtCore.QSize(200, 0))
        self.pso_settings.setMaximumSize(QtCore.QSize(600, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pso_settings.setPalette(palette)
        self.pso_settings.setObjectName("pso_settings")
        self.verticalLayout_66 = QtWidgets.QVBoxLayout(self.pso_settings)
        self.verticalLayout_66.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.pso_settings_1 = QtWidgets.QFrame(self.pso_settings)
        self.pso_settings_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pso_settings_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_settings_1.setObjectName("pso_settings_1")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.pso_settings_1)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pso_settings_labels_frame = QtWidgets.QFrame(self.pso_settings_1)
        self.pso_settings_labels_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pso_settings_labels_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_settings_labels_frame.setObjectName("pso_settings_labels_frame")
        self.verticalLayout_67 = QtWidgets.QVBoxLayout(self.pso_settings_labels_frame)
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        self.pso_particle_label = QtWidgets.QLabel(self.pso_settings_labels_frame)
        self.pso_particle_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pso_particle_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.pso_particle_label.setObjectName("pso_particle_label")
        self.verticalLayout_67.addWidget(self.pso_particle_label)
        self.pso_iterations_label = QtWidgets.QLabel(self.pso_settings_labels_frame)
        self.pso_iterations_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pso_iterations_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.pso_iterations_label.setObjectName("pso_iterations_label")
        self.verticalLayout_67.addWidget(self.pso_iterations_label)
        self.pso_executions_label = QtWidgets.QLabel(self.pso_settings_labels_frame)
        self.pso_executions_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pso_executions_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.pso_executions_label.setObjectName("pso_executions_label")
        self.verticalLayout_67.addWidget(self.pso_executions_label)
        self.horizontalLayout_21.addWidget(self.pso_settings_labels_frame)
        self.pso_settings_fields_frame = QtWidgets.QFrame(self.pso_settings_1)
        self.pso_settings_fields_frame.setMinimumSize(QtCore.QSize(70, 0))
        self.pso_settings_fields_frame.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pso_settings_fields_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pso_settings_fields_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_settings_fields_frame.setObjectName("pso_settings_fields_frame")
        self.verticalLayout_68 = QtWidgets.QVBoxLayout(self.pso_settings_fields_frame)
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName("verticalLayout_68")
        self.pso_particle_field = QtWidgets.QLineEdit(self.pso_settings_fields_frame)
        self.pso_particle_field.setMinimumSize(QtCore.QSize(0, 0))
        self.pso_particle_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pso_particle_field.setObjectName("pso_particle_field")
        self.verticalLayout_68.addWidget(self.pso_particle_field)
        self.pso_iteration_field = QtWidgets.QLineEdit(self.pso_settings_fields_frame)
        self.pso_iteration_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pso_iteration_field.setObjectName("pso_iteration_field")
        self.verticalLayout_68.addWidget(self.pso_iteration_field)
        self.pso_executions_field = QtWidgets.QLineEdit(self.pso_settings_fields_frame)
        self.pso_executions_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pso_executions_field.setObjectName("pso_executions_field")
        self.verticalLayout_68.addWidget(self.pso_executions_field)
        self.horizontalLayout_21.addWidget(self.pso_settings_fields_frame)
        self.verticalLayout_66.addWidget(self.pso_settings_1)
        self.horizontalLayout_20.addWidget(self.pso_settings)
        self.pso_velocity = QtWidgets.QGroupBox(self.pso_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pso_velocity.sizePolicy().hasHeightForWidth())
        self.pso_velocity.setSizePolicy(sizePolicy)
        self.pso_velocity.setMinimumSize(QtCore.QSize(100, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pso_velocity.setPalette(palette)
        self.pso_velocity.setObjectName("pso_velocity")
        self.verticalLayout_70 = QtWidgets.QVBoxLayout(self.pso_velocity)
        self.verticalLayout_70.setObjectName("verticalLayout_70")
        self.pso_classic_radiobutton = QtWidgets.QRadioButton(self.pso_velocity)
        self.pso_classic_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.pso_classic_radiobutton.setChecked(True)
        self.pso_classic_radiobutton.setObjectName("pso_classic_radiobutton")
        self.verticalLayout_70.addWidget(self.pso_classic_radiobutton)
        self.pso_canonica_radiobutton = QtWidgets.QRadioButton(self.pso_velocity)
        self.pso_canonica_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.pso_canonica_radiobutton.setObjectName("pso_canonica_radiobutton")
        self.verticalLayout_70.addWidget(self.pso_canonica_radiobutton)
        self.horizontalLayout_20.addWidget(self.pso_velocity)
        self.pso_cost = QtWidgets.QGroupBox(self.pso_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pso_cost.sizePolicy().hasHeightForWidth())
        self.pso_cost.setSizePolicy(sizePolicy)
        self.pso_cost.setObjectName("pso_cost")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.pso_cost)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.pso_mse_radiobutton = QtWidgets.QRadioButton(self.pso_cost)
        self.pso_mse_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.pso_mse_radiobutton.setChecked(True)
        self.pso_mse_radiobutton.setObjectName("pso_mse_radiobutton")
        self.verticalLayout_15.addWidget(self.pso_mse_radiobutton)
        self.pso_ae_radiobutton = QtWidgets.QRadioButton(self.pso_cost)
        self.pso_ae_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.pso_ae_radiobutton.setObjectName("pso_ae_radiobutton")
        self.verticalLayout_15.addWidget(self.pso_ae_radiobutton)
        self.horizontalLayout_20.addWidget(self.pso_cost)
        self.pso_inertial = QtWidgets.QGroupBox(self.pso_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pso_inertial.sizePolicy().hasHeightForWidth())
        self.pso_inertial.setSizePolicy(sizePolicy)
        self.pso_inertial.setMinimumSize(QtCore.QSize(210, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pso_inertial.setPalette(palette)
        self.pso_inertial.setObjectName("pso_inertial")
        self.verticalLayout_71 = QtWidgets.QVBoxLayout(self.pso_inertial)
        self.verticalLayout_71.setObjectName("verticalLayout_71")
        self.constant_radiobutton = QtWidgets.QRadioButton(self.pso_inertial)
        self.constant_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.constant_radiobutton.setChecked(True)
        self.constant_radiobutton.setObjectName("constant_radiobutton")
        self.verticalLayout_71.addWidget(self.constant_radiobutton)
        self.linear_fall_radiobutton = QtWidgets.QRadioButton(self.pso_inertial)
        self.linear_fall_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.linear_fall_radiobutton.setObjectName("linear_fall_radiobutton")
        self.verticalLayout_71.addWidget(self.linear_fall_radiobutton)
        self.linear_rise_radiobutton = QtWidgets.QRadioButton(self.pso_inertial)
        self.linear_rise_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.linear_rise_radiobutton.setObjectName("linear_rise_radiobutton")
        self.verticalLayout_71.addWidget(self.linear_rise_radiobutton)
        self.w_frame = QtWidgets.QFrame(self.pso_inertial)
        self.w_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.w_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.w_frame.setObjectName("w_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.w_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.w_label_frame = QtWidgets.QFrame(self.w_frame)
        self.w_label_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.w_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.w_label_frame.setObjectName("w_label_frame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.w_label_frame)
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.w_label = QtWidgets.QLabel(self.w_label_frame)
        self.w_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.w_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.w_label.setObjectName("w_label")
        self.verticalLayout_13.addWidget(self.w_label)
        self.horizontalLayout_7.addWidget(self.w_label_frame)
        self.w_field_frame = QtWidgets.QFrame(self.w_frame)
        self.w_field_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.w_field_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.w_field_frame.setObjectName("w_field_frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.w_field_frame)
        self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.w_field = QtWidgets.QLineEdit(self.w_field_frame)
        self.w_field.setMaximumSize(QtCore.QSize(100, 16777215))
        self.w_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.w_field.setObjectName("w_field")
        self.verticalLayout_12.addWidget(self.w_field)
        self.horizontalLayout_7.addWidget(self.w_field_frame)
        self.verticalLayout_71.addWidget(self.w_frame)
        self.horizontalLayout_20.addWidget(self.pso_inertial)
        self.pso_constants = QtWidgets.QGroupBox(self.pso_settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pso_constants.sizePolicy().hasHeightForWidth())
        self.pso_constants.setSizePolicy(sizePolicy)
        self.pso_constants.setMinimumSize(QtCore.QSize(200, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pso_constants.setPalette(palette)
        self.pso_constants.setObjectName("pso_constants")
        self.verticalLayout_72 = QtWidgets.QVBoxLayout(self.pso_constants)
        self.verticalLayout_72.setObjectName("verticalLayout_72")
        self.normal_radiobutton = QtWidgets.QRadioButton(self.pso_constants)
        self.normal_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.normal_radiobutton.setChecked(True)
        self.normal_radiobutton.setObjectName("normal_radiobutton")
        self.verticalLayout_72.addWidget(self.normal_radiobutton)
        self.pso_constants_frame = QtWidgets.QFrame(self.pso_constants)
        self.pso_constants_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pso_constants_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_constants_frame.setObjectName("pso_constants_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.pso_constants_frame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.constants_label_frame = QtWidgets.QFrame(self.pso_constants_frame)
        self.constants_label_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.constants_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.constants_label_frame.setObjectName("constants_label_frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.constants_label_frame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.c1_label = QtWidgets.QLabel(self.constants_label_frame)
        self.c1_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.c1_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.c1_label.setObjectName("c1_label")
        self.verticalLayout_11.addWidget(self.c1_label)
        self.c2_label = QtWidgets.QLabel(self.constants_label_frame)
        self.c2_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.c2_label.setStyleSheet("color: rgb(238, 238, 236);")
        self.c2_label.setObjectName("c2_label")
        self.verticalLayout_11.addWidget(self.c2_label)
        self.horizontalLayout_10.addWidget(self.constants_label_frame)
        self.constants_field_frame = QtWidgets.QFrame(self.pso_constants_frame)
        self.constants_field_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.constants_field_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.constants_field_frame.setObjectName("constants_field_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.constants_field_frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.c1_field = QtWidgets.QLineEdit(self.constants_field_frame)
        self.c1_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.c1_field.setObjectName("c1_field")
        self.verticalLayout_10.addWidget(self.c1_field)
        self.c2_field = QtWidgets.QLineEdit(self.constants_field_frame)
        self.c2_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.c2_field.setObjectName("c2_field")
        self.verticalLayout_10.addWidget(self.c2_field)
        self.horizontalLayout_10.addWidget(self.constants_field_frame)
        self.verticalLayout_72.addWidget(self.pso_constants_frame)
        self.dynamic_mutation_radiobutton = QtWidgets.QRadioButton(self.pso_constants)
        self.dynamic_mutation_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.dynamic_mutation_radiobutton.setObjectName("dynamic_mutation_radiobutton")
        self.verticalLayout_72.addWidget(self.dynamic_mutation_radiobutton)
        self.horizontalLayout_20.addWidget(self.pso_constants)
        self.verticalLayout_21.addWidget(self.pso_settings_frame)
        self.pso_upper_frame = QtWidgets.QFrame(self.pso_tab)
        self.pso_upper_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pso_upper_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_upper_frame.setObjectName("pso_upper_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.pso_upper_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pso_frame_lag_0 = QtWidgets.QFrame(self.pso_upper_frame)
        self.pso_frame_lag_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pso_frame_lag_0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_frame_lag_0.setObjectName("pso_frame_lag_0")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.pso_frame_lag_0)
        self.gridLayout_18.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_18.setSpacing(5)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_lag_pso_0 = QtWidgets.QLabel(self.pso_frame_lag_0)
        self.label_lag_pso_0.setObjectName("label_lag_pso_0")
        self.gridLayout_18.addWidget(self.label_lag_pso_0, 0, 0, 1, 1)
        self.start_pso_0 = QtWidgets.QPushButton(self.pso_frame_lag_0)
        self.start_pso_0.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_pso_0.setObjectName("start_pso_0")
        self.gridLayout_18.addWidget(self.start_pso_0, 0, 1, 1, 1)
        self.stop_pso_0 = QtWidgets.QPushButton(self.pso_frame_lag_0)
        self.stop_pso_0.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_pso_0.setObjectName("stop_pso_0")
        self.gridLayout_18.addWidget(self.stop_pso_0, 0, 2, 1, 1)
        self.label_pso_0 = QtWidgets.QLabel(self.pso_frame_lag_0)
        self.label_pso_0.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_pso_0.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pso_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pso_0.setObjectName("label_pso_0")
        self.gridLayout_18.addWidget(self.label_pso_0, 1, 0, 1, 3)
        self.horizontalLayout_8.addWidget(self.pso_frame_lag_0)
        self.pso_frame_lag_1 = QtWidgets.QFrame(self.pso_upper_frame)
        self.pso_frame_lag_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pso_frame_lag_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_frame_lag_1.setObjectName("pso_frame_lag_1")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.pso_frame_lag_1)
        self.gridLayout_19.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_19.setSpacing(5)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_lag_pso_1 = QtWidgets.QLabel(self.pso_frame_lag_1)
        self.label_lag_pso_1.setObjectName("label_lag_pso_1")
        self.gridLayout_19.addWidget(self.label_lag_pso_1, 0, 0, 1, 1)
        self.start_pso_1 = QtWidgets.QPushButton(self.pso_frame_lag_1)
        self.start_pso_1.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_pso_1.setObjectName("start_pso_1")
        self.gridLayout_19.addWidget(self.start_pso_1, 0, 1, 1, 1)
        self.stop_pso_1 = QtWidgets.QPushButton(self.pso_frame_lag_1)
        self.stop_pso_1.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_pso_1.setObjectName("stop_pso_1")
        self.gridLayout_19.addWidget(self.stop_pso_1, 0, 2, 1, 1)
        self.label_pso_1 = QtWidgets.QLabel(self.pso_frame_lag_1)
        self.label_pso_1.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_pso_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pso_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pso_1.setObjectName("label_pso_1")
        self.gridLayout_19.addWidget(self.label_pso_1, 1, 0, 1, 3)
        self.horizontalLayout_8.addWidget(self.pso_frame_lag_1)
        self.pso_frame_lag_2 = QtWidgets.QFrame(self.pso_upper_frame)
        self.pso_frame_lag_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pso_frame_lag_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_frame_lag_2.setObjectName("pso_frame_lag_2")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.pso_frame_lag_2)
        self.gridLayout_20.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_20.setSpacing(5)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_lag_pso_2 = QtWidgets.QLabel(self.pso_frame_lag_2)
        self.label_lag_pso_2.setObjectName("label_lag_pso_2")
        self.gridLayout_20.addWidget(self.label_lag_pso_2, 0, 0, 1, 1)
        self.start_pso_2 = QtWidgets.QPushButton(self.pso_frame_lag_2)
        self.start_pso_2.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_pso_2.setObjectName("start_pso_2")
        self.gridLayout_20.addWidget(self.start_pso_2, 0, 1, 1, 1)
        self.stop_pso_2 = QtWidgets.QPushButton(self.pso_frame_lag_2)
        self.stop_pso_2.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_pso_2.setObjectName("stop_pso_2")
        self.gridLayout_20.addWidget(self.stop_pso_2, 0, 2, 1, 1)
        self.label_pso_2 = QtWidgets.QLabel(self.pso_frame_lag_2)
        self.label_pso_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_pso_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pso_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pso_2.setObjectName("label_pso_2")
        self.gridLayout_20.addWidget(self.label_pso_2, 1, 0, 1, 3)
        self.horizontalLayout_8.addWidget(self.pso_frame_lag_2)
        self.pso_frame_lag_3 = QtWidgets.QFrame(self.pso_upper_frame)
        self.pso_frame_lag_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pso_frame_lag_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_frame_lag_3.setObjectName("pso_frame_lag_3")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.pso_frame_lag_3)
        self.gridLayout_21.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_21.setSpacing(5)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_lag_pso_3 = QtWidgets.QLabel(self.pso_frame_lag_3)
        self.label_lag_pso_3.setObjectName("label_lag_pso_3")
        self.gridLayout_21.addWidget(self.label_lag_pso_3, 0, 0, 1, 1)
        self.start_pso_3 = QtWidgets.QPushButton(self.pso_frame_lag_3)
        self.start_pso_3.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_pso_3.setObjectName("start_pso_3")
        self.gridLayout_21.addWidget(self.start_pso_3, 0, 1, 1, 1)
        self.stop_pso_3 = QtWidgets.QPushButton(self.pso_frame_lag_3)
        self.stop_pso_3.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_pso_3.setObjectName("stop_pso_3")
        self.gridLayout_21.addWidget(self.stop_pso_3, 0, 2, 1, 1)
        self.label_pso_3 = QtWidgets.QLabel(self.pso_frame_lag_3)
        self.label_pso_3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_pso_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pso_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pso_3.setObjectName("label_pso_3")
        self.gridLayout_21.addWidget(self.label_pso_3, 1, 0, 1, 3)
        self.horizontalLayout_8.addWidget(self.pso_frame_lag_3)
        self.verticalLayout_21.addWidget(self.pso_upper_frame)
        self.pso_bottom_frame = QtWidgets.QFrame(self.pso_tab)
        self.pso_bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pso_bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_bottom_frame.setObjectName("pso_bottom_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.pso_bottom_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pso_frame_lag_4 = QtWidgets.QFrame(self.pso_bottom_frame)
        self.pso_frame_lag_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pso_frame_lag_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_frame_lag_4.setObjectName("pso_frame_lag_4")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.pso_frame_lag_4)
        self.gridLayout_22.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_22.setSpacing(5)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_lag_pso_4 = QtWidgets.QLabel(self.pso_frame_lag_4)
        self.label_lag_pso_4.setObjectName("label_lag_pso_4")
        self.gridLayout_22.addWidget(self.label_lag_pso_4, 0, 0, 1, 1)
        self.start_pso_4 = QtWidgets.QPushButton(self.pso_frame_lag_4)
        self.start_pso_4.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_pso_4.setObjectName("start_pso_4")
        self.gridLayout_22.addWidget(self.start_pso_4, 0, 1, 1, 1)
        self.stop_pso_4 = QtWidgets.QPushButton(self.pso_frame_lag_4)
        self.stop_pso_4.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_pso_4.setObjectName("stop_pso_4")
        self.gridLayout_22.addWidget(self.stop_pso_4, 0, 2, 1, 1)
        self.label_pso_4 = QtWidgets.QLabel(self.pso_frame_lag_4)
        self.label_pso_4.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_pso_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pso_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pso_4.setObjectName("label_pso_4")
        self.gridLayout_22.addWidget(self.label_pso_4, 1, 0, 1, 3)
        self.horizontalLayout_9.addWidget(self.pso_frame_lag_4)
        self.pso_frame_lag_5 = QtWidgets.QFrame(self.pso_bottom_frame)
        self.pso_frame_lag_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pso_frame_lag_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_frame_lag_5.setObjectName("pso_frame_lag_5")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.pso_frame_lag_5)
        self.gridLayout_23.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_23.setSpacing(5)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.label_lag_pso_5 = QtWidgets.QLabel(self.pso_frame_lag_5)
        self.label_lag_pso_5.setObjectName("label_lag_pso_5")
        self.gridLayout_23.addWidget(self.label_lag_pso_5, 0, 0, 1, 1)
        self.start_pso_5 = QtWidgets.QPushButton(self.pso_frame_lag_5)
        self.start_pso_5.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_pso_5.setObjectName("start_pso_5")
        self.gridLayout_23.addWidget(self.start_pso_5, 0, 1, 1, 1)
        self.stop_pso_5 = QtWidgets.QPushButton(self.pso_frame_lag_5)
        self.stop_pso_5.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_pso_5.setObjectName("stop_pso_5")
        self.gridLayout_23.addWidget(self.stop_pso_5, 0, 2, 1, 1)
        self.label_pso_5 = QtWidgets.QLabel(self.pso_frame_lag_5)
        self.label_pso_5.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_pso_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pso_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pso_5.setObjectName("label_pso_5")
        self.gridLayout_23.addWidget(self.label_pso_5, 1, 0, 1, 3)
        self.horizontalLayout_9.addWidget(self.pso_frame_lag_5)
        self.pso_frame_lag_6 = QtWidgets.QFrame(self.pso_bottom_frame)
        self.pso_frame_lag_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pso_frame_lag_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_frame_lag_6.setObjectName("pso_frame_lag_6")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.pso_frame_lag_6)
        self.gridLayout_24.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_24.setSpacing(5)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_lag_pso_6 = QtWidgets.QLabel(self.pso_frame_lag_6)
        self.label_lag_pso_6.setObjectName("label_lag_pso_6")
        self.gridLayout_24.addWidget(self.label_lag_pso_6, 0, 0, 1, 1)
        self.start_pso_6 = QtWidgets.QPushButton(self.pso_frame_lag_6)
        self.start_pso_6.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_pso_6.setObjectName("start_pso_6")
        self.gridLayout_24.addWidget(self.start_pso_6, 0, 1, 1, 1)
        self.stop_pso_6 = QtWidgets.QPushButton(self.pso_frame_lag_6)
        self.stop_pso_6.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_pso_6.setObjectName("stop_pso_6")
        self.gridLayout_24.addWidget(self.stop_pso_6, 0, 2, 1, 1)
        self.label_pso_6 = QtWidgets.QLabel(self.pso_frame_lag_6)
        self.label_pso_6.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_pso_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pso_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pso_6.setObjectName("label_pso_6")
        self.gridLayout_24.addWidget(self.label_pso_6, 1, 0, 1, 3)
        self.horizontalLayout_9.addWidget(self.pso_frame_lag_6)
        self.pso_frame_lag_7 = QtWidgets.QFrame(self.pso_bottom_frame)
        self.pso_frame_lag_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pso_frame_lag_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pso_frame_lag_7.setObjectName("pso_frame_lag_7")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.pso_frame_lag_7)
        self.gridLayout_25.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_25.setSpacing(5)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.label_lag_pso_7 = QtWidgets.QLabel(self.pso_frame_lag_7)
        self.label_lag_pso_7.setObjectName("label_lag_pso_7")
        self.gridLayout_25.addWidget(self.label_lag_pso_7, 0, 0, 1, 1)
        self.start_pso_7 = QtWidgets.QPushButton(self.pso_frame_lag_7)
        self.start_pso_7.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.start_pso_7.setObjectName("start_pso_7")
        self.gridLayout_25.addWidget(self.start_pso_7, 0, 1, 1, 1)
        self.stop_pso_7 = QtWidgets.QPushButton(self.pso_frame_lag_7)
        self.stop_pso_7.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(0, 0, 0);")
        self.stop_pso_7.setObjectName("stop_pso_7")
        self.gridLayout_25.addWidget(self.stop_pso_7, 0, 2, 1, 1)
        self.label_pso_7 = QtWidgets.QLabel(self.pso_frame_lag_7)
        self.label_pso_7.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_pso_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pso_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pso_7.setObjectName("label_pso_7")
        self.gridLayout_25.addWidget(self.label_pso_7, 1, 0, 1, 3)
        self.horizontalLayout_9.addWidget(self.pso_frame_lag_7)
        self.verticalLayout_21.addWidget(self.pso_bottom_frame)
        self.tabWidget.addTab(self.pso_tab, "")
        self.results_tab = QtWidgets.QWidget()
        self.results_tab.setObjectName("results_tab")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.results_tab)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setSpacing(5)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.graph_file_field = QtWidgets.QLineEdit(self.results_tab)
        self.graph_file_field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.graph_file_field.setObjectName("graph_file_field")
        self.gridLayout_26.addWidget(self.graph_file_field, 1, 0, 1, 1)
        self.process_open_button = QtWidgets.QPushButton(self.results_tab)
        self.process_open_button.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.process_open_button.setObjectName("process_open_button")
        self.gridLayout_26.addWidget(self.process_open_button, 1, 1, 1, 1)
        self.graph_frame = QtWidgets.QFrame(self.results_tab)
        self.graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_frame.setObjectName("graph_frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.graph_frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.graph_groupbox = QtWidgets.QGroupBox(self.graph_frame)
        self.graph_groupbox.setObjectName("graph_groupbox")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.graph_groupbox)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.database_radiobutton = QtWidgets.QRadioButton(self.graph_groupbox)
        self.database_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.database_radiobutton.setChecked(True)
        self.database_radiobutton.setObjectName("database_radiobutton")
        self.verticalLayout_17.addWidget(self.database_radiobutton)
        self.rxp_test_radiobutton = QtWidgets.QRadioButton(self.graph_groupbox)
        self.rxp_test_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.rxp_test_radiobutton.setChecked(False)
        self.rxp_test_radiobutton.setObjectName("rxp_test_radiobutton")
        self.verticalLayout_17.addWidget(self.rxp_test_radiobutton)
        self.rxp_training_radiobutton = QtWidgets.QRadioButton(self.graph_groupbox)
        self.rxp_training_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.rxp_training_radiobutton.setObjectName("rxp_training_radiobutton")
        self.verticalLayout_17.addWidget(self.rxp_training_radiobutton)
        self.gb_fitness_radiobutton = QtWidgets.QRadioButton(self.graph_groupbox)
        self.gb_fitness_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.gb_fitness_radiobutton.setObjectName("gb_fitness_radiobutton")
        self.verticalLayout_17.addWidget(self.gb_fitness_radiobutton)
        self.gb_cost_radiobutton = QtWidgets.QRadioButton(self.graph_groupbox)
        self.gb_cost_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.gb_cost_radiobutton.setObjectName("gb_cost_radiobutton")
        self.verticalLayout_17.addWidget(self.gb_cost_radiobutton)
        self.boxplot_fitness_radiobutton = QtWidgets.QRadioButton(self.graph_groupbox)
        self.boxplot_fitness_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.boxplot_fitness_radiobutton.setObjectName("boxplot_fitness_radiobutton")
        self.verticalLayout_17.addWidget(self.boxplot_fitness_radiobutton)
        self.boxplot_cost_radiobutton = QtWidgets.QRadioButton(self.graph_groupbox)
        self.boxplot_cost_radiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.boxplot_cost_radiobutton.setObjectName("boxplot_cost_radiobutton")
        self.verticalLayout_17.addWidget(self.boxplot_cost_radiobutton)
        self.plot_graph_button = QtWidgets.QPushButton(self.graph_groupbox)
        self.plot_graph_button.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.plot_graph_button.setObjectName("plot_graph_button")
        self.verticalLayout_17.addWidget(self.plot_graph_button)
        self.horizontalLayout_11.addWidget(self.graph_groupbox)
        self.tableresults_groupbox = QtWidgets.QGroupBox(self.graph_frame)
        self.tableresults_groupbox.setObjectName("tableresults_groupbox")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.tableresults_groupbox)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.lag2_label = QtWidgets.QLabel(self.tableresults_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lag2_label.sizePolicy().hasHeightForWidth())
        self.lag2_label.setSizePolicy(sizePolicy)
        self.lag2_label.setObjectName("lag2_label")
        self.gridLayout_28.addWidget(self.lag2_label, 4, 0, 1, 1)
        self.copy_lag1_pushbutton = QtWidgets.QPushButton(self.tableresults_groupbox)
        self.copy_lag1_pushbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.copy_lag1_pushbutton.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.copy_lag1_pushbutton.setObjectName("copy_lag1_pushbutton")
        self.gridLayout_28.addWidget(self.copy_lag1_pushbutton, 3, 0, 1, 1)
        self.lag1_label = QtWidgets.QLabel(self.tableresults_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lag1_label.sizePolicy().hasHeightForWidth())
        self.lag1_label.setSizePolicy(sizePolicy)
        self.lag1_label.setObjectName("lag1_label")
        self.gridLayout_28.addWidget(self.lag1_label, 2, 0, 1, 1)
        self.copy_lag7_pushbutton = QtWidgets.QPushButton(self.tableresults_groupbox)
        self.copy_lag7_pushbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.copy_lag7_pushbutton.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.copy_lag7_pushbutton.setObjectName("copy_lag7_pushbutton")
        self.gridLayout_28.addWidget(self.copy_lag7_pushbutton, 18, 0, 1, 1)
        self.lag0_label = QtWidgets.QLabel(self.tableresults_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lag0_label.sizePolicy().hasHeightForWidth())
        self.lag0_label.setSizePolicy(sizePolicy)
        self.lag0_label.setObjectName("lag0_label")
        self.gridLayout_28.addWidget(self.lag0_label, 0, 0, 1, 1)
        self.lag4_label = QtWidgets.QLabel(self.tableresults_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lag4_label.sizePolicy().hasHeightForWidth())
        self.lag4_label.setSizePolicy(sizePolicy)
        self.lag4_label.setObjectName("lag4_label")
        self.gridLayout_28.addWidget(self.lag4_label, 8, 0, 1, 1)
        self.copy_lag0_pushbutton = QtWidgets.QPushButton(self.tableresults_groupbox)
        self.copy_lag0_pushbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.copy_lag0_pushbutton.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.copy_lag0_pushbutton.setObjectName("copy_lag0_pushbutton")
        self.gridLayout_28.addWidget(self.copy_lag0_pushbutton, 1, 0, 1, 1)
        self.lag6_label = QtWidgets.QLabel(self.tableresults_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lag6_label.sizePolicy().hasHeightForWidth())
        self.lag6_label.setSizePolicy(sizePolicy)
        self.lag6_label.setObjectName("lag6_label")
        self.gridLayout_28.addWidget(self.lag6_label, 15, 0, 1, 1)
        self.copy_lag5_pushbutton = QtWidgets.QPushButton(self.tableresults_groupbox)
        self.copy_lag5_pushbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.copy_lag5_pushbutton.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.copy_lag5_pushbutton.setObjectName("copy_lag5_pushbutton")
        self.gridLayout_28.addWidget(self.copy_lag5_pushbutton, 14, 0, 1, 1)
        self.copy_lag2_pushbutton = QtWidgets.QPushButton(self.tableresults_groupbox)
        self.copy_lag2_pushbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.copy_lag2_pushbutton.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.copy_lag2_pushbutton.setObjectName("copy_lag2_pushbutton")
        self.gridLayout_28.addWidget(self.copy_lag2_pushbutton, 5, 0, 1, 1)
        self.copy_lag6_pushbutton = QtWidgets.QPushButton(self.tableresults_groupbox)
        self.copy_lag6_pushbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.copy_lag6_pushbutton.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.copy_lag6_pushbutton.setObjectName("copy_lag6_pushbutton")
        self.gridLayout_28.addWidget(self.copy_lag6_pushbutton, 16, 0, 1, 1)
        self.copy_lag3_pushbutton = QtWidgets.QPushButton(self.tableresults_groupbox)
        self.copy_lag3_pushbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.copy_lag3_pushbutton.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.copy_lag3_pushbutton.setObjectName("copy_lag3_pushbutton")
        self.gridLayout_28.addWidget(self.copy_lag3_pushbutton, 7, 0, 1, 1)
        self.copy_lag4_pushbutton = QtWidgets.QPushButton(self.tableresults_groupbox)
        self.copy_lag4_pushbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.copy_lag4_pushbutton.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.copy_lag4_pushbutton.setObjectName("copy_lag4_pushbutton")
        self.gridLayout_28.addWidget(self.copy_lag4_pushbutton, 9, 0, 1, 1)
        self.lag3_label = QtWidgets.QLabel(self.tableresults_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lag3_label.sizePolicy().hasHeightForWidth())
        self.lag3_label.setSizePolicy(sizePolicy)
        self.lag3_label.setObjectName("lag3_label")
        self.gridLayout_28.addWidget(self.lag3_label, 6, 0, 1, 1)
        self.lag5_label = QtWidgets.QLabel(self.tableresults_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lag5_label.sizePolicy().hasHeightForWidth())
        self.lag5_label.setSizePolicy(sizePolicy)
        self.lag5_label.setObjectName("lag5_label")
        self.gridLayout_28.addWidget(self.lag5_label, 10, 0, 1, 1)
        self.lag7_label = QtWidgets.QLabel(self.tableresults_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lag7_label.sizePolicy().hasHeightForWidth())
        self.lag7_label.setSizePolicy(sizePolicy)
        self.lag7_label.setObjectName("lag7_label")
        self.gridLayout_28.addWidget(self.lag7_label, 17, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.tableresults_groupbox)
        self.gridLayout_26.addWidget(self.graph_frame, 2, 0, 1, 3)
        self.tabWidget.addTab(self.results_tab, "")
        self.gridLayout_27.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_file_label.setText(_translate("MainWindow", "File with excel:"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.dayindex_field.setText(_translate("MainWindow", "0"))
        self.prediction_field.setText(_translate("MainWindow", "1"))
        self.number_test_samples_field.setText(_translate("MainWindow", "156"))
        self.number_test_samples_label.setText(_translate("MainWindow", "Number of test samples:"))
        self.prediction_label.setText(_translate("MainWindow", "Observed Value Index:"))
        self.dayindex_label.setText(_translate("MainWindow", "Day Index:"))
        self.dayoftheweek_field.setText(_translate("MainWindow", "5"))
        self.dayoftheweek_label.setText(_translate("MainWindow", "Day of the week index:"))
        self.exec_method_groupbox.setTitle(_translate("MainWindow", "Execution Method Type"))
        self.exec_method_radiobutton.setText(_translate("MainWindow", "Execution Method"))
        self.debug_method_radiobutton.setText(_translate("MainWindow", "Debug Method"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.globalsettings_tab), _translate("MainWindow", "Global Settings"))
        self.ga_settings.setTitle(_translate("MainWindow", "Settings"))
        self.ga_population_label.setText(_translate("MainWindow", "Population size:"))
        self.ga_generations_label.setText(_translate("MainWindow", "Number of generations:"))
        self.ga_executions_label.setText(_translate("MainWindow", "Number of executions:"))
        self.ga_population_field.setText(_translate("MainWindow", "100"))
        self.ga_gerations_field.setText(_translate("MainWindow", "2000"))
        self.ga_executions_field.setText(_translate("MainWindow", "30"))
        self.ga_selection.setTitle(_translate("MainWindow", "Type of Selection"))
        self.roulette_radiobutton.setText(_translate("MainWindow", "Roulette"))
        self.roulette_sus_radiobutton.setText(_translate("MainWindow", "Roulette S.U.S."))
        self.single_tournament_radiobutton.setText(_translate("MainWindow", "Single Tournament"))
        self.death_tournament_radiobutton.setText(_translate("MainWindow", "Death Tournament"))
        self.local_search_label.setText(_translate("MainWindow", "Local search every:"))
        self.ga_cost.setTitle(_translate("MainWindow", "Type of Cost"))
        self.ga_mse_radiobutton.setText(_translate("MainWindow", "MSE"))
        self.ga_ae_radiobutton.setText(_translate("MainWindow", "AE"))
        self.ga_crossover.setTitle(_translate("MainWindow", "Type of Crossover"))
        self.point_radiobutton.setText(_translate("MainWindow", "Point"))
        self.arithmetic_radiobutton.setText(_translate("MainWindow", "Arithmetic"))
        self.sbx_radiobutton.setText(_translate("MainWindow", "SBX"))
        self.crossover_rate_label.setText(_translate("MainWindow", "Crossover rate:"))
        self.ga_mutation.setTitle(_translate("MainWindow", "Type of Mutation"))
        self.fixed_mutation_radiobutton.setText(_translate("MainWindow", "Fixed Mutation"))
        self.dyn_mutation_radiobutton.setText(_translate("MainWindow", "Dynamic Mutation"))
        self.mutation_rate_label.setText(_translate("MainWindow", "Mutation Rate:"))
        self.label_lag_ga_0.setText(_translate("MainWindow", "Lag 0"))
        self.start_ga_0.setText(_translate("MainWindow", "Start"))
        self.stop_ga_0.setText(_translate("MainWindow", "Stop"))
        self.label_ga_0.setText(_translate("MainWindow", "available"))
        self.label_lag_ga_1.setText(_translate("MainWindow", "Lag 1"))
        self.start_ga_1.setText(_translate("MainWindow", "Start"))
        self.stop_ga_1.setText(_translate("MainWindow", "Stop"))
        self.label_ga_1.setText(_translate("MainWindow", "available"))
        self.label_lag_ga_2.setText(_translate("MainWindow", "Lag 2"))
        self.start_ga_2.setText(_translate("MainWindow", "Start"))
        self.stop_ga_2.setText(_translate("MainWindow", "Stop"))
        self.label_ga_2.setText(_translate("MainWindow", "available"))
        self.label_lag_ga_3.setText(_translate("MainWindow", "Lag 3"))
        self.start_ga_3.setText(_translate("MainWindow", "Start"))
        self.stop_ga_3.setText(_translate("MainWindow", "Stop"))
        self.label_ga_3.setText(_translate("MainWindow", "available"))
        self.label_lag_ga_4.setText(_translate("MainWindow", "Lag 4"))
        self.start_ga_4.setText(_translate("MainWindow", "Start"))
        self.stop_ga_4.setText(_translate("MainWindow", "Stop"))
        self.label_ga_4.setText(_translate("MainWindow", "available"))
        self.label_lag_ga_5.setText(_translate("MainWindow", "Lag 5"))
        self.start_ga_5.setText(_translate("MainWindow", "Start"))
        self.stop_ga_5.setText(_translate("MainWindow", "Stop"))
        self.label_ga_5.setText(_translate("MainWindow", "available"))
        self.label_lag_ga_6.setText(_translate("MainWindow", "Lag 6"))
        self.start_ga_6.setText(_translate("MainWindow", "Start"))
        self.stop_ga_6.setText(_translate("MainWindow", "Stop"))
        self.label_ga_6.setText(_translate("MainWindow", "available"))
        self.label_lag_ga_7.setText(_translate("MainWindow", "Lag 7"))
        self.start_ga_7.setText(_translate("MainWindow", "Start"))
        self.stop_ga_7.setText(_translate("MainWindow", "Stop"))
        self.label_ga_7.setText(_translate("MainWindow", "available"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ga_tab), _translate("MainWindow", "GA"))
        self.de_settings.setTitle(_translate("MainWindow", "Settings"))
        self.de_population_label.setText(_translate("MainWindow", "Population size:"))
        self.de_generations_label.setText(_translate("MainWindow", "Number of generations:"))
        self.de_executions_label.setText(_translate("MainWindow", "Number of executions:"))
        self.de_population_field.setText(_translate("MainWindow", "100"))
        self.de_gerations_field.setText(_translate("MainWindow", "1000"))
        self.de_executions_field.setText(_translate("MainWindow", "30"))
        self.de_selection.setTitle(_translate("MainWindow", "Type of Selection"))
        self.greedy_radiobutton.setText(_translate("MainWindow", "Greedy"))
        self.number_f_label.setText(_translate("MainWindow", "Number of \"F\":"))
        self.de_cost.setTitle(_translate("MainWindow", "Type of Cost"))
        self.de_mse_radiobutton.setText(_translate("MainWindow", "MSE"))
        self.de_ae_radiobutton.setText(_translate("MainWindow", "AE"))
        self.de_crossover.setTitle(_translate("MainWindow", "Type of Crossover"))
        self.exponential_radiobutton.setText(_translate("MainWindow", "Exponential"))
        self.binary_radiobutton.setText(_translate("MainWindow", "Binary"))
        self.crossover_rate_label_2.setText(_translate("MainWindow", "Crossover rate:"))
        self.de_mutation.setTitle(_translate("MainWindow", "Type of Mutation"))
        self.rand_radiobutton.setText(_translate("MainWindow", "Rand"))
        self.rand2dp_radiobutton.setText(_translate("MainWindow", "Rand2DP"))
        self.best_radiobutton.setText(_translate("MainWindow", "Best"))
        self.best2dp_radiobutton.setText(_translate("MainWindow", "Best2DP"))
        self.target_to_best_radiobutton.setText(_translate("MainWindow", "Target to best"))
        self.mutation_rate_label_2.setText(_translate("MainWindow", "Mutation Rate:"))
        self.label_lag_de_0.setText(_translate("MainWindow", "Lag 0"))
        self.start_de_0.setText(_translate("MainWindow", "Start"))
        self.stop_de_0.setText(_translate("MainWindow", "Stop"))
        self.label_de_0.setText(_translate("MainWindow", "available"))
        self.label_lag_de_1.setText(_translate("MainWindow", "Lag 1"))
        self.start_de_1.setText(_translate("MainWindow", "Start"))
        self.stop_de_1.setText(_translate("MainWindow", "Stop"))
        self.label_de_1.setText(_translate("MainWindow", "available"))
        self.label_lag_de_2.setText(_translate("MainWindow", "Lag 2"))
        self.start_de_2.setText(_translate("MainWindow", "Start"))
        self.stop_de_2.setText(_translate("MainWindow", "Stop"))
        self.label_de_2.setText(_translate("MainWindow", "available"))
        self.label_lag_de_3.setText(_translate("MainWindow", "Lag 3"))
        self.start_de_3.setText(_translate("MainWindow", "Start"))
        self.stop_de_3.setText(_translate("MainWindow", "Stop"))
        self.label_de_3.setText(_translate("MainWindow", "available"))
        self.label_lag_de_4.setText(_translate("MainWindow", "Lag 4"))
        self.start_de_4.setText(_translate("MainWindow", "Start"))
        self.stop_de_4.setText(_translate("MainWindow", "Stop"))
        self.label_de_4.setText(_translate("MainWindow", "available"))
        self.label_lag_de_5.setText(_translate("MainWindow", "Lag 5"))
        self.start_de_5.setText(_translate("MainWindow", "Start"))
        self.stop_de_5.setText(_translate("MainWindow", "Stop"))
        self.label_de_5.setText(_translate("MainWindow", "available"))
        self.label_lag_de_6.setText(_translate("MainWindow", "Lag 6"))
        self.start_de_6.setText(_translate("MainWindow", "Start"))
        self.stop_de_6.setText(_translate("MainWindow", "Stop"))
        self.label_de_6.setText(_translate("MainWindow", "available"))
        self.label_lag_de_7.setText(_translate("MainWindow", "Lag 7"))
        self.start_de_7.setText(_translate("MainWindow", "Start"))
        self.stop_de_7.setText(_translate("MainWindow", "Stop"))
        self.label_de_7.setText(_translate("MainWindow", "available"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.de_tab), _translate("MainWindow", "DE"))
        self.pso_settings.setTitle(_translate("MainWindow", "Settings"))
        self.pso_particle_label.setText(_translate("MainWindow", "Particle number:"))
        self.pso_iterations_label.setText(_translate("MainWindow", "Number of iterations:"))
        self.pso_executions_label.setText(_translate("MainWindow", "Number of executions:"))
        self.pso_particle_field.setText(_translate("MainWindow", "50"))
        self.pso_iteration_field.setText(_translate("MainWindow", "2000"))
        self.pso_executions_field.setText(_translate("MainWindow", "30"))
        self.pso_velocity.setTitle(_translate("MainWindow", "Type of Velocity"))
        self.pso_classic_radiobutton.setText(_translate("MainWindow", "Classic"))
        self.pso_canonica_radiobutton.setText(_translate("MainWindow", "Canonica"))
        self.pso_cost.setTitle(_translate("MainWindow", "Type of Cost"))
        self.pso_mse_radiobutton.setText(_translate("MainWindow", "MSE"))
        self.pso_ae_radiobutton.setText(_translate("MainWindow", "AE"))
        self.pso_inertial.setTitle(_translate("MainWindow", "Type of Inertial"))
        self.constant_radiobutton.setText(_translate("MainWindow", "Constant"))
        self.linear_fall_radiobutton.setText(_translate("MainWindow", "Linear Fall"))
        self.linear_rise_radiobutton.setText(_translate("MainWindow", "Linear Rise"))
        self.w_label.setText(_translate("MainWindow", "W:"))
        self.w_field.setText(_translate("MainWindow", "0.8"))
        self.pso_constants.setTitle(_translate("MainWindow", "Type of Constants"))
        self.normal_radiobutton.setText(_translate("MainWindow", "Normal"))
        self.c1_label.setText(_translate("MainWindow", "C1:"))
        self.c2_label.setText(_translate("MainWindow", "C2:"))
        self.c1_field.setText(_translate("MainWindow", "2"))
        self.c2_field.setText(_translate("MainWindow", "2"))
        self.dynamic_mutation_radiobutton.setText(_translate("MainWindow", "Dynamic"))
        self.label_lag_pso_0.setText(_translate("MainWindow", "Lag 0"))
        self.start_pso_0.setText(_translate("MainWindow", "Start"))
        self.stop_pso_0.setText(_translate("MainWindow", "Stop"))
        self.label_pso_0.setText(_translate("MainWindow", "available"))
        self.label_lag_pso_1.setText(_translate("MainWindow", "Lag 1"))
        self.start_pso_1.setText(_translate("MainWindow", "Start"))
        self.stop_pso_1.setText(_translate("MainWindow", "Stop"))
        self.label_pso_1.setText(_translate("MainWindow", "available"))
        self.label_lag_pso_2.setText(_translate("MainWindow", "Lag 2"))
        self.start_pso_2.setText(_translate("MainWindow", "Start"))
        self.stop_pso_2.setText(_translate("MainWindow", "Stop"))
        self.label_pso_2.setText(_translate("MainWindow", "available"))
        self.label_lag_pso_3.setText(_translate("MainWindow", "Lag 3"))
        self.start_pso_3.setText(_translate("MainWindow", "Start"))
        self.stop_pso_3.setText(_translate("MainWindow", "Stop"))
        self.label_pso_3.setText(_translate("MainWindow", "available"))
        self.label_lag_pso_4.setText(_translate("MainWindow", "Lag 4"))
        self.start_pso_4.setText(_translate("MainWindow", "Start"))
        self.stop_pso_4.setText(_translate("MainWindow", "Stop"))
        self.label_pso_4.setText(_translate("MainWindow", "available"))
        self.label_lag_pso_5.setText(_translate("MainWindow", "Lag 5"))
        self.start_pso_5.setText(_translate("MainWindow", "Start"))
        self.stop_pso_5.setText(_translate("MainWindow", "Stop"))
        self.label_pso_5.setText(_translate("MainWindow", "available"))
        self.label_lag_pso_6.setText(_translate("MainWindow", "Lag 6"))
        self.start_pso_6.setText(_translate("MainWindow", "Start"))
        self.stop_pso_6.setText(_translate("MainWindow", "Stop"))
        self.label_pso_6.setText(_translate("MainWindow", "available"))
        self.label_lag_pso_7.setText(_translate("MainWindow", "Lag 7"))
        self.start_pso_7.setText(_translate("MainWindow", "Start"))
        self.stop_pso_7.setText(_translate("MainWindow", "Stop"))
        self.label_pso_7.setText(_translate("MainWindow", "available"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pso_tab), _translate("MainWindow", "PSO"))
        self.process_open_button.setText(_translate("MainWindow", "Open"))
        self.graph_groupbox.setTitle(_translate("MainWindow", "Graph "))
        self.database_radiobutton.setText(_translate("MainWindow", "Database"))
        self.rxp_test_radiobutton.setText(_translate("MainWindow", "Real X Prediction (Test)"))
        self.rxp_training_radiobutton.setText(_translate("MainWindow", "Real X Prediction (Training)"))
        self.gb_fitness_radiobutton.setText(_translate("MainWindow", "Global Best Fitness Evolution"))
        self.gb_cost_radiobutton.setText(_translate("MainWindow", "Global Best Cost Evolution"))
        self.boxplot_fitness_radiobutton.setText(_translate("MainWindow", "Boxplot Fitness"))
        self.boxplot_cost_radiobutton.setText(_translate("MainWindow", "Boxplot Cost"))
        self.plot_graph_button.setText(_translate("MainWindow", "Plot Graph"))
        self.tableresults_groupbox.setTitle(_translate("MainWindow", "Table Results"))
        self.lag2_label.setText(_translate("MainWindow", "available"))
        self.copy_lag1_pushbutton.setText(_translate("MainWindow", "Copy Lag 1"))
        self.lag1_label.setText(_translate("MainWindow", "available"))
        self.copy_lag7_pushbutton.setText(_translate("MainWindow", "Copy Lag 7"))
        self.lag0_label.setText(_translate("MainWindow", "available"))
        self.lag4_label.setText(_translate("MainWindow", "available"))
        self.copy_lag0_pushbutton.setText(_translate("MainWindow", "Copy Lag 0"))
        self.lag6_label.setText(_translate("MainWindow", "available"))
        self.copy_lag5_pushbutton.setText(_translate("MainWindow", "Copy Lag 5"))
        self.copy_lag2_pushbutton.setText(_translate("MainWindow", "Copy Lag 2"))
        self.copy_lag6_pushbutton.setText(_translate("MainWindow", "Copy Lag 6"))
        self.copy_lag3_pushbutton.setText(_translate("MainWindow", "Copy Lag 3"))
        self.copy_lag4_pushbutton.setText(_translate("MainWindow", "Copy Lag 4"))
        self.lag3_label.setText(_translate("MainWindow", "available"))
        self.lag5_label.setText(_translate("MainWindow", "available"))
        self.lag7_label.setText(_translate("MainWindow", "available"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results_tab), _translate("MainWindow", "Results"))

