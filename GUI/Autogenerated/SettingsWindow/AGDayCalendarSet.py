# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AGDayCalendarSet.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(594, 592)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 594, 475))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sectionTitleLabel_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sectionTitleLabel_1.setFont(font)
        self.sectionTitleLabel_1.setObjectName("sectionTitleLabel_1")
        self.gridLayout_2.addWidget(self.sectionTitleLabel_1, 0, 0, 1, 1)
        self.calendarBackColourBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.calendarBackColourBtn.setMinimumSize(QtCore.QSize(50, 30))
        self.calendarBackColourBtn.setMaximumSize(QtCore.QSize(50, 30))
        self.calendarBackColourBtn.setText("")
        self.calendarBackColourBtn.setObjectName("calendarBackColourBtn")
        self.gridLayout_2.addWidget(self.calendarBackColourBtn, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.linesColourBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.linesColourBtn.setMinimumSize(QtCore.QSize(50, 30))
        self.linesColourBtn.setMaximumSize(QtCore.QSize(50, 30))
        self.linesColourBtn.setText("")
        self.linesColourBtn.setObjectName("linesColourBtn")
        self.gridLayout_3.addWidget(self.linesColourBtn, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 3, 1, 1)
        self.lineColourLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lineColourLabel.setMinimumSize(QtCore.QSize(120, 0))
        self.lineColourLabel.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineColourLabel.setFont(font)
        self.lineColourLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineColourLabel.setObjectName("lineColourLabel")
        self.gridLayout_3.addWidget(self.lineColourLabel, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 0, 1, 1)
        self.lineThicknessLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lineThicknessLabel.setMinimumSize(QtCore.QSize(120, 0))
        self.lineThicknessLabel.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineThicknessLabel.setFont(font)
        self.lineThicknessLabel.setObjectName("lineThicknessLabel")
        self.gridLayout_4.addWidget(self.lineThicknessLabel, 0, 1, 1, 1)
        self.hourLinesRatioSpinBox = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.hourLinesRatioSpinBox.setMinimumSize(QtCore.QSize(50, 30))
        self.hourLinesRatioSpinBox.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.hourLinesRatioSpinBox.setFont(font)
        self.hourLinesRatioSpinBox.setStyleSheet("background-color: rgb(255,255,255);")
        self.hourLinesRatioSpinBox.setDecimals(1)
        self.hourLinesRatioSpinBox.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.hourLinesRatioSpinBox.setObjectName("hourLinesRatioSpinBox")
        self.gridLayout_4.addWidget(self.hourLinesRatioSpinBox, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.sectionTitleLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sectionTitleLabel_2.setFont(font)
        self.sectionTitleLabel_2.setObjectName("sectionTitleLabel_2")
        self.gridLayout_5.addWidget(self.sectionTitleLabel_2, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.sectionTitleLabel_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sectionTitleLabel_3.setFont(font)
        self.sectionTitleLabel_3.setObjectName("sectionTitleLabel_3")
        self.gridLayout_7.addWidget(self.sectionTitleLabel_3, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 0, 0, 1, 1)
        self.eventSpaceRatioLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eventSpaceRatioLabel.setFont(font)
        self.eventSpaceRatioLabel.setObjectName("eventSpaceRatioLabel")
        self.gridLayout_6.addWidget(self.eventSpaceRatioLabel, 0, 1, 1, 1)
        self.eventSpaceRatioSpinBox = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.eventSpaceRatioSpinBox.setMinimumSize(QtCore.QSize(50, 30))
        self.eventSpaceRatioSpinBox.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.eventSpaceRatioSpinBox.setFont(font)
        self.eventSpaceRatioSpinBox.setStyleSheet("background-color: rgb(255,255,255);")
        self.eventSpaceRatioSpinBox.setDecimals(1)
        self.eventSpaceRatioSpinBox.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.eventSpaceRatioSpinBox.setObjectName("eventSpaceRatioSpinBox")
        self.gridLayout_6.addWidget(self.eventSpaceRatioSpinBox, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 0, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem7, 1, 0, 1, 1)
        self.titleLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.titleLabel_2.setFont(font)
        self.titleLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleLabel_2.setObjectName("titleLabel_2")
        self.gridLayout_6.addWidget(self.titleLabel_2, 1, 1, 1, 1)
        self.titleCheckBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.titleCheckBox.setText("")
        self.titleCheckBox.setObjectName("titleCheckBox")
        self.gridLayout_6.addWidget(self.titleCheckBox, 1, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem8, 1, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 2, 0, 1, 1)
        self.descriptionLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.descriptionLabel_2.setFont(font)
        self.descriptionLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.descriptionLabel_2.setObjectName("descriptionLabel_2")
        self.gridLayout_6.addWidget(self.descriptionLabel_2, 2, 1, 1, 1)
        self.descriptionCheckBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.descriptionCheckBox.setText("")
        self.descriptionCheckBox.setObjectName("descriptionCheckBox")
        self.gridLayout_6.addWidget(self.descriptionCheckBox, 2, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem10, 2, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem11, 3, 0, 1, 1)
        self.localizationLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.localizationLabel.setFont(font)
        self.localizationLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.localizationLabel.setObjectName("localizationLabel")
        self.gridLayout_6.addWidget(self.localizationLabel, 3, 1, 1, 1)
        self.localizationCheckBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.localizationCheckBox.setText("")
        self.localizationCheckBox.setObjectName("localizationCheckBox")
        self.gridLayout_6.addWidget(self.localizationCheckBox, 3, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem12, 3, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem13, 4, 0, 1, 1)
        self.reminderLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reminderLabel.setFont(font)
        self.reminderLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.reminderLabel.setObjectName("reminderLabel")
        self.gridLayout_6.addWidget(self.reminderLabel, 4, 1, 1, 1)
        self.reminderCheckBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.reminderCheckBox.setText("")
        self.reminderCheckBox.setObjectName("reminderCheckBox")
        self.gridLayout_6.addWidget(self.reminderCheckBox, 4, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem14, 4, 3, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 2)
        self.settingsTitleLabel = QtWidgets.QLabel(Form)
        self.settingsTitleLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.settingsTitleLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.settingsTitleLabel.setFont(font)
        self.settingsTitleLabel.setObjectName("settingsTitleLabel")
        self.gridLayout.addWidget(self.settingsTitleLabel, 0, 0, 1, 2)
        self.settingsDescriptionLabel = QtWidgets.QLabel(Form)
        self.settingsDescriptionLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.settingsDescriptionLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.settingsDescriptionLabel.setFont(font)
        self.settingsDescriptionLabel.setObjectName("settingsDescriptionLabel")
        self.gridLayout.addWidget(self.settingsDescriptionLabel, 1, 0, 1, 2)
        self.applyButton = QtWidgets.QPushButton(Form)
        self.applyButton.setMinimumSize(QtCore.QSize(120, 40))
        self.applyButton.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.applyButton.setFont(font)
        self.applyButton.setStyleSheet("background-color: rgb(135, 189, 216);")
        self.applyButton.setObjectName("applyButton")
        self.gridLayout.addWidget(self.applyButton, 4, 1, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sectionTitleLabel_1.setText(_translate("Form", "Calendar\'s background colour"))
        self.lineColourLabel.setText(_translate("Form", "Colour"))
        self.lineThicknessLabel.setText(_translate("Form", "Line\'s thickness "))
        self.sectionTitleLabel_2.setText(_translate("Form", "Hour lines\' style"))
        self.sectionTitleLabel_3.setText(_translate("Form", "Events\' presentation style"))
        self.eventSpaceRatioLabel.setText(_translate("Form", "Space ratio between events"))
        self.titleLabel_2.setText(_translate("Form", "Title"))
        self.descriptionLabel_2.setText(_translate("Form", "Decription"))
        self.localizationLabel.setText(_translate("Form", "Localization"))
        self.reminderLabel.setText(_translate("Form", "Reminder"))
        self.settingsTitleLabel.setText(_translate("Form", "Day view"))
        self.settingsDescriptionLabel.setText(_translate("Form", "Customize appearance of the day calendar by setting colours etc."))
        self.applyButton.setText(_translate("Form", "APPLY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())