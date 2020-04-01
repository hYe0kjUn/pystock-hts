import requests
import json
from bs4 import BeautifulSoup


def getKospi200Future():
    res = requests.get('https://kr.investing.com/indices/korea-200-futures')
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    now_price = soup.select(
        '#last_last'
    )
    print(now_price)

getKospi200Future()