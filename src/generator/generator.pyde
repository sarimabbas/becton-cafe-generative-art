import json
import sys
import os
from random import randint, choice

sys.path.insert(0, "../utils")
from display import Display, DisplayImporter
from emoji import emojiLists


class GlobalV:
    displays = []
    scaleFactor = 0.5


# class EmojiDisplay(Display):


# def pickRandomEmoji():
#     listStrs = list(emojiLists.keys())
#     randomListIndex = randint(0, len(emojiLists) - 1)
#     randomList = emojiLists[listStrs[randomListIndex]]
#     randomEmoji = randomList[randint(0, len(randomList) - 1)]
#     return randomEmoji


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


def setup():
    # size(1920 / 2, 1080 / 2)
    fullScreen(2)

    di = DisplayImporter("../mapper/mapping-final.json")
    di.importFile(GlobalV.displays)
    # di.dimensionScaler()

    # # draw small panels
    # for d in GlobalV.displays[1:]:
    #     d.draw(callback=smallPanelEmojiDraw)


def draw():
    for d in GlobalV.displays[1:]:
        d.draw(callback=smallPanelEmojiDraw)
    delay(5000)
