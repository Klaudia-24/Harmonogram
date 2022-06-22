from datetime import datetime
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

from GUI.MainCalendarWidget import MainCalendarWidget
from Objects.Event import getEventsDataForDay


class DayCalendar(QtWidgets.QWidget):

    __startPoint = None
    __pointsList = []
    __shapes = []

    def __init__(self, *args, **kwargs):
        super(DayCalendar, self).__init__(*args, **kwargs)
        self.setMinimumHeight(2000)
        self.mainCalendarWidget = MainCalendarWidget()
        self.dayDataList = []
        self.setDayDataList()

    def mousePressEvent(self, event):
        self.__startPoint = event.pos()

    def mouseReleaseEvent(self, event) -> None:
        self.__shapes.append([self.__startPoint, event.pos()])
        print(self.__shapes)
        self.update()

    def setDayDataList(self):
        self.dayDataList = getEventsDataForDay(
            self.mainCalendarWidget.dateOnDateBar.day,
            self.mainCalendarWidget.dateOnDateBar.month,
            self.mainCalendarWidget.dateOnDateBar.year)

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
            hourHeight = self.height()//25

            painter.setFont(QtGui.QFont('Times', self.height() // 130, QtGui.QFont.Bold))
            painter.drawText(QtCore.QRect(hourXStart, hourYStart, hourWidth, hourHeight),
                             Qt.AlignTop | Qt.AlignHCenter, f"{i}:00")

            painter.drawLine(5, i*(self.height()//24) + 10, self.width() - 5, i*(self.height()//24) + 10)

            for event in self.dayDataList:
                if event[0].split(":")[0] == str(i):

                    timeStart = datetime.strptime(event[0], '%H:%M')
                    timeEnd = datetime.strptime(event[1], '%H:%M')

                    timeDiff = str(timeEnd - timeStart)
                    heightFactor = int(timeDiff.split(":")[0])
                    heightFactorFraction = int(timeDiff.split(":")[1]) / 60
                    heightFactor += heightFactorFraction

                    brush.setColor(QtGui.QColor(event[3]))
                    brush.setStyle(Qt.SolidPattern)
                    painter.fillRect(
                        QtCore.QRect(
                            hourXStart + hourWidth + 20,
                            hourYStart,
                            self.width() // 10,
                            int(hourHeight * heightFactor) + 10),
                        brush)

                    painter.setFont(QtGui.QFont('Times', self.height() // 150, QtGui.QFont.Normal))
                    painter.drawText(QtCore.QRect(
                        hourXStart + hourWidth + 25,
                        hourYStart,
                        self.width() // 10 - 5,
                        int(hourHeight * heightFactor) + 10),
                        Qt.AlignTop | Qt.AlignLeft, event[2])

        painter.drawLine(5, 24 * (self.height() // 24) + 10, self.width() - 5, 24 * (self.height() // 24) + 10)



def __main__():
    app = QtWidgets.QApplication(sys.argv)
    dayCalendar = DayCalendar()
    dayCalendar.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()

