from GUI.AGMainW import Ui_MainWindow
import GUI.AGNewEventW as nw
import GUI.NewEventW as newEventW
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import datetime
import dateutils
from calendar import monthrange

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for i in range(1, 8):
            getattr(getattr(self.ui, 'weekDay' + str(i)), 'setStyleSheet')("background-color: rgb(191, 191, 191)")
            getattr(getattr(self.ui, 'weekDay' + str(i)), 'setFont')(QtGui.QFont('Times', 11, QtGui.QFont.Bold))
            getattr(getattr(self.ui, 'weekDay' + str(i)), 'setAlignment')(QtCore.Qt.AlignCenter)

        for i in range(1, 7):
            getattr(getattr(self.ui, 'weekNumber' + str(i)), 'setStyleSheet')("background-color: rgb(191, 191, 191)")
            getattr(getattr(self.ui, 'weekNumber' + str(i)), 'setFont')(QtGui.QFont('Times', 10, QtGui.QFont.Bold))
            getattr(getattr(self.ui, 'weekNumber' + str(i)), 'setAlignment')(QtCore.Qt.AlignCenter)

        for i in range(1, 43):
            getattr(getattr(self.ui, 'day_' + str(i)), 'setFont')(QtGui.QFont('Times', 9))
            getattr(getattr(self.ui, 'day_' + str(i)), 'setAlignment')(QtCore.Qt.AlignCenter)

        self.ui.weekLabel.setStyleSheet("background-color: rgb(191, 191, 191)")
        self.ui.weekLabel.setFont(QtGui.QFont('Times', 11, QtGui.QFont.Bold))
        self.ui.weekLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.calendarGridLayout.setSpacing(1)

        #self.ui.ui_newEventWindow = nw.Ui_NewEventWindow()
        self.ui.ui_newEventWindow = newEventW.NewEventW()
        self.ui.newEventButton.clicked.connect(self.openNewEventWindow)
        self.dateOnDateBar = date.today()
        self.ui.prevButton.clicked.connect(self.changeMonthToPrev)
        self.ui.nextButton.clicked.connect(self.changeMonthToNext)
        for i in range(1,43):
            getattr(getattr(self.ui, 'day_' + str(i)), 'setClicked')(self.getLabelNamefromCalendarDayLabel)

        self.generateCalendarDays()

    def setDateInBar(self):
        self.ui.dayFromDate.setText(str(self.dateOnDateBar.day))
        self.ui.monthFromDate.setText(self.dateOnDateBar.strftime("%B"))
        self.ui.yearFromDate.setText(str(self.dateOnDateBar.year))

    def getDateOnDateBar(self):
        return self.dateOnDateBar

    def generateCalendarDays(self):
        firstWeekDayOfMonth = int(
            datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, 1).strftime('%w'))
        currentMonthRange = int(monthrange(self.dateOnDateBar.year, self.dateOnDateBar.month)[1])

        if firstWeekDayOfMonth == 0:
            firstWeekDayOfMonth = 7

        for i in range(1, 43):
            if i < firstWeekDayOfMonth:
                newDate = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, self.dateOnDateBar.day) \
                          - dateutils.relativedelta(months=1)
                prevMonthRange = int(monthrange(newDate.year, newDate.month)[1])
                getattr(getattr(self.ui, 'day_' + str(i)), 'setText')(str(prevMonthRange - firstWeekDayOfMonth + i + 1))
                getattr(getattr(self.ui, 'day_' + str(i)), 'setStyleSheet')("background-color: rgb(204, 230, 255)")

            elif firstWeekDayOfMonth <= i <= currentMonthRange + firstWeekDayOfMonth - 1:
                getattr(getattr(self.ui, 'day_' + str(i)), 'setText')(str(i - firstWeekDayOfMonth + 1))
                getattr(getattr(self.ui, 'day_' + str(i)), 'setStyleSheet')("background-color: rgb(128, 191, 255)")

            else:
                getattr(getattr(self.ui, 'day_' + str(i)), 'setText')(str(i - firstWeekDayOfMonth - currentMonthRange + 1))
                getattr(getattr(self.ui, 'day_' + str(i)), 'setStyleSheet')("background-color: rgb(204, 230, 255)")

        self.setDateInBar()

        if self.dateOnDateBar.year == date.today().year and self.dateOnDateBar.month == date.today().month:
            self.distinguishDayFromDateBar()
        else:
            for i in range(1, 43):
                getattr(getattr(self.ui, 'day_' + str(i)), 'setFont')(QtGui.QFont('Times', 9, QtGui.QFont.Normal))

        self.setWeekNumbers()

    def changeMonthToPrev(self):

        self.dateOnDateBar = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month,
                                               self.dateOnDateBar.day) - dateutils.relativedelta(months=1)
        self.generateCalendarDays()

    def changeMonthToNext(self):

        self.dateOnDateBar = datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month,
                                               self.dateOnDateBar.day) + dateutils.relativedelta(months=1)
        self.generateCalendarDays()

    def distinguishDayFromDateBar(self):
        firstWeekDayOfMonth = int(
            datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, 1).strftime('%w'))

        if firstWeekDayOfMonth == 0:
            firstWeekDayOfMonth = 7

        todayIndex = date.today().day + firstWeekDayOfMonth - 1
        getattr(getattr( self.ui, 'day_' + str(todayIndex)), 'setStyleSheet')("background-color: rgb(51, 153, 102)")
        getattr(getattr( self.ui, 'day_' + str(todayIndex)), 'setFont')(QtGui.QFont('Times', 11, QtGui.QFont.Bold))

    def setWeekNumbers(self):
        firstSundayDate = date(self.dateOnDateBar.year, self.dateOnDateBar.month, int(self.ui.day_7.text()))

        for i in range(0, 6):
            number = (firstSundayDate + dateutils.relativedelta(days=7 * i)).strftime('%W').lstrip("0")
            i += 1
            getattr(getattr(self.ui, 'weekNumber' + str(i)), 'setText')(str(number))

    def openNewEventWindow(self):
        self.ui.ui_newEventWindow.setDateFromCalendar(self.dateOnDateBar)
        self.ui.ui_newEventWindow.show()

    def distinguishClickedDay(self):
        firstWeekDayOfMonth = int(
            datetime.datetime(self.dateOnDateBar.year, self.dateOnDateBar.month, 1).strftime('%w'))

        if firstWeekDayOfMonth == 0:
            firstWeekDayOfMonth = 7

        clickedIndex = self.dateOnDateBar.day + firstWeekDayOfMonth - 1
        getattr(getattr(self.ui, 'day_' + str(clickedIndex)), 'setStyleSheet')("background-color: rgb(102, 204, 153)")

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

    def getLabelNamefromCalendarDayLabel(self, event, labelName):
        button = event.button()
        modify = event.modifiers()
        if modify == QtCore.Qt.NoModifier and button == QtCore.Qt.LeftButton:
            labelObject = getattr(self.ui, labelName)
            self.setClickedDateInDateBar(labelObject.text(), labelName)
            self.distinguishClickedDay()
            return
