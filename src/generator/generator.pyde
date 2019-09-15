import json
import sys
import os
from random import randint, choice

sys.path.insert(0, "../utils")
from display import Display, DisplayImporter
from emoji import largePanelConfig


class GlobalV:
    displays = []


def pickRandomEmojiImage():
    imagesList = os.listdir("data/emoji-160")
    return choice(imagesList)


def smallPanelEmojiDraw(display):
    # black background
    fill(color(0, 0, 0))
    rect(display.xLeft, display.yTop, display.dWidth, display.dHeight)
    # get random emoji
    imageData = loadImage("emoji-160/" + pickRandomEmojiImage())
    # draw emoji
    imageMode(CENTER)
    image(
        imageData,
        display.xLeft + (display.dWidth / 2),
        display.yTop + (display.dHeight / 2),
        display.dHeight,  # size
        display.dHeight,  # size
    )


def largePanelConfigInit():
    xL = GlobalV.displays[0].xLeft
    yT = GlobalV.displays[0].yTop
    dW = GlobalV.displays[0].dWidth
    dH = GlobalV.displays[0].dHeight
    # column 1
    largePanelConfig[0]["x"] = xL + (dW / 6)
    largePanelConfig[0]["y"] = yT + (dH * 1 / 8)
    largePanelConfig[1]["x"] = xL + (dW / 6)
    largePanelConfig[1]["y"] = yT + (dH * 3 / 8)
    largePanelConfig[2]["x"] = xL + (dW / 6)
    largePanelConfig[2]["y"] = yT + (dH * 5 / 8)
    largePanelConfig[3]["x"] = xL + (dW / 6)
    largePanelConfig[3]["y"] = yT + (dH * 7 / 8)
    # column 2
    largePanelConfig[4]["x"] = xL + (dW * 3 / 6)
    largePanelConfig[4]["y"] = yT + (dH * 1 / 8)
    largePanelConfig[5]["x"] = xL + (dW * 3 / 6)
    largePanelConfig[5]["y"] = yT + (dH * 3 / 8)
    largePanelConfig[6]["x"] = xL + (dW * 3 / 6)
    largePanelConfig[6]["y"] = yT + (dH * 5 / 8)
    largePanelConfig[7]["x"] = xL + (dW * 3 / 6)
    largePanelConfig[7]["y"] = yT + (dH * 7 / 8)
    # column 3
    largePanelConfig[8]["x"] = xL + (dW * 5 / 6)
    largePanelConfig[8]["y"] = yT + (dH * 1 / 8)
    largePanelConfig[9]["x"] = xL + (dW * 5 / 6)
    largePanelConfig[9]["y"] = yT + (dH * 3 / 8)
    largePanelConfig[10]["x"] = xL + (dW * 5 / 6)
    largePanelConfig[10]["y"] = yT + (dH * 5 / 8)
    largePanelConfig[11]["x"] = xL + (dW * 5 / 6)
    largePanelConfig[11]["y"] = yT + (dH * 7 / 8)


def largePanelEmojiDraw():
    # get vars
    xL = GlobalV.displays[0].xLeft
    yT = GlobalV.displays[0].yTop
    dW = GlobalV.displays[0].dWidth
    dH = GlobalV.displays[0].dHeight
    # black background
    fill(color(0, 0, 0))
    rect(xL, yT, dW, dH)
    # draw the emojis
    imageMode(CENTER)
    for img in largePanelConfig:
        imageData = loadImage("emoji-160/" + pickRandomEmojiImage())
        # draw image
        image(imageData, img["x"], img["y"])
        # increment for next render
        direction = -1 if img["direction"] == "down" else 1
        # img["y"] = (img["y"] + (10 * direction)) % GlobalV.displays[0].dHeight


def setup():
    fullScreen(2)
    di = DisplayImporter("../mapper/mapping-final.json")
    di.importFile(GlobalV.displays)
    largePanelConfigInit()


def draw():
    # draw on the large panel
    largePanelEmojiDraw()
    # draw on the small panels outside
    for d in GlobalV.displays[1:]:
        d.draw(callback=smallPanelEmojiDraw)
    delay(5000)
