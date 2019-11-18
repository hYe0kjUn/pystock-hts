from analy import basic, method

code = '035420'

total_stock_price = basic.getTotalStockPrice(code)
net_profit = basic.getNetProfit(code)

print("당기 순이익: ",format(net_profit,','), '원')
print("현재 주식 가격: ",format(basic.getNowPrice(code),','), '원')
print("총 주식 수: ",format(basic.getTotalStock(code),','), '주')
print("현재 시가 총액: ",format(total_stock_price,','),' 원')
print(60 - method.getBreakenPoint(total_stock_price,net_profit))

# 첫번째 가설 ("당기 순이익/현재 시가 총액 =" 이 20보다 많을 경우 1단위로 buy_point - 1, 반대인 경우 buy_point + 1)