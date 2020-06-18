import apiRequestService as apiRequestService
import json
import time

dashin_api = apiRequestService.dashin()

stock_code_list = []
stock_name_list = []

is_connected = json.loads(dashin_api.getConnected().text)['connected']
if is_connected == True:
  json_stock_list = json.loads(dashin_api.getAllStocks().text)
  print("get stock_list success. ")

  # stock_name, stock_code 별로 list 만듬
  for key, value in json_stock_list.items():
    stock_code_list.append(key)
    stock_name_list.append(value)

  for stock_code, stock_name in zip(stock_code_list, stock_name_list):
    
    date_list = []
    volume_list = []

    json_stock_chart = json.loads(dashin_api.getStockChart(request_count=60, stock_code=stock_code, field=8))['result']
    print('get stock_chart success. ')

    # stock_chart 에서 date 와 volume 별로 list 만듬
    for key, value in json_stock_chart.items():
      date_list.append(key)
      volume_list.append(value)
    volume_average = (sum(volume_list) - volume_list[0]) / len(volume_list) - 1
    if volume_list[0] > volume_average:
      print(stock_code, stock_name)
