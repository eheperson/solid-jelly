from django.db import models
from django.utils.timezone import now

from orderbook import models as orderbookModels
# Create your models here.


class Market(models.Model):
    baseCurrencyCode = models.CharField(max_length=5, unique=True)
    counterCurrencyCode = models.CharField(max_length=5)
    marketCode = models.CharField(max_length=10)
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.marketCode + " - " + str(self.date)

    def get_queryset(self):
        data = orderbookModels.Market.objects.all()
        return data

    @staticmethod
    def save_market(market_):
        market_ = market_["market"]
        print(market_)
        marketObject, _ = orderbookModels.Market.objects.get_or_create(baseCurrencyCode = market_["base_currency_code"],
                                                                    counterCurrencyCode = market_["counter_currency_code"],
                                                                    marketCode = market_["market_code"])
        # marketObject.save()
        print(marketObject)
        return marketObject

        


class MarketData(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    bid = models.FloatField()
    ask = models.FloatField()
    lastPrice = models.FloatField()
    lastSize = models.FloatField()
    volume24h = models.FloatField()
    change24h = models.FloatField()
    low24h = models.FloatField()
    high24h = models.FloatField()
    avg24h = models.FloatField()
    timestamp = models.FloatField()
    date = models.DateTimeField(default=now, editable=False)


    def __str__(self):
        return self.market.marketCode + "-data" + " - " + str(self.date)

    def get_queryset(self):
        data = orderbookModels.MarketData.objects.all()
        return data
    
    @staticmethod
    def save_marketdata(market_, marketdata_):
        marketdataObject = orderbookModels.MarketData.objects.create(market=market_,
                                                            bid=float(marketdata_["bid"]),
                                                            ask=float(marketdata_["ask"]),
                                                            lastPrice=float(marketdata_["last_price"]),
                                                            lastSize=float(marketdata_["last_size"]),
                                                            volume24h=float(marketdata_["volume_24h"]),
                                                            change24h=float(marketdata_["change_24h"]),
                                                            low24h=float(marketdata_["low_24h"]),
                                                            high24h=float(marketdata_["high_24h"]),
                                                            avg24h=float(marketdata_["avg_24h"]),
                                                            timestamp=float(marketdata_["timestamp"]),
                                                    )
        # marketdataObject.save()
        print(marketdataObject)

class Buyer(models.Model):
    market =  models.ForeignKey(Market, on_delete=models.CASCADE)
    ordersTotalAmount = models.FloatField()
    ordersPrice = models.FloatField()
    timestamp = models.FloatField()
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.market.marketCode + "-Buyer" + " - " + str(self.date)

    def get_queryset(self):
        data = orderbookModels.Buyer.objects.all()
        return data
    
    @staticmethod
    def save_buyers(market_, buyers):
        allBuyers = buyers["buyers"]
        timestamp = buyers["timestamp"]
        for buyer in allBuyers:
            buyerObject = orderbookModels.Buyer.objects.create(market=market_,
                                                        ordersTotalAmount=float(buyer["orders_total_amount"]),
                                                        ordersPrice=float(buyer["orders_price"]),
                                                        timestamp=float(timestamp))
            # buyerObject.save()
            print(buyerObject)



class Seller(models.Model):
    market =  models.ForeignKey(Market, on_delete=models.CASCADE)
    ordersTotalAmount = models.FloatField()
    ordersPrice = models.FloatField()
    timestamp = models.FloatField()
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.market.marketCode + "-Seller" + " - " + str(self.date)

    def get_queryset(self):
        data = orderbookModels.Seller.objects.all()
        return data
    
    @staticmethod
    def save_sellers(market_, sellers):
        allSellers = sellers["sellers"]
        timestamp = sellers["timestamp"]
        for seller in allSellers:
            sellerObject = orderbookModels.Seller.objects.create(market=market_,
                                                        ordersTotalAmount=float(seller["orders_total_amount"]),
                                                        ordersPrice=float(seller["orders_price"]),
                                                        timestamp=float(timestamp))
            # sellerObject.save()
            print(sellerObject)


class Transaction(models.Model):
    market =  models.ForeignKey(Market, on_delete=models.CASCADE)
    amount = models.FloatField()
    price = models.FloatField()
    time = models.FloatField()
    type = models.CharField(max_length=5)
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.market.marketCode + "-Transaction" + " - " + str(self.date)

    def get_queryset(self):
        data = orderbookModels.Transaction.objects.all()
        return data

    @staticmethod
    def save_transactions(market_, transactions):
        allTransactions = transactions["transactions"]
        timestamp = transactions["timestamp"]
        for transaction in allTransactions:
            transactionObject = orderbookModels.Transaction.objects.create(market=market_,
                                                                amount=float(transaction["amount"]),
                                                                price=float(transaction["price"]),
                                                                time=float(transaction["time"]),
                                                                type=transaction["type"])
            # transactionObject.save()
            print(transactionObject)