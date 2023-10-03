from Objects.AppSettings import GeneralSettings, DayCalendarSettings, WeekCalendarSettings, MonthCalendarSettings, settingsDict
from Lib.FileOperationMethods import writeToYamlFile
import logging
logger = logging.getLogger('main')

def createSettingsFile():
    settingsDict['generalSettings'] = GeneralSettings(windowBackColour='#cccccc',
                                                             navBtnStyle=2,
                                                             eventsFilePath='./events.json',
                                                             dateBarFontColour='#19334d',
                                                             dateBarFontSize=16,
                                                             dateBarFontBold=True
                                                             ).to_dict()

    settingsDict['dayCalendarSettings'] = DayCalendarSettings(calendarBackColour='#cfe0e8',
                                                                         linesColour='#001a33',
                                                                         hoursColour='#001a33',
                                                                         hourLinesThicknessRatio=2.0,
                                                                         spaceRatioBetweenEvents=10,
                                                                         eventTitleShow=True,
                                                                         eventDescriptionShow=False,
                                                                         eventLocalizationShow=False,
                                                                         eventReminderShow=False
                                                                         ).to_dict()

    settingsDict['weekCalendarSettings'] = WeekCalendarSettings(calendarBackColour='#9fdfbf',
                                                                            hourLinesColour='#001a33',
                                                                            dayLinesColour='#001a33',
                                                                            hourLinesThicknessRatio=2.0,
                                                                            dayLinesThicknessRatio=4.0
                                                                            ).to_dict()

    settingsDict['monthCalendarSettings'] = MonthCalendarSettings(weekNumbersColour='#001a33',
                                                                               weekDaysColour='#001a33',
                                                                               currentDayColour='#339966',
                                                                               selectedDayColour='#66cc99',
                                                                               prevMonthColour='#cce6ff',
                                                                               currentMonthColour='#80bfff',
                                                                               nextMonthColour='#cce6ff',
                                                                               weekNumbersFontRatio=7.0,
                                                                               weekDaysFontRatio=8.1,
                                                                               currentDayFontRatio=3.5,
                                                                               selectedDayFontRatio=3.5,
                                                                               prevMonthFontRatio=3.5,
                                                                               currentMonthFontRatio=3.5,
                                                                               nextMonthFontRatio=3.5,
                                                                               todayDateBold=True
                                                                               ).to_dict()

    writeToYamlFile(settingsDict, './Lib/appConfig.yaml')

    #file in the Lib
