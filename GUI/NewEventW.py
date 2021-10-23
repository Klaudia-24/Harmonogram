import datetime

from PyQt5 import QtCore, QtWidgets

from Lib import FileOperationMethods
from GUI.AGNewEventTypeW import Ui_NewEventTypeWindow
from Objects.Event import *
from Lib.FileOperationMethods import writeToJsonFile
from Objects.Event import eventsDictionary

from GUI.AGNewEventW3 import Ui_Form

class NewEventW(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.newEventW = Ui_Form()
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

        if self.newEventW.allDayEventRadioButton.isChecked():
            timeFrom = datetime.datetime.strptime("00:00", '%H:%M')
            timeTo = datetime.datetime.strptime("23:59", '%H:%M')
            eventDuration = EventDuration(True, timeFrom, timeTo)
            event = Event(datetime.datetime(self.newEventW.dateEdit.date().year(), self.newEventW.dateEdit.date().month(), self.newEventW.dateEdit.date().day()),
                          self.newEventW.eventTitlePlainTextEdit.toPlainText(), self.newEventW.eventDescriptionPlaneTextEdit.toPlainText(),
                          self.newEventW.eventLocalizationPlainTextEdit.toPlainText(), eventDuration,
                          str(self.newEventW.eventTypeComboBox.currentText()), str(self.newEventW.remindBeforeComboBox.currentText()))

            eventHash = hash(event)

            eventDict = {
                "eventId": str(eventHash),
                "eventYear": self.newEventW.dateEdit.date().year(),
                "eventMonth": self.newEventW.dateEdit.date().month(),
                "eventDay": self.newEventW.dateEdit.date().day(),
                "allDayEvent": int(eventDuration.getIsAllDayEvent()),
                "timeFromHour": 0,
                "timeFromMinute": 0,
                "timeToHour": 23,
                "timeToMinute": 59,
                "type": str(self.newEventW.eventTypeComboBox.currentText()),
                "title": self.newEventW.eventTitlePlainTextEdit.toPlainText(),
                "description": self.newEventW.eventDescriptionPlaneTextEdit.toPlainText(),
                "localization": self.newEventW.eventLocalizationPlainTextEdit.toPlainText(),
                "reminder": str(self.newEventW.remindBeforeComboBox.currentText())
            }

        if self.newEventW.setDurationEventRadioButton.isChecked():

            timeFrom = datetime.datetime.strptime(str(self.newEventW.timeFromEdit.time().hour()) + ":" + str(self.newEventW.timeFromEdit.time().minute()), '%H:%M')
            timeTo = datetime.datetime.strptime(str(self.newEventW.timeToEdit.time().hour()) + ":" + str(self.newEventW.timeToEdit.time().minute()), '%H:%M')

            eventDuration = EventDuration(False, timeFrom, timeTo)
            event = Event(datetime.datetime(self.newEventW.dateEdit.date().year(), self.newEventW.dateEdit.date().month(), self.newEventW.dateEdit.date().day()),
                          self.newEventW.eventTitlePlainTextEdit.toPlainText(), self.newEventW.eventDescriptionPlaneTextEdit.toPlainText(),
                          self.newEventW.eventLocalizationPlainTextEdit.toPlainText(), eventDuration,
                          str(self.newEventW.eventTypeComboBox.currentText()), str(self.newEventW.remindBeforeComboBox.currentText()))

            eventHash = hash(event)

            eventDict = {
                "eventId": str(eventHash),
                "eventYear": self.newEventW.dateEdit.date().year(),
                "eventMonth": self.newEventW.dateEdit.date().month(),
                "eventDay": self.newEventW.dateEdit.date().day(),
                "allDayEvent": int(eventDuration.getIsAllDayEvent()),
                "timeFromHour": self.newEventW.timeFromEdit.time().hour(),
                "timeFromMinute": self.newEventW.timeFromEdit.time().minute(),
                "timeToHour": self.newEventW.timeToEdit.time().hour(),
                "timeToMinute": self.newEventW.timeToEdit.time().minute(),
                "type": str(self.newEventW.eventTypeComboBox.currentText()),
                "title": self.newEventW.eventTitlePlainTextEdit.toPlainText(),
                "description": self.newEventW.eventDescriptionPlaneTextEdit.toPlainText(),
                "localization": self.newEventW.eventLocalizationPlainTextEdit.toPlainText(),
                "reminder": str(self.newEventW.remindBeforeComboBox.currentText())
            }
        return eventDict

    def confirmAddingNewEvent(self) -> None:
        """Used for 'Confirm' button. Adds new event to the events dictionary,
        saves the event dictionary to the JSON file and closes the new event window."""

        eventsDictionary["events"].append(self.changeEventToJsonFile())
        writeToJsonFile("./events.json", eventsDictionary)
        self.closeWindow()

