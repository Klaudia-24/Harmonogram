import json
import os


def writeToJsonFile(fileName, dataToWrite, dictKey):

    if os.path.isfile(fileName) and os.access(fileName, os.R_OK):
        print("File exists and is readable")
        with open(fileName, 'rb') as file:
            fileData = json.load(file)
            fileData[dictKey].append(dataToWrite)
            file.seek(0)
            json.dump(fileData, file, indent=4)
            file.close()
    else:
        print("File does NOT exist or is NOT readable")
        with open(fileName, 'w') as file:
            newDict = dict()
            newDict[dictKey] = []
            newDict[dictKey].append(dataToWrite)
            jsonItem = json.dumps(newDict, indent=4)
            file.write(jsonItem)
            file.close()
