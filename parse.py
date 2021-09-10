from wazirX_API import getPrice
import json
import datetime

resp = json.loads(getPrice("var"))

btcLast = resp["btcusdt"]["last"]
time = datetime.datetime.fromtimestamp(int(resp["btcusdt"]["at"])).strftime('%Y-%m-%d %H:%M:%S')

print("BTC/USDT at " + time + " was " + btcLast)