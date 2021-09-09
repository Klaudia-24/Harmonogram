import json


def writeToJsonFile(fileName, dataToWrite):

    with open(fileName, 'w') as file:
        jsonItem = json.dumps(dataToWrite, indent=4)
        file.write(jsonItem)


def readFromJsonFileToDict(fileName, dictName, keyName):
    with open(fileName, 'r') as file:
        dataFromFile = json.load(file)
        for i in dataFromFile[keyName]:
            dictName[keyName].append(i)