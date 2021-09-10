import json
import requests
from parse import parseJSON

coinList = ["btcusdt", "adainr"]

for i in coinList:
    name, lastPrice, time = parseJSON(i)
    print(name, lastPrice, time)