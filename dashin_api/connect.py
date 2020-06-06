import win32com.client
import sys, os


class dashinApi():

    def getClient(self, api_method):
        api_enpoint = f'CpUtil.{api_method}'
        win_client = win32com.client.Dispatch(api_enpoint)
        return win_client

    # 연결 상태 확인
    def getConnect(self):
        return self.getClient('CpCybos').IsConnect

    # 전체 종목 수
    def getCount(self):
        return self.getClient('CpStockCode').getCount()

    # 전체 종목 코드 리스트
    def getStockCodeList(self):
        return self.getClient('CpCodeMgr').GetStockListByMarket(1)

    # 종목코드에 대한 종목 이름 반환
    def getStockCodeToName(self, stock_code):
        return self.getClient('CpCodeMgr').CodeToName(stock_code)

    # 전체 종목에 대한 코드 (key), 이름 (value) 반환
    def getStockCodeAndName(self):
        stock_code_list = self.getStockCodeList()
        stock_info_obj = {}
        for stock_code in stock_code_list:
            stock_name = self.getStockCodeToName(stock_code)
            stock_info_obj[stock_code] = stock_name
        return stock_info_obj

#dashinApi().getClient('CpCybos')

#print('Test [getConnect] --- ', dashinApi().getConnect())

#print('Test [getCount] --- ', dashinApi().getCount())

#print('Test [getStockCodeList] --- ', dashinApi().getStockCodeList())

#print('Test [getStockCodeToName] --- ',dashinApi().getStockCodeToName('A002220'))

print('Test [getStockCodeAndName] --- ',dashinApi().getStockCodeAndName())