import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont

from Lib import FileOperationMethods
from GUI.AGNewEventTypeW import Ui_NewEventTypeWindow
from Objects.Event import *
from Lib.FileOperationMethods import writeToJsonFile
from Objects.Event import eventsDictionary

import GUI.AGNewEventW_2 as agNewEventW
from GUI.AGNewEventW_2 import Ui_NewEventWindow

class NewEventW(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.newEventW = Ui_NewEventWindow()
        self.newEventW.setupUi(self)
        self.init_ui()

    def init_ui(self) -> None:
        """Contains additional setups and methods calls."""

        self.newEventW.remindBeforeComboBox.addItem("15 minutes")
        self.newEventW.remindBeforeComboBox.addItem("30 minutes")
        self.newEventW.remindBeforeComboBox.addItem("1 hour")
        self.newEventW.remindBeforeComboBox.addItem("5 hours")
        self.newEventW.remindBeforeComboBox.addItem("1 day")
        self.newEventW.addEventTypeButton.clicked.connect(self.openNewEventTypeWindow)
        self.newEventW.cancelButton.clicked.connect(self.closeWindow)
        self.newEventW.addEventButton.clicked.connect(self.confirmAddingNewEvent)
        FileOperationMethods.readFromJsonFileToDict("./events.json", eventsDictionary, "events")
        self.newEventW.setDurationEventRadioButton.setChecked(True)

    def openNewEventTypeWindow(self) -> None:
        """Create a window for adding new type of the event."""

        self.mainWindow = QtWidgets.QMainWindow()
        self.ui_newEventTypeWindow = Ui_NewEventTypeWindow()
        self.ui_newEventTypeWindow.setupUi(self.mainWindow)
        self.mainWindow.show()

    def closeWindow(self) -> None:
        """Only close the opened window, used for 'Close' buttons etc."""

        self.close()

    def setDateFromCalendar(self, date) -> None:
        """Sets date in the date edit field. The date is taken from the date bar in the main window."""

        self.newEventW.dateFromCalendar = date
        self.newEventW.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.newEventW.dateFromCalendar.year,
                                                                          self.newEventW.dateFromCalendar.month,
                                                                          self.newEventW.dateFromCalendar.day), QtCore.QTime(0, 0, 0)))

    def changeEventToJsonFile(self) -> dict:
        """Changes the event object to the JSON dictionary."""

        eventDict = {}

        if self.allDayEventRadioButton.isChecked():
            timeFrom = datetime.datetime.strptime("00:00", '%H:%M')
            timeTo = datetime.datetime.strptime("23:59", '%H:%M')
            eventDuration = EventDuration(True, timeFrom, timeTo)
            event = Event(datetime.datetime(self.dateEdit.date().year(), self.dateEdit.date().month(), self.dateEdit.date().day()),
                          self.eventTitlePlainTextEdit.toPlainText(), self.eventDescriptionPlaneTextEdit.toPlainText(),
                          self.eventLocalizationPlainTextEdit.toPlainText(), eventDuration,
                          str(self.eventTypeComboBox.currentText()), str(self.remindBeforeComboBox.currentText()))

            eventHash = hash(event)

            eventDict = {
                "eventId": str(eventHash),
                "eventYear": self.dateEdit.date().year(),
                "eventMonth": self.dateEdit.date().month(),
                "eventDay": self.dateEdit.date().day(),
                "allDayEvent": int(eventDuration.getIsAllDayEvent()),
                "timeFromHour": 0,
                "timeFromMinute": 0,
                "timeToHour": 23,
                "timeToMinute": 59,
                "type": str(self.eventTypeComboBox.currentText()),
                "title": self.eventTitlePlainTextEdit.toPlainText(),
                "description": self.eventDescriptionPlaneTextEdit.toPlainText(),
                "localization": self.eventLocalizationPlainTextEdit.toPlainText(),
                "reminder": str(self.remindBeforeComboBox.currentText())
            }

        if self.setDurationEventRadioButton.isChecked():

            timeFrom = datetime.datetime.strptime(str(self.timeFromEdit.time().hour()) + ":" + str(self.timeFromEdit.time().minute()), '%H:%M')
            timeTo = datetime.datetime.strptime(str(self.timeToEdit.time().hour()) + ":" + str(self.timeToEdit.time().minute()), '%H:%M')

            eventDuration = EventDuration(False, timeFrom, timeTo)
            event = Event(datetime.datetime(self.dateEdit.date().year(), self.dateEdit.date().month(), self.dateEdit.date().day()),
                          self.eventTitlePlainTextEdit.toPlainText(), self.eventDescriptionPlaneTextEdit.toPlainText(),
                          self.eventLocalizationPlainTextEdit.toPlainText(), eventDuration,
                          str(self.eventTypeComboBox.currentText()), str(self.remindBeforeComboBox.currentText()))

            eventHash = hash(event)

            eventDict = {
                "eventId": str(eventHash),
                "eventYear": self.dateEdit.date().year(),
                "eventMonth": self.dateEdit.date().month(),
                "eventDay": self.dateEdit.date().day(),
                "allDayEvent": int(eventDuration.getIsAllDayEvent()),
                "timeFromHour": self.timeFromEdit.time().hour(),
                "timeFromMinute": self.timeFromEdit.time().minute(),
                "timeToHour": self.timeToEdit.time().hour(),
                "timeToMinute": self.timeToEdit.time().minute(),
                "type": str(self.eventTypeComboBox.currentText()),
                "title": self.eventTitlePlainTextEdit.toPlainText(),
                "description": self.eventDescriptionPlaneTextEdit.toPlainText(),
                "localization": self.eventLocalizationPlainTextEdit.toPlainText(),
                "reminder": str(self.remindBeforeComboBox.currentText())
            }
        return eventDict

    def confirmAddingNewEvent(self) -> None:
        """Used for 'Confirm' button. Adds new event to the events dictionary,
        saves the event dictionary to the JSON file and closes the new event window."""

        eventsDictionary["events"].append(self.changeEventToJsonFile())
        writeToJsonFile("./events.json", eventsDictionary)
        self.closeWindow()

