import dateutils

from GUI.Autogenerated.MainWindow.AGMainW import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from GUI.MainWindow import NewEventW
from GUI.MainWindow.DayCalendarWidget import DayCalendarWidget
from GUI.SettingsWindow.SettingsW import SettingsW
from GUI.MainWindow.WeekCalendarWidget import WeekCalendarWidget
from Objects.Event import loadEventsList, loadEventTypesList, Event
from GUI.MainWindow.MonthCalendarWidget import MainCalendarWidget
from GUI.MainWindow.EventDataW import EventDataW


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadEventsList()
        loadEventTypesList()
        self.mainCalendarWidget = MainCalendarWidget()
        self.dayCalendarWidget = DayCalendarWidget()
        self.weekCalendarWidget = WeekCalendarWidget()
        self.settingsWindow = SettingsW()
        self.eventDataWindow = EventDataW()
        self.ui.stackedWidget.addWidget(self.mainCalendarWidget)
        self.ui.stackedWidget.addWidget(self.dayCalendarWidget)
        self.ui.stackedWidget.addWidget(self.weekCalendarWidget)
        self.ui_newEventWindow = NewEventW.NewEventW()
        self.ui.newEventButton.clicked.connect(self.openNewEventWindow)
        self.ui.prevButton.clicked.connect(self.setDateInBarToPrev)
        self.ui.nextButton.clicked.connect(self.setDateInBarToNext)
        self.setDateInBar(str(self.mainCalendarWidget.dateOnDateBar.day),
                          self.mainCalendarWidget.dateOnDateBar.strftime("%B"),
                          str(self.mainCalendarWidget.dateOnDateBar.year))
        self.mainCalendarWidget.clickedDaySignal.connect(self.setClickedDateInBar)
        self.ui_newEventWindow.newEventAddedSignal.connect(self.mainCalendarWidget.updateEventTypeColours)

        self.ui.dayCalendarButton.clicked.connect(self.switchToTheDayCalendar)
        self.ui.monthCalendarButton.clicked.connect(self.switchToTheMonthCalendar)
        self.ui.weekCalendarButton.clicked.connect(self.switchToTheWeekCalendar)

        self.setMinimumSize(1300, 600)
        self.ui.settingsButton.setStyleSheet("QPushButton {"

                                                             "border-radius: 6px;"
                                                             "  background-image: url(./WindowObjects/Resources/settingsImage.png);"
                                                             "background-repeat:no-repeat;"
                                                             " background-position:center;"
                                                             "  min-width: 60px;"
                                                             "}"

                                                             "QPushButton:pressed {"
                                                             "   background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,"
                                                             " stop: 0 #dadbde, stop: 1 #f6f7fa);"
                                                             "}"

                                                             "QPushButton:flat {"
                                                             "   border: none; /* no border for a flat push button */"
                                                             "}"

                                                             "QPushButton:default {"
                                                             "    border-color: navy; /* make the default button prominent */"
                                                             "}")
        self.ui.settingsButton.clicked.connect(self.openSettingsWindow)

        self.eventDataWidget = DayCalendarWidget()
        self.dayCalendarWidget.dayCalendar.eventClickedSignal.connect(self.eventDataShow)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.mainCalendarWidget.updateWidgetSize()

    def setDateInBar(self, day: str, month: str, year: str):
        # self.ui.dayFromDate.setText(str(self.mainCalendarWidget.dateOnDateBar.day))
        # self.ui.monthFromDate.setText(self.mainCalendarWidget.dateOnDateBar.strftime("%B"))
        # self.ui.yearFromDate.setText(str(self.mainCalendarWidget.dateOnDateBar.year))

        self.ui.dayFromDate.setText(day)
        self.ui.monthFromDate.setText(month)
        self.ui.yearFromDate.setText(year)

    @QtCore.pyqtSlot()
    def setClickedDateInBar(self):
        self.setDateInBar(str(self.mainCalendarWidget.dateOnDateBar.day),
                          self.mainCalendarWidget.dateOnDateBar.strftime("%B"),
                          str(self.mainCalendarWidget.dateOnDateBar.year))

    def getDateOnDateBar(self):
        return self.dateOnDateBar

    def setDateInBarToPrev(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            self.mainCalendarWidget.changeDate("month", "prev")
            self.setDateInBar(str(self.mainCalendarWidget.dateOnDateBar.day),
                              self.mainCalendarWidget.dateOnDateBar.strftime("%B"),
                              str(self.mainCalendarWidget.dateOnDateBar.year))
        elif self.ui.stackedWidget.currentIndex() == 1:
            self.mainCalendarWidget.changeDate("day", "prev")
            self.dayCalendarWidget.dayCalendar.setDayDataList(self.mainCalendarWidget.dateOnDateBar)
            self.setDateInBar(str(self.mainCalendarWidget.dateOnDateBar.day),
                              self.mainCalendarWidget.dateOnDateBar.strftime("%B"),
                              str(self.mainCalendarWidget.dateOnDateBar.year))

        elif self.ui.stackedWidget.currentIndex() == 2:
            weekDayFromDateBar = self.mainCalendarWidget.dateOnDateBar.weekday()
            if weekDayFromDateBar != 0:
                firstDayOfWeekDate = self.mainCalendarWidget.dateOnDateBar - dateutils.relativedelta(days=(weekDayFromDateBar + 7))
            else:
                firstDayOfWeekDate = self.mainCalendarWidget.dateOnDateBar
            self.weekCalendarWidget.weekCalendar.setWeekEventsList(firstDayOfWeekDate)
            self.mainCalendarWidget.changeDate("week", "prev")
            lastDayOfWeekDate = firstDayOfWeekDate + dateutils.relativedelta(days=6)
            self.setDateInBar(f"{firstDayOfWeekDate.day} - {lastDayOfWeekDate.day}",
                              self.mainCalendarWidget.dateOnDateBar.strftime("%B"),
                              str(self.mainCalendarWidget.dateOnDateBar.year))

    def setDateInBarToNext(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            self.mainCalendarWidget.changeDate("month", "next")
            self.setDateInBar(str(self.mainCalendarWidget.dateOnDateBar.day),
                              self.mainCalendarWidget.dateOnDateBar.strftime("%B"),
                              str(self.mainCalendarWidget.dateOnDateBar.year))
        elif self.ui.stackedWidget.currentIndex() == 1:
            self.mainCalendarWidget.changeDate("day", "next")
            self.dayCalendarWidget.dayCalendar.setDayDataList(self.mainCalendarWidget.dateOnDateBar)
            self.setDateInBar(str(self.mainCalendarWidget.dateOnDateBar.day),
                              self.mainCalendarWidget.dateOnDateBar.strftime("%B"),
                              str(self.mainCalendarWidget.dateOnDateBar.year))

        elif self.ui.stackedWidget.currentIndex() == 2:
            self.mainCalendarWidget.changeDate("week", "next")
            weekDayFromDateBar = self.mainCalendarWidget.dateOnDateBar.weekday()
            if weekDayFromDateBar != 0:
                firstDayOfWeekDate = self.mainCalendarWidget.dateOnDateBar - dateutils.relativedelta(days=weekDayFromDateBar)
            else:
                firstDayOfWeekDate = self.mainCalendarWidget.dateOnDateBar
            self.weekCalendarWidget.weekCalendar.setWeekEventsList(firstDayOfWeekDate)
            lastDayOfWeekDate = firstDayOfWeekDate + dateutils.relativedelta(days=6)
            self.ui.dayFromDate.setText(f"{firstDayOfWeekDate.day} - {lastDayOfWeekDate.day}")
            self.setDateInBar(f"{firstDayOfWeekDate.day} - {lastDayOfWeekDate.day}",
                              self.mainCalendarWidget.dateOnDateBar.strftime("%B"),
                              str(self.mainCalendarWidget.dateOnDateBar.year))

    def openNewEventWindow(self):
        self.ui_newEventWindow.setDateFromCalendar(self.mainCalendarWidget.dateOnDateBar)
        self.ui_newEventWindow.timeEditDisabled()
        self.ui_newEventWindow.clearEventDataInFormular()
        self.ui_newEventWindow.show()

    def switchToTheDayCalendar(self):
        self.dayCalendarWidget.dayCalendar.setDayDataList(self.mainCalendarWidget.dateOnDateBar)
        self.ui.stackedWidget.setCurrentIndex(1)

    def switchToTheWeekCalendar(self):
        weekDayFromDateBar = self.mainCalendarWidget.dateOnDateBar.weekday()
        if weekDayFromDateBar != 0:
            firstDayOfWeekDate = self.mainCalendarWidget.dateOnDateBar - dateutils.relativedelta(days=weekDayFromDateBar)
        else:
            firstDayOfWeekDate = self.mainCalendarWidget.dateOnDateBar
        self.weekCalendarWidget.weekCalendar.setWeekEventsList(firstDayOfWeekDate)

        lastDayOfWeekDate = firstDayOfWeekDate + dateutils.relativedelta(days=6)
        self.ui.dayFromDate.setText(f"{firstDayOfWeekDate.day} - {lastDayOfWeekDate.day}")
        self.ui.stackedWidget.setCurrentIndex(2)

    def switchToTheMonthCalendar(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.mainCalendarWidget.generateCalendarDays()
        self.mainCalendarWidget.distinguishClickedDay()

    def openSettingsWindow(self):
        self.settingsWindow.show()

    @QtCore.pyqtSlot(Event)
    def eventDataShow(self, event):
        self.eventDataWindow.setLabelsText(event)
        self.eventDataWindow.show()
