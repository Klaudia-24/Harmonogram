from PyQt5 import QtWidgets
from GUI.Autogenerated.AGNewEventTypeW import Ui_NewEventTypeWindow


class NewTypeEventW(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.newEventW = Ui_NewEventTypeWindow()
        self.newEventW.setupUi(self)

    def getColorFromDialog(self):
        self.color_RGB = self.dialog.ReturnColor()
