from analy import profit

code = '035420'

print("당기 순이익: ",profit.getNetProfit(code))
print("현재 주식 가격: ",profit.getNowPrice(code))
print("총 주식 수: ",profit.getTotalStock(code))
print("현재 시가 총액: ",profit.getTotalStockPrice(code))