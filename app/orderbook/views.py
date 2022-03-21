from django.shortcuts import render
from rest_framework import viewsets
import requests

from orderbook import (
    serializers,
    models,
    utils
)
# Create your views here


class MarketViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MarketSerializer

    def get_queryset(self):
        pass

    def get_market(self):
        pass


        
class MarketDataViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MarketDataSerializer

    def get_queryset(self): 
        data = models.MarketData.objects.all()
        return data

    def get_marketdata(self):
        orderbook = utils.OrderBookCall("BTC", "USDT")
        return orderbook.marketData()

    def save_marketdata(self):
        marketdata = self.get_marketdata()
        print(marketdata)
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


class SellerViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SellerSerializer
    
    def get_queryset(self):
        data = models.Seller.objects.all()
        return data

    def get_sellers(self):
        orderbook = utils.OrderBookCall("BTC", "USDT")
        return orderbook.sellers()

    def save_sellers(self):
        sellers = self.get_sellers()
        print(sellers)
        if sellers is not None:
            try:
                for key, value in sellers.items():
                    # sellerObject = models.Seller.objects.create(ordersTotalAmount=
                    print(key)
                    print(value)
            except:
                pass
    