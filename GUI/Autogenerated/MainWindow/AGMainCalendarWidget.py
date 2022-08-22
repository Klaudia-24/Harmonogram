# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AGMainCalendarWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from WindowObjects.CalendarCellWidget import CalendarCellWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(900, 480)
        Form.setToolTip("")
        self.layoutWidget = QtWidgets.QWidget(Form)
        # self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 881, 459))
        self.layoutWidget.setObjectName("layoutWidget")
        self.calendarGridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.calendarGridLayout.setContentsMargins(0, 0, 0, 0)
        self.calendarGridLayout.setObjectName("calendarGridLayout")
        self.weekDay3 = CalendarCellWidget(self.layoutWidget)
        self.weekDay3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay3.setObjectName("weekDay3")
        self.calendarGridLayout.addWidget(self.weekDay3, 0, 3, 1, 1)
        self.weekNumber4 = CalendarCellWidget(self.layoutWidget)
        self.weekNumber4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber4.setObjectName("weekNumber4")
        self.calendarGridLayout.addWidget(self.weekNumber4, 4, 0, 1, 1)
        self.weekNumber0 = CalendarCellWidget(self.layoutWidget)
        self.weekNumber0.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekNumber0.setObjectName("weekNumber0")
        self.calendarGridLayout.addWidget(self.weekNumber0, 0, 0, 1, 1)
        self.weekDay2 = CalendarCellWidget(self.layoutWidget)
        self.weekDay2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay2.setObjectName("weekDay2")
        self.calendarGridLayout.addWidget(self.weekDay2, 0, 2, 1, 1)
        self.weekDay6 = CalendarCellWidget(self.layoutWidget)
        self.weekDay6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay6.setObjectName("weekDay6")
        self.calendarGridLayout.addWidget(self.weekDay6, 0, 6, 1, 1)
        self.weekNumber2 = CalendarCellWidget(self.layoutWidget)
        self.weekNumber2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber2.setObjectName("weekNumber2")
        self.calendarGridLayout.addWidget(self.weekNumber2, 2, 0, 1, 1)
        self.weekNumber1 = CalendarCellWidget(self.layoutWidget)
        self.weekNumber1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber1.setObjectName("weekNumber1")
        self.calendarGridLayout.addWidget(self.weekNumber1, 1, 0, 1, 1)
        self.weekDay4 = CalendarCellWidget(self.layoutWidget)
        self.weekDay4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay4.setObjectName("weekDay4")
        self.calendarGridLayout.addWidget(self.weekDay4, 0, 4, 1, 1)
        self.weekNumber3 = CalendarCellWidget(self.layoutWidget)
        self.weekNumber3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber3.setObjectName("weekNumber3")
        self.calendarGridLayout.addWidget(self.weekNumber3, 3, 0, 1, 1)
        self.weekNumber5 = CalendarCellWidget(self.layoutWidget)
        self.weekNumber5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber5.setObjectName("weekNumber5")
        self.calendarGridLayout.addWidget(self.weekNumber5, 5, 0, 1, 1)
        self.weekDay7 = CalendarCellWidget(self.layoutWidget)
        self.weekDay7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay7.setObjectName("weekDay7")
        self.calendarGridLayout.addWidget(self.weekDay7, 0, 7, 1, 1)
        self.weekDay1 = CalendarCellWidget(self.layoutWidget)
        self.weekDay1.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.weekDay1.setObjectName("weekDay1")
        self.calendarGridLayout.addWidget(self.weekDay1, 0, 1, 1, 1)
        self.weekNumber6 = CalendarCellWidget(self.layoutWidget)
        self.weekNumber6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.weekNumber6.setObjectName("weekNumber6")
        self.calendarGridLayout.addWidget(self.weekNumber6, 6, 0, 1, 1)
        self.day_1 = CalendarCellWidget(self.layoutWidget)
        self.day_1.setMinimumSize(QtCore.QSize(0, 0))
        self.day_1.setObjectName("day_1")
        self.calendarGridLayout.addWidget(self.day_1, 1, 1, 1, 1)
        self.day_2 = CalendarCellWidget(self.layoutWidget)
        self.day_2.setObjectName("day_2")
        self.calendarGridLayout.addWidget(self.day_2, 1, 2, 1, 1)
        self.day_3 = CalendarCellWidget(self.layoutWidget)
        self.day_3.setObjectName("day_3")
        self.calendarGridLayout.addWidget(self.day_3, 1, 3, 1, 1)
        self.day_4 = CalendarCellWidget(self.layoutWidget)
        self.day_4.setObjectName("day_4")
        self.calendarGridLayout.addWidget(self.day_4, 1, 4, 1, 1)
        self.day_5 = CalendarCellWidget(self.layoutWidget)
        self.day_5.setObjectName("day_5")
        self.calendarGridLayout.addWidget(self.day_5, 1, 5, 1, 1)
        self.day_6 = CalendarCellWidget(self.layoutWidget)
        self.day_6.setObjectName("day_6")
        self.calendarGridLayout.addWidget(self.day_6, 1, 6, 1, 1)
        self.day_7 = CalendarCellWidget(self.layoutWidget)
        self.day_7.setObjectName("day_7")
        self.calendarGridLayout.addWidget(self.day_7, 1, 7, 1, 1)
        self.day_8 = CalendarCellWidget(self.layoutWidget)
        self.day_8.setMinimumSize(QtCore.QSize(0, 0))
        self.day_8.setObjectName("day_8")
        self.calendarGridLayout.addWidget(self.day_8, 2, 1, 1, 1)
        self.day_9 = CalendarCellWidget(self.layoutWidget)
        self.day_9.setObjectName("day_9")
        self.calendarGridLayout.addWidget(self.day_9, 2, 2, 1, 1)
        self.day_10 = CalendarCellWidget(self.layoutWidget)
        self.day_10.setObjectName("day_10")
        self.calendarGridLayout.addWidget(self.day_10, 2, 3, 1, 1)
        self.day_11 = CalendarCellWidget(self.layoutWidget)
        self.day_11.setObjectName("day_11")
        self.calendarGridLayout.addWidget(self.day_11, 2, 4, 1, 1)
        self.day_12 = CalendarCellWidget(self.layoutWidget)
        self.day_12.setObjectName("day_12")
        self.calendarGridLayout.addWidget(self.day_12, 2, 5, 1, 1)
        self.day_13 = CalendarCellWidget(self.layoutWidget)
        self.day_13.setObjectName("day_13")
        self.calendarGridLayout.addWidget(self.day_13, 2, 6, 1, 1)
        self.day_14 = CalendarCellWidget(self.layoutWidget)
        self.day_14.setObjectName("day_14")
        self.calendarGridLayout.addWidget(self.day_14, 2, 7, 1, 1)
        self.day_15 = CalendarCellWidget(self.layoutWidget)
        self.day_15.setMinimumSize(QtCore.QSize(0, 0))
        self.day_15.setObjectName("day_15")
        self.calendarGridLayout.addWidget(self.day_15, 3, 1, 1, 1)
        self.day_16 = CalendarCellWidget(self.layoutWidget)
        self.day_16.setObjectName("day_16")
        self.calendarGridLayout.addWidget(self.day_16, 3, 2, 1, 1)
        self.day_17 = CalendarCellWidget(self.layoutWidget)
        self.day_17.setObjectName("day_17")
        self.calendarGridLayout.addWidget(self.day_17, 3, 3, 1, 1)
        self.day_18 = CalendarCellWidget(self.layoutWidget)
        self.day_18.setObjectName("day_18")
        self.calendarGridLayout.addWidget(self.day_18, 3, 4, 1, 1)
        self.day_19 = CalendarCellWidget(self.layoutWidget)
        self.day_19.setObjectName("day_19")
        self.calendarGridLayout.addWidget(self.day_19, 3, 5, 1, 1)
        self.day_20 = CalendarCellWidget(self.layoutWidget)
        self.day_20.setObjectName("day_20")
        self.calendarGridLayout.addWidget(self.day_20, 3, 6, 1, 1)
        self.day_21 = CalendarCellWidget(self.layoutWidget)
        self.day_21.setObjectName("day_21")
        self.calendarGridLayout.addWidget(self.day_21, 3, 7, 1, 1)
        self.day_22 = CalendarCellWidget(self.layoutWidget)
        self.day_22.setMinimumSize(QtCore.QSize(0, 0))
        self.day_22.setObjectName("day_22")
        self.calendarGridLayout.addWidget(self.day_22, 4, 1, 1, 1)
        self.day_23 = CalendarCellWidget(self.layoutWidget)
        self.day_23.setObjectName("day_23")
        self.calendarGridLayout.addWidget(self.day_23, 4, 2, 1, 1)
        self.day_24 = CalendarCellWidget(self.layoutWidget)
        self.day_24.setObjectName("day_24")
        self.calendarGridLayout.addWidget(self.day_24, 4, 3, 1, 1)
        self.day_25 = CalendarCellWidget(self.layoutWidget)
        self.day_25.setObjectName("day_25")
        self.calendarGridLayout.addWidget(self.day_25, 4, 4, 1, 1)
        self.day_26 = CalendarCellWidget(self.layoutWidget)
        self.day_26.setObjectName("day_26")
        self.calendarGridLayout.addWidget(self.day_26, 4, 5, 1, 1)
        self.day_27 = CalendarCellWidget(self.layoutWidget)
        self.day_27.setObjectName("day_27")
        self.calendarGridLayout.addWidget(self.day_27, 4, 6, 1, 1)
        self.day_28 = CalendarCellWidget(self.layoutWidget)
        self.day_28.setObjectName("day_28")
        self.calendarGridLayout.addWidget(self.day_28, 4, 7, 1, 1)
        self.day_29 = CalendarCellWidget(self.layoutWidget)
        self.day_29.setMinimumSize(QtCore.QSize(0, 0))
        self.day_29.setObjectName("day_29")
        self.calendarGridLayout.addWidget(self.day_29, 5, 1, 1, 1)
        self.day_30 = CalendarCellWidget(self.layoutWidget)
        self.day_30.setObjectName("day_30")
        self.calendarGridLayout.addWidget(self.day_30, 5, 2, 1, 1)
        self.day_31 = CalendarCellWidget(self.layoutWidget)
        self.day_31.setObjectName("day_31")
        self.calendarGridLayout.addWidget(self.day_31, 5, 3, 1, 1)
        self.day_32 = CalendarCellWidget(self.layoutWidget)
        self.day_32.setObjectName("day_32")
        self.calendarGridLayout.addWidget(self.day_32, 5, 4, 1, 1)
        self.day_33 = CalendarCellWidget(self.layoutWidget)
        self.day_33.setObjectName("day_33")
        self.calendarGridLayout.addWidget(self.day_33, 5, 5, 1, 1)
        self.day_34 = CalendarCellWidget(self.layoutWidget)
        self.day_34.setObjectName("day_34")
        self.calendarGridLayout.addWidget(self.day_34, 5, 6, 1, 1)
        self.day_35 = CalendarCellWidget(self.layoutWidget)
        self.day_35.setObjectName("day_35")
        self.calendarGridLayout.addWidget(self.day_35, 5, 7, 1, 1)
        self.day_36 = CalendarCellWidget(self.layoutWidget)
        self.day_36.setMinimumSize(QtCore.QSize(0, 0))
        self.day_36.setObjectName("day_36")
        self.calendarGridLayout.addWidget(self.day_36, 6, 1, 1, 1)
        self.day_37 = CalendarCellWidget(self.layoutWidget)
        self.day_37.setObjectName("day_37")
        self.calendarGridLayout.addWidget(self.day_37, 6, 2, 1, 1)
        self.day_38 = CalendarCellWidget(self.layoutWidget)
        self.day_38.setObjectName("day_38")
        self.calendarGridLayout.addWidget(self.day_38, 6, 3, 1, 1)
        self.day_39 = CalendarCellWidget(self.layoutWidget)
        self.day_39.setObjectName("day_39")
        self.calendarGridLayout.addWidget(self.day_39, 6, 4, 1, 1)
        self.day_40 = CalendarCellWidget(self.layoutWidget)
        self.day_40.setObjectName("day_40")
        self.calendarGridLayout.addWidget(self.day_40, 6, 5, 1, 1)
        self.day_41 = CalendarCellWidget(self.layoutWidget)
        self.day_41.setObjectName("day_41")
        self.calendarGridLayout.addWidget(self.day_41, 6, 6, 1, 1)
        self.day_42 = CalendarCellWidget(self.layoutWidget)
        self.day_42.setObjectName("day_42")
        self.calendarGridLayout.addWidget(self.day_42, 6, 7, 1, 1)
        self.weekDay5 = CalendarCellWidget(self.layoutWidget)
        self.weekDay5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.weekDay5.setObjectName("weekDay5")
        self.calendarGridLayout.addWidget(self.weekDay5, 0, 5, 1, 1)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.weekDay3.setText(_translate("Form", "Wednesday"))
        self.weekNumber4.setText(_translate("Form", "29"))
        self.weekNumber0.setText(_translate("Form", "Week"))
        self.weekDay2.setText(_translate("Form", "Tuesday"))
        self.weekDay6.setText(_translate("Form", "Saturday"))
        self.weekNumber2.setText(_translate("Form", "27"))
        self.weekNumber1.setText(_translate("Form", "26"))
        self.weekDay4.setText(_translate("Form", "Thursday"))
        self.weekNumber3.setText(_translate("Form", "28"))
        self.weekNumber5.setText(_translate("Form", "30"))
        self.weekDay7.setText(_translate("Form", "Sunday"))
        self.weekDay1.setText(_translate("Form", "Monday"))
        self.weekNumber6.setText(_translate("Form", "31"))
        self.day_1.setText(_translate("Form", "TextLabel"))
        self.day_2.setText(_translate("Form", "TextLabel"))
        self.day_3.setText(_translate("Form", "TextLabel"))
        self.day_4.setText(_translate("Form", "TextLabel"))
        self.day_5.setText(_translate("Form", "TextLabel"))
        self.day_6.setText(_translate("Form", "TextLabel"))
        self.day_7.setText(_translate("Form", "TextLabel"))
        self.day_8.setText(_translate("Form", "TextLabel"))
        self.day_9.setText(_translate("Form", "TextLabel"))
        self.day_10.setText(_translate("Form", "TextLabel"))
        self.day_11.setText(_translate("Form", "TextLabel"))
        self.day_12.setText(_translate("Form", "TextLabel"))
        self.day_13.setText(_translate("Form", "TextLabel"))
        self.day_14.setText(_translate("Form", "TextLabel"))
        self.day_15.setText(_translate("Form", "TextLabel"))
        self.day_16.setText(_translate("Form", "TextLabel"))
        self.day_17.setText(_translate("Form", "TextLabel"))
        self.day_18.setText(_translate("Form", "TextLabel"))
        self.day_19.setText(_translate("Form", "TextLabel"))
        self.day_20.setText(_translate("Form", "TextLabel"))
        self.day_21.setText(_translate("Form", "TextLabel"))
        self.day_22.setText(_translate("Form", "TextLabel"))
        self.day_23.setText(_translate("Form", "TextLabel"))
        self.day_24.setText(_translate("Form", "TextLabel"))
        self.day_25.setText(_translate("Form", "TextLabel"))
        self.day_26.setText(_translate("Form", "TextLabel"))
        self.day_27.setText(_translate("Form", "TextLabel"))
        self.day_28.setText(_translate("Form", "TextLabel"))
        self.day_29.setText(_translate("Form", "TextLabel"))
        self.day_30.setText(_translate("Form", "TextLabel"))
        self.day_31.setText(_translate("Form", "TextLabel"))
        self.day_32.setText(_translate("Form", "TextLabel"))
        self.day_33.setText(_translate("Form", "TextLabel"))
        self.day_34.setText(_translate("Form", "TextLabel"))
        self.day_35.setText(_translate("Form", "TextLabel"))
        self.day_36.setText(_translate("Form", "TextLabel"))
        self.day_37.setText(_translate("Form", "TextLabel"))
        self.day_38.setText(_translate("Form", "TextLabel"))
        self.day_39.setText(_translate("Form", "TextLabel"))
        self.day_40.setText(_translate("Form", "TextLabel"))
        self.day_41.setText(_translate("Form", "TextLabel"))
        self.day_42.setText(_translate("Form", "TextLabel"))
        self.weekDay5.setText(_translate("Form", "Friday"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
