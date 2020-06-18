import apiRequestService as apiRequestService
import json
import time

stock_code_list = []
stock_name_list = []

date_list = []
volume_list = []


json_connected = json.loads(apiRequestService.dashin().getConnected().text)

if json_connected['connected'] == True:
  stock_list = apiRequestService.dashin().getAllStocks()
  time.sleep(1)
  json_stock_list = json.loads(stock_list.text)
  for key, value in json_stock_list.items():
    stock_code_list.append(key)
    stock_name_list.append(value)

  for stock_code, stock_name in zip(stock_code_list, stock_name_list):
    stock_chart = apiRequestService.dashin().getStockChart(60, stock_code, 8)
    json_stock_chart = json.loads(stock_chart.text)
    result = json_stock_chart['result']

    for key, value in result.items():
      date_list.append(key)
      volume_list.append(value)

    average_volume = (sum(volume_list) - volume_list[0]) / (len(volume_list) - 1)

    if volume_list[0] > average_volume * 10:
      print(f'nice stock {stock_code} {stock_name}')
      time.sleep(0.5)
    else:
      print(f'general {stock_code} {stock_name}')
      time.sleep(0.5)
else:
  print("check the connected.")