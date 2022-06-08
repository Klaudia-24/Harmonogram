# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AGMainW_v3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1219, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.calendarGridLayout = QtWidgets.QGridLayout()
        self.calendarGridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.calendarGridLayout.setObjectName("calendarGridLayout")
        self.gridLayout.addLayout(self.calendarGridLayout, 1, 3, 1, 1)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setMinimumSize(QtCore.QSize(0, 50))
        self.nextButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 1, 4, 1, 1)
        self.sideBarVerticalLayout = QtWidgets.QVBoxLayout()
        self.sideBarVerticalLayout.setObjectName("sideBarVerticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sideBarVerticalLayout.addItem(spacerItem)
        self.newEventButton = QtWidgets.QPushButton(self.centralwidget)
        self.newEventButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newEventButton.setFont(font)
        self.newEventButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.newEventButton.setObjectName("newEventButton")
        self.sideBarVerticalLayout.addWidget(self.newEventButton)
        self.gridLayout.addLayout(self.sideBarVerticalLayout, 1, 0, 1, 1)
        self.dateBarLayout = QtWidgets.QHBoxLayout()
        self.dateBarLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.dateBarLayout.setObjectName("dateBarLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.dateBarLayout.addItem(spacerItem1)
        self.dayFromDate = QtWidgets.QLabel(self.centralwidget)
        self.dayFromDate.setMaximumSize(QtCore.QSize(16777215, 100))
        self.dayFromDate.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.dayFromDate.setObjectName("dayFromDate")
        self.dateBarLayout.addWidget(self.dayFromDate)
        self.monthFromDate = QtWidgets.QLabel(self.centralwidget)
        self.monthFromDate.setMaximumSize(QtCore.QSize(16777215, 100))
        self.monthFromDate.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.monthFromDate.setObjectName("monthFromDate")
        self.dateBarLayout.addWidget(self.monthFromDate)
        self.yearFromDate = QtWidgets.QLabel(self.centralwidget)
        self.yearFromDate.setMaximumSize(QtCore.QSize(16777215, 100))
        self.yearFromDate.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.yearFromDate.setObjectName("yearFromDate")
        self.dateBarLayout.addWidget(self.yearFromDate)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.dateBarLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.dateBarLayout, 0, 0, 1, 5)
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setMinimumSize(QtCore.QSize(0, 50))
        self.prevButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.prevButton.setObjectName("prevButton")
        self.gridLayout.addWidget(self.prevButton, 1, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(3, 4)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shedule"))
        self.nextButton.setText(_translate("MainWindow", "NEXT"))
        self.newEventButton.setText(_translate("MainWindow", "New event"))
        self.dayFromDate.setText(_translate("MainWindow", "16"))
        self.monthFromDate.setText(_translate("MainWindow", "July"))
        self.yearFromDate.setText(_translate("MainWindow", "2021"))
        self.prevButton.setText(_translate("MainWindow", "PREV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
