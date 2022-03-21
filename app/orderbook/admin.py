from django.contrib import admin

from orderbook import models
# Register your models here.


admin.site.register(models.MarketData)
admin.site.register(models.Buyer)
admin.site.register(models.Seller)
admin.site.register(models.Transaction)