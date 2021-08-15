from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ColorSetting ")
        self.setGeometry(100, 100, 500, 400)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        dialog = QColorDialog(self)

        dialog.setCustomColor(1, Qt.red)
        dialog.setCustomColor(2, Qt.green)
        dialog.setCustomColor(3, Qt.yellow)
        dialog.setCustomColor(4, Qt.blue)
        color = dialog.customColor(4)
        graphic = QGraphicsColorizeEffect(self)
        graphic.setColor(color)
        layout = dialog.layout()
        dialog.setLayout(layout)
        dialog.setStyleSheet("background-color: rgb(204, 229, 255);")
        print(dialog.children())
        dialog.exec_()
        self.deleteLater()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())