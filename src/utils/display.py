import json


class Display:
    def __init__(self, number=-1, xLeft=0, yTop=0, dWidth=0, dHeight=0, exists=True):
        self.number = number
        self.xLeft = xLeft
        self.yTop = yTop
        self.dWidth = dWidth
        self.dHeight = dHeight
        self.rgb = (random(255) * 1.3, random(255) * 1.3, random(255) * 1.3)
        self.exists = exists

    def __repr__(self):
        return "<D{self.number} : ({self.xLeft} , {self.yTop}), (width: {self.dWidth}, height: {self.dHeight})>".format(
            self=self
        )

    def toObj(self):
        return {
            "number": self.number,
            "xLeft": self.xLeft,
            "yTop": self.yTop,
            "dWidth": self.dWidth,
            "dHeight": self.dHeight,
            "exists": self.exists,
        }

    def clear(self):
        self.exists = False

    def draw(self, callback=None):
        if callback:
            callback(self)
        else:
            # rectangle
            fill(color(self.rgb[0], self.rgb[1], self.rgb[2]))
            rect(self.xLeft, self.yTop, self.dWidth, self.dHeight)

            # add text
            textFont(createFont("Arial", 16, True))
            fill(color(0, 0, 0))
            text(
                self.number, self.xLeft + self.dWidth / 2, self.yTop + self.dHeight / 2
            )


class DisplayImporter:
    def __init__(self, filePath):
        self.filePath = filePath

    def importFile(self, displays):
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
