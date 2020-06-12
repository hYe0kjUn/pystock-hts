from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

import json

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
  data = CpUtil().getStockCodeAndName()
  return Response(data)


@api_view(['GET'])
def getStockChart():
  stock_chart = CpSysDib().getStockChart()
  data = {
    stock_chart,
  }
  return Response(data)
