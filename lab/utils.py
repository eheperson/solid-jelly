import requests


class OrderBook():
    def __init__(self, token_, currency_):
        self.token = token_
        self.currency = currency_
        self.marketCode = token_ + currency_ + "/"
        #
        self.api =  "https://www.bitexen.com/api/v1/order_book/"
        res = requests.get(self.api + self.marketCode)
        self.status = res.status_code
        self.data = res.json()
        
    def buyers(self):
        if self.status == 200:
            return self.data["data"]["buyers"]
        return -1

    def sellers(self):
        if self.status == 200:
            return self.data["data"]["sellers"]
        return -1

    def transactions(self):
        if self.status == 200:
            return self.data["data"]["transactions"]
        return -1

    def ticker(self):
        if self.status == 200:
            return self.data["data"]["transactions"]
        return -1

    def timestamp(self):
        if self.status == 200:
            return self.data["data"]["timestamp"]
        return -1



    

ob = OrderBook("BTC", "TRY")

print(ob.buyers())
