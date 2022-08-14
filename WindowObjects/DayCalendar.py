from datetime import datetime
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen

from Objects.Event import getEventsForDay


class DayCalendar(QtWidgets.QWidget):

    __startPoint = None
    __pointsList = []
    __shapes = []

    def __init__(self, *args, **kwargs):
        super(DayCalendar, self).__init__(*args, **kwargs)
        self.setMinimumHeight(2000)
        self.dayDataList = []
        self.calculateEventsOffsets()

    def mousePressEvent(self, event):
        self.__startPoint = event.pos()

    def mouseReleaseEvent(self, event) -> None:
        self.__shapes.append([self.__startPoint, event.pos()])
        print(self.__shapes)
        self.update()

    def setDayDataList(self, day, month, year):
        self.dayDataList = getEventsForDay(day, month, year)
        self.calculateEventsOffsets()
        self.update()

    def isOverlapping(self, event_1, event_2):
        if event_2["timeFrom"] <= event_1["timeFrom"] <= event_2["timeTo"]:
            return True
        if event_2["timeFrom"] < event_1["timeTo"] < event_2["timeTo"]:
            return True
        if event_1["timeFrom"] <= event_2["timeFrom"] <= event_1["timeTo"]:
            return True
        if event_1["timeFrom"] < event_2["timeTo"] < event_1["timeTo"]:
            return True
        return False

    def calculateEventsOffsets(self):
        for i in range(0, len(self.dayDataList)-1):
            for j in range(i+1, len(self.dayDataList)):
                if self.isOverlapping(self.dayDataList[i], self.dayDataList[j]):
                    self.dayDataList[j]["order"] += 1
                    self.dayDataList[i]["overlap"] += 1
                    self.dayDataList[j]["overlap"] += 1

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        backgroundBrush = QtGui.QBrush()
        brush = QtGui.QBrush()
        backgroundBrush.setColor(QtGui.QColor("#cfe0e8"))
        backgroundBrush.setStyle(Qt.SolidPattern)
        painter.fillRect(QtCore.QRect(0, 0, painter.device().width(), painter.device().height()), backgroundBrush)

        # brush.setColor(QtGui.QColor("#80bfff"))
        # brush.setColor(QtGui.QColor("#cc3300"))
        brush.setStyle(Qt.SolidPattern)

        if self.__shapes:
            for point in self.__shapes:
                painter.fillRect(QtCore.QRect(point[0].x(), point[0].y(), point[1].x() - point[0].x(), point[1].y() - point[0].y()), brush)

        for i in range(0, 24):
            painter.setPen(QPen(QtGui.QColor("#001a33"), 2, Qt.SolidLine))
            painter.drawLine(5, i*(self.height()//24) + 10, self.width() - 5, i*(self.height()//24) + 10)

        for i in range(0, 24):
            painter.setPen(QPen(QtGui.QColor("#001a33"), 2, Qt.SolidLine))
            hourXStart = 10
            hourYStart = i*(self.height()//24) + 10
            hourWidth = self.width()//15
            hourHeight = self.height()//24

            painter.setFont(QtGui.QFont('Times', self.height() // 130, QtGui.QFont.Bold))
            painter.drawText(QtCore.QRect(hourXStart, hourYStart, hourWidth, hourHeight),
                             Qt.AlignTop | Qt.AlignHCenter, f"{i}:00")
            self.drawEventsForDay(brush, painter, i,
                                  hourXStart, hourYStart, hourHeight, hourWidth)

    def drawEventsForDay(self, brush, painter, hour, hourXStart, hourYStart, hourHeight, hourWidth):

        wholePaintingSpace = self.width() - hourXStart - hourWidth - 20

        for event in self.dayDataList:
            if event["timeFrom"].hour == hour:
                timeDiff = str(event["timeTo"] - event["timeFrom"])
                heightFactor = int(timeDiff.split(":")[0])
                heightFactorFraction = int(timeDiff.split(":")[1]) / 60
                heightFactor += heightFactorFraction

                eventRectX = hourXStart + hourWidth + (wholePaintingSpace // event["overlap"]) * event["order"] + 10

                brush.setColor(QtGui.QColor(event["type"]))
                brush.setStyle(Qt.SolidPattern)

                painter.setPen(Qt.NoPen)
                painter.setBrush(brush)

                spaceBetweenEvents = 10

                painter.drawRoundedRect(QtCore.QRect(
                    eventRectX,
                    hourYStart,
                    (wholePaintingSpace // event["overlap"]) - spaceBetweenEvents,
                    int(hourHeight * heightFactor)), 10, 10)

                painter.setPen(Qt.black)

                painter.setFont(QtGui.QFont('Times', self.height() // 150, QtGui.QFont.Normal))

                painter.drawText(QtCore.QRect(
                    eventRectX + 10,
                    hourYStart,
                    wholePaintingSpace // (event["overlap"] + 1) - 5,
                    int(hourHeight * heightFactor) + 10),
                    Qt.AlignTop | Qt.AlignLeft, event["title"])


def __main__():
    app = QtWidgets.QApplication(sys.argv)
    dayCalendar = DayCalendar()
    dayCalendar.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()

