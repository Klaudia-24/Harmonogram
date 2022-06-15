from PyQt5 import QtCore, QtWidgets
from GUI.NewEventTypeW import NewTypeEventW
from GUI.Autogenerated.AGNewEventW import Ui_Form
from Objects.Event import addEventToList, saveEventList, getEventTypesList, EventDuration, Event


class NewEventW(QtWidgets.QWidget):

    newEventAddedSignal = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.newEventW = Ui_Form()
        self.newEventW.setupUi(self)
        self.ui_newEventTypeWindow = NewTypeEventW()
        self.init_ui()

    def init_ui(self) -> None:
        """Contains additional setups and methods calls."""

        self.newEventW.remindBeforeComboBox.addItem("15 minutes")
        self.newEventW.remindBeforeComboBox.addItem("30 minutes")
        self.newEventW.remindBeforeComboBox.addItem("1 hour")
        self.newEventW.remindBeforeComboBox.addItem("5 hours")
        self.newEventW.remindBeforeComboBox.addItem("1 day")
        self.newEventW.addEventTypeButton.clicked.connect(self.openNewEventTypeWindow)
        self.newEventW.allDayEventRadioButton.clicked.connect(self.timeEditDisabled)
        self.newEventW.setDurationEventRadioButton.clicked.connect(self.timeEditEnabled)
        self.newEventW.cancelButton.clicked.connect(self.closeWindow)
        self.newEventW.addEventButton.clicked.connect(self.confirmAddingNewEvent)
        self.addEventTypesToComboBox()
        self.ui_newEventTypeWindow.submitted.connect(self.updateEventTypeComboBox)

    def openNewEventTypeWindow(self) -> None:
        """Create a window for adding new type of the event."""

        self.ui_newEventTypeWindow.show()

    def closeWindow(self) -> None:
        """Only close the opened window, used for 'Close' buttons etc."""

        self.close()

    def setDateFromCalendar(self, date) -> None:
        """Sets date in the date edit field. The date is taken from the date bar in the main window."""

        self.newEventW.dateFromCalendar = date
        self.newEventW.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.newEventW.dateFromCalendar.year,
                                                                          self.newEventW.dateFromCalendar.month,
                                                                          self.newEventW.dateFromCalendar.day), QtCore.QTime(0, 0, 0)))

    def createNewEvent(self) -> dict:
        """Changes the event object to the JSON dictionary."""

        if self.newEventW.allDayEventRadioButton.isChecked():
            timeFrom = "00:00"
            timeTo = "23:59"
            eventDuration=EventDuration(True, timeFrom, timeTo)
        else:
            timeFrom = str(self.newEventW.timeFromEdit.time().hour())+ ":" + str(self.newEventW.timeFromEdit.time().minute())
            timeTo = str(self.newEventW.timeToEdit.time().hour()) + ":" + str(self.newEventW.timeToEdit.time().minute())
            eventDuration = EventDuration(False, timeFrom, timeTo)

        event = Event(
            eventDuration=eventDuration,
            type=str(self.newEventW.eventTypeComboBox.currentText()),
            title=self.newEventW.eventTitlePlainTextEdit.toPlainText(),
            description=self.newEventW.eventDescriptionPlaneTextEdit.toPlainText(),
            localization=self.newEventW.eventLocalizationPlainTextEdit.toPlainText(),
            reminder=str(self.newEventW.remindBeforeComboBox.currentText())
        )
        return event.to_dict()

    def confirmAddingNewEvent(self) -> None:
        """Used for 'Confirm' button. Adds new event to the events' dictionary,
        saves the event dictionary to the JSON file and closes the new event window."""

        year = str(self.newEventW.dateEdit.date().year())
        month = str(self.newEventW.dateEdit.date().month())
        day = str(self.newEventW.dateEdit.date().day())

        addEventToList(year, month, day, self.createNewEvent())
        saveEventList()
        self.newEventAddedSignal.emit()
        self.closeWindow()

    def addEventTypesToComboBox(self):
        for element in getEventTypesList():
            self.newEventW.eventTypeComboBox.addItem(element)

    @QtCore.pyqtSlot(str)
    def updateEventTypeComboBox(self, newEventType: str):
        self.newEventW.eventTypeComboBox.addItem(newEventType)

    def clearEventDataInFormular(self):
        self.newEventW.eventTitlePlainTextEdit.setPlainText("")
        self.newEventW.eventDescriptionPlaneTextEdit.setPlainText("")
        self.newEventW.eventLocalizationPlainTextEdit.setPlainText("")
        self.newEventW.allDayEventRadioButton.setChecked(True)
        self.newEventW.setDurationEventRadioButton.setChecked(False)
        self.newEventW.remindBeforeComboBox.setCurrentIndex(0)
        self.newEventW.eventTypeComboBox.setCurrentIndex(0)

    def timeEditDisabled(self):
        self.newEventW.timeFromEdit.setDisabled(True)
        self.newEventW.timeToEdit.setDisabled(True)

    def timeEditEnabled(self):
        self.newEventW.timeFromEdit.setDisabled(False)
        self.newEventW.timeToEdit.setDisabled(False)
