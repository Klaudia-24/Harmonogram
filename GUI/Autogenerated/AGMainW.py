# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_main_window2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from WindowObjects.QLabelClickable import QLabelClickable

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1219, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mainHorizontalLayout = QtWidgets.QHBoxLayout()
        self.mainHorizontalLayout.setObjectName("mainHorizontalLayout")
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
        self.mainHorizontalLayout.addLayout(self.sideBarVerticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.mainHorizontalLayout.addWidget(self.line)
        self.dateCalendarVerticalLayout = QtWidgets.QVBoxLayout()
        self.dateCalendarVerticalLayout.setObjectName("dateCalendarVerticalLayout")
        self.dateBarLayout = QtWidgets.QHBoxLayout()
        self.dateBarLayout.setObjectName("dateBarLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.dateBarLayout.addItem(spacerItem1)
        self.dayFromDate = QtWidgets.QLabel(self.centralwidget)
        self.dayFromDate.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.dayFromDate.setObjectName("dayFromDate")
        self.dateBarLayout.addWidget(self.dayFromDate)
        self.monthFromDate = QtWidgets.QLabel(self.centralwidget)
        self.monthFromDate.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.monthFromDate.setObjectName("monthFromDate")
        self.dateBarLayout.addWidget(self.monthFromDate)
        self.yearFromDate = QtWidgets.QLabel(self.centralwidget)
        self.yearFromDate.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.yearFromDate.setObjectName("yearFromDate")
        self.dateBarLayout.addWidget(self.yearFromDate)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.dateBarLayout.addItem(spacerItem2)
        self.dateCalendarVerticalLayout.addLayout(self.dateBarLayout)
        self.navCalendarHorizontalLayout = QtWidgets.QHBoxLayout()
        self.navCalendarHorizontalLayout.setObjectName("navCalendarHorizontalLayout")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setMinimumSize(QtCore.QSize(0, 50))
        self.prevButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.prevButton.setObjectName("prevButton")
        self.navCalendarHorizontalLayout.addWidget(self.prevButton)
        self.calendarGridLayout = QtWidgets.QGridLayout()
        self.calendarGridLayout.setObjectName("calendarGridLayout")
        self.weekDay3 = QtWidgets.QLabel(self.centralwidget)
        self.weekDay3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay3.setObjectName("weekDay3")
        self.calendarGridLayout.addWidget(self.weekDay3, 0, 3, 1, 1)
        self.weekNumber4 = QtWidgets.QLabel(self.centralwidget)
        self.weekNumber4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber4.setObjectName("weekNumber4")
        self.calendarGridLayout.addWidget(self.weekNumber4, 4, 0, 1, 1)
        self.weekLabel = QtWidgets.QLabel(self.centralwidget)
        self.weekLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekLabel.setObjectName("weekLabel")
        self.calendarGridLayout.addWidget(self.weekLabel, 0, 0, 1, 1)
        self.weekDay2 = QtWidgets.QLabel(self.centralwidget)
        self.weekDay2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay2.setObjectName("weekDay2")
        self.calendarGridLayout.addWidget(self.weekDay2, 0, 2, 1, 1)
        self.weekDay6 = QtWidgets.QLabel(self.centralwidget)
        self.weekDay6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay6.setObjectName("weekDay6")
        self.calendarGridLayout.addWidget(self.weekDay6, 0, 6, 1, 1)
        self.weekNumber2 = QtWidgets.QLabel(self.centralwidget)
        self.weekNumber2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber2.setObjectName("weekNumber2")
        self.calendarGridLayout.addWidget(self.weekNumber2, 2, 0, 1, 1)
        self.weekNumber1 = QtWidgets.QLabel(self.centralwidget)
        self.weekNumber1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber1.setObjectName("weekNumber1")
        self.calendarGridLayout.addWidget(self.weekNumber1, 1, 0, 1, 1)
        self.weekDay4 = QtWidgets.QLabel(self.centralwidget)
        self.weekDay4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay4.setObjectName("weekDay4")
        self.calendarGridLayout.addWidget(self.weekDay4, 0, 4, 1, 1)
        self.weekDay5 = QtWidgets.QLabel(self.centralwidget)
        self.weekDay5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay5.setObjectName("weekDay5")
        self.calendarGridLayout.addWidget(self.weekDay5, 0, 5, 1, 1)
        self.weekNumber3 = QtWidgets.QLabel(self.centralwidget)
        self.weekNumber3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber3.setObjectName("weekNumber3")
        self.calendarGridLayout.addWidget(self.weekNumber3, 3, 0, 1, 1)
        self.weekNumber5 = QtWidgets.QLabel(self.centralwidget)
        self.weekNumber5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber5.setObjectName("weekNumber5")
        self.calendarGridLayout.addWidget(self.weekNumber5, 5, 0, 1, 1)
        self.weekDay7 = QtWidgets.QLabel(self.centralwidget)
        self.weekDay7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay7.setObjectName("weekDay7")
        self.calendarGridLayout.addWidget(self.weekDay7, 0, 7, 1, 1)
        self.weekDay1 = QtWidgets.QLabel(self.centralwidget)
        self.weekDay1.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.weekDay1.setObjectName("weekDay1")
        self.calendarGridLayout.addWidget(self.weekDay1, 0, 1, 1, 1)
        self.weekNumber6 = QtWidgets.QLabel(self.centralwidget)
        self.weekNumber6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber6.setObjectName("weekNumber6")
        self.calendarGridLayout.addWidget(self.weekNumber6, 6, 0, 1, 1)
        self.day_1 = QLabelClickable(self.centralwidget)
        self.day_1.setMinimumSize(QtCore.QSize(0, 0))
        self.day_1.setObjectName("day_1")
        self.calendarGridLayout.addWidget(self.day_1, 1, 1, 1, 1)
        self.day_2 = QLabelClickable(self.centralwidget)
        self.day_2.setObjectName("day_2")
        self.calendarGridLayout.addWidget(self.day_2, 1, 2, 1, 1)
        self.day_3 = QLabelClickable(self.centralwidget)
        self.day_3.setObjectName("day_3")
        self.calendarGridLayout.addWidget(self.day_3, 1, 3, 1, 1)
        self.day_4 = QLabelClickable(self.centralwidget)
        self.day_4.setObjectName("day_4")
        self.calendarGridLayout.addWidget(self.day_4, 1, 4, 1, 1)
        self.day_5 = QLabelClickable(self.centralwidget)
        self.day_5.setObjectName("day_5")
        self.calendarGridLayout.addWidget(self.day_5, 1, 5, 1, 1)
        self.day_6 = QLabelClickable(self.centralwidget)
        self.day_6.setObjectName("day_6")
        self.calendarGridLayout.addWidget(self.day_6, 1, 6, 1, 1)
        self.day_7 = QLabelClickable(self.centralwidget)
        self.day_7.setObjectName("day_7")
        self.calendarGridLayout.addWidget(self.day_7, 1, 7, 1, 1)
        self.day_8 = QLabelClickable(self.centralwidget)
        self.day_8.setMinimumSize(QtCore.QSize(0, 0))
        self.day_8.setObjectName("day_8")
        self.calendarGridLayout.addWidget(self.day_8, 2, 1, 1, 1)
        self.day_9 = QLabelClickable(self.centralwidget)
        self.day_9.setObjectName("day_9")
        self.calendarGridLayout.addWidget(self.day_9, 2, 2, 1, 1)
        self.day_10 = QLabelClickable(self.centralwidget)
        self.day_10.setObjectName("day_10")
        self.calendarGridLayout.addWidget(self.day_10, 2, 3, 1, 1)
        self.day_11 = QLabelClickable(self.centralwidget)
        self.day_11.setObjectName("day_11")
        self.calendarGridLayout.addWidget(self.day_11, 2, 4, 1, 1)
        self.day_12 = QLabelClickable(self.centralwidget)
        self.day_12.setObjectName("day_12")
        self.calendarGridLayout.addWidget(self.day_12, 2, 5, 1, 1)
        self.day_13 = QLabelClickable(self.centralwidget)
        self.day_13.setObjectName("day_13")
        self.calendarGridLayout.addWidget(self.day_13, 2, 6, 1, 1)
        self.day_14 = QLabelClickable(self.centralwidget)
        self.day_14.setObjectName("day_14")
        self.calendarGridLayout.addWidget(self.day_14, 2, 7, 1, 1)
        self.day_15 = QLabelClickable(self.centralwidget)
        self.day_15.setMinimumSize(QtCore.QSize(0, 0))
        self.day_15.setObjectName("day_15")
        self.calendarGridLayout.addWidget(self.day_15, 3, 1, 1, 1)
        self.day_16 = QLabelClickable(self.centralwidget)
        self.day_16.setObjectName("day_16")
        self.calendarGridLayout.addWidget(self.day_16, 3, 2, 1, 1)
        self.day_17 = QLabelClickable(self.centralwidget)
        self.day_17.setObjectName("day_17")
        self.calendarGridLayout.addWidget(self.day_17, 3, 3, 1, 1)
        self.day_18 = QLabelClickable(self.centralwidget)
        self.day_18.setObjectName("day_18")
        self.calendarGridLayout.addWidget(self.day_18, 3, 4, 1, 1)
        self.day_19 = QLabelClickable(self.centralwidget)
        self.day_19.setObjectName("day_19")
        self.calendarGridLayout.addWidget(self.day_19, 3, 5, 1, 1)
        self.day_20 = QLabelClickable(self.centralwidget)
        self.day_20.setObjectName("day_20")
        self.calendarGridLayout.addWidget(self.day_20, 3, 6, 1, 1)
        self.day_21 = QLabelClickable(self.centralwidget)
        self.day_21.setObjectName("day_21")
        self.calendarGridLayout.addWidget(self.day_21, 3, 7, 1, 1)
        self.day_22 = QLabelClickable(self.centralwidget)
        self.day_22.setMinimumSize(QtCore.QSize(0, 0))
        self.day_22.setObjectName("day_22")
        self.calendarGridLayout.addWidget(self.day_22, 4, 1, 1, 1)
        self.day_23 = QLabelClickable(self.centralwidget)
        self.day_23.setObjectName("day_23")
        self.calendarGridLayout.addWidget(self.day_23, 4, 2, 1, 1)
        self.day_24 = QLabelClickable(self.centralwidget)
        self.day_24.setObjectName("day_24")
        self.calendarGridLayout.addWidget(self.day_24, 4, 3, 1, 1)
        self.day_25 = QLabelClickable(self.centralwidget)
        self.day_25.setObjectName("day_25")
        self.calendarGridLayout.addWidget(self.day_25, 4, 4, 1, 1)
        self.day_26 = QLabelClickable(self.centralwidget)
        self.day_26.setObjectName("day_26")
        self.calendarGridLayout.addWidget(self.day_26, 4, 5, 1, 1)
        self.day_27 = QLabelClickable(self.centralwidget)
        self.day_27.setObjectName("day_27")
        self.calendarGridLayout.addWidget(self.day_27, 4, 6, 1, 1)
        self.day_28 = QLabelClickable(self.centralwidget)
        self.day_28.setObjectName("day_28")
        self.calendarGridLayout.addWidget(self.day_28, 4, 7, 1, 1)
        self.day_29 = QLabelClickable(self.centralwidget)
        self.day_29.setMinimumSize(QtCore.QSize(0, 0))
        self.day_29.setObjectName("day_29")
        self.calendarGridLayout.addWidget(self.day_29, 5, 1, 1, 1)
        self.day_30 = QLabelClickable(self.centralwidget)
        self.day_30.setObjectName("day_30")
        self.calendarGridLayout.addWidget(self.day_30, 5, 2, 1, 1)
        self.day_31 = QLabelClickable(self.centralwidget)
        self.day_31.setObjectName("day_31")
        self.calendarGridLayout.addWidget(self.day_31, 5, 3, 1, 1)
        self.day_32 = QLabelClickable(self.centralwidget)
        self.day_32.setObjectName("day_32")
        self.calendarGridLayout.addWidget(self.day_32, 5, 4, 1, 1)
        self.day_33 = QLabelClickable(self.centralwidget)
        self.day_33.setObjectName("day_33")
        self.calendarGridLayout.addWidget(self.day_33, 5, 5, 1, 1)
        self.day_34 = QLabelClickable(self.centralwidget)
        self.day_34.setObjectName("day_34")
        self.calendarGridLayout.addWidget(self.day_34, 5, 6, 1, 1)
        self.day_35 = QLabelClickable(self.centralwidget)
        self.day_35.setObjectName("day_35")
        self.calendarGridLayout.addWidget(self.day_35, 5, 7, 1, 1)
        self.day_36 = QLabelClickable(self.centralwidget)
        self.day_36.setMinimumSize(QtCore.QSize(0, 0))
        self.day_36.setObjectName("day_36")
        self.calendarGridLayout.addWidget(self.day_36, 6, 1, 1, 1)
        self.day_37 = QLabelClickable(self.centralwidget)
        self.day_37.setObjectName("day_37")
        self.calendarGridLayout.addWidget(self.day_37, 6, 2, 1, 1)
        self.day_38 = QLabelClickable(self.centralwidget)
        self.day_38.setObjectName("day_38")
        self.calendarGridLayout.addWidget(self.day_38, 6, 3, 1, 1)
        self.day_39 = QLabelClickable(self.centralwidget)
        self.day_39.setObjectName("day_39")
        self.calendarGridLayout.addWidget(self.day_39, 6, 4, 1, 1)
        self.day_40 = QLabelClickable(self.centralwidget)
        self.day_40.setObjectName("day_40")
        self.calendarGridLayout.addWidget(self.day_40, 6, 5, 1, 1)
        self.day_41 = QLabelClickable(self.centralwidget)
        self.day_41.setObjectName("day_41")
        self.calendarGridLayout.addWidget(self.day_41, 6, 6, 1, 1)
        self.day_42 = QLabelClickable(self.centralwidget)
        self.day_42.setObjectName("day_42")
        self.calendarGridLayout.addWidget(self.day_42, 6, 7, 1, 1)
        self.calendarGridLayout.setColumnStretch(0, 1)
        self.calendarGridLayout.setColumnStretch(1, 1)
        self.calendarGridLayout.setColumnStretch(2, 1)
        self.calendarGridLayout.setColumnStretch(3, 1)
        self.calendarGridLayout.setColumnStretch(4, 1)
        self.calendarGridLayout.setColumnStretch(5, 1)
        self.calendarGridLayout.setColumnStretch(6, 1)
        self.calendarGridLayout.setColumnStretch(7, 1)
        self.calendarGridLayout.setRowStretch(0, 1)
        self.calendarGridLayout.setRowStretch(1, 1)
        self.calendarGridLayout.setRowStretch(2, 1)
        self.calendarGridLayout.setRowStretch(3, 1)
        self.calendarGridLayout.setRowStretch(4, 1)
        self.calendarGridLayout.setRowStretch(5, 1)
        self.calendarGridLayout.setRowStretch(6, 1)
        self.navCalendarHorizontalLayout.addLayout(self.calendarGridLayout)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setMinimumSize(QtCore.QSize(0, 50))
        self.nextButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.nextButton.setObjectName("nextButton")
        self.navCalendarHorizontalLayout.addWidget(self.nextButton)
        self.navCalendarHorizontalLayout.setStretch(1, 1)
        self.dateCalendarVerticalLayout.addLayout(self.navCalendarHorizontalLayout)
        self.dateCalendarVerticalLayout.setStretch(1, 1)
        self.mainHorizontalLayout.addLayout(self.dateCalendarVerticalLayout)
        self.gridLayout_2.addLayout(self.mainHorizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shedule"))
        self.newEventButton.setText(_translate("MainWindow", "New event"))
        self.dayFromDate.setText(_translate("MainWindow", "16"))
        self.monthFromDate.setText(_translate("MainWindow", "July"))
        self.yearFromDate.setText(_translate("MainWindow", "2021"))
        self.prevButton.setText(_translate("MainWindow", "PREV"))
        self.weekDay3.setText(_translate("MainWindow", "Wednesday"))
        self.weekNumber4.setText(_translate("MainWindow", "29"))
        self.weekLabel.setText(_translate("MainWindow", "Week"))
        self.weekDay2.setText(_translate("MainWindow", "Tuesday"))
        self.weekDay6.setText(_translate("MainWindow", "Saturday"))
        self.weekNumber2.setText(_translate("MainWindow", "27"))
        self.weekNumber1.setText(_translate("MainWindow", "26"))
        self.weekDay4.setText(_translate("MainWindow", "Thursday"))
        self.weekDay5.setText(_translate("MainWindow", "Friday"))
        self.weekNumber3.setText(_translate("MainWindow", "28"))
        self.weekNumber5.setText(_translate("MainWindow", "30"))
        self.weekDay7.setText(_translate("MainWindow", "Sunday"))
        self.weekDay1.setText(_translate("MainWindow", "Monday"))
        self.weekNumber6.setText(_translate("MainWindow", "31"))
        self.day_1.setText(_translate("MainWindow", "TextLabel"))
        self.day_2.setText(_translate("MainWindow", "TextLabel"))
        self.day_3.setText(_translate("MainWindow", "TextLabel"))
        self.day_4.setText(_translate("MainWindow", "TextLabel"))
        self.day_5.setText(_translate("MainWindow", "TextLabel"))
        self.day_6.setText(_translate("MainWindow", "TextLabel"))
        self.day_7.setText(_translate("MainWindow", "TextLabel"))
        self.day_8.setText(_translate("MainWindow", "TextLabel"))
        self.day_9.setText(_translate("MainWindow", "TextLabel"))
        self.day_10.setText(_translate("MainWindow", "TextLabel"))
        self.day_11.setText(_translate("MainWindow", "TextLabel"))
        self.day_12.setText(_translate("MainWindow", "TextLabel"))
        self.day_13.setText(_translate("MainWindow", "TextLabel"))
        self.day_14.setText(_translate("MainWindow", "TextLabel"))
        self.day_15.setText(_translate("MainWindow", "TextLabel"))
        self.day_16.setText(_translate("MainWindow", "TextLabel"))
        self.day_17.setText(_translate("MainWindow", "TextLabel"))
        self.day_18.setText(_translate("MainWindow", "TextLabel"))
        self.day_19.setText(_translate("MainWindow", "TextLabel"))
        self.day_20.setText(_translate("MainWindow", "TextLabel"))
        self.day_21.setText(_translate("MainWindow", "TextLabel"))
        self.day_22.setText(_translate("MainWindow", "TextLabel"))
        self.day_23.setText(_translate("MainWindow", "TextLabel"))
        self.day_24.setText(_translate("MainWindow", "TextLabel"))
        self.day_25.setText(_translate("MainWindow", "TextLabel"))
        self.day_26.setText(_translate("MainWindow", "TextLabel"))
        self.day_27.setText(_translate("MainWindow", "TextLabel"))
        self.day_28.setText(_translate("MainWindow", "TextLabel"))
        self.day_29.setText(_translate("MainWindow", "TextLabel"))
        self.day_30.setText(_translate("MainWindow", "TextLabel"))
        self.day_31.setText(_translate("MainWindow", "TextLabel"))
        self.day_32.setText(_translate("MainWindow", "TextLabel"))
        self.day_33.setText(_translate("MainWindow", "TextLabel"))
        self.day_34.setText(_translate("MainWindow", "TextLabel"))
        self.day_35.setText(_translate("MainWindow", "TextLabel"))
        self.day_36.setText(_translate("MainWindow", "TextLabel"))
        self.day_37.setText(_translate("MainWindow", "TextLabel"))
        self.day_38.setText(_translate("MainWindow", "TextLabel"))
        self.day_39.setText(_translate("MainWindow", "TextLabel"))
        self.day_40.setText(_translate("MainWindow", "TextLabel"))
        self.day_41.setText(_translate("MainWindow", "TextLabel"))
        self.day_42.setText(_translate("MainWindow", "TextLabel"))
        self.nextButton.setText(_translate("MainWindow", "NEXT"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
