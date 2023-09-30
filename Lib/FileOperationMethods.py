import json
import yaml
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


def writeSettingsToYamlFile(settingsList):
    with open('./Lib/appConfig.yaml', mode='wt', encoding="utf-8") as f:
        yaml.safe_dump_all(settingsList, f)

def readSettingsFromYamlFile():
    settingsList = []
    with open('./Lib/appConfig.yaml', 'r') as f:
        settingsList = list(yaml.safe_load_all(f))

    return settingsList

def readColourPalettesFromYamlFile():
    with open('./Lib/colourPalettes.yaml', 'r') as f:
        return yaml.safe_load(f)

