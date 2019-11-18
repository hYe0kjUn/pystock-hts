def getBreakenPoint(total_stock_price,net_profit):
    breaken_point = int(total_stock_price)/int(net_profit)
    breaken_point = round(breaken_point, 2)
    result = breaken_point / 4
    result -= 50
    return result