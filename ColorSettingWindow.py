from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from Event import eventsTypesColorsDict


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.dialog = QColorDialog(self)

    def ReturnColor(self):
        return self.dialog.getColor()