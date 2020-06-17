import requests
import json

class dashin():
  host = "localhost:8000/"

  def getConnected(self):
    url = self.host+"dashin/"
    return requests.get(url)

  def getStockCount(self):
    url = self.host+"dashin/stock/"
    return requests.get(url)

  def getStockChart(self ,request_count, stock_code, field):
    url = self.host+"dashin/stock/chart"
    data = {
      "request_count": request_count,
      "stock_code": stock_code,
      "field": field,
    }
    return requests.post(url, data)

  def getAllStocks(self):
    url = self.host+"dashin/stock"
    return requests.get(url)