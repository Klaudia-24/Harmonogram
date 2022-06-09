from PyQt5 import QtWidgets
from GUI.Autogenerated.AGNewEventTypeW import Ui_NewEventTypeWindow
from GUI.ColorSettingWindow import *
from Objects.Event import addEventTypeToList, saveEventTypesList
from PyQt5 import QtCore


class NewTypeEventW(QtWidgets.QWidget):
    submitted = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.newEventTypeW = Ui_NewEventTypeWindow()
        self.newEventTypeW.setupUi(self)

        self.dialogColorW = Window()

        self.newEventTypeW.colorsPaletteButton.setStyleSheet("QPushButton {"
                                                             
                                                             "border-radius: 6px;"
                                                             "  background-image: url(./WindowObjects/paletteImage.png);"
                                                             "background-repeat:no-repeat;"
                                                             " background-position:center;"
                                                             "  min-width: 80px;"
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

        self.newEventTypeW.colorsPaletteButton.clicked.connect(self.getColorFromDialog)

        self.newEventTypeW.savePushButton.clicked.connect(self.saveNewEventType)
        self.newEventTypeW.cancelPushButton.clicked.connect(self.cancelNewEventTypeAdding)

    def getColorFromDialog(self):
        self.color_RGB = self.dialogColorW.ReturnColor().name()

    def changeEventTypeJsonFile(self):

        eventTypeDict = {self.newEventTypeW.eventTypeNamePlainText.toPlainText(): self.color_RGB}
        return eventTypeDict

    def saveNewEventType(self):
        addEventTypeToList(self.newEventTypeW.eventTypeNamePlainText.toPlainText(), self.color_RGB)
        saveEventTypesList()

        self.submitted.emit(
            self.newEventTypeW.eventTypeNamePlainText.toPlainText()
        )
        self.clearEventTypeDataInFormular()
        self.close()

    def cancelNewEventTypeAdding(self):
        self.clearEventTypeDataInFormular()
        self.close()

    def clearEventTypeDataInFormular(self):
        self.newEventTypeW.eventTypeNamePlainText.setPlainText("")
        self.color_RGB = ""


