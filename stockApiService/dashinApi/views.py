from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .dashin_api.connect import CpUtil, CpSysDib
from .dashin_api.test import *

# Create your views here.

@api_view(['GET'])
def getConnect(request):
  is_connected = CpUtil().getConnect()
  if is_connected == 1:
    data = {
      'connected': True,
    }
  else:
    data = {
      'connected': False,
    }
  return Response(data)


@api_view(['GET'])
def getCount(request):
  stock_count = CpUtil().getCount()
  data = {
    'count': stock_count,
  }
  return Response(data)


@api_view(['GET'])
def getStockList(request):
  stocks_dict = CpUtil().getStockCodeAndName()
  data = {
    stocks_dict,
  }
  return Response(data)


@api_view(['GET'])
def getStockChart():
  stock_chart = CpSysDib().getStockChart()
  data = {
    stock_chart,
  }
  return Response(data)


def getTest():
  result = ggg()
  data = {
    'result': result,
  }
  return Response(data)