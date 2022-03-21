from pyexpat import model
from django.db import models

# Create your models here.


class Market(models.Model):
    baseCurrencyCode = models.CharField(max_length=5)
    counterCurrencyCode = models.CharField(max_length=5)
    marketCode = models.CharField(max_length=10)

    def __str__(self):
        return self.marketCode


class MarketData(models.Model):
    # market = models.ForeignKey(Ticker, on_delete=models.CASCADE)
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

class Buyer(models.Model):
    ordersTotalAmount = models.FloatField()
    ordersPrice = models.FloatField()
    timestamp = models.FloatField()


class Seller(models.Model):
    ordersTotalAmount = models.FloatField()
    ordersPrice = models.FloatField()
    timestamp = models.FloatField()


class Transaction(models.Model):
    amount = models.FloatField()
    price = models.FloatField()
    time = models.FloatField()
    type = models.CharField(max_length=5)