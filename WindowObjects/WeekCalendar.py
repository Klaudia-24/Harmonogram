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

        rowHeight = (self.height())//25

        for i in range(0, 24):
            painter.drawLine(5, i * rowHeight + rowHeight, self.width() - 5, i * rowHeight + rowHeight)

        self.drawHours(painter)
        painter.drawLine(80, 5, 80, self.height() - 5)
        self.drawWeekDay(painter)

    def drawHours(self, painter):
        rowHeight = self.height() // 25

        for i in range(0, 24):
            hourYStart = rowHeight + i*rowHeight
            hourWidth = self.width()//30
            rowHeight = (self.height())//25

            painter.setFont(QtGui.QFont('Times', self.height() // 130, QtGui.QFont.Bold))
            painter.drawText(QtCore.QRect(0, hourYStart, hourWidth, rowHeight),
                             Qt.AlignTop | Qt.AlignHCenter, f"{i}:00")
            painter.drawText(QtCore.QRect(self.width() - hourWidth, hourYStart, hourWidth, rowHeight),
                             Qt.AlignTop | Qt.AlignHCenter, f"{i}:00")

    def drawWeekDay(self, painter):
        for day in Week:
            weekDayYStart = 20 # top margin
            weekDayWidth = (4 * self.width() // 30)
            rowHeight = self.height() // 25
            weekDayXStart = self.width()//30 + weekDayWidth * day.value

            painter.setFont(QtGui.QFont('Times', self.height() // 130, QtGui.QFont.Bold))
            painter.drawText(QtCore.QRect(weekDayXStart, weekDayYStart, weekDayWidth, rowHeight),
                             Qt.AlignTop | Qt.AlignHCenter, day.name)
            painter.drawLine(weekDayXStart + weekDayWidth,
                             5,
                             weekDayXStart + weekDayWidth,
                             self.height() - 5)

            self.drawDayEvents(painter, weekEvents[day.name], weekDayXStart, rowHeight, weekDayWidth)


    def drawDayEvents(self, painter, dayDataList, hourLeftMargin, rowHeight, weekDayWidth):
        brush = QtGui.QBrush()
        brush.setStyle(Qt.SolidPattern)
        spaceBetweenEvents = 10
        for event in dayDataList:
            brush.setColor(QtGui.QColor(event["type"]))
            painter.setPen(Qt.NoPen)
            painter.setBrush(brush)
            eventVerticalStart = int((int(event["timeFrom"].strftime("%H"))+int(event["timeFrom"].strftime("%M"))/60)*rowHeight) + rowHeight
            eventVerticalEnd = int((int(event["timeTo"].strftime("%H"))+int(event["timeTo"].strftime("%M"))/60) * rowHeight)
            eventHorizontalStart = hourLeftMargin + (weekDayWidth // event["overlap"]) * event["order"] + 5
            eventHorizontalEnd = (weekDayWidth // event["overlap"]) - spaceBetweenEvents

            painter.drawRoundedRect(QtCore.QRect(eventHorizontalStart, eventVerticalStart, eventHorizontalEnd, eventVerticalEnd), 10, 10)

            painter.setPen(Qt.black)
            painter.setFont(QtGui.QFont('Times', self.height() // 150, QtGui.QFont.Normal))

            eventText = event["title"] + "\n" + event["description"] + "\n" + event["localization"] + "\n" + event["reminder"]

            painter.drawText(QtCore.QRect(
                eventHorizontalStart + 10,
                eventVerticalStart + 5,
                eventHorizontalEnd - 20,
                eventVerticalEnd),
                Qt.AlignTop | Qt.AlignLeft, eventText)

def __main__():
    app = QtWidgets.QApplication(sys.argv)
    weekCalendar = WeekCalendar()
    weekCalendar.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()