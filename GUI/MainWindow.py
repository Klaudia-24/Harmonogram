from GUI.UI_main_window import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.generateCalendarDays()