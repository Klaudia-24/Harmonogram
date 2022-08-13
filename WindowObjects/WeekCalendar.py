import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from Objects.Event import getEventsForDay


class WeekCalendar(QtWidgets.QWidget):

    __startPoint = None
    __pointsList = []
    __shapes = []
    __weekNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def __init__(self, *args, **kwargs):
        super(WeekCalendar, self).__init__(*args, **kwargs)
        self.setMinimumHeight(2000)
        self.setMinimumWidth(2500)
        self.weekDataList = []



    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        backgroundBrush = QtGui.QBrush()
        brush = QtGui.QBrush()
        backgroundBrush.setColor(QtGui.QColor("#9fdfbf"))
        backgroundBrush.setStyle(Qt.SolidPattern)
        painter.fillRect(QtCore.QRect(0, 0, painter.device().width(), painter.device().height()), backgroundBrush)

        brush.setColor(QtGui.QColor("#80bfff"))
        brush.setStyle(Qt.SolidPattern)

        if self.__shapes:
            for point in self.__shapes:
                painter.fillRect(QtCore.QRect(point[0].x(), point[0].y(), point[1].x() - point[0].x(), point[1].y() - point[0].y()), brush)

        rowHeight = (self.height() - 0)//25

        for i in range(0, 24):
            painter.drawLine(5, i * rowHeight + rowHeight, self.width() - 5, i * rowHeight + rowHeight)

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

        painter.drawLine(80,
                         5,
                         80,
                         self.height() - 5)

        for i in range(0, 7):
            weekDayXStart = 50 + ((self.width()-150) // 7) * i
            weekDayYStart = 20
            weekDayWidth = self.width() // 7
            weekDayHeight = rowHeight

            painter.setFont(QtGui.QFont('Times', self.height() // 130, QtGui.QFont.Bold))
            painter.drawText(QtCore.QRect(weekDayXStart, weekDayYStart, weekDayWidth, weekDayHeight),
                             Qt.AlignTop | Qt.AlignHCenter, self.__weekNames[i])
            painter.drawLine(weekDayXStart + weekDayWidth,
                             5,
                             weekDayXStart + weekDayWidth,
                             self.height() - 5)


def __main__():
    app = QtWidgets.QApplication(sys.argv)
    weekCalendar = WeekCalendar()
    weekCalendar.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()