from requests import get
import json


orderBookUrl = "https://www.bitexen.com/api/v1/order_book/"

res = get(orderBookUrl+"BTCUSDT/")

data = res.json()
print(data["status"])
with open('data.json', 'w') as fp:
    json.dump(data, fp, indent=4)