def getPrice():
    import requests
    import json
    
    r = requests.get("https://api.wazirx.com/api/v2/tickers")

    # print(r.text)

    data = json.loads(r.text)

    with open("response.json", "w") as write_file:
        json.dump(data, write_file, indent=4)
