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


@api_view(['POST'])
def getStockChart(request):
  json_body = json.loads(request.body)
  result = {}
  if json_body:
    try:
      #json_body parsing
      request_count = json_body['request_count']
      stock_code = json_body['stock_code']
      field = json_body['field']
    except:
      data = {
        "result": "didn't parse json",
      }
    try:
      date_list, stock_chart_list = CpSysDib().getStockChart(request_count, stock_code, field)
      for date, stock_chart in zip(date_list, stock_chart_list):
        result[date] = stock_chart
      data = {
        "stock_code": stock_code,
        "stock_name": CpUtil().getStockCodeToName(stock_code),
        "result": result,
      }
      status = 200
    except:
      data = {
        "result": "json data is invalid"
      }
      status = 400
  else:
    data = {
      "result": "has no json body",
    }
    status = 400
  return Response(data, status)


@api_view(['GET'])
def getStockTechChart(request, stock_code):
  try:
    now_price, per, esp, last_year = CpSysDib().getStockPer(stock_code)
    year = str(last_year)[0:4]
    month = str(last_year)[4:]
    last_year = f'{year}-{month}'
    data = {
      "stock_code": stock_code,
      "stock_name": CpUtil().getStockCodeToName(stock_code),
      "result": {
        "now_price": now_price,
        "per": per,
        "esp": esp,
        "last_year": last_year,
      },
    }
  except:
    data = {
      "result": "stock_code is invalid",
    }
  return Response(data)
