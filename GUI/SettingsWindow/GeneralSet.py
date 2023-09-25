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

    def getCurrentData(self):
        pass

def __main__():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    generalSet = GeneralSet()
    generalSet.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    __main__()