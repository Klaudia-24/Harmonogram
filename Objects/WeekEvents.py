from enum import IntEnum
import dateutils
from Objects.Event import getEventsForDay

weekEvents = dict()

class Week(IntEnum):

    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

def clearWeekEventsList():
    global weekEvents
    for day in Week:
        weekEvents[day.name] = []

def getEventsForWeek(firstDayOfWeekDate):
    global weekEvents
    clearWeekEventsList()

    for weekDay in Week:
        dayDate = firstDayOfWeekDate + dateutils.relativedelta(days=(int(weekDay.value)))
        weekEvents[weekDay.name] = getEventsForDay(dayDate)

# def getEventsListForWeekDay(weekDay):
#     global weekEvents
#     return weekEvents[weekDay]

def __main__():
    pass
    # date = datetime.datetime(2022, 8, 8)
    # l = getEventsForDay(date.day, date.month, date.year)
    # print(l)
    # getEventsForWeek(date)

if __name__ == '__main__':
    __main__()