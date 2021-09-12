from typing import Tuple
from parse import parseJSON
from url import *
from dhooks import Webhook, Embed

coinList = ["btcusdt", "adainr", "adausdt"]

for i in coinList:
    allInOne = [name, lastPrice, openPrice] = parseJSON(i)
    
    upORdown = str(round(float(lastPrice) - float(openPrice), 3))
    
    if float(lastPrice) < float(openPrice):
        price = " :arrow_down_small:  " + "( " + upORdown + ")"
        crl = 0xE32636
    
    elif float(lastPrice) > float(openPrice):
        price = " :arrow_up_small: " + "( "+ upORdown + ")"
        crl = 0x1DB954
        
    else:
        price = lastPrice + " :arrow_forward: "
    
    embeded = Embed(
        description = "Here is the price",
        color = crl
    )
    
    embeded.set_author(name = "PriceBot")
    embeded.add_field(name = "Name", value = name)
    embeded.add_field(name = "Price", value = lastPrice)
    embeded.add_field(name = "Change", value = price)
    
    Webhook(webhook_url).send(embed=embeded)
