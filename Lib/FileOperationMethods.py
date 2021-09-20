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
        #TODO add dialog window with information

        messageWindow = QMessageBox()
        messageWindow.setWindowTitle("File not found")
        messageWindow.setText("File with saved events was not found. New file will be created.")
        button = messageWindow.exec()

        if button == QMessageBox.Ok:
            print("OK!")

    except PermissionError:

        messageWindow = QMessageBox()
        messageWindow.setWindowTitle("Problem with permission")
        messageWindow.setText("Occurred some problems with file permission.")
        button = messageWindow.exec()

        if button == QMessageBox.Ok:
            print("OK!")
