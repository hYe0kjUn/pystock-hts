
from stockApiService.dashinApi.dashin_api.connect import CpUtil, CpSysDib
import sys

print("getConnected: ", CpUtil().getConnected())
print("getStockCount: ", CpUtil().getStockCount())
# print("getStockCodeList: ", CpUtil().getStockCodeList())
print("getStockCodeToName: ", CpUtil().getStockCodeToName('A005930'))
# print("getStockCodeAndName: ", CpUtil().getStockCodeAndName())
# print("getStockChartPriceToDate: ", CpSysDib().getStockChartPriceToDate(60, 'Q590007'))
print("getStockPer: ", CpSysDib().getStockPer("A005930"))