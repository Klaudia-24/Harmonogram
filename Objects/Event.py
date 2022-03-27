from dataclasses import dataclass, field

eventsTypesColorsDict = {"Home": "#00b33c", "Work": "#1a75ff", "School": "#e62e00"}
eventsDictionary = dict()
eventTypesDictionary = dict()
eventsDictionary["events"] = []
eventTypesDictionary["eventTypes"] = []


class Event:

    def __init__(self, eventDate, title, description, localization, eventDuration, eventType, eventRemind=None):
        self.__eventDuration = eventDuration
        self.__eventDate = eventDate
        self.__title = title
        self.__description = description
        self.__localization = localization
        self.__eventType = eventType
        self.__eventRemind = eventRemind

    def setEventDuration(self, eventDuration):
        self.__eventDuration = eventDuration

    def setEventDate(self, eventDate):
        self.__eventDate = eventDate

    def setTitle(self, title):
        self.__title = title

    def setDescription(self, description):
        self.__description = description

    def setLocalization(self, localization):
        self.__localization = localization

    def setEventType(self, eventType):
        self.__eventType = eventType

    def setEventRemind(self, eventRemind):
        self.__eventRemind = eventRemind

    def getEventDuration(self):
        return self.__eventDuration

    def getEventDate(self):
        return self.__eventDate

    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description

    def getLocalization(self):
        return self.__localization

    def getEventType(self):
        return self.__eventType

    def getEventRemind(self):
        return self.__eventRemind

    def __hash__(self):
        return hash((self.__eventDate, self.__title, self.__description, self.__localization,
                    self.__eventType, self.__eventRemind if self.__eventRemind is not None else ""))

class EventDuration:

    def __init__(self, isAllDayEvent, dateTimeFrom=None, dateTimeTo=None):
        self.__isAllDayEvent = isAllDayEvent
        self.__dateTimeFrom = dateTimeFrom
        self.__dateTimeTo = dateTimeTo

    def setIsAllDayEvent(self, isAllDayEvent):
        self.__isAllDayEvent = isAllDayEvent

    def setDateTimeFrom(self, dateTimeFrom):
        self.__dateTimeFrom = dateTimeFrom

    def setDateTimeTo(self, dateTimeTo):
        self.__dateTimeTo = dateTimeTo

    def getIsAllDayEvent(self):
        return self.__isAllDayEvent

    def getDateTimeFrom(self):
        return self.__dateTimeFrom

    def getDateTimeTo(self):
        return self.__dateTimeTo


# "eventId": "6044419142954959992",
# "eventYear": 2021,
# "eventMonth": 9,
# "eventDay": 20,
# "allDayEvent": 0,
# "timeFromHour": 0,
# "timeFromMinute": 0,
# "timeToHour": 1,
# "timeToMinute": 0,
# "type": "Home",
# "title": "xxxxx",
# "description": "",
# "localization": "",
# "reminder": "15 minutes"


@dataclass
class Event_2:

    #TODO use dataclass and json write/read

    eventId: int = field(init=False, repr=False)
    eventYear: int
    eventMonth: int
    eventDay: int
    allDayEvent: int
    timeFromHour: int
    timeFromMinute: int
    timeToHour: int
    timeToMinute: int
    type: str
    title: str
    description: str
    localization: str
    reminder: str

    def __post_init__(self):
        self.eventId = self.__hash__()

    def __hash__(self):
        return hash((self.eventYear, self.eventMonth, self.eventDay, self.allDayEvent, self.timeFromHour, self.timeFromMinute,
                     self.timeToHour, self.timeToMinute, self.type, self.title, self.description, self.localization, self.reminder))