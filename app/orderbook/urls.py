from django.urls import path

from orderbook import views

urlpatterns = [
    # ex: /btcusdt/5/
    path('btcusdt/<int:days_>/', views.BTCUSDT_view, name='btc-usdt'),
    # ex: /ethusdt/5/
    path('ethusdt/<int:days_>/', views.ETHUSDT_view, name='eth-usdt'),

    # this section is experimental
    # ex: /experimental/BTC/USDT/5
    # path('experimental/<str:token_>/<str:currency_>/<int:days_>/', views.experimental_view, name='experimental'),
]