from dataclasses import dataclass, field
from datetime import datetime

from dataclasses_json import dataclass_json
from Lib.FileOperationMethods import writeToJsonFile, readFromJsonFileToDict

# TODO try to remove declarations below
eventsDictionary = dict()
eventTypesDictionary = dict()
eventsDictionary["events"] = dict()
eventTypesDictionary["eventTypes"] = dict()


@dataclass_json
@dataclass
class EventDuration:
    allDayEvent: bool
    timeFrom: str
    timeTo: str


@dataclass_json
@dataclass
class Event:

    eventId: int = field(init=False, repr=False)
    eventDuration: EventDuration
    type: str
    title: str
    description: str
    localization: str
    reminder: str

    def __post_init__(self):
        self.eventId = self.__hash__()

    def __hash__(self):
        return hash((self.type, self.title, self.description, self.localization, self.reminder))



def addEventToList(year, month, day, newEvent: Event):
    global eventsDictionary
    if year not in eventsDictionary["events"]:
        eventsDictionary["events"][year] = dict()
    if month not in eventsDictionary["events"][year]:
        eventsDictionary["events"][year][month] = dict()
    if day not in eventsDictionary["events"][year][month]:
        eventsDictionary["events"][year][month][day] = []

    eventsDictionary["events"][year][month][day].append(newEvent.to_dict())


# TODO config file with file names etc.


def getEventsDictionary():
    return eventsDictionary


def getEventTypesDictionary():
    return eventTypesDictionary


def addEventTypeToList(key, value):
    global eventTypesDictionary
    eventTypesDictionary["eventTypes"][key] = value


def saveEventList():
    global eventsDictionary
    writeToJsonFile("./events.json", eventsDictionary)


def saveEventTypesList():
    global eventTypesDictionary
    writeToJsonFile("./eventTypes.json", eventTypesDictionary)


def loadEventTypesList():
    global eventTypesDictionary
    readFromJsonFileToDict("./eventTypes.json", eventTypesDictionary, "eventTypes")


def loadEventsList():
    global eventsDictionary
    readFromJsonFileToDict("./events.json", eventsDictionary, "events")


def getEventTypesList():
    global eventTypesDictionary
    return sorted(eventTypesDictionary["eventTypes"].keys())


def getEventTypeColour(eventType):
    global eventTypesDictionary
    return eventTypesDictionary["eventTypes"][eventType]


def getEventsForDay(day, month, year):
    global eventsDictionary
    dayDataList = []
    if str(year) in eventsDictionary["events"] and \
       str(month) in eventsDictionary["events"][str(year)] and \
       str(day) in eventsDictionary["events"][str(year)][str(month)]:

        for event in eventsDictionary["events"][str(year)][str(month)][str(day)]:
            dataDict = dict()
            # TODO change to the data class
            dataDict["timeFrom"] = datetime.strptime(event["eventDuration"]["timeFrom"], '%H:%M')
            dataDict["timeTo"] = datetime.strptime(event["eventDuration"]["timeTo"], '%H:%M')
            dataDict["title"] = event["title"]
            dataDict["description"] = event["description"]
            dataDict["localization"] = event["localization"]
            dataDict["reminder"] = event["reminder"]
            dataDict["type"] = getEventTypeColour(event["type"])
            dataDict["overlap"] = 1 # number of events overlapping
            dataDict["order"] = 0 # ordinal number of event
            dayDataList.append(dataDict)

    return dayDataList

