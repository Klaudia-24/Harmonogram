from PyQt5 import QtWidgets, QtGui, QtCore
from GUI.Autogenerated.AGMainCalendarWidget import Ui_Form
from datetime import date
import datetime
import dateutils
from calendar import monthrange
# from GUI.MainWindow import MainWindow
from Objects.Event import getEventsDictionary, getEventTypeColour


class MainCalendarWidget(QtWidgets.QWidget):

    clickedDaySignal = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mainCalendarWidget = Ui_Form()
        self.mainCalendarWidget.setupUi(self)
        self.dateOnDateBar = date.today()
        self.init_ui()

    def init_ui(self) -> None:
        self.setWeekDaysAppearance()
        self.setWeekNumbersAppearance()
        self.setAdditionalCalendarAppearance()
        self.setDaysWidgetAppearance()
        self.generateCalendarDays()

        for i in range(1, 43):
            getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setClicked')(self.getLabelNameFromCalendarDayLabel)

        print("1 " + str(self.mainCalendarWidget.day_1.getEventColorList()))
        print("2 " + str(self.mainCalendarWidget.day_2.getEventColorList()))
        print("3 " + str(self.mainCalendarWidget.day_3.getEventColorList()))
        print("4 " + str(self.mainCalendarWidget.day_4.getEventColorList()))
        print("5 " + str(self.mainCalendarWidget.day_5.getEventColorList()))
        print("6 " + str(self.mainCalendarWidget.day_6.getEventColorList()))
        print("7 " + str(self.mainCalendarWidget.day_7.getEventColorList()))
        print("8 " + str(self.mainCalendarWidget.day_8.getEventColorList()))
        print("9 " + str(self.mainCalendarWidget.day_9.getEventColorList()))
        print("10 " + str(self.mainCalendarWidget.day_10.getEventColorList()))
        print("11 " + str(self.mainCalendarWidget.day_11.getEventColorList()))
        print("12 " + str(self.mainCalendarWidget.day_12.getEventColorList()))

    def setWeekDaysAppearance(self):
        for i in range(1, 8):
            getattr(getattr(self.mainCalendarWidget, 'weekDay' + str(i)), 'setBackgroundColor')("#bfbfbf")
            getattr(getattr(self.mainCalendarWidget, 'weekDay' + str(i)), 'setEventShapeSize')(0)
            getattr(getattr(self.mainCalendarWidget, 'weekDay' + str(i)), 'setFontAppearance')('Times', QtGui.QFont.Normal, 8.1)
            # getattr(getattr(self.mainCalendarWidget, 'weekDay' + str(i)), 'setAlignment')(QtCore.Qt.AlignCenter)

    def setWeekNumbersAppearance(self):
        for i in range(1, 7):
            getattr(getattr(self.mainCalendarWidget, 'weekNumber' + str(i)), 'setBackgroundColor')("#bfbfbf")
            getattr(getattr(self.mainCalendarWidget, 'weekNumber' + str(i)), 'setEventShapeSize')(0)
            getattr(getattr(self.mainCalendarWidget, 'weekNumber' + str(i)), 'setFontAppearance')('Times', QtGui.QFont.Normal, 7)
            # getattr(getattr(self.mainCalendarWidget, 'weekNumber' + str(i)), 'setAlignment')(QtCore.Qt.AlignCenter)

    def setDaysWidgetAppearance(self):
        for i in range(1, 43):
            getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setEventShapeSize')(10)
            getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setFontAppearance')('Times', QtGui.QFont.Normal, 3.5)
            # getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setFont')(QtGui.QFont('Times', 9))
            # getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setAlignment')(QtCore.Qt.AlignCenter)

    def setAdditionalCalendarAppearance(self):
        self.mainCalendarWidget.weekLabel.setBackgroundColor("#bfbfbf")
        self.mainCalendarWidget.weekLabel.setEventShapeSize(0)
        self.mainCalendarWidget.weekLabel.setFontAppearance('Times', QtGui.QFont.Normal, 8.1)
        # self.mainCalendarWidget.weekLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainCalendarWidget.calendarGridLayout.setSpacing(1)

    def generateCalendarDays(self):
        firstWeekDayOfMonth = int(
            datetime.datetime(self.dateOnDateBar.year,
                              self.dateOnDateBar.month, 1).strftime('%w'))
        currentMonthRange = int(monthrange(self.dateOnDateBar.year,
                                           self.dateOnDateBar.month)[1])

        if firstWeekDayOfMonth == 0:
            firstWeekDayOfMonth = 7

        for i in range(1, 43):
            if i < firstWeekDayOfMonth:
                print(i)
                newDate = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, self.dateOnDateBar.day) - dateutils.relativedelta(months=1)
                prevMonthRange = int(monthrange(newDate.year, newDate.month)[1])
                getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setText')(str(prevMonthRange - firstWeekDayOfMonth + i + 1))
                getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setBackgroundColor')("#cce6ff")

                if str(newDate.year) in getEventsDictionary()["events"]:
                    if str(newDate.month) in getEventsDictionary()["events"][str(newDate.year)]:
                        if str(prevMonthRange - firstWeekDayOfMonth + i + 1) in getEventsDictionary()["events"][str(newDate.year)][str(newDate.month)]:
                            for event in getEventsDictionary()["events"][str(newDate.year)][str(newDate.month)][str(prevMonthRange - firstWeekDayOfMonth + i + 1)]:
                                getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'addEventColor')(getEventTypeColour(event["type"]))

            elif firstWeekDayOfMonth <= i <= currentMonthRange + firstWeekDayOfMonth - 1:
                getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setText')(str(i - firstWeekDayOfMonth + 1))
                getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setBackgroundColor')("#80bfff")

                if str(self.dateOnDateBar.year) in getEventsDictionary()["events"]:
                    if str(self.dateOnDateBar.month) in getEventsDictionary()["events"][str(self.dateOnDateBar.year)]:
                        if str(i - firstWeekDayOfMonth + 1) in getEventsDictionary()["events"][str(self.dateOnDateBar.year)][str(self.dateOnDateBar.month)]:
                            for event in getEventsDictionary()["events"][str(self.dateOnDateBar.year)][str(self.dateOnDateBar.month)][str(i - firstWeekDayOfMonth + 1)]:
                                getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'addEventColor')(getEventTypeColour(event["type"]))

            else:
                getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setText')(str(i - firstWeekDayOfMonth - currentMonthRange + 1))
                getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setBackgroundColor')("#cce6ff")

                if str(self.dateOnDateBar.year) in getEventsDictionary()["events"]:
                    if str(self.dateOnDateBar.month+1) in getEventsDictionary()["events"][str(self.dateOnDateBar.year)]:
                        if str(i - firstWeekDayOfMonth - currentMonthRange + 1) in getEventsDictionary()["events"][str(self.dateOnDateBar.year)][str(self.dateOnDateBar.month+1)]:
                            for event in getEventsDictionary()["events"][str(self.dateOnDateBar.year)][str(self.dateOnDateBar.month+1)][str(i - firstWeekDayOfMonth - currentMonthRange + 1)]:
                                getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'addEventColor')(getEventTypeColour(event["type"]))


        # self.setDateInBar()

        if self.dateOnDateBar.year == date.today().year and self.dateOnDateBar.month == date.today().month:
            self.distinguishDayFromDateBar()
        else:
            for i in range(1, 43):
                # getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setFont')(QtGui.QFont('Times', 9, QtGui.QFont.Normal))
                getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setFontAppearance')('Times', QtGui.QFont.Normal, 3.5)

        self.setWeekNumbers()

    def distinguishDayFromDateBar(self):
        firstWeekDayOfMonth = int(
            datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, 1).strftime('%w'))

        if firstWeekDayOfMonth == 0:
            firstWeekDayOfMonth = 7

        todayIndex = date.today().day + firstWeekDayOfMonth - 1
        getattr(getattr(self.mainCalendarWidget, 'day_' + str(todayIndex)), 'setBackgroundColor')("#339966")
        # getattr(getattr(self.mainCalendarWidget, 'day_' + str(todayIndex)), 'setFont')(QtGui.QFont('Times', 11, QtGui.QFont.Bold))
        getattr(getattr(self.mainCalendarWidget, 'day_' + str(todayIndex)), 'setFontAppearance')('Times', QtGui.QFont.Bold, 3.5)

    def setWeekNumbers(self):
        firstSundayDate = date(self.dateOnDateBar.year, self.dateOnDateBar.month, int(self.mainCalendarWidget.day_7.getText()))

        for i in range(0, 6):
            number = (firstSundayDate + dateutils.relativedelta(days=7 * i)).strftime('%W').lstrip("0")
            i += 1
            getattr(getattr(self.mainCalendarWidget, 'weekNumber' + str(i)), 'setText')(str(number))

    def distinguishClickedDay(self):
        firstWeekDayOfMonth = int(
            datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, 1).strftime('%w'))

        if firstWeekDayOfMonth == 0:
            firstWeekDayOfMonth = 7

        clickedIndex = self.dateOnDateBar.day + firstWeekDayOfMonth - 1
        getattr(getattr(self.mainCalendarWidget, 'day_' + str(clickedIndex)), 'setBackgroundColor')("#66cc99")

        self.clickedDaySignal.emit()

    def getLabelNameFromCalendarDayLabel(self, event, labelName):
        button = event.button()
        modify = event.modifiers()
        if modify == QtCore.Qt.NoModifier and button == QtCore.Qt.LeftButton:
            labelObject = getattr(self.mainCalendarWidget, labelName)
            self.setClickedDateInDateBar(labelObject.getText(), labelName)
            self.distinguishClickedDay()
            return

    def updateWidgetSize(self):
        # print("width: " + str(self.width()))
        # print("height: " + str(self.height()))

        cellWidth = (self.width()//8) - 6
        cellHeight = (self.height()//7) - 6

        self.mainCalendarWidget.widget.setGeometry(0, 0, self.width(), self.height())
        self.resize(self.width(), self.height())
        # self.setMinimumWidth(self.width())

        self.mainCalendarWidget.calendarGridLayout.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))

        # for i in range(0, 8):
        #     self.mainCalendarWidget.calendarGridLayout.setColumnMinimumWidth(i, cellWidth)
        #
        # for i in range(0, 7):
        #     self.mainCalendarWidget.calendarGridLayout.setRowMinimumHeight(i, cellHeight)

        # for i in range(1, 7):
        #     getattr(getattr(self.mainCalendarWidget, 'weekNumber' + str(i)), 'setWidgetSize')(cellWidth, cellHeight)
        #     getattr(getattr(self.mainCalendarWidget, 'weekNumber' + str(i)), 'refresh')
        #
        # for i in range(1, 8):
        #     getattr(getattr(self.mainCalendarWidget, 'weekDay' + str(i)), 'setWidgetSize')(cellWidth, cellHeight)
        #     getattr(getattr(self.mainCalendarWidget, 'weekDay' + str(i)), 'refresh')

        # self.mainCalendarWidget.calendarGridLayout.setColumnMinimumWidth(cellWidth)
        # self.mainCalendarWidget.calendarGridLayout.

        # for i in range(1, 43):
        #     getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setWidgetSize')(cellWidth, cellHeight)
        #     getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'refresh')
        #
        # self.mainCalendarWidget.weekLabel.setWidgetSize(cellWidth, cellHeight)
        # self.mainCalendarWidget.weekLabel.refresh()

    def changeMonthToPrev(self):

        self.dateOnDateBar = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month,
                                               self.dateOnDateBar.day) - dateutils.relativedelta(months=1)
        for i in range(1, 43):
            getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setEventColorList')([])
        self.generateCalendarDays()
        self.distinguishClickedDay()

    def changeMonthToNext(self):

        self.dateOnDateBar = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month,
                                               self.dateOnDateBar.day) + dateutils.relativedelta(months=1)
        for i in range(1, 43):
            getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setEventColorList')([])
        self.generateCalendarDays()
        self.distinguishClickedDay()

    def setClickedDateInDateBar(self, labelText: str, labelName: str):
        offset = 0
        if int(labelName.split("_")[1]) <= 6 and int(labelText) >= 7:
            offset = -1

        elif int(labelName.split("_")[1]) >= 29 and int(labelText) <= 14:
            offset = 1

        self.dateOnDateBar = datetime.datetime(self.dateOnDateBar.year,
                                               self.dateOnDateBar.month + offset if 1 <= self.dateOnDateBar.month + offset <= 12
                                               else 12 if self.dateOnDateBar.month + offset < 1 else 1,
                                               int(labelText))
        self.generateCalendarDays()
        # self.setDateInBar()

# def __main__():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Mainwindow = MainCalendarWidget()
#
#     Mainwindow.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     __main__()
