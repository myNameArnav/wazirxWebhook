def parseJSON(coin):
    from wazirX_API import getPrice
    import json
    import datetime

    resp = json.loads(getPrice("var"))

    name = resp[coin]["name"]
    lastPrice = resp[coin]["last"]
    time = datetime.datetime.fromtimestamp(int(resp[coin]["at"])).strftime('%Y-%m-%d %H:%M:%S')
    return name, lastPrice, time
