from dataclasses import dataclass
from dataclasses_json import dataclass_json

settingsDict = dict()
settingsDict['generalSettings'] = dict()
settingsDict['dayCalendarSettings'] = dict()
settingsDict['weekCalendarSettings'] = dict()
settingsDict['monthCalendarSettings'] = dict()

colourPaletteDict = dict()

@dataclass_json
@dataclass
class GeneralSettings:
    windowBackColour: str
    navBtnStyle: str
    eventsFilePath: str
    dateBarFontColour: str
    dateBarFontSize: int
    dateBarFontBold: bool

@dataclass_json
@dataclass
class DayCalendarSettings:
    calendarBackColour: str
    linesColour: str
    hoursColour: str
    hourLinesThicknessRatio: float
    spaceRatioBetweenEvents: int
    eventTitleShow: bool
    eventDescriptionShow: bool
    eventLocalizationShow: bool
    eventReminderShow: bool

@dataclass_json
@dataclass
class WeekCalendarSettings:
    calendarBackColour: str
    hourLinesColour: str
    dayLinesColour: str
    hourLinesThicknessRatio: float
    dayLinesThicknessRatio: float

@dataclass_json
@dataclass
class MonthCalendarSettings:
    weekNumbersColour: str
    weekDaysColour: str
    currentDayColour: str
    selectedDayColour: str
    prevMonthColour: str
    currentMonthColour: str
    nextMonthColour: str

    weekNumbersFontRatio: float
    weekDaysFontRatio: float
    currentDayFontRatio: float
    selectedDayFontRatio: float
    prevMonthFontRatio: float
    currentMonthFontRatio: float
    nextMonthFontRatio: float

    todayDateBold: bool

@dataclass_json
@dataclass
class ColourPalette:
    name: str
    colour1: str
    fontColour1: str
    colour2: str
    fontColour2: str
    colour3: str
    fontColour3: str
    colour4: str
    fontColour4: str

# def classFromArgs(className, argDict):
#     fieldSet = {f.name for f in fields(className) if f.init}
#     filteredArgDict = {k: v for k, v in argDict.items() if k in fieldSet}
#     return className(**filteredArgDict)

def __main__():
    pass

if __name__ == '__main__':
    __main__()