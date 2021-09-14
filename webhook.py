from os import altsep
from typing import Tuple
from parse import parseJSON
from url import *
from dhooks import Webhook, Embed

# coinList = ["btcusdt", "adainr", "adausdt"]

coinDict = {
    "btcusdt":[],
    "adausdt":[]
}

for i in coinDict:
    coinDict[i] = [name, lastPrice, openPrice] = (parseJSON(i))
    
    lastPrice = float(lastPrice)
    openPrice = float(openPrice)
    
    upORdown = str(round(lastPrice - openPrice, 3))
    
    if float(lastPrice) < float(openPrice):
        coinDict[i].append(upORdown)
        coinDict[i][0] = "🔴 " + name
        
    elif float(lastPrice) > float(openPrice):
        coinDict[i].append("+" + upORdown)
        coinDict[i][0] = "🟢 " + name
        
    else:
        coinDict[i].append (lastPrice + " :arrow_forward: ")
        coinDict[i][0] = "🔵 " + name
    
    perChange = str(round(((lastPrice - openPrice) / lastPrice)* 100, 2))
    
    # if perChange[:-1] not '-':
    #     perChange = "+" + perChange
    
    coinDict[i].append(perChange)
        
embedded = Embed(
    description = "Here is the prices: ")

for i in coinDict:
    embedded.add_field(name = "Name", value = coinDict[i][0], inline = False)
    embedded.add_field(name = "Price", value = coinDict[i][1], inline = True)
    embedded.add_field(name = "Change", value = coinDict[i][3], inline = True)
    embedded.add_field(name = "%", value = coinDict[i][4], inline = True)
    embedded.set_footer(".                                                                                                            .")
    
Webhook(bot_url).send(embed=embedded)
