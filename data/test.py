import requests
import csv


def requestTrade(date,code):
    url = f'http://hogaplay.com/player/contract.php?d={date}&c={code}'
    res = requests.get(url)
    with open(f'{code}.csv','w') as temp:
        temp.write(res.text)
    getLowAndMaxPrice(code)


def getLowAndMaxPrice(code):
    with open(f'{code}.csv','r') as csv_file:
        csv_file = csv.reader(csv_file)
        high_price = 0
        low_price = 10000000000000000000
        for i in csv_file:
            s_time = i[0]
            s_price = i[1]
            s_count = i[2]
            if s_price == "체결가":
                pass
            else:
                s_price = int(s_price)
                if high_price <= s_price:
                    high_price = s_price
                    high_time = s_time
                    high_count = s_count
                elif low_price >= s_price:
                    low_price = s_price
                    low_time = s_time
                    low_count = s_count
        print('high p :',high_price)
        print('high t :',high_time)
        print('high c :',high_count)
        print('- - -')
        print('low p :',low_price)
        print('low t :',low_time)
        print('low c :',low_count)


requestTrade('20200309','005930')