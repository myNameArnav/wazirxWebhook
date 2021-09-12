def parseJSON(coin):
    from wazirX_API import getPrice
    import json

    resp = json.loads(getPrice("var"))

    name = resp[coin]["name"]
    lastPrice = resp[coin]["last"]
    openPrice = resp[coin]["open"]
    return name, lastPrice, openPrice
