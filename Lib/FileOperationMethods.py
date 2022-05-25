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
            dictName[keyName] = dataFromFile[keyName]
    except FileNotFoundError:

        # TODO create empty file
        messageWindow = QMessageBox()
        messageWindow.setWindowTitle("Info")
        messageWindow.setText("File with saved events was not found. New file will be created.")
        messageWindow.exec()
        # TODO raise, file with own errors

    except PermissionError:

        messageWindow = QMessageBox()
        messageWindow.setWindowTitle("Info")
        messageWindow.setText("Occurred some problems with file permission.")
        messageWindow.exec()
