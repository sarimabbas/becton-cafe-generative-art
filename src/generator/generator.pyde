import json
import sys

sys.path.insert(0, "../utils")
from display import Display

displays = []


class DisplayImporter:
    def __init__(self, filePath):
        self.filePath = filePath

    def importFile(self):
        with open(self.filePath) as fp:
            contents = json.loads(fp.read())
            for rectangle in contents["rectangles"]:
                displays.append(
                    Display(
                        number=rectangle["number"],
                        xLeft=rectangle["x"],
                        yTop=rectangle["y"],
                        dWidth=rectangle["width"],
                        dHeight=rectangle["height"],
                    )
                )

    def dimensionScaler(self):
        for d in displays:
            d.xLeft = 1.5 * d.xLeft
            d.dWidth = 1.5 * d.dWidth
            d.yTop = (5 / 3) * d.yTop
            d.dHeight = (5 / 3) * d.dHeight


def setup():
    fullScreen()
    background(0)
    noStroke()
    di = DisplayImporter("../mapper/mapping.json")
    di.importFile()
    di.dimensionScaler()

    print(displays[0])
    print(displays[0].dWidth, displays[0].dHeight)

    for d in displays:
        rect(d.xLeft, d.yTop, d.dWidth, d.dHeight)


def draw():
    pass
