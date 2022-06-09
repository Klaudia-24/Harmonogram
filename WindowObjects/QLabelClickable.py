from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel


class QLabelClickable(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._whenClicked=None

    def setClicked(self, whenClicked):
        self._whenClicked = whenClicked

    def mousePressEvent(self, event):
        if self._whenClicked is None:
            return
        self._whenClicked(event, self.objectName())
