import json
import requests
from parse import parseJSON
from url import testwebhook_url, webhook_url, bot_url
from dhooks import Webhook

coinList = ["btcusdt", "adainr"]

for i in coinList:
    namePriceTime = [name, lastPrice, time] = parseJSON(i)
    Webhook(bot_url).send(str(namePriceTime))