#TODO

# method for different objects
# generateButtonWithIcon -> image and width

# imagePath, minWidth, maxWidth
# ./WindowObjects/Resources/settingsImage.png
def getImageButtonStyleSheet(imagePath):
    return f'QPushButton {{border-radius: 6px;\
            background-image: url({imagePath});\
           background-position:center; \
           background-repeat:no-repeat; \
           min-width: 60px; \
           max-width: 50px; \
           }}\
           QPushButton:pressed {{\
           background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\
           stop: 0 #dadbde, stop: 1 #f6f7fa);\
           }}\
           QPushButton:flat {{\
           border: none;\
           }}\
           QPushButton:default {{\
           border-color: navy; \
           }}'

if __name__=="__main__":
    print(getImageButtonStyleSheet("./WindowObjects/Resources/settingsImage.png"))