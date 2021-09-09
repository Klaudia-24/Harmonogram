from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel


class QLabelClickable(QLabel):
    def __init__(self, whenClicked, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self._whenClicked = whenClicked

    def mousePressEvent(self, event):
        self._whenClicked(event, self.objectName())
