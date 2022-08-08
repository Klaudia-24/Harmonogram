from PyQt5 import QtWidgets

from GUI.MainWindow.MainWindow import MainWindow
import sys
import logging.config

logging.config.fileConfig('logging.config') # only one import of this file
logger = logging.getLogger('main')

def __main__():
    # if we want to run file as standalone
    # logging.config.fileConfig('logging.config')
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = MainWindow()
    Mainwindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()