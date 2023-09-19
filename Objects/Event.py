from dataclasses import dataclass, field
from datetime import datetime

from PyQt5.QtWidgets import QMessageBox
from marshmallow import fields
from dataclasses_json import dataclass_json, config
from Lib.FileOperationMethods import writeToJsonFile, readFromJsonFileToDict
from typing import Optional
import json
from PyQt5.QtCore import QRect

# TODO try to remove declarations below
eventsDictionary = dict()
eventTypesDictionary = dict()
eventTypesDictionary["eventTypes"] = dict()


@dataclass_json
@dataclass
class EventDuration:
    allDayEvent: bool
    timeFrom: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        )

    )
    timeTo: datetime= field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        )
    )


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
    overlap: Optional[int] = field(repr=False, default=1,
                                   metadata=config(
                                       exclude=lambda x: True
                                   )
                                   )
    order: Optional[int] = field(repr=False, default=0,
                                 metadata=config(
                                       exclude=lambda x: True
                                   ))
    rectangle: Optional[QRect] = field(repr=False, default=QRect(0, 0, 0, 0),
                                       metadata=config(
                                           exclude=lambda x: True
                                       )
                                       )

    def __post_init__(self):
        self.eventId = self.__hash__()

    def __hash__(self):
        return hash((self.type, self.title, self.description, self.localization, self.reminder))



def addEventToList(year, month, day, newEvent: Event):
    global eventsDictionary
    if year not in eventsDictionary:
        eventsDictionary[year] = dict()
    if month not in eventsDictionary[year]:
        eventsDictionary[year][month] = dict()
    if day not in eventsDictionary[year][month]:
        eventsDictionary[year][month][day] = []

    eventsDictionary[year][month][day].append(newEvent)


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
    with open("./events.json", 'w') as file:
        jsonItem = json.dumps(eventsDictionary, indent=4, default=eventEncoder)
        file.write(jsonItem)


def saveEventTypesList():
    global eventTypesDictionary
    writeToJsonFile("./eventTypes.json", eventTypesDictionary)


def loadEventTypesList():
    global eventTypesDictionary
    readFromJsonFileToDict("./eventTypes.json", eventTypesDictionary, "eventTypes")


def loadEventsList():
    # global eventsDictionary
    # readFromJsonFileToDict("./events.json", eventsDictionary, "events")

    global eventsDictionary
    eventsDictionary.clear()
    try:
        with open("./events.json", 'r') as file:
            dataFromFile = json.load(file)
            for year in dataFromFile.keys():
                for month in dataFromFile[year].keys():
                    for day in dataFromFile[year][month].keys():
                        for event in dataFromFile[year][month][day]:
                            temp = Event.from_dict(event)
                            # temp['eventDuration'] = EventDuration.from_dict(temp['eventDuration'])
                            addEventToList(int(year), int(month), int(day), temp)
    except FileNotFoundError:

        # TODO create empty file
        messageWindow = QMessageBox()
        messageWindow.setWindowTitle("Info")
        messageWindow.setText("File with saved events was not found. New file will be created.")
        messageWindow.exec()


def getEventTypesList():
    global eventTypesDictionary
    return sorted(eventTypesDictionary["eventTypes"].keys())


def getEventTypeColour(eventType):
    global eventTypesDictionary
    return eventTypesDictionary["eventTypes"][eventType]


def getEventsForDay(date: datetime) -> list[Event]:
    global eventsDictionary
    dayDataList = []
    if date.year in eventsDictionary and \
       date.month in eventsDictionary[date.year] and \
       date.day in eventsDictionary[date.year][date.month]:
        for event in eventsDictionary[date.year][date.month][date.day]:
            dayDataList.append(event)

    return dayDataList


def eventEncoder(event):
    if isinstance(event, Event):
        return event.to_dict()

#TODO method modify; 2 param: removedEventId, newEvent; remove old event, add new one