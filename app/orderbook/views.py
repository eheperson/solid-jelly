from django.shortcuts import render
from rest_framework import viewsets
import requests
from orderbook import utils
# import importlib
from django.http import JsonResponse


def BTCUSDT_view(request, days_):
    # importlib.reload(utils)
    res = utils.calculate_days("BTCUSDT", days_)
    return JsonResponse(res)

def ETHUSDT_view(request, days_):
    # importlib.reload(utils)
    res = utils.calculate_days("ETHUSDT", days_)
    return JsonResponse(res)

# def experimental_view(request, token_, currency_, days_):
    # importlib.reload(utils)
    # print(token_.upper(), currency_.upper(), days_)
    # res = utils.experimentalDynamic(token_.upper(), currency_.upper(), days_)
    # return JsonResponse(res)