from PyQt5 import QtWidgets
from GUI.Autogenerated.SettingsWindow.AGGeneralSet import Ui_Form
from Objects.AppSettings import GeneralSettings

class GeneralSet(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.generalSet = Ui_Form()
        self.generalSet.setupUi(self)
        self.init_ui()

    def init_ui(self) -> None:
        pass

    def setCurrentData(self, settingsDict):
        self.generalSet.windowsBackColourBtn.setStyleSheet(f"background-color:{settingsDict['windowBackColour']}")
        self.generalSet.navBtnStyleComboBox.clear()
        self.generalSet.navBtnStyleComboBox.addItem(settingsDict['navBtnStyle'])
        self.generalSet.eventsFilePathPlainTextEdit.setPlainText(settingsDict['eventsFilePath'])
        self.generalSet.dateBarFontColourBtn.setStyleSheet(f"background-color:{settingsDict['dateBarFontColour']}")
        self.generalSet.dateBarFontSizeSpinBox.setValue(settingsDict['dateBarFontSize'])
        self.generalSet.dateBarFontBoldCheckBox.setChecked(bool(settingsDict['dateBarFontBold']))

    def getCurrentData(self):
        return GeneralSettings(self.generalSet.windowsBackColourBtn.palette().window().color().name(),
                               self.generalSet.navBtnStyleComboBox.currentText(),
                               self.generalSet.eventsFilePathPlainTextEdit.toPlainText(),
                               self.generalSet.dateBarFontColourBtn.palette().window().color().name(),
                               self.generalSet.dateBarFontSizeSpinBox.value(),
                               self.generalSet.dateBarFontBoldCheckBox.isChecked()
                               )

def __main__():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    generalSet = GeneralSet()
    generalSet.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    __main__()