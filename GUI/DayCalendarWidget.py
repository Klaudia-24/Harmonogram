from PyQt5 import QtWidgets
from GUI.Autogenerated.AGDayCalendarWidget import Ui_Form
from WindowObjects.DayCalendar import DayCalendar


class DayCalendarWidget(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dayCalendarWidget = Ui_Form()
        self.dayCalendarWidget.setupUi(self)
        # self.dayCalendarWidget.scrollAreaWidget.resize(2000, 374)
        self.dayCalendar = DayCalendar()
        self.dayCalendarWidget.scrollArea.setWidget(self.dayCalendar)
        # self.init_ui()

    # def init_ui(self) -> None: