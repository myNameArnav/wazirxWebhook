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
    
    upORdown = str(round(float(lastPrice) - float(openPrice), 3))
    
    if float(lastPrice) < float(openPrice):
        coinDict[i].append(" :arrow_down_small: " + "( " + upORdown + ")")
        coinDict[i][0] = "🔴 " + name
        
    elif float(lastPrice) > float(openPrice):
        coinDict[i].append(" :arrow_up_small: " + "( "+ upORdown + ")")
        coinDict[i][0] = "🟢 " + name
        
    else:
        coinDict[i].append (lastPrice + " :arrow_forward: ")
        coinDict[i][0] = "🔵 " + name

embedded = Embed(
    description = "Here is the price",
)
embedded.set_author(name = "PriceBot")

for i in coinDict:
    embedded.add_field(name = "Name", value = coinDict[i][0])
    embedded.add_field(name = "Price", value = coinDict[i][1])
    embedded.add_field(name = "Change", value = coinDict[i][3])
    
Webhook(webhook_url).send(embed=embedded)
