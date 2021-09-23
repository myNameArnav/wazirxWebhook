from os import altsep
from typing import Tuple
from parse import parseJSON
from url import *
from dhooks import Webhook, File
from img import responseImg

# coinList = ["btcusdt", "adainr", "adausdt"]

coinDict = {
    "btcusdt": [],
    "avaxinr": [],
    "shibinr": [],
    "adausdt": [],
    # "vetinr": [],
    # "uniusdt": [],
    # "xrpinr": [],
    # "ethusdt": []
}

for i in coinDict:
    coinDict[i] = [name, lastPrice, openPrice] = parseJSON(i)

    lastPrice = float(lastPrice)
    openPrice = float(openPrice)

    upORdown = str(round(lastPrice - openPrice, 3))

    if float(lastPrice) < float(openPrice):
        coinDict[i].append(upORdown)
        coinDict[i].append("")
        coinDict[i].append((239, 48, 84))

    elif float(lastPrice) > float(openPrice):
        coinDict[i].append("+" + upORdown)
        coinDict[i].append("")
        coinDict[i].append((141, 233, 105))

    else:
        coinDict[i].append(lastPrice + " :arrow_forward: ")
        coinDict[i].append("")
        coinDict[i].append((86, 203, 249))

    perChange = str(round(((lastPrice - openPrice) / lastPrice) * 100, 2))


    coinDict[i].append(perChange)

responseImg(coinDict)


imgFile = File("picture.png", name="output.png")

Webhook(webhook_url).send(file=imgFile)
