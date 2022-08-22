from typing import List

from PyQt5 import QtWidgets, QtGui, QtCore
from GUI.Autogenerated.MainWindow.AGMainCalendarWidget import Ui_Form
from datetime import date
import datetime
import dateutils
from calendar import monthrange
from Objects.Event import getEventsDictionary, getEventTypeColour
from WindowObjects.CalendarCellWidget import CalendarCellWidget


class MainCalendarWidget(QtWidgets.QWidget):
    clickedDaySignal = QtCore.pyqtSignal()
    dayLabelList: List[CalendarCellWidget] = list()
    weekDaysLabelList: List[CalendarCellWidget] = list()
    weekNumbersLabelList: List[CalendarCellWidget] = list() # zero element is column name, not week number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mainCalendarWidget = Ui_Form()
        self.mainCalendarWidget.setupUi(self)
        self.dateOnDateBar = date.today()
        self.init_ui()

    def init_ui(self) -> None:
        self.setWeekDaysAppearance()
        self.setWeekNumbersAppearance()
        # self.setAdditionalCalendarAppearance()
        self.setDaysWidgetAppearance()
        self.generateCalendarDays()
        self.mainCalendarWidget.calendarGridLayout.setSpacing(1)

        for i in range(1, 43):
            self.dayLabelList.append(getattr(self.mainCalendarWidget, 'day_' + str(i)))
        for label in self.dayLabelList:
            label.setClicked(self.getLabelNameFromCalendarDayLabel)

        for i in range(1, 8):
            self.weekDaysLabelList.append(getattr(self.mainCalendarWidget, 'weekDay' + str(i)))
        for i in range(0, 7):
            self.weekNumbersLabelList.append(getattr(self.mainCalendarWidget, 'weekNumber' + str(i)))

    def setWeekDaysAppearance(self):
        for label in self.weekDaysLabelList:
            label.setBackgroundColor("#bfbfbf")
            label.setEventTypeDotRatio(0)
            label.setFontAppearance('Times', QtGui.QFont.Normal, 8.1)

    def setWeekNumbersAppearance(self):
        for label in self.weekNumbersLabelList:
            label.setBackgroundColor("#bfbfbf")
            label.setEventTypeDotRatio(0)
            label.setFontAppearance('Times', QtGui.QFont.Normal, 7)

    def setDaysWidgetAppearance(self):
        for label in self.dayLabelList:
            label.setEventTypeDotRatio(10)
            label.setFontAppearance('Times', QtGui.QFont.Normal,  3.5)

    # def setAdditionalCalendarAppearance(self):
    #     self.mainCalendarWidget.weekNumber0.setBackgroundColor("#bfbfbf")
    #     self.mainCalendarWidget.weekNumber0.setEventTypeDotRatio(0)
    #     self.mainCalendarWidget.weekNumber0.setFontAppearance('Times', QtGui.QFont.Normal, 8.1)
    #     self.mainCalendarWidget.calendarGridLayout.setSpacing(1)

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
                # newDate = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month,
                #                             self.dateOnDateBar.day) - dateutils.relativedelta(months=1)
                # prevMonthRange = int(monthrange(newDate.year, newDate.month)[1])
                # getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setText')(
                #     str(prevMonthRange - firstWeekDayOfMonth + i + 1))
                # getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setBackgroundColor')("#cce6ff")
                #
                # if str(newDate.year) in getEventsDictionary()["events"]:
                #     if str(newDate.month) in getEventsDictionary()["events"][str(newDate.year)]:
                #         if str(prevMonthRange - firstWeekDayOfMonth + i + 1) in \
                #                 getEventsDictionary()["events"][str(newDate.year)][str(newDate.month)]:
                #             for event in getEventsDictionary()["events"][str(newDate.year)][str(newDate.month)][
                #                 str(prevMonthRange - firstWeekDayOfMonth + i + 1)]:
                #                 getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'addEventColor')(
                #                     getEventTypeColour(event["type"]))

                self.generatePrevMonth(i, firstWeekDayOfMonth, "#cce6ff")

            elif firstWeekDayOfMonth <= i <= currentMonthRange + firstWeekDayOfMonth - 1:
                # getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setText')(str(i - firstWeekDayOfMonth + 1))
                # getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setBackgroundColor')("#80bfff")
                #
                # if str(self.dateOnDateBar.year) in getEventsDictionary()["events"]:
                #     if str(self.dateOnDateBar.month) in getEventsDictionary()["events"][str(self.dateOnDateBar.year)]:
                #         if str(i - firstWeekDayOfMonth + 1) in \
                #                 getEventsDictionary()["events"][str(self.dateOnDateBar.year)][
                #                     str(self.dateOnDateBar.month)]:
                #             for event in getEventsDictionary()["events"][str(self.dateOnDateBar.year)][
                #                 str(self.dateOnDateBar.month)][str(i - firstWeekDayOfMonth + 1)]:
                #                 getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'addEventColor')(
                #                     getEventTypeColour(event["type"]))

                self.generateCurrentMonth(i, firstWeekDayOfMonth, "#80bfff")

            else:
                # getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setText')(
                #     str(i - firstWeekDayOfMonth - currentMonthRange + 1))
                # getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setBackgroundColor')("#cce6ff")
                #
                # if str(self.dateOnDateBar.year) in getEventsDictionary()["events"]:
                #     if str(self.dateOnDateBar.month + 1) in getEventsDictionary()["events"][
                #         str(self.dateOnDateBar.year)]:
                #         if str(i - firstWeekDayOfMonth - currentMonthRange + 1) in \
                #                 getEventsDictionary()["events"][str(self.dateOnDateBar.year)][
                #                     str(self.dateOnDateBar.month + 1)]:
                #             for event in getEventsDictionary()["events"][str(self.dateOnDateBar.year)][
                #                 str(self.dateOnDateBar.month + 1)][
                #                 str(i - firstWeekDayOfMonth - currentMonthRange + 1)]:
                #                 getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'addEventColor')(
                #                     getEventTypeColour(event["type"]))

                self.generateNextMonth(i, firstWeekDayOfMonth, currentMonthRange, "#cce6ff")

        if self.dateOnDateBar.year == date.today().year and self.dateOnDateBar.month == date.today().month:
            self.distinguishTodayDate()
        else:
            for i in range(1, 43):
                getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setFontAppearance')('Times',  QtGui.QFont.Normal, 3.5)

        self.setWeekNumbers()


    def generatePrevMonth(self, labelIndex, firstWeekDayOfMonth, monthColour):

        newDate = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month,
                                    self.dateOnDateBar.day) - dateutils.relativedelta(months=1)
        prevMonthRange = int(monthrange(newDate.year, newDate.month)[1])
        getattr(getattr(self.mainCalendarWidget, 'day_' + str(labelIndex)), 'setText')(
            str(prevMonthRange - firstWeekDayOfMonth + labelIndex + 1))
        getattr(getattr(self.mainCalendarWidget, 'day_' + str(labelIndex)), 'setBackgroundColor')(monthColour)

        if str(newDate.year) in getEventsDictionary()["events"]:
            if str(newDate.month) in getEventsDictionary()["events"][str(newDate.year)]:
                if str(prevMonthRange - firstWeekDayOfMonth + labelIndex + 1) in \
                        getEventsDictionary()["events"][str(newDate.year)][str(newDate.month)]:
                    for event in getEventsDictionary()["events"][str(newDate.year)][str(newDate.month)][
                        str(prevMonthRange - firstWeekDayOfMonth + labelIndex + 1)]:
                        getattr(getattr(self.mainCalendarWidget, 'day_' + str(labelIndex)), 'addEventColor')(
                            getEventTypeColour(event["type"]))

    def generateCurrentMonth(self, labelIndex, firstWeekDayOfMonth, monthColour):

        getattr(getattr(self.mainCalendarWidget, 'day_' + str(labelIndex)), 'setText')(str(labelIndex - firstWeekDayOfMonth + 1))
        getattr(getattr(self.mainCalendarWidget, 'day_' + str(labelIndex)), 'setBackgroundColor')(monthColour)

        if str(self.dateOnDateBar.year) in getEventsDictionary()["events"]:
            if str(self.dateOnDateBar.month) in getEventsDictionary()["events"][str(self.dateOnDateBar.year)]:
                if str(labelIndex - firstWeekDayOfMonth + 1) in \
                        getEventsDictionary()["events"][str(self.dateOnDateBar.year)][
                            str(self.dateOnDateBar.month)]:
                    for event in getEventsDictionary()["events"][str(self.dateOnDateBar.year)][
                        str(self.dateOnDateBar.month)][str(labelIndex - firstWeekDayOfMonth + 1)]:
                        getattr(getattr(self.mainCalendarWidget, 'day_' + str(labelIndex)), 'addEventColor')(
                            getEventTypeColour(event["type"]))

    def generateNextMonth(self, labelIndex, firstWeekDayOfMonth, currentMonthRange, monthColour):

        getattr(getattr(self.mainCalendarWidget, 'day_' + str(labelIndex)), 'setText')(
            str(labelIndex - firstWeekDayOfMonth - currentMonthRange + 1))
        getattr(getattr(self.mainCalendarWidget, 'day_' + str(labelIndex)), 'setBackgroundColor')(monthColour)

        if str(self.dateOnDateBar.year) in getEventsDictionary()["events"]:
            if str(self.dateOnDateBar.month + 1) in getEventsDictionary()["events"][
                str(self.dateOnDateBar.year)]:
                if str(labelIndex - firstWeekDayOfMonth - currentMonthRange + 1) in \
                        getEventsDictionary()["events"][str(self.dateOnDateBar.year)][
                            str(self.dateOnDateBar.month + 1)]:
                    for event in getEventsDictionary()["events"][str(self.dateOnDateBar.year)][
                        str(self.dateOnDateBar.month + 1)][
                        str(labelIndex - firstWeekDayOfMonth - currentMonthRange + 1)]:
                        getattr(getattr(self.mainCalendarWidget, 'day_' + str(labelIndex)), 'addEventColor')(
                            getEventTypeColour(event["type"]))

    def distinguishTodayDate(self):
        firstWeekDayOfMonth = int(
            datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, 1).strftime('%w'))

        if firstWeekDayOfMonth == 0:
            firstWeekDayOfMonth = 7

        todayIndex = date.today().day + firstWeekDayOfMonth - 1
        getattr(getattr(self.mainCalendarWidget, 'day_' + str(todayIndex)), 'setBackgroundColor')("#339966")
        getattr(getattr(self.mainCalendarWidget, 'day_' + str(todayIndex)), 'setFontAppearance')('Times', QtGui.QFont.Bold, 3.5)

    def setWeekNumbers(self):
        firstSundayDate = date(self.dateOnDateBar.year, self.dateOnDateBar.month,
                               int(self.mainCalendarWidget.day_7.getText()))

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

        self.mainCalendarWidget.layoutWidget.setGeometry(0, 0, self.width(), self.height())
        self.resize(self.width(), self.height())
        self.mainCalendarWidget.calendarGridLayout.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.updateWidgetSize()

    # def changeMonthToPrev(self):
    #
    #     self.dateOnDateBar = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month,
    #                                            self.dateOnDateBar.day) - dateutils.relativedelta(months=1)
    #     for i in range(1, 43):
    #         getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setEventColorList')([])
    #     self.generateCalendarDays()
    #     self.distinguishClickedDay()
    #
    # def changeMonthToNext(self):
    #
    #     self.dateOnDateBar = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month,
    #                                            self.dateOnDateBar.day) + dateutils.relativedelta(months=1)
    #     for i in range(1, 43):
    #         getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setEventColorList')([])
    #     self.generateCalendarDays()
    #     self.distinguishClickedDay()

    def changeDate(self, calendarType: str, changeType: str):
        offset = 1 if changeType == "next" else -1
        dateOffset = 0
        if calendarType == "day":
            dateOffset = dateutils.relativedelta(days=offset)
        if calendarType == "week":
            dateOffset = dateutils.relativedelta(weeks=offset)
        if calendarType == "month":
            dateOffset = dateutils.relativedelta(months=offset)


        self.dateOnDateBar = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month,
                                               self.dateOnDateBar.day) + dateOffset

        if calendarType == "month":
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

        for i in range(1, 43):
            getattr(getattr(self.mainCalendarWidget, 'day_' + str(i)), 'setEventColorList')([])

        self.generateCalendarDays()

    @QtCore.pyqtSlot()
    def updateEventTypeColours(self):
        self.generateCalendarDays()
