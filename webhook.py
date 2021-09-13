from typing import Tuple
from parse import parseJSON
from url import *
from dhooks import Webhook, Embed

coinList = ["btcusdt", "adainr", "adausdt"]

priceDict = {
    "btcusdt":[],
     "adainr":[],
     "adausdt":[]
}

j = parseJSON("adausdt")
for i in coinList:
    priceDict[i] = [name, lastPrice, openPrice] = (parseJSON(i))
    
    upORdown = str(round(float(lastPrice) - float(openPrice), 3))
    
    if float(lastPrice) < float(openPrice):
        priceDict[i].append(" :arrow_down_small:  " + "( " + upORdown + ")")
    
    elif float(lastPrice) > float(openPrice):
        priceDict[i]["price"]= " :arrow_up_small: " + "( "+ upORdown + ")"
        
    else:
        priceDict[i]["price"] = lastPrice + " :arrow_forward: "
    
embeded = Embed(
    description = "Here is the price",
)
embeded.set_author(name = "PriceBot")

for i in priceDict:
    embeded.add_field(name = "Name", value = priceDict[i][0])
    embeded.add_field(name = "Price", value = priceDict[i][1])
    embeded.add_field(name = "Change", value = priceDict[i][3])
    
Webhook(webhook_url).send(embed=embeded)

