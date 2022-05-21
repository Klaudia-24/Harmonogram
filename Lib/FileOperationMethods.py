import json

from PyQt5.QtWidgets import QMessageBox


def writeToJsonFile(fileName, dataToWrite):

    with open(fileName, 'w') as file:
        jsonItem = json.dumps(dataToWrite, indent=4)
        file.write(jsonItem)


def readFromJsonFileToDict(fileName, dictName, keyName):
    try:
        with open(fileName, 'r') as file:
            dataFromFile = json.load(file)
            for i in dataFromFile[keyName]:
                dictName[keyName].append(i)
    except FileNotFoundError:

        messageWindow = QMessageBox()
        messageWindow.setWindowTitle("Info")
        messageWindow.setText("File with saved events was not found. New file will be created.")
        messageWindow.exec()
        #raise, file with own errors

    except PermissionError:

        messageWindow = QMessageBox()
        messageWindow.setWindowTitle("Info")
        messageWindow.setText("Occurred some problems with file permission.")
        messageWindow.exec()

def readFromJsonFileToDict_v2(fileName, dictName, keyName):
    try:
        with open(fileName, 'r') as file:
            dataFromFile = json.load(file)
            print(dataFromFile)
            dictName[keyName] = dataFromFile[keyName]
            # for i in dataFromFile[keyName]:
            #     dictName[keyName].append(i)
    except FileNotFoundError:

        messageWindow = QMessageBox()
        messageWindow.setWindowTitle("Info")
        messageWindow.setText("File with saved events was not found. New file will be created.")
        messageWindow.exec()
        #raise, file with own errors

    except PermissionError:

        messageWindow = QMessageBox()
        messageWindow.setWindowTitle("Info")
        messageWindow.setText("Occurred some problems with file permission.")
        messageWindow.exec()
