class Display:
    def __init__(self, number=-1, xLeft=0, yTop=0, dWidth=0, dHeight=0):
        self.number = number
        self.xLeft = xLeft
        self.yTop = yTop
        self.dWidth = dWidth
        self.dHeight = dHeight
        self.rgb = (random(255) * 1.3, random(255) * 1.3, random(255) * 1.3)
        self.exists = True

    def __repr__(self):
        return "<D{self.number} : ({self.xLeft} , {self.yTop}), (width: {self.dWidth}, height: {self.dHeight})>".format(
            self=self
        )

    def clear(self):
        self.exists = False

    def draw(self):
        # rectangle
        fill(color(self.rgb[0], self.rgb[1], self.rgb[2]))
        rect(self.xLeft, self.yTop, self.dWidth, self.dHeight)

        # add text
        textFont(createFont("Arial", 16, True))
        fill(color(0, 0, 0))
        text(self.number, self.xLeft + self.dWidth / 2, self.yTop + self.dHeight / 2)
