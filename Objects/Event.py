from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from Lib.FileOperationMethods import writeToJsonFile, readFromJsonFileToDict_v2

eventsTypesColorsDict = {"Home": "#00b33c", "Work": "#1a75ff", "School": "#e62e00"}
eventsDictionary = dict()
eventTypesDictionary = dict()
eventsDictionary["events"] = dict()
eventTypesDictionary["eventTypes"] = dict()


@dataclass_json
@dataclass
class EventDuration_2:
    allDayEvent: bool
    timeFrom: str
    timeTo: str


@dataclass_json
@dataclass
class Event_2:

    #TODO use dataclass and json write/read

    eventId: int = field(init=False, repr=False)
    eventDuration: EventDuration_2
    type: str
    title: str
    description: str
    localization: str
    reminder: str

    def __post_init__(self):
        self.eventId = self.__hash__()

    def __hash__(self):
        return hash((self.type, self.title, self.description, self.localization, self.reminder))




def addEventToList(year, month, day, event):
    global eventsDictionary
    if year not in eventsDictionary["events"]:
        eventsDictionary["events"][year] = dict()
    if month not in eventsDictionary["events"][year]:
        eventsDictionary["events"][year][month] = dict()
    if day not in eventsDictionary["events"][year][month]:
        eventsDictionary["events"][year][month][day] = []
    eventsDictionary["events"][year][month][day].append(event)


def addEventTypeToList(key,value):
    global eventTypesDictionary
    eventTypesDictionary["eventTypes"][key]=value

def saveEventList():
    global eventsDictionary
    writeToJsonFile("./events.json", eventsDictionary)


def saveEventTypeList():
    global eventTypesDictionary
    writeToJsonFile("./eventTypes.json", eventTypesDictionary)


def loadEventTypeList():
    global eventTypesDictionary
    readFromJsonFileToDict_v2("./eventTypes.json", eventTypesDictionary, "eventTypes")


def loadEventList():
    global eventsDictionary
    readFromJsonFileToDict_v2("./events.json", eventsDictionary, "events")


def getEventTypeList():
    global eventTypesDictionary
    return eventTypesDictionary["eventTypes"].keys()
