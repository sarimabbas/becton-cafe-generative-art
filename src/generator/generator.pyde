import json
import sys
from random import randint

sys.path.insert(0, "../utils")
from display import Display, DisplayImporter
from emoji import emojiLists


class GlobalV:
    displays = []
    scaleFactor = 0.5


def pickRandomEmoji():
    listStrs = list(emojiLists.keys())
    randomListIndex = randint(0, len(emojiLists) - 1)
    randomList = emojiLists[listStrs[randomListIndex]]
    randomEmoji = randomList[randint(0, len(randomList))]
    return randomEmoji


def setup():
    # size(1920 / 2, 1080 / 2)
    fullScreen(2)

    di = DisplayImporter("../mapper/mapping-final.json")
    di.importFile(GlobalV.displays)
    # di.dimensionScaler()

    print(pickRandomEmoji())
    print(GlobalV.displays)

    for d in GlobalV.displays:
        d.draw()


def draw():
    pass
