from PyQt5 import QtWidgets
from GUI.Autogenerated.SettingsWindow.AGEventTypesSet import Ui_Form
from Objects.Event import eventTypesDictionary
from GUI.MainWindow.ColorSettingWindow import *

import logging
logger = logging.getLogger('eventTypeSetLogger')

class EventTypesSet(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.eventTypesSet = Ui_Form()
        self.eventTypesSet.setupUi(self)
        self.dialogColorW = Window()
        self.init_ui()

        self.eventTypesSet.addTypeBtn.setStyleSheet("QPushButton {"

                                                     "border-radius: 6px;"
                                                     "  background-image: url(./WindowObjects/Resources/addImage_24.png);"
                                                     "background-repeat:no-repeat;"
                                                     " background-position:center;"
                                                     "  min-width: 30px;"
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
        self.eventTypesSet.removeTypeBtn.setStyleSheet("QPushButton {"

                                                          "border-radius: 6px;"
                                                          "  background-image: url(./WindowObjects/Resources/trashImage_24.png);"
                                                          "background-repeat:no-repeat;"
                                                          " background-position:center;"
                                                          "  min-width: 40px;"
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
        self.eventTypesSet.editTypeBtn.setStyleSheet("QPushButton {"

                                                     "border-radius: 6px;"
                                                     "  background-image: url(./WindowObjects/Resources/editImage_24.png);"
                                                     "background-repeat:no-repeat;"
                                                     " background-position:center;"
                                                     "  min-width: 40px;"
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

        self.eventTypesSet.groupBox.setStyleSheet("QGroupBox#groupBox { border: 1px solid #8c8c8c ;}")

        self.eventTypesSet.typesListWidget.addItems(eventTypesDictionary['eventTypes'].keys())
        self.eventTypesSet.typesListWidget.clicked.connect(self.setSelectedItemData)

        self.eventTypesSet.addTypeBtn.setEnabled(False)
        self.eventTypesSet.removeTypeBtn.setEnabled(False)
        self.eventTypesSet.editTypeBtn.setEnabled(False)
        # gray scale w css / online gray


    def init_ui(self) -> None:
        pass

    def getColorFromDialog(self):
        self.color_RGB = self.dialogColorW.ReturnColor().name()

    def setSelectedItemData(self):
        currentTypeName = self.eventTypesSet.typesListWidget.currentItem().text()
        # logger.debug(currentTypeName)
        # logger.debug(eventTypesDictionary['eventTypes'][currentTypeName])
        self.eventTypesSet.typeNameTextEdit.setText(currentTypeName)
        self.eventTypesSet.typeColourBtn.setStyleSheet(f"background-color:{eventTypesDictionary['eventTypes'][currentTypeName]}")

def __main__():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    eventTypesSet = EventTypesSet()
    eventTypesSet.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    __main__()