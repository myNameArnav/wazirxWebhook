from os import altsep
from typing import Tuple
from parse import parseJSON
from url import *
from dhooks import Webhook, File
from img import responseImg

# coinList = ["btcusdt", "adainr", "adausdt"]

coinDict = {
    "btcusdt": [],
    "adausdt": []
}

for i in coinDict:
    coinDict[i] = [name, lastPrice, openPrice] = parseJSON(i)

    lastPrice = float(lastPrice)
    openPrice = float(openPrice)

    upORdown = str(round(lastPrice - openPrice, 3))

    if float(lastPrice) < float(openPrice):
        coinDict[i].append(upORdown)
        coinDict[i].append("")
        coinDict[i].append((255,0,0))

    elif float(lastPrice) > float(openPrice):
        coinDict[i].append("+" + upORdown)
        coinDict[i].append("")
        coinDict[i].append((0,255,0))

    else:
        coinDict[i].append(lastPrice + " :arrow_forward: ")
        coinDict[i].append("")
        coinDict[i].append((0,0,255))

    perChange = str(round(((lastPrice - openPrice) / lastPrice) * 100, 2))

    # if perChange[:-1] not '-':
    #     perChange = "+" + perChange

    coinDict[i].append(perChange)

responseImg(coinDict)

hook = Webhook(webhook_url)
imgFile = File("picture.png", name="output.png")
# # embedded = Embed(
# #     description="Here is the prices: ")

# # for i in coinDict:
# #     embedded.add_field(name="Name", value=coinDict[i][0], inline=False)
# #     embedded.add_field(name="Price", value=coinDict[i][1], inline=True)
# #     embedded.add_field(name="Change", value=coinDict[i][3], inline=True)
# #     embedded.add_field(name="%", value=coinDict[i][4], inline=True)
# #     embedded.set_footer(
# #         ".                                                                                                            .")

# # embedded.send(imgFile)
hook.send("Yo sup", file=imgFile)
