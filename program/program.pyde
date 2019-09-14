# transform file to display objects
import json

displays = []


class Display:
    def __init__(
        self,
        number=None,
        xLeft=None,
        xRight=None,
        yTop=None,
        yBottom=None,
        dWidth=None,
        dHeight=None,
    ):
        self.number = number
        self.xLeft = xLeft
        self.xRight = xRight
        self.yTop = yTop
        self.yBottom = yBottom
        self.dWidth = dWidth
        self.dHeight = dHeight
        self.exists = False

    def __repr__(self):
        return "<D{self.number} : ({self.xLeft} , {self.yTop}), ({self.xRight}, {self.yBottom})>".format(
            self=self
        )


class DisplayImporter:
    def __init__(self, filePath):
        self.filePath = filePath

    def importFile(self):
        with open(self.filePath) as fp:
            contents = json.loads(fp.read())
            for rectangle in contents["rectangles"]:
                displays.append(
                    Display(
                        rectangle["number"],
                        rectangle["x"],
                        rectangle["x"] + rectangle["width"],
                        rectangle["y"],
                        rectangle["y"] + rectangle["height"],
                        rectangle["width"],
                        rectangle["height"],
                    )
                )


def setup():
    fullScreen()
    di = DisplayImporter("../mapping/mapping.json")
    di.importFile()

    print(displays)
    print(len(displays))


def draw():
    rect(20, 40, 80, 100)
