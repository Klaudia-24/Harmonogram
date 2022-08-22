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

    def setDayDataList(self, data : datetime):
        self.dayDataList = getEventsForDay(data)
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
        hourWidth = self.width() // 15
        hourHeight = self.height() // 24
        hourXStart = 10 # margines lewostronny godziny
        painter.fillRect(QtCore.QRect(0, 0, painter.device().width(), painter.device().height()), #background size
                         QtGui.QBrush(QtGui.QColor("#cfe0e8"), Qt.SolidPattern) #background color
                        )
        painter.setFont(QtGui.QFont('Times', self.height() // 130, QtGui.QFont.Bold))

        # Rysowanie lini poziomych i godzin
        for hour in range(0, 24):
            painter.setPen(QPen(QtGui.QColor("#001a33"), 2, Qt.SolidLine))
            VerticalPosition = hour * hourHeight + 10 #pozycja pionowa
            painter.drawLine(5, # margines lewy
                             VerticalPosition,
                             self.width() - 5, # marines prawy
                             VerticalPosition
                             )
            painter.drawText(
                QtCore.QRect(hourXStart,
                             VerticalPosition,
                             hourWidth, #szerokosc gdziny
                             hourHeight #wysokość godziny
                            ),
                Qt.AlignTop | Qt.AlignHCenter,
                f"{hour}:00" #format godziny do wyswietlenia
            )

        #rysowanie Eventow
        self.drawEvents(painter, hourXStart, hourHeight, hourWidth)

    def drawEvents(self, painter, hourLeftMargin, hourHeight, hourWidth):
        brush = QtGui.QBrush()
        brush.setStyle(Qt.SolidPattern)
        spaceBetweenEvents = 10
        wholePaintingSpace = self.width() - hourLeftMargin - hourWidth - 20
        for event in self.dayDataList:
            brush.setColor(QtGui.QColor(event["type"]))
            painter.setPen(Qt.NoPen)
            painter.setBrush(brush)
            eventVerticalStart = int((int(event["timeFrom"].strftime("%H"))+int(event["timeFrom"].strftime("%M"))/60)*hourHeight+10)
            eventVerticalEnd = int((int(event["timeTo"].strftime("%H"))+int(event["timeTo"].strftime("%M"))/60) * hourHeight)
            eventHorizontalStart = hourLeftMargin + hourWidth + (wholePaintingSpace // event["overlap"]) * event["order"] + 10
            eventHorizontalEnd = (wholePaintingSpace // event["overlap"]) - spaceBetweenEvents
            painter.drawRoundedRect(QtCore.QRect(eventHorizontalStart, eventVerticalStart, eventHorizontalEnd, eventVerticalEnd), 10, 10)

            painter.setPen(Qt.black)
            painter.setFont(QtGui.QFont('Times', self.height() // 150, QtGui.QFont.Normal))

            painter.drawText(QtCore.QRect(
                eventHorizontalStart + 10,
                eventVerticalStart + 5,
                eventHorizontalEnd - 20,
                eventVerticalEnd),
                Qt.AlignTop | Qt.AlignLeft, event["title"])

            painter.drawText(QtCore.QRect(
                eventHorizontalStart + 10,
                eventVerticalStart + 35,
                eventHorizontalEnd - 20,
                eventVerticalEnd),
                Qt.AlignTop | Qt.AlignLeft, event["description"])

            painter.drawText(QtCore.QRect(
                eventHorizontalStart + 10,
                eventVerticalStart + 65,
                eventHorizontalEnd - 20,
                eventVerticalEnd),
                Qt.AlignTop | Qt.AlignLeft, event["localization"])

            painter.drawText(QtCore.QRect(
                eventHorizontalStart + 10,
                eventVerticalStart + 95,
                eventHorizontalEnd - 20,
                eventVerticalEnd),
                Qt.AlignTop | Qt.AlignLeft, event["reminder"])

def __main__():
    app = QtWidgets.QApplication(sys.argv)
    dayCalendar = DayCalendar()
    dayCalendar.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()

