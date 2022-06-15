

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen


class CalendarCellWidget(QtWidgets.QWidget):
    __labelText = None
    __whenClicked = None
    __shapeSize = None
    __backgroundColor = None
    __fontName = None
    __fontStyle = None
    __fontHeightRatio = None

    def __init__(self, *args, **kwargs):
        super(CalendarCellWidget, self).__init__(*args, **kwargs)
        self.__eventColorList = []

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
        if color not in self.__eventColorList:
            self.__eventColorList.append(color)

    def clearEventColorList(self):
        self.__eventColorList.clear()
        self.refresh()

    def setEventColorList(self, newList):
        self.__eventColorList = newList

    def getEventColorList(self):
        return self.__eventColorList

    def refresh(self):
        self.update()

    def setBackgroundColor(self, color):
        self.__backgroundColor = color
        self.refresh()

    def setFontAppearance(self, fontName, fontStyle, fontHeightRatio):
        self.__fontName = fontName
        self.__fontStyle = fontStyle
        self.__fontHeightRatio = fontHeightRatio
        self.refresh()

    def setEventShapeSize(self, shapeSize):
        self.__shapeSize = shapeSize
        self.refresh()

    def setWidgetSize(self, width, height):
        self.setMinimumSize(width, height)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        backgroundBrush = QtGui.QBrush()
        brush = QtGui.QBrush()
        backgroundBrush.setColor(QtGui.QColor(self.__backgroundColor))
        backgroundBrush.setStyle(Qt.SolidPattern)
        painter.fillRect(QtCore.QRect(0, 0, painter.device().width(), painter.device().height()), backgroundBrush)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        #TODO fix font size calculations
        if self.__shapeSize != 0:
            painter.setFont(QtGui.QFont(self.__fontName, ((painter.device().height()-2*self.__shapeSize)//self.__fontHeightRatio), self.__fontStyle))
        else:
            painter.setFont(QtGui.QFont(self.__fontName, (painter.device().width()) // self.__fontHeightRatio, self.__fontStyle))
        # painter.setFont(QtGui.QFont(self.__fontName, (painter.device().height() - 2 * self.__shapeSize) // 2, QtGui.QFont.Normal))
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