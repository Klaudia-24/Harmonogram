from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class QLabel_alterada(QLabel):
    clicked=pyqtSignal()

    def mousePressEvent(self, ev):
        self.clicked.emit()