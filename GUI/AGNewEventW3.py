# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AGNewEventW3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(513, 711)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.dateLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.horizontalLayout_12.addWidget(self.dateLabel)
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.dateEdit.setFont(font)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 8, 8), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_12.addWidget(self.dateEdit)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.horizontalLayout_13.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.allDayEventRadioButton = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.allDayEventRadioButton.setFont(font)
        self.allDayEventRadioButton.setObjectName("allDayEventRadioButton")
        self.horizontalLayout_11.addWidget(self.allDayEventRadioButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.setDurationEventRadioButton = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.setDurationEventRadioButton.setFont(font)
        self.setDurationEventRadioButton.setObjectName("setDurationEventRadioButton")
        self.horizontalLayout_11.addWidget(self.setDurationEventRadioButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.horizontalLayout_11.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.fromLabel = QtWidgets.QLabel(Form)
        self.fromLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.fromLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fromLabel.setFont(font)
        self.fromLabel.setObjectName("fromLabel")
        self.horizontalLayout_9.addWidget(self.fromLabel)
        self.timeFromEdit = QtWidgets.QTimeEdit(Form)
        self.timeFromEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.timeFromEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timeFromEdit.setFont(font)
        self.timeFromEdit.setObjectName("timeFromEdit")
        self.horizontalLayout_9.addWidget(self.timeFromEdit)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.toLabel = QtWidgets.QLabel(Form)
        self.toLabel.setMinimumSize(QtCore.QSize(40, 0))
        self.toLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toLabel.setFont(font)
        self.toLabel.setObjectName("toLabel")
        self.horizontalLayout_7.addWidget(self.toLabel)
        self.timeToEdit = QtWidgets.QTimeEdit(Form)
        self.timeToEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.timeToEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timeToEdit.setFont(font)
        self.timeToEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(1, 0, 0)))
        self.timeToEdit.setObjectName("timeToEdit")
        self.horizontalLayout_7.addWidget(self.timeToEdit)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.horizontalLayout_8.setStretch(2, 1)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        spacerItem12 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.eventTypeLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.eventTypeLabel.setFont(font)
        self.eventTypeLabel.setObjectName("eventTypeLabel")
        self.horizontalLayout_6.addWidget(self.eventTypeLabel)
        self.eventTypeComboBox = QtWidgets.QComboBox(Form)
        self.eventTypeComboBox.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eventTypeComboBox.setFont(font)
        self.eventTypeComboBox.setCurrentText("")
        self.eventTypeComboBox.setObjectName("eventTypeComboBox")
        self.horizontalLayout_6.addWidget(self.eventTypeComboBox)
        self.addEventTypeButton = QtWidgets.QPushButton(Form)
        self.addEventTypeButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setKerning(True)
        self.addEventTypeButton.setFont(font)
        self.addEventTypeButton.setStyleSheet("background-color: rgb(128, 200, 255);")
        self.addEventTypeButton.setObjectName("addEventTypeButton")
        self.horizontalLayout_6.addWidget(self.addEventTypeButton)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.titleLabel = QtWidgets.QLabel(Form)
        self.titleLabel.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout_5.addWidget(self.titleLabel)
        self.eventTitlePlainTextEdit = QtWidgets.QPlainTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventTitlePlainTextEdit.sizePolicy().hasHeightForWidth())
        self.eventTitlePlainTextEdit.setSizePolicy(sizePolicy)
        self.eventTitlePlainTextEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.eventTitlePlainTextEdit.setMaximumSize(QtCore.QSize(340, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eventTitlePlainTextEdit.setFont(font)
        self.eventTitlePlainTextEdit.setObjectName("eventTitlePlainTextEdit")
        self.horizontalLayout_5.addWidget(self.eventTitlePlainTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem14)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.descriptionLabel = QtWidgets.QLabel(Form)
        self.descriptionLabel.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.horizontalLayout_4.addWidget(self.descriptionLabel)
        self.eventDescriptionPlaneTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.eventDescriptionPlaneTextEdit.setMaximumSize(QtCore.QSize(340, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eventDescriptionPlaneTextEdit.setFont(font)
        self.eventDescriptionPlaneTextEdit.setObjectName("eventDescriptionPlaneTextEdit")
        self.horizontalLayout_4.addWidget(self.eventDescriptionPlaneTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem15 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem15)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.localizationLabel = QtWidgets.QLabel(Form)
        self.localizationLabel.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.localizationLabel.setFont(font)
        self.localizationLabel.setObjectName("localizationLabel")
        self.horizontalLayout_3.addWidget(self.localizationLabel)
        self.eventLocalizationPlainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.eventLocalizationPlainTextEdit.setMaximumSize(QtCore.QSize(340, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eventLocalizationPlainTextEdit.setFont(font)
        self.eventLocalizationPlainTextEdit.setObjectName("eventLocalizationPlainTextEdit")
        self.horizontalLayout_3.addWidget(self.eventLocalizationPlainTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem16 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem16)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem17)
        self.remindLabel = QtWidgets.QLabel(Form)
        self.remindLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remindLabel.setFont(font)
        self.remindLabel.setObjectName("remindLabel")
        self.horizontalLayout_2.addWidget(self.remindLabel)
        self.remindBeforeComboBox = QtWidgets.QComboBox(Form)
        self.remindBeforeComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remindBeforeComboBox.setFont(font)
        self.remindBeforeComboBox.setObjectName("remindBeforeComboBox")
        self.horizontalLayout_2.addWidget(self.remindBeforeComboBox)
        spacerItem18 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem18)
        self.beforeEventLabel = QtWidgets.QLabel(Form)
        self.beforeEventLabel.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.beforeEventLabel.setFont(font)
        self.beforeEventLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.beforeEventLabel.setObjectName("beforeEventLabel")
        self.horizontalLayout_2.addWidget(self.beforeEventLabel)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem19)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem20 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem20)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem21)
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("background-color: rgb(213, 0, 0);")
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem22)
        self.addEventButton = QtWidgets.QPushButton(Form)
        self.addEventButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.addEventButton.setFont(font)
        self.addEventButton.setStyleSheet("background-color: rgb(0, 181, 0);")
        self.addEventButton.setObjectName("addEventButton")
        self.horizontalLayout.addWidget(self.addEventButton)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem23)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(9, 1)
        self.verticalLayout.setStretch(11, 1)
        self.verticalLayout.setStretch(13, 1)
        self.verticalLayout.setStretch(15, 1)
        self.verticalLayout.setStretch(16, 1)
        self.verticalLayout.setStretch(17, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dateLabel.setText(_translate("Form", "Date"))
        self.allDayEventRadioButton.setText(_translate("Form", "All day event"))
        self.setDurationEventRadioButton.setText(_translate("Form", "Set duration"))
        self.fromLabel.setText(_translate("Form", "From: "))
        self.toLabel.setText(_translate("Form", "To: "))
        self.eventTypeLabel.setText(_translate("Form", "Event type"))
        self.addEventTypeButton.setText(_translate("Form", "Add new type"))
        self.titleLabel.setText(_translate("Form", "Title"))
        self.descriptionLabel.setText(_translate("Form", "Description"))
        self.localizationLabel.setText(_translate("Form", "Localization"))
        self.remindLabel.setText(_translate("Form", "Remind "))
        self.beforeEventLabel.setText(_translate("Form", "before event"))
        self.cancelButton.setText(_translate("Form", "Cancel"))
        self.addEventButton.setText(_translate("Form", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
