from typing import Tuple
from parse import parseJSON
from url import *
from dhooks import Webhook, Embed

# coinList = ["btcusdt", "adainr", "adausdt"]

coinDict = {
    "btcusdt":[],
     "adainr":[],
     "adausdt":[]
}

for i in coinDict:
    coinDict[i] = [name, lastPrice, openPrice] = (parseJSON(i))
    
    upORdown = str(round(float(lastPrice) - float(openPrice), 3))
    
    if float(lastPrice) < float(openPrice):
        coinDict[i].append(" :arrow_down_small: " + "( " + upORdown + ")")
    
    elif float(lastPrice) > float(openPrice):
        coinDict[i].append(" :arrow_up_small: " + "( "+ upORdown + ")")
        
    else:
        coinDict[i].append (lastPrice + " :arrow_forward: ")
    
embeded = Embed(
    description = "Here is the price",
)
embeded.set_author(name = "PriceBot")

for i in coinDict:
    embeded.add_field(name = "Name", value = coinDict[i][0])
    embeded.add_field(name = "Price", value = coinDict[i][1])
    embeded.add_field(name = "Change", value = coinDict[i][3])
    
Webhook(webhook_url).send(embed=embeded)

