from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem

from GUI.Autogenerated.SettingsWindow.AGSettingsW import Ui_Form
from GUI.SettingsWindow.GeneralSet import GeneralSet
from GUI.SettingsWindow.DayCalendarSet import DayCalendarSet
from GUI.SettingsWindow.MonthCalendarSet import MonthCalendarSet
from GUI.SettingsWindow.WeekCalendarSet import WeekCalendarSet
from GUI.SettingsWindow.EventTypeSet import EventTypesSet

from Objects.AppSettings import settingsDict

import logging
logger = logging.getLogger('settingsWLogger')

class SettingsW(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #do usuniecia
        self.item_1 = None
        self.item_2 = None
        self.item_3 = None
        self.item_4 = None
        self.item_5 = None
        self.settingsWindow = Ui_Form()
        self.settingsWindow.setupUi(self)
        self.init_ui()
        self.setSelectedWidget()

    def init_ui(self) -> None:

        self.item_1 = QListWidgetItem('General')
        self.item_2 = QListWidgetItem('Day view')
        self.item_3 = QListWidgetItem('Week view')
        self.item_4 = QListWidgetItem('Month view')
        self.item_5 = QListWidgetItem('Event types manager')
        #wprowadzic bezposrednio do listy
        self.settingsWindow.listWidget.addItem(self.item_1)
        self.settingsWindow.listWidget.addItem(self.item_2)
        self.settingsWindow.listWidget.addItem(self.item_3)
        self.settingsWindow.listWidget.addItem(self.item_4)
        self.settingsWindow.listWidget.addItem(self.item_5)

        self.generalSet = GeneralSet()
        self.dayCalendarSet = DayCalendarSet()
        self.weekCalendarSet = WeekCalendarSet()
        self.monthCalendarSet = MonthCalendarSet()
        self.eventTypesSet = EventTypesSet()
        self.settingsWindow.stackedWidget.addWidget(self.generalSet)
        self.settingsWindow.stackedWidget.addWidget(self.dayCalendarSet)
        self.settingsWindow.stackedWidget.addWidget(self.weekCalendarSet)
        self.settingsWindow.stackedWidget.addWidget(self.monthCalendarSet)
        self.settingsWindow.stackedWidget.addWidget(self.eventTypesSet)

        self.settingsWindow.listWidget.currentItemChanged.connect(lambda: self.setSelectedWidget())

        self.settingsWindow.okBtn.clicked.connect(self.settingsOkBtn)
        self.settingsWindow.cancelBtn.clicked.connect(self.settingsCancelBtn)
        self.settingsWindow.applyBtn.clicked.connect(self.settingsApplyBtn)

    def settingsOkBtn(self):
        pass
        # call settingsApplyBtn()
        # close window

    def settingsCancelBtn(self):
        pass

    def settingsApplyBtn(self):
        pass
        # reload style
        # save to the file

    def switchToTheGeneralSet(self):
        self.settingsWindow.stackedWidget.setCurrentIndex(2)
        self.generalSet.setCurrentData(settingsDict['generalSettings'])


    def switchToTheDayCalendarSet(self):
        self.settingsWindow.stackedWidget.setCurrentIndex(3)
        self.dayCalendarSet.setCurrentData(settingsDict['dayCalendarSettings'])

    def switchToTheWeekCalendarSet(self):
        self.settingsWindow.stackedWidget.setCurrentIndex(4)
        self.weekCalendarSet.setCurrentData(settingsDict['weekCalendarSettings'])

    def switchToTheMonthCalendarSet(self):
        self.settingsWindow.stackedWidget.setCurrentIndex(5)
        self.monthCalendarSet.setCurrentData(settingsDict['monthCalendarSettings'])

    def switchToTheEventTypesSet(self):
        self.settingsWindow.stackedWidget.setCurrentIndex(6)

    def setSelectedWidget(self):
        # self.settingsWindow.listWidget.item(0) pomoze naprawic
        match self.settingsWindow.listWidget.currentItem():
            case self.item_1:
                self.switchToTheGeneralSet()
            case self.item_2:
                self.switchToTheDayCalendarSet()
            case self.item_3:
                self.switchToTheWeekCalendarSet()
            case self.item_4:
                self.switchToTheMonthCalendarSet()
            case self.item_5:
                self.switchToTheEventTypesSet()

    def clearSelectedListItem(self):
        self.settingsWindow.listWidget.clearSelection()

def __main__():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settingsW = SettingsW()
    settingsW.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()
