# import win32com.client
# import time

# stock_codes = [
#     "A000020",
#     "A000040",
#     "A000215",
# "A000220",
# "A000225",
# "A000227",
# "A000230",
# "A000240",
# "A000270",
# "A000300",
# "A000320",
# "A000325",
# "A000370",
# "A000390",
# "A000400",
# "A000430",
# "A000480",
# "A000490",
# "A000500",
# "A000520",
# "A000540",
# "A000545",
# "A000547",
# "A000590",
# "A000640",
# "A000650",
# "A000660",
# "A000670",
# "A000680",
# "A000700",
# "A000720",
# "A000725",
# "A000760",
# "A000050",
# "A000060",
# "A000070",
# "A000075",
# "A000080",
# "A000087",
# "A000100",
# "A000105",
# "A000120",
# "A000140",
# "A000145",
# "A000150",
# "A000155",
# "A000157",
# "A000180",
# "A000210"
# ]

# # Create object
# def getNiceStock(stock_code):
#     instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

#     # SetInputValue
#     instStockChart.SetInputValue(0, stock_code)
#     instStockChart.SetInputValue(1, ord('2'))
#     instStockChart.SetInputValue(4, 60)
#     instStockChart.SetInputValue(5, 8)
#     instStockChart.SetInputValue(6, ord('D'))
#     instStockChart.SetInputValue(9, ord('1'))

#     # BlockRequest
#     instStockChart.BlockRequest()

#     # GetData
#     volumes = []
#     numData = instStockChart.GetHeaderValue(3)
#     for i in range(numData):
#         volume = instStockChart.GetDataValue(0, i)
#         volumes.append(volume)

#     # Calculate average volume
#     averageVolume = (sum(volumes) - volumes[0]) / (len(volumes) -1)

#     if(volumes[0] > averageVolume * 10):
#         print("good", stock_code)
#     else:
#         print("general", volumes[0] / averageVolume)
#     time.sleep(1)


# for i in stock_codes:
#     getNiceStock(i)