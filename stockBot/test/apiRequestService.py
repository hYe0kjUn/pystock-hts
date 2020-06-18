import requests
import json

class dashin():
  host = "http://1.230.33.44:8000/"

  def getConnected(self):
    url = self.host+"dashin/"
    return requests.get(url)

  def getStockCount(self):
    url = self.host+"dashin/stock"
    return requests.get(url)

  def getStockChart(self , request_count, stock_code, field):
    url = self.host+"dashin/stock/chart"
    data = json.dumps({
      "request_count": int(request_count),
      "stock_code": str(stock_code),
      "field": int(field)
    })
    return requests.post(url=url, headers={'content-type': 'application/json'}, data=data)

  def getAllStocks(self):
    url = self.host+"dashin/stock/list"
    return requests.get(url)