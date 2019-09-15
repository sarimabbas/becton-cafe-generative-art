import json
import sys
import os
from random import randint, choice

sys.path.insert(0, "../utils")
from display import Display, DisplayImporter


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


def largePanelEmojiDraw(display):
    # black background
    fill(color(0, 0, 0))
    rect(display.xLeft, display.yTop, display.dWidth, display.dHeight)
    # get a column of emojis
    emojiList = [
        # first column
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth / 6),
            "y": display.yTop + (display.dHeight * 1 / 8),
        },
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth / 6),
            "y": display.yTop + (display.dHeight * 3 / 8),
        },
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth / 6),
            "y": display.yTop + (display.dHeight * 5 / 8),
        },
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth / 6),
            "y": display.yTop + (display.dHeight * 7 / 8),
        },
        # second column
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth * 3 / 6),
            "y": display.yTop + (display.dHeight * 1 / 8),
        },
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth * 3 / 6),
            "y": display.yTop + (display.dHeight * 3 / 8),
        },
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth * 3 / 6),
            "y": display.yTop + (display.dHeight * 5 / 8),
        },
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth * 3 / 6),
            "y": display.yTop + (display.dHeight * 7 / 8),
        },
        # third column
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth * 5 / 6),
            "y": display.yTop + (display.dHeight * 1 / 8),
        },
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth * 5 / 6),
            "y": display.yTop + (display.dHeight * 3 / 8),
        },
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth * 5 / 6),
            "y": display.yTop + (display.dHeight * 5 / 8),
        },
        {
            "column": 0,
            "direction": "down",
            "x": display.xLeft + (display.dWidth * 5 / 6),
            "y": display.yTop + (display.dHeight * 7 / 8),
        },
    ]
    imageMode(CENTER)
    for img in emojiList:
        imageData = loadImage("emoji-160/" + pickRandomEmojiImage())
        # draw image
        image(imageData, img["x"], img["y"])


def setup():
    fullScreen()
    di = DisplayImporter("../mapper/mapping-final.json")
    di.importFile(GlobalV.displays)


def draw():
    # draw on the large panel
    GlobalV.displays[0].draw(callback=largePanelEmojiDraw)
    # draw on the small panels outside
    for d in GlobalV.displays[1:]:
        d.draw(callback=smallPanelEmojiDraw)
    delay(5000)
