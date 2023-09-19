from Objects.AppSettings import GeneralSettings, DayCalendarSettings, WeekCalendarSettings, MonthCalendarSettings
from Lib.FileOperationMethods import writeSettingsToYamlFile


generalSettingsDict = dict()
generalSettingsDict['generalSettings'] = dict()
dayCalendarSettingsDict = dict()
dayCalendarSettingsDict['dayCalendarSettings'] = dict()
weekCalendarSettingsDict = dict()
weekCalendarSettingsDict['weekCalendarSettings'] = dict()
monthCalendarSettingsDict = dict()
monthCalendarSettingsDict['monthCalendarSettings'] = dict()

generalSettingsDict['generalSettings'] = GeneralSettings(windowBackColour='#cccccc',
                                                         navBtnStyle='skyPalette',
                                                         eventsFilePath='./events.json',
                                                         dateBarFontColour='#19334d',
                                                         dateBarFontSize=16,
                                                         dateBarFontBold=True
                                                         ).to_dict()

dayCalendarSettingsDict['dayCalendarSettings'] = DayCalendarSettings(calendarBackColour='#cfe0e8',
                                                                     linesColour='#001a33',
                                                                     hoursColour='#001a33',
                                                                     hourLinesThicknessRatio=2.0,
                                                                     spaceRatioBetweenEvents=10,
                                                                     eventTitleShow=True,
                                                                     eventDescriptionShow=False,
                                                                     eventLocalizationShow=False,
                                                                     eventReminderShow=False
                                                                     ).to_dict()

weekCalendarSettingsDict['weekCalendarSettings'] = WeekCalendarSettings(calendarBackColour='#9fdfbf',
                                                                            hourLinesColour='#001a33',
                                                                            dayLinesColour='#001a33',
                                                                            hourLinesThicknessRatio=2.0,
                                                                            dayLinesThicknessRatio=4.0
                                                                            ).to_dict()

monthCalendarSettingsDict['monthCalendarSettings'] = MonthCalendarSettings(weekNumbersColour='#001a33',
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

def createSettingsFile():
    settingsList = [generalSettingsDict,
                    dayCalendarSettingsDict,
                    weekCalendarSettingsDict,
                    monthCalendarSettingsDict]

    writeSettingsToYamlFile(settingsList)

    #file in the Lib
