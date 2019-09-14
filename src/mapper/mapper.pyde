import json
import sys

sys.path.insert(0, "../utils")
from display import Display


class GlobalV:
    # static variables
    rectA = 0
    rectB = 0
    rectC = 0
    rectD = 0
    isDrawing = False
    displayCount = 0
    displays = []


def setup():
    size(1920 / 2, 1080 / 2)
    # fullScreen()


def draw():
    # clear background
    if not GlobalV.isDrawing:
        background(255, 255, 255)
    # draw all displays
    for d in GlobalV.displays:
        if d.exists:
            d.draw()
    # cross-hairs
    textFont(createFont("Arial", 16, True))
    strokeWeight(3)
    stroke(color(250, 50, 50))
    line(mouseX, 0, mouseX, height)
    line(0, mouseY, width, mouseY)
    # coordinates next to cursor
    if mouseX >= width / 2:
        if mouseY >= height / 2:
            textAlign(RIGHT, BOTTOM)
        else:
            textAlign(RIGHT, TOP)
    else:
        if mouseY >= height / 2:
            textAlign(LEFT, BOTTOM)
        else:
            textAlign(LEFT, TOP)
    text("x: " + str(mouseX) + " y: " + str(mouseY), mouseX, mouseY)
    fill(0, 0, 0)


def mousePressed():
    if not GlobalV.isDrawing:
        # start drawing new object
        GlobalV.rectA = mouseX
        GlobalV.rectB = mouseY
        GlobalV.isDrawing = True
    else:
        # finish drawing new object
        GlobalV.isDrawing = False
        GlobalV.rectC = mouseX - GlobalV.rectA
        GlobalV.rectD = mouseY - GlobalV.rectB
        # set x,y coord as the top left hand corner
        if GlobalV.rectA > mouseX:
            GlobalV.rectA = mouseX
            GlobalV.rectC = GlobalV.rectC * -1
        if GlobalV.rectB > mouseY:
            GlobalV.rectB = mouseY
            GlobalV.rectD = GlobalV.rectD * -1
        # instantiate Display
        GlobalV.displays.append(
            Display(
                number=GlobalV.displayCount,
                xLeft=GlobalV.rectA,
                yTop=GlobalV.rectB,
                dWidth=GlobalV.rectC,
                dHeight=GlobalV.rectD,
            )
        )
        GlobalV.displayCount += 1


# track the mouse cursor as it draws
def mouseMoved():
    if GlobalV.isDrawing:
        background(255, 255, 255)
        draw()
        rect(
            GlobalV.rectA, GlobalV.rectB, mouseX - GlobalV.rectA, mouseY - GlobalV.rectB
        )


def keyPressed():
    # save
    if key == "s":
        saveFrame("mapping.png")
        mapping = {"rectangles": [d.toObj() for d in GlobalV.displays]}
        with open("mapping.json", "w") as fp:
            fp.write(json.dumps(mapping, sort_keys=True, indent=4))
    # exit
    if key == "e":
        exit()
    # undo
    if key == "z":
        GlobalV.displays.pop()
        GlobalV.displayCount -= 1
    # clear all
    if key == "d":
        GlobalV.displays = []
        GlobalV.displayCount = 0
