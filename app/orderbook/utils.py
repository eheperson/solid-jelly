import requests
from apscheduler.schedulers.background import BackgroundScheduler
from orderbook import views, models

class OrderBookCall():
    def __init__(self, token_, currency_):
        self.token = token_
        self.currency = currency_
        self.marketCode = token_ + currency_ + "/"
        #
        self.api =  "https://www.bitexen.com/api/v1/order_book/"
        res = requests.get(self.api + self.marketCode)
        self.status = res.status_code
        self.data = res.json()
        self.timestamp = self.data["data"]["ticker"]["timestamp"]
        
    def buyers(self):
        if self.status == 200:
            data = {}
            data["buyers"] = self.data["data"]["buyers"]
            data["timestamp"] = self.timestamp
            return data
        return -1

    def sellers(self):
        if self.status == 200:
            data = {}
            data["sellers"] = self.data["data"]["sellers"]
            data["timestamp"] = self.timestamp
            return data
        return -1

    def transactions(self):
        if self.status == 200:
            data = {}
            data["transactions"] = self.data["data"]["last_transactions"]
            data["timestamp"] = self.timestamp
            return data
        return -1

    def market(self):
        if self.status == 200:
            data = {}
            data["market"] = self.data["ticker"]["market"]
            data["timestamp"] = self.timestamp
            return self.data["data"]["ticker"]
        return -1


    def marketData(self):
        data = self.data["data"]["ticker"]
        if self.status == 200:
            tmp = {}
            tmp["bid"] = data["bid"]
            tmp["ask"] = data["ask"]
            tmp["last_price"] = data["last_price"]
            tmp["last_size"] = data["last_size"]
            tmp["volume_24h"] = data["volume_24h"]
            tmp["change_24h"] = data["change_24h"]
            tmp["low_24h"] = data["low_24h"]
            tmp["high_24h"] = data["high_24h"]
            tmp["avg_24h"] = data["avg_24h"]
            tmp["timestamp"] = data["timestamp"]
            return tmp
        return -1


def orderbookQuery():
    orderbook = OrderBookCall("BTC", "USDT")
    marketdata = orderbook.marketData()
    sellers = orderbook.sellers()
    buyers = orderbook.buyers()
    transactions = orderbook.transactions()

    if marketdata is not None:
        try:
            marketdataObject = models.MarketData.objects.create(bid=float(marketdata["bid"]),
                                                        ask=float(marketdata["ask"]),
                                                        lastPrice=float(marketdata["last_price"]),
                                                        lastSize=float(marketdata["last_size"]),
                                                        volume24h=float(marketdata["volume_24h"]),
                                                        change24h=float(marketdata["change_24h"]),
                                                        low24h=float(marketdata["low_24h"]),
                                                        high24h=float(marketdata["high_24h"]),
                                                        avg24h=float(marketdata["avg_24h"]),
                                                        timestamp=float(marketdata["timestamp"]),
                                                        )
            marketdataObject.save()
        except:
            pass

    if buyers is not None:
        try:
            allBuyers = buyers["buyers"]
            timestamp = buyers["timestamp"]
            for buyer in allBuyers:
                buyerObject = models.Buyer.objects.create(ordersTotalAmount=float(buyer["orders_total_amount"]),
                                                            ordersPrice=float(buyer["orders_price"]),
                                                            timestamp=float(timestamp))
                buyerObject.save()
        except:
            pass

    if sellers is not None:
        try:
            allSellers = sellers["sellers"]
            timestamp = sellers["timestamp"]
            for seller in allSellers:
                sellerObject = models.Seller.objects.create(ordersTotalAmount=float(seller["orders_total_amount"]),
                                                            ordersPrice=float(seller["orders_price"]),
                                                            timestamp=float(timestamp))
                sellerObject.save()
        except:
            pass

    if transactions is not None:
        try:
            allTransactions = transactions["transactions"]
            timestamp = transactions["timestamp"]
            for transaction in allTransactions:
                transactionObject = models.Transaction.objects.create(amount=float(transaction["amount"]),
                                                                      price=float(transaction["price"]),
                                                                      time=float(transaction["time"]),
                                                                      type=transaction["type"])
                transactionObject.save()
        except:
            pass


def solidScheduler():
    scheduler = BackgroundScheduler()    
    scheduler.add_job(orderbookQuery, "interval", seconds=10, id="orderbook_001", replace_existing=True)
    scheduler.start()