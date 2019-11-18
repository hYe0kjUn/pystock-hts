import requests
from bs4 import BeautifulSoup

def getNowPrice(finance_code):
    #naver finance 에서 주식 정보 가져오기
    res = requests.get(f'https://finance.naver.com/item/main.nhn?code={finance_code}')
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    #현재가
    now_prices = soup.select(
        '#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)'
    )
    for now_price in now_prices:
        now_price = now_price.text
        now_price = int(now_price.replace(',', ''))

    return now_price


def getTotalStockPrice(finance_code):
    #naver finance 에서 주식 정보 가져오기
    res = requests.get(f'https://finance.naver.com/item/main.nhn?code={finance_code}')
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    #시가 총액
    total_stock_prices = soup.select(
        '#content > div.section.trade_compare > table > tbody > tr:nth-child(4) > td:nth-child(2)'
    )
    for total_stock_price in total_stock_prices:
        total_stock_price = total_stock_price.text
        total_stock_price = int(total_stock_price.replace(',', ''))
        total_stock_price = total_stock_price * 100000000

    return total_stock_price


def getTotalStock(finance_code):
    #총 주식 수
    total_stock = getTotalStockPrice(finance_code) / getNowPrice(finance_code)
    total_stock = round(total_stock)
    
    return total_stock


def getNetProfit(finance_code):
    #naver finance 에서 주식 정보 가져오기
    res = requests.get(f'https://finance.naver.com/item/main.nhn?code={finance_code}')
    html = res.text
    soup = BeautifulSoup(html, 'lxml')

    #연간실적
    net_profits = soup.select(
        '#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(3) > td.last.cell_strong'
    )
    for net_profit in net_profits:
        net_profit = net_profit.text
        net_profit = int(net_profit.replace(',', ''))
        net_profit = net_profit * 100000000

    return net_profit