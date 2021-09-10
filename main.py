from PyQt5 import QtWidgets

from GUI.UI_main_window import Ui_MainWindow
import sys


def __main__():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.generateCalendarDays()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()

