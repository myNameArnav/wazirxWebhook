from requests.api import get


def getPrice(option):
    import requests
    import json
    
    r = requests.get("https://api.wazirx.com/api/v2/tickers")
    data = json.loads(r.text)
    
    if option == "var":
        resp = json.dumps(data, indent=4)
        return resp

    elif option == "file":
        with open("response.json", "w") as write_file:
            json.dump(data, write_file, indent=4)
