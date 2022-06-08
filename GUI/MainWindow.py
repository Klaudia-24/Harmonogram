import json

from GUI.Autogenerated.AGMainW_v3 import Ui_MainWindow
import GUI.NewEventW as newEventW
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import datetime
import dateutils
from calendar import monthrange
from PyQt5.QtGui import QPainter, QBrush, QPen

from Lib import FileOperationMethods
from Objects.Event import loadEventsList, loadEventTypesList, getEventsDictionary
from GUI.MainCalendarWidget import MainCalendarWidget


class MainWindow(QtWidgets.QMainWindow):

    # dateOnDateBar = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadEventsList()
        loadEventTypesList()
        # self.ui.dateCalendarVerticalLayout.setStretch(0, 0)
        # self.ui.dateCalendarVerticalLayout.SetFixedSize = True
        self.mainCalendarWidget = MainCalendarWidget()
        # self.mainCalendarWidget.setMinimumHeight(int(self.height()*0.8))
        self.ui.calendarGridLayout.addWidget(self.mainCalendarWidget)

        # for i in range(1, 8):
        #     getattr(getattr(self.ui, 'weekDay' + str(i)), 'setStyleSheet')("background-color: rgb(191, 191, 191)")
        #     getattr(getattr(self.ui, 'weekDay' + str(i)), 'setFont')(QtGui.QFont('Times', 11, QtGui.QFont.Bold))
        #     getattr(getattr(self.ui, 'weekDay' + str(i)), 'setAlignment')(QtCore.Qt.AlignCenter)
        #
        # for i in range(1, 7):
        #     getattr(getattr(self.ui, 'weekNumber' + str(i)), 'setStyleSheet')("background-color: rgb(191, 191, 191)")
        #     getattr(getattr(self.ui, 'weekNumber' + str(i)), 'setFont')(QtGui.QFont('Times', 10, QtGui.QFont.Bold))
        #     getattr(getattr(self.ui, 'weekNumber' + str(i)), 'setAlignment')(QtCore.Qt.AlignCenter)
        #
        # for i in range(1, 43):
        #     getattr(getattr(self.ui, 'day_' + str(i)), 'setFont')(QtGui.QFont('Times', 9))
        #     getattr(getattr(self.ui, 'day_' + str(i)), 'setAlignment')(QtCore.Qt.AlignCenter)
        #
        # self.ui.weekLabel.setStyleSheet("background-color: rgb(191, 191, 191)")
        # self.ui.weekLabel.setFont(QtGui.QFont('Times', 11, QtGui.QFont.Bold))
        # self.ui.weekLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.ui.calendarGridLayout.setSpacing(1)


        self.ui_newEventWindow = newEventW.NewEventW()
        self.ui.newEventButton.clicked.connect(self.openNewEventWindow)
        # self.dateOnDateBar = date.today()
        self.ui.prevButton.clicked.connect(self.setDateInBarToPrevMonth)
        self.ui.nextButton.clicked.connect(self.setDateInBarToNextMonth)
        self.setDateInBar()
        # for i in range(1, 43):
        #     getattr(getattr(self.ui, 'day_' + str(i)), 'setClicked')(self.getLabelNameFromCalendarDayLabel)

        # self.generateCalendarDays()

        # FileOperationMethods.readFromJsonFileToDict("./events.json", eventsDictionary, "events")
        self.mainCalendarWidget.clickedDaySignal.connect(self.setClickedDateInBar)

    # def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
    #     self.mainCalendarWidget.resize(int(self.width()*0.7), int(self.height()*0.8))
    #     self.mainCalendarWidget.updateWidgetSize()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.mainCalendarWidget.resize(int(self.width()*0.73), int(self.height()*0.85))
        self.mainCalendarWidget.updateWidgetSize()

    def setDateInBar(self):
        self.ui.dayFromDate.setText(str(self.mainCalendarWidget.dateOnDateBar.day))
        self.ui.monthFromDate.setText(self.mainCalendarWidget.dateOnDateBar.strftime("%B"))
        self.ui.yearFromDate.setText(str(self.mainCalendarWidget.dateOnDateBar.year))

    @QtCore.pyqtSlot()
    def setClickedDateInBar(self):
        self.setDateInBar()

    def getDateOnDateBar(self):
        return self.dateOnDateBar

    def setDateInBarToPrevMonth(self):
        self.mainCalendarWidget.changeMonthToPrev()
        self.setDateInBar()

    def setDateInBarToNextMonth(self):
        self.mainCalendarWidget.changeMonthToNext()
        self.setDateInBar()


    # def generateCalendarDays(self):
    #     firstWeekDayOfMonth = int(
    #         datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, 1).strftime('%w'))
    #     currentMonthRange = int(monthrange(self.dateOnDateBar.year, self.dateOnDateBar.month)[1])
    #
    #     if firstWeekDayOfMonth == 0:
    #         firstWeekDayOfMonth = 7
    #
    #     for i in range(1, 43):
    #         if i < firstWeekDayOfMonth:
    #             newDate = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, self.dateOnDateBar.day) \
    #                       - dateutils.relativedelta(months=1)
    #             prevMonthRange = int(monthrange(newDate.year, newDate.month)[1])
    #             getattr(getattr(self.ui, 'day_' + str(i)), 'setText')(str(prevMonthRange - firstWeekDayOfMonth + i + 1))
    #             getattr(getattr(self.ui, 'day_' + str(i)), 'setStyleSheet')("background-color: rgb(204, 230, 255)")
    #
    #         elif firstWeekDayOfMonth <= i <= currentMonthRange + firstWeekDayOfMonth - 1:
    #             getattr(getattr(self.ui, 'day_' + str(i)), 'setText')(str(i - firstWeekDayOfMonth + 1))
    #             getattr(getattr(self.ui, 'day_' + str(i)), 'setStyleSheet')("background-color: rgb(128, 191, 255)")
    #
    #         else:
    #             getattr(getattr(self.ui, 'day_' + str(i)), 'setText')(
    #                 str(i - firstWeekDayOfMonth - currentMonthRange + 1))
    #             getattr(getattr(self.ui, 'day_' + str(i)), 'setStyleSheet')("background-color: rgb(204, 230, 255)")
    #
    #     self.setDateInBar()
    #
    #     if self.dateOnDateBar.year == date.today().year and self.dateOnDateBar.month == date.today().month:
    #         self.distinguishDayFromDateBar()
    #     else:
    #         for i in range(1, 43):
    #             getattr(getattr(self.ui, 'day_' + str(i)), 'setFont')(QtGui.QFont('Times', 9, QtGui.QFont.Normal))
    #
    #     self.setWeekNumbers()

    # def changeMonthToPrev(self):
    #
    #     self.dateOnDateBar = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month,
    #                                            self.dateOnDateBar.day) - dateutils.relativedelta(months=1)
    #     self.generateCalendarDays()
    #
    # def changeMonthToNext(self):
    #
    #     self.dateOnDateBar = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month,
    #                                            self.dateOnDateBar.day) + dateutils.relativedelta(months=1)
    #     self.generateCalendarDays()

    # def distinguishDayFromDateBar(self):
    #     firstWeekDayOfMonth = int(
    #         datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, 1).strftime('%w'))
    #
    #     if firstWeekDayOfMonth == 0:
    #         firstWeekDayOfMonth = 7
    #
    #     todayIndex = date.today().day + firstWeekDayOfMonth - 1
    #     getattr(getattr(self.ui, 'day_' + str(todayIndex)), 'setStyleSheet')("background-color: rgb(51, 153, 102)")
    #     getattr(getattr(self.ui, 'day_' + str(todayIndex)), 'setFont')(QtGui.QFont('Times', 11, QtGui.QFont.Bold))
    #
    # def setWeekNumbers(self):
    #     firstSundayDate = date(self.dateOnDateBar.year, self.dateOnDateBar.month, int(self.ui.day_7.text()))
    #
    #     for i in range(0, 6):
    #         number = (firstSundayDate + dateutils.relativedelta(days=7 * i)).strftime('%W').lstrip("0")
    #         i += 1
    #         getattr(getattr(self.ui, 'weekNumber' + str(i)), 'setText')(str(number))

    def openNewEventWindow(self):
        self.ui_newEventWindow.setDateFromCalendar(self.mainCalendarWidget.dateOnDateBar)
        self.ui_newEventWindow.timeEditDisabled()
        self.ui_newEventWindow.clearEventDataInFormular()
        self.ui_newEventWindow.show()

    # def distinguishClickedDay(self):
    #     firstWeekDayOfMonth = int(
    #         datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, 1).strftime('%w'))
    #
    #     if firstWeekDayOfMonth == 0:
    #         firstWeekDayOfMonth = 7
    #
    #     clickedIndex = self.dateOnDateBar.day + firstWeekDayOfMonth - 1
    #     getattr(getattr(self.ui, 'day_' + str(clickedIndex)), 'setStyleSheet')("background-color: rgb(102, 204, 153)")

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
        self.setDateInBar()

    def getLabelNameFromCalendarDayLabel(self, event, labelName):
        button = event.button()
        modify = event.modifiers()
        if modify == QtCore.Qt.NoModifier and button == QtCore.Qt.LeftButton:
            labelObject = getattr(self.ui, labelName)
            self.setClickedDateInDateBar(labelObject.text(), labelName)
            self.distinguishClickedDay()
            return

# TODO colors in calendar days for events also by starting app and changing months
