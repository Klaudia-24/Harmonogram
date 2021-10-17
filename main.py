from PyQt5 import QtWidgets

from GUI.MainWindow import MainWindow
import sys

def __main__():
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = MainWindow()
    Mainwindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()


