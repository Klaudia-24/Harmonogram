from calendar import *
from datetime import date

eventsTypesColorsDict = {"Home": "#00b33c", "Work": "#1a75ff", "School": "#e62e00"}

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
        return hash(self.__eventDate, self.__title, self.__description, self.__localization,
                    self.__eventType, self.__eventRemind)

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
