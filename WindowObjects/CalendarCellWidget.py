

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen


class CalendarCellWidget(QtWidgets.QWidget):
    __eventColorList = []
    __labelText = None
    __whenClicked = None
    __shapeSize = 10
    __backgroundColor = None
    __fontName = None
    __fontStyle = None

    def __init__(self, *args, **kwargs):
        super(CalendarCellWidget, self).__init__(*args, **kwargs)

    def setClicked(self, whenClicked):
        self.__whenClicked = whenClicked

    def mousePressEvent(self, event):
        if self.__whenClicked is None:
            return
        self.__whenClicked(event, self.objectName())
    # TODO poprawic na przekazywanie jakiejkolwiek funkcji.

    def setText(self, text: str):
        """Set text for the label"""
        self.__labelText = text

    def getText(self):
        return self.__labelText

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

    def setFontAppearance(self, fontName):
        self.__fontName = fontName
        # self.__fontStyle = fontStyle
        self.refresh()

    def setEventShapeSize(self, shapeSize):
        self.__shapeSize = shapeSize
        self.refresh()

    def setWidgetSize(self, width, height):
        self.setMinimumSize(width, height)

    #TODO calculate shapeSize or fontSet

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        backgroundBrush = QtGui.QBrush()
        brush = QtGui.QBrush()
        backgroundBrush.setColor(QtGui.QColor(self.__backgroundColor))
        backgroundBrush.setStyle(Qt.SolidPattern)
        painter.fillRect(QtCore.QRect(0, 0, painter.device().width(), painter.device().height()), backgroundBrush)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        # print(painter.device().height())
        # painter.setFont(QtGui.QFont(self.__fontName, (painter.device().height()-2*self.__shapeSize)//2, self.__fontStyle))
        painter.setFont(QtGui.QFont(self.__fontName, (painter.device().height() - 2 * self.__shapeSize) // 2, QtGui.QFont.Normal))
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
    Mainwindow = CalendarCellWidget()

    Mainwindow.setBackgroundColor("#FF0000")
    Mainwindow.setFontAppearance('Times')
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
