from PyQt5 import QtWidgets
from Objects.DefaultAppSettings import createSettingsFile
from GUI.MainWindow.MainWindow import MainWindow
import sys
import logging.config

logging.config.fileConfig('logging.config') # only one import of this file
logger = logging.getLogger('main')

def __main__():
    # if we want to run file as standalone
    # logging.config.fileConfig('logging.config')

    createSettingsFile()

    # empty file???
    # if os.path.getsize(./Lib/appConfig.yaml) == 0:

    # try:
    #  # reading from config file

    # except FileNotFoundError:
    #   # create default config and read from this file

    # else:
    # #run app


    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())




if __name__ == '__main__':
    __main__()