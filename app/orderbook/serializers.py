from rest_framework import serializers
from orderbook import models

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Market
        fields = [
            "baseCurrencyCode",
            "counterCurrencyCode",
            "marketCode"
        ]


class MarketDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MarketData
        fields = [
            "market",
            "bid",
            "ask",
            "lastPrice",
            "lastSize",
            "volume24h",
            "change24h",
            "low24h",
            "high24h",
            "avg24h",
            "timestamp"
        ]


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Buyer
        fields = [
            "ordersTotalAmount",
            "ordersPrice",
            "timestamp"
        ]


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seller
        fields = [
            "ordersTotalAmount",
            "ordersPrice",
            "timestamp"
        ]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = [
            "amount",
            "price",
            "time",
            "type"
        ]