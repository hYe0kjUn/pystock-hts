import sys, os
import pythoncom
import win32com.client
import json 

class CpUtil():

    def getClient(self, api_method):
        """
        [api_method]:
            Dispatch 를 통해 호출할 method
        """
        api_enpoint = f'CpUtil.{api_method}'
        
        pythoncom.CoInitialize()
        win_client = win32com.client.Dispatch(api_enpoint)

        return win_client

    def getTest(self):
        return 1

    # 연결 상태 확인
    def getConnect(self):
        """
        1 (connected), 0 (disconnected) 의 값을 int 로 return
        """
        return self.getClient('CpCybos').IsConnect


    # 전체 종목 수
    def getCount(self):
        """
        전체 종목 갯수 int로 return
        """
        if self.getConnect() == 1:
            return self.getClient('CpStockCode').getCount()
        else:
            return 'check the connected'

    # 전체 종목 코드 리스트
    def getStockCodeList(self):
        """
        전체 종목 코드 리스트 return
        """
        if self.getConnect() == 1:
            return self.getClient('CpCodeMgr').GetStockListByMarket(1)
        else:
            return 'check the connected'

    # 종목코드에 대한 종목 이름 반환
    def getStockCodeToName(self, stock_code):
        """
        stock_code 에 대한 종목 이름을 str으로 return
        """
        if self.getConnect() == 1:
            return self.getClient('CpCodeMgr').CodeToName(stock_code)
        else:
            return 'check the connected'

    # 전체 종목에 대한 코드 (key), 이름 (value) 반환
    def getStockCodeAndName(self):
        """
        전체 종목에 대한 코드와 이름을 dict 로 return
        """
        if self.getConnect() == 1:
            stock_code_list = self.getStockCodeList()
            stock_info_obj = {}
            for stock_code in stock_code_list:
                stock_name = self.getStockCodeToName(stock_code)
                stock_info_obj[stock_code] = stock_name
            return stock_info_obj
        else:
            return 'check the connected'


class CpSysDib():
    
    def getClient(self, api_method):
        api_endpoint = f'CpSysDib.{api_method}'
        win_client = win32com.client.Dispatch(api_endpoint)

        return win_client

    def getStockChart(self, request_count, stock_code, request_field):
        """
        stock_code 에 대한 chart return
        """
        if CpUtil().getConnect() == 1:
            stock_chart_list = []
            date_list = []

            fields = [request_field, 0]

            instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
            
            for field in fields:
                instStockChart.SetInputValue(0, stock_code) #종목코드
                instStockChart.SetInputValue(1, ord('2')) #1=기간, 2=갯수
                instStockChart.SetInputValue(4, request_count) #요청 갯수

                #요청 받을 필드값
                instStockChart.SetInputValue(5, field)
                #0: 날짜 / 1: 시간 / 2: 시가 / 3: 고가 / 4: 저가 / 5: 종가 / 8: 거래량 / 9: 거래대금

                instStockChart.SetInputValue(6, ord('D')) #차트 구분
                # D: 일 / W: 주 / M: 월 / m: 분 / T: 틱

                instStockChart.SetInputValue(9, ord('1'))

                pythoncom.CoInitialize()
                instStockChart.BlockRequest()

                data_count = instStockChart.GetHeaderValue(3)
                
                if stock_chart_list:
                    for i in range(data_count):
                        year = str(instStockChart.GetDataValue(0, i))[0:4]
                        month = str(instStockChart.GetDataValue(0, i))[4:6]
                        day = str(instStockChart.GetDataValue(0, i))[6:]
                        date = f'{year}-{month}-{day}'
                        date_list.append(date)
                else:
                    for i in range(data_count):
                        stock_chart_list.append(instStockChart.GetDataValue(0, i))

            return date_list, stock_chart_list
        else:
            return 'check the connected'

    def getStockPer(self, stock_code):
        """
        stock_code 에 대한 PER 지수 반환
        """
        if CpUtil().getConnect() == 1:
            instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

            instMarketEye.SetInputValue(0, (4, 67, 70, 111))
            instMarketEye.SetInputValue(1, stock_code)

            pythoncom.CoInitialize()
            instMarketEye.BlockRequest()

            now_price = instMarketEye.GetDataValue(0, 0)
            per = instMarketEye.GetDataValue(1, 0)
            eps = instMarketEye.GetDataValue(2, 0)
            last_year = instMarketEye.GetDataValue(3, 0)

            return now_price, per, eps, last_year


    

# print(CpUtil().getConnect())

#print('Test [CpUtil.getCount] --- ', CpUtil().getCount())

#print('Test [CpUtil.getStockCodeList] --- ', CpUtil().getStockCodeList())

#print('Test [CpUtil.getStockCodeToName] --- ',CpUtil().getStockCodeToName('A002220'))
#print('Test [CpUtil.getStockCodeAndName] --- ', CpUtil().getStockCodeAndName())
# print('Test [getStockChart] --- ', CpSysDib().getStockChart(10,'A003540',5))