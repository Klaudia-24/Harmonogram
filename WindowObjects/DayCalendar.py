import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt


class DayCalendar(QtWidgets.QWidget):

    __startPoint = None
    __pointsList = []
    __shapes = []

    def __init__(self, *args, **kwargs):
        super(DayCalendar, self).__init__(*args, **kwargs)
        self.setMinimumHeight(2000)

    def mousePressEvent(self, event):
        self.__startPoint = event.pos()

    def mouseReleaseEvent(self, event) -> None:
        self.__shapes.append([self.__startPoint, event.pos()])
        self.update()

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

        painter.setFont(QtGui.QFont('Times', self.height()//130, QtGui.QFont.Bold))
        for i in range(0, 24):
            # painter.fillRect(QtCore.QRect(10, i*(self.height()//24) + 10, self.width()//15, (self.height()//25) + 0), brush)
            painter.drawText(QtCore.QRect(10, i*(self.height()//24) + 10, self.width()//17, (self.height()//25)),
                             Qt.AlignTop | Qt.AlignHCenter, f"{i}:00")

            painter.drawLine(5, i*(self.height()//24) + 10, self.width() - 5, i*(self.height()//24) + 10)

        painter.drawLine(5, 24 * (self.height() // 24) + 10, self.width() - 5, 24 * (self.height() // 24) + 10)



def __main__():
    app = QtWidgets.QApplication(sys.argv)
    dayCalendar = DayCalendar()
    dayCalendar.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()

