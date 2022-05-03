# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AGNewEventTypeW.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewEventTypeWindow(object):
    def setupUi(self, NewEventTypeWindow):
        NewEventTypeWindow.setObjectName("NewEventTypeWindow")
        NewEventTypeWindow.setEnabled(True)
        NewEventTypeWindow.resize(569, 269)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewEventTypeWindow.sizePolicy().hasHeightForWidth())
        NewEventTypeWindow.setSizePolicy(sizePolicy)
        NewEventTypeWindow.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.centralwidget = QtWidgets.QWidget(NewEventTypeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancelPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelPushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.cancelPushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cancelPushButton.setFont(font)
        self.cancelPushButton.setStyleSheet("background-color: rgb(255, 51, 51);")
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.savePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.savePushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.savePushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.savePushButton.setFont(font)
        self.savePushButton.setStyleSheet("background-color: rgb(0, 179, 0);")
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout_3.addWidget(self.savePushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.colorsPaletteButton = QtWidgets.QPushButton(self.centralwidget)
        self.colorsPaletteButton.setMinimumSize(QtCore.QSize(90, 70))
        self.colorsPaletteButton.setMaximumSize(QtCore.QSize(90, 70))
        self.colorsPaletteButton.setText("")
        self.colorsPaletteButton.setObjectName("colorsPaletteButton")
        self.horizontalLayout.addWidget(self.colorsPaletteButton)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 1, 0, 1, 1)
        # NewEventTypeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewEventTypeWindow)
        QtCore.QMetaObject.connectSlotsByName(NewEventTypeWindow)

    def retranslateUi(self, NewEventTypeWindow):
        _translate = QtCore.QCoreApplication.translate
        NewEventTypeWindow.setWindowTitle(_translate("NewEventTypeWindow", "New Event Type"))
        self.cancelPushButton.setText(_translate("NewEventTypeWindow", "Cancel"))
        self.savePushButton.setText(_translate("NewEventTypeWindow", "Save"))
        self.label.setText(_translate("NewEventTypeWindow", "Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewEventTypeWindow = QtWidgets.QMainWindow()
    ui = Ui_NewEventTypeWindow()
    ui.setupUi(NewEventTypeWindow)
    NewEventTypeWindow.show()
    sys.exit(app.exec_())
