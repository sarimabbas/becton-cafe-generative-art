import json
import sys

sys.path.insert(0, "../utils")
from display import Display

displays = []

scaleFactor = 0.5


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
                        xLeft=rectangle["xLeft"],
                        yTop=rectangle["yTop"],
                        dWidth=rectangle["dWidth"],
                        dHeight=rectangle["dHeight"],
                    )
                )

    def dimensionScaler(self):
        for d in displays:
            d.xLeft = d.xLeft * scaleFactor
            d.dWidth = d.dWidth * scaleFactor
            d.yTop = d.yTop * scaleFactor
            d.dHeight = d.dHeight * scaleFactor


def setup():
    # size(1920 / 2, 1080 / 2)
    fullScreen(2)
    # background(0)
    # noStroke()
    di = DisplayImporter("../mapper/mapping-final.json")
    di.importFile()
    # di.dimensionScaler()

    print(displays[0])
    print(displays[0].dWidth, displays[0].dHeight)

    for d in displays:
        d.draw()


def draw():
    pass
