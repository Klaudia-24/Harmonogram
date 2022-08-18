import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from Objects.WeekEvents import getEventsForWeek, weekEvents
from Objects.WeekEvents import Week


class WeekCalendar(QtWidgets.QWidget):

    __startPoint = None
    __pointsList = []
    __shapes = []

    def __init__(self, *args, **kwargs):
        super(WeekCalendar, self).__init__(*args, **kwargs)
        self.setMinimumHeight(2000)
        self.setMinimumWidth(2500)

    def setWeekEventsList(self, firstDayOfWeekDate):
        getEventsForWeek(firstDayOfWeekDate)
        for weekDay in weekEvents:
            self.calculateEventsOffsets(weekEvents[weekDay])
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

    def calculateEventsOffsets(self, dayEventsList):
        for i in range(0, len(dayEventsList)-1):
            for j in range(i+1, len(dayEventsList)):
                if self.isOverlapping(dayEventsList[i], dayEventsList[j]):
                    dayEventsList[j]["order"] += 1
                    dayEventsList[i]["overlap"] += 1
                    dayEventsList[j]["overlap"] += 1

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        backgroundBrush = QtGui.QBrush()
        brush = QtGui.QBrush()
        backgroundBrush.setColor(QtGui.QColor("#9fdfbf"))
        backgroundBrush.setStyle(Qt.SolidPattern)
        painter.fillRect(QtCore.QRect(0, 0, painter.device().width(), painter.device().height()), backgroundBrush)

        brush.setColor(QtGui.QColor("#80bfff"))
        brush.setStyle(Qt.SolidPattern)

        rowHeight = (self.height() - 0)//25

        for i in range(0, 24):
            painter.drawLine(5, i * rowHeight + rowHeight, self.width() - 5, i * rowHeight + rowHeight)

            # painter.setPen(QPen(QtGui.QColor("#001a33"), 2, Qt.SolidLine))
            # hourXStart = 10
            # hourYStart = i * (self.height() // 24) + 10
            # hourWidth = self.width() // 15
            # hourHeight = self.height() // 24
            #
            # painter.setFont(QtGui.QFont('Times', self.height() // 130, QtGui.QFont.Bold))
            # painter.drawText(QtCore.QRect(hourXStart, hourYStart, hourWidth, hourHeight),
            #                  Qt.AlignTop | Qt.AlignHCenter, f"{i}:00")

        self.drawHours(painter, rowHeight)
        painter.drawLine(80, 5, 80, self.height() - 5)
        self.drawWeekDay(painter, brush, rowHeight)

    def drawHours(self, painter, rowHeight):
        for i in range(0, 24):
            hourXStart = -40
            hourYStart = i*rowHeight + rowHeight
            hourWidth = self.width()//15
            hourHeight = rowHeight

            painter.setFont(QtGui.QFont('Times', self.height() // 130, QtGui.QFont.Bold))
            painter.drawText(QtCore.QRect(hourXStart, hourYStart, hourWidth, hourHeight),
                             Qt.AlignTop | Qt.AlignHCenter, f"{i}:00")
            painter.drawText(QtCore.QRect(self.width() - 130, hourYStart, hourWidth, hourHeight),
                             Qt.AlignTop | Qt.AlignHCenter, f"{i}:00")

    def drawWeekDay(self, painter, brush, rowHeight):
        for day in Week:
            weekDayXStart = 50 + ((self.width()-150) // 7) * day.value
            weekDayYStart = 20
            weekDayWidth = self.width() // 7
            weekDayHeight = rowHeight

            painter.setFont(QtGui.QFont('Times', self.height() // 130, QtGui.QFont.Bold))
            painter.drawText(QtCore.QRect(weekDayXStart, weekDayYStart, weekDayWidth, weekDayHeight),
                             Qt.AlignTop | Qt.AlignHCenter, day.name)
            painter.drawLine(weekDayXStart + weekDayWidth,
                             5,
                             weekDayXStart + weekDayWidth,
                             self.height() - 5)

            for i in range(0, 24):
                hourXStart = 10
                hourYStart = i * (self.height() // 24) + 10 + weekDayHeight
                hourWidth = self.width() // 15
                hourHeight = self.height() // 25

                self.drawEventsForDay(weekEvents[day.name], brush, painter, i, weekDayXStart, hourYStart, hourWidth,
                                      hourHeight, weekDayWidth, weekDayHeight)

    def drawEventsForDay(self, eventsList, brush, painter, hour, weekDayXStart, hourYStart, hourWidth,
                         hourHeight, weekDayWidth, weekDayHeight):

        # wholePaintingSpace = self.width() - dayXStart - dayWidth - 20

        wholePaintingSpace = weekDayWidth - 40

        # for weekDay in weekEvents:
        for event in eventsList:
            if event["timeFrom"].hour == hour:
                timeDiff = str(event["timeTo"] - event["timeFrom"])
                heightFactor = int(timeDiff.split(":")[0])
                heightFactorFraction = int(timeDiff.split(":")[1]) / 60
                heightFactor += heightFactorFraction

                eventRectX = weekDayXStart + 40 + (wholePaintingSpace // event["overlap"]) * event["order"]

                brush.setColor(QtGui.QColor(event["type"]))
                brush.setStyle(Qt.SolidPattern)
                painter.setPen(Qt.NoPen)
                painter.setBrush(brush)

                spaceBetweenEvents = 10

                painter.drawRoundedRect(QtCore.QRect(
                    eventRectX,
                    hourYStart - 10,
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
    weekCalendar = WeekCalendar()
    weekCalendar.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()