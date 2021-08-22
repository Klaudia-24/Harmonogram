from PyQt5.QtWidgets import *

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.dialog = QColorDialog(self)

    def ReturnColor(self):
        return self.dialog.getColor()