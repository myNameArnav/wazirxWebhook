import json
import requests
from parse import parseJSON
from url import *
from dhooks import Webhook, Embed, embed

coinList = ["btcusdt", "adainr", "adausdt"]

for i in coinList:
    namePriceTime = [name, lastPrice, time] = parseJSON(i)
    
    embeded = Embed(
        description = "Here is the price",
        color = 0x1DB954
    )
    
    embeded.set_author(name = "PriceBot")
    embeded.add_field(name = "Time", value = time)
    embeded.add_field(name = "Name", value = name)
    embeded.add_field(name = "Price", value = lastPrice)
    
    Webhook(webhook_url).send(embed=embeded)
