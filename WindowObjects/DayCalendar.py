from datetime import datetime
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
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
        if event_2["timeFrom"] < event_1["timeFrom"] < event_2["timeTo"]:
            return True
        if event_2["timeFrom"] < event_1["timeTo"] < event_2["timeTo"]:
            return True
        if event_1["timeFrom"] < event_2["timeFrom"] < event_1["timeTo"]:
            return True
        if event_1["timeFrom"] < event_2["timeTo"] < event_1["timeTo"]:
            return True
        return False

    def calculateEventsOffsets(self):
        for i in range(0, len(self.dayDataList)):
            counter = 1
            for j in range(i, len(self.dayDataList)):
                if self.isOverlapping(self.dayDataList[i], self.dayDataList[j]):
                    counter += 1
                    self.dayDataList[j]["order"] += 1
                    self.dayDataList[j]["overlap"] += 1
            self.dayDataList[i]["overlap"] += counter

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        backgroundBrush = QtGui.QBrush()
        brush = QtGui.QBrush()
        backgroundBrush.setColor(QtGui.QColor("#cfe0e8"))
        backgroundBrush.setStyle(Qt.SolidPattern)
        painter.fillRect(QtCore.QRect(0, 0, painter.device().width(), painter.device().height()), backgroundBrush)

        brush.setColor(QtGui.QColor("#80bfff"))
        brush.setStyle(Qt.SolidPattern)

        if self.__shapes:
            for point in self.__shapes:
                painter.fillRect(QtCore.QRect(point[0].x(), point[0].y(), point[1].x() - point[0].x(), point[1].y() - point[0].y()), brush)

        for i in range(0, 24):
            # painter.fillRect(QtCore.QRect(10, i*(self.height()//24) + 10, self.width()//15, (self.height()//25) + 0), brush)

            hourXStart = 10
            hourYStart = i*(self.height()//24) + 10
            hourWidth = self.width()//15
            hourHeight = self.height()//24
            wholePaintingSpace = self.width() - hourXStart - hourWidth - 30

            painter.setFont(QtGui.QFont('Times', self.height() // 130, QtGui.QFont.Bold))
            painter.drawText(QtCore.QRect(hourXStart, hourYStart, hourWidth, hourHeight),
                             Qt.AlignTop | Qt.AlignHCenter, f"{i}:00")

            painter.drawLine(5, i*(self.height()//24) + 10, self.width() - 5, i*(self.height()//24) + 10)

            for event in self.dayDataList:
                if event["timeFrom"].hour == i:

                    timeDiff = str(event["timeTo"] - event["timeFrom"])
                    heightFactor = int(timeDiff.split(":")[0])
                    heightFactorFraction = int(timeDiff.split(":")[1]) / 60
                    heightFactor += heightFactorFraction

                    eventRectX = hourXStart + hourWidth + (wholePaintingSpace // event["overlap"]) * event["order"] + 10

                    brush.setColor(QtGui.QColor(event["type"]))
                    brush.setStyle(Qt.SolidPattern)
                    painter.fillRect(
                        QtCore.QRect(
                            eventRectX,
                            hourYStart,
                            wholePaintingSpace // event["overlap"],
                            int(hourHeight * heightFactor)),
                        brush)

                    painter.setFont(QtGui.QFont('Times', self.height() // 150, QtGui.QFont.Normal))

                    painter.drawText(QtCore.QRect(
                        eventRectX + 10,
                        hourYStart,
                        wholePaintingSpace // (event["overlap"] + 1) - 5,
                        int(hourHeight * heightFactor) + 10),
                        Qt.AlignTop | Qt.AlignLeft, event["title"])

        painter.drawLine(5, 24 * (self.height() // 24) + 10, self.width() - 5, 24 * (self.height() // 24) + 10)


def __main__():
    app = QtWidgets.QApplication(sys.argv)
    dayCalendar = DayCalendar()
    dayCalendar.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()

