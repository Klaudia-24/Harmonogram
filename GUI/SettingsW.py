from PyQt5 import QtCore, QtWidgets
from GUI.Autogenerated.AGSettingsW import Ui_Form


class SettingsW(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.settingsWindow = Ui_Form()
        self.settingsWindow.setupUi(self)
        self.init_ui()

    def init_ui(self) -> None:
        pass


def __main__():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settingsW = SettingsW()
    settingsW.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()