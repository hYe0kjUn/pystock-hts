import win32com.client
inStockWeek = win32com.client.Dispatch("dscbo1.StockWeek")
inStockWeek.SetInputValue(0, "A000660")

inStockWeek.BlockRequest()
count = inStockWeek.GetHeaderValue(1)                      # 데이터의 개수를 얻어옴

for i in range(count):
    day = inStockWeek.GetDataValue(0, i)
    starting_price = inStockWeek.GetDataValue(1, i)                          # 시가
    high_price = inStockWeek.GetDataValue(2, i)                               # 고가
    low_price = inStockWeek.GetDataValue(3, i)                                # 저가
    ending_price = inStockWeek.GetDataValue(4, i)                           # 종가
    print(day, starting_price, high_price, low_price, ending_price)   # 가격 출력
print(count)