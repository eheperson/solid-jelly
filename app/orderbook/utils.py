import requests
from apscheduler.schedulers.background import BackgroundScheduler
from orderbook import views, models
from datetime import timedelta
from django.utils import timezone


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
            data["market"] = self.data["data"]["ticker"]["market"]
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


def orderbookQuery(token_, currency_):
    orderbook = OrderBookCall(token_, currency_)
    market = orderbook.market()
    marketdata = orderbook.marketData()
    buyers = orderbook.buyers()
    sellers = orderbook.sellers()
    transactions = orderbook.transactions()

    marketObject = models.Market.save_market(market)
    models.MarketData.save_marketdata(marketObject, marketdata)

    models.Buyer.save_buyers(marketObject, buyers)
    models.Seller.save_sellers(marketObject, sellers)
    models.Transaction.save_transactions(marketObject, transactions)
    
def main_scheduler():
    # experimentalDynamic()
    orderbookQuery('BTC', 'USDT')
    orderbookQuery('ETH', 'USDT')


def solidScheduler():
    scheduler = BackgroundScheduler(job_defaults={'max_instances': 5})  
    scheduler.add_job(main_scheduler, "interval", seconds=10, id="orderbook_001", replace_existing=True)
    scheduler.start()


def calculate_days(marketCode_, lastDays_):
    timedifference = timezone.now().date() - timedelta(days=lastDays_)
    marketdatas = models.MarketData.objects.filter(date__gte=timedifference).filter(market__marketCode__contains=marketCode_)
    
    min = 0.0
    max = 0.0
    avg = 0.0
    vol = 0.0
    n = len(marketdatas)
    res = {}
    
    for i in marketdatas:
        min += i.low24h
        max += i.high24h
        avg += i.avg24h
        vol += i.volume24h
    
    if n == 0: # zero division error
        n=1

    res["min"] = min/n
    res["max"] = max/n
    res["avg"] = avg/n
    res["vol"] = vol/n
    # print(res)
    return res


# def experimentalDynamic(token_, currency_, days_):
#     import os
#     baseDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
#     utils = os.path.join(baseDir, "utils.py")
#     res = {"error":"the signal is lost.."}
#     with open(utils, "r") as f:
#         lines = f.readlines()
#         if "    orderbookQuery('{}', '{}')\n".format(token_, currency_) not in lines:
#             index = None
#             for i,line in enumerate(lines):
#                 if line == "    orderbookQuery('ETH', 'USDT')\n":
#                     index = i
#                     break
#             lines.insert(index-1, "    orderbookQuery('{}', '{}')\n".format(token_, currency_))
#             with open(utils, "w") as f_inner:
#                 f_inner.writelines(lines)
#             res = calculate_days(token_+currency_, days_)
#         else:
#             res = calculate_days(token_+currency_, days_)

#     return res