

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen


class CalendarDayWidget(QtWidgets.QWidget):
    __eventColorList = []
    __labelText = None
    __whenClicked = None
    __shapeSize = 50
    __backgroundColor = None

    def __init__(self, *args, **kwargs):
        super(CalendarDayWidget, self).__init__(*args, **kwargs)
        # self.eventColorList = {"item": "black"}
        # self.layout = QtWidgets.QVBoxLayout()
        # self.label = QtWidgets.QLabel("Tekst")
        # self.layout.addWidget(self.label)
        # self.layout.setAlignment(Qt.AlignCenter)
        # self.setLayout(self.layout)
        # self.backgroundColor = "blue"
        #self.setStyleSheet("background-color: blue;")

    def setClicked(self, whenClicked):
        self.__whenClicked = whenClicked

    def mousePressEvent(self, event):
        if self.__whenClicked is None:
            return
        self.__whenClicked(event, self.objectName())
    # TODO poprawic na przekazywanie jakiejkolwiek funkcji.

    # def changeTextAlignment(self, alignment: Qt.Alignment):
    #     """Change the alignment of the label"""
    #     self.layout.setAlignment(alignment)

    def setText(self, text: str):
        """Set text for the label"""
        self.__labelText = text

    def addEventColor(self, color):
        self.__eventColorList.append(color)

    def clearEventColorList(self):
        self.__eventColorList.clear()

    def refresh(self):
        self.update()

    def setBackgroundColor(self, color):
        #self.label.setStyleSheet(f"background-color: {color}")
        self.__backgroundColor = color
        self.refresh()

    def setWidgetSize(self, width, height):
        self.setMaximumSize(width, height)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        backgroundBrush = QtGui.QBrush()
        brush = QtGui.QBrush()
        backgroundBrush.setColor(QtGui.QColor(self.__backgroundColor))
        backgroundBrush.setStyle(Qt.SolidPattern)
        painter.fillRect(QtCore.QRect(0, 0, painter.device().width(), painter.device().height()), backgroundBrush)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.setFont(QtGui.QFont('Times', (painter.device().height()-2*self.__shapeSize)//2, QtGui.QFont.Normal))
        painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, self.__labelText)

        colorIndex = 0
        spaceOffset = 10

        if (self.__shapeSize+spaceOffset)*len(self.__eventColorList) > painter.device().width():
            spaceSize = (painter.device().width() - spaceOffset - self.__shapeSize) // (len(self.__eventColorList))
        else:
            spaceSize = self.__shapeSize+spaceOffset

        for i in self.__eventColorList:

            painter.setPen(QPen(QtGui.QColor(i), 5, Qt.SolidLine))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(i), Qt.SolidPattern))
            painter.drawEllipse(spaceSize*colorIndex+spaceOffset, 10, self.__shapeSize, self.__shapeSize)
            colorIndex += 1


def __main__():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = CalendarDayWidget()

    Mainwindow.setBackgroundColor("#FF0000")
    Mainwindow.setText("10")
    Mainwindow.addEventColor("#3366FF")
    Mainwindow.addEventColor("#006600")
    Mainwindow.addEventColor("#3366FF")
    Mainwindow.addEventColor("#006600")
    Mainwindow.addEventColor("#3366FF")
    Mainwindow.addEventColor("#006600")
    Mainwindow.setWidgetSize(600, 300)

    Mainwindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()
