from PyQt5 import QtWidgets
from GUI.Autogenerated.AGNewEventTypeW import Ui_NewEventTypeWindow
from GUI.ColorSettingWindow import *


class NewTypeEventW(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.newEventTypeW = Ui_NewEventTypeWindow()
        self.newEventTypeW.setupUi(self)

        #self.dialogColorW = Window()
        #TODO move buttons clicked connect here like in MainWindow

        self.newEventTypeW.colorsPaletteButton.setStyleSheet("background-image : url(paletteImage.png);")
        self.newEventTypeW.setEventColorButton.clicked.connect(self.getColorFromDialog)

        self.newEventTypeW.savePushButton.clicked.connect(self.saveNewEventType)
        self.newEventTypeW.cancelPushButton.clicked.connect(self.cancelNewEventTypeAdding)

    def getColorFromDialog(self):
        self.color_RGB = self.dialogColorW.ReturnColor()

    def saveNewEventType(self):
        print("Save button")

    def cancelNewEventTypeAdding(self):
        print("Cancel button")

#TODO add button for adding new event type and method