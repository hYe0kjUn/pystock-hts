import win32com.client
import sys, os
import pythoncom


class CpUtil():

    def getClient(self, api_method):
        """
        [api_method]:
            Dispatch 를 통해 호출할 method
        """
        api_enpoint = f'CpUtil.{api_method}'
        
        pythoncom.CoInitialize()
        win_client = win32com.client.Dispatch(api_enpoint)
        pythoncom.CoUninitialize()

        return win_client

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
        pythoncom.CoInitialize()
        win_client = win32com.client.Dispatch(api_endpoint)
        pythoncom.CoUnInitialize()

        return win_client

    def getStockChart(self, stock_code=None):
        """
        stock_code 에 대한 chart return
        """
        if CpUtil().getConnect() == 1:
            api_method = 'StockChart'

            self.getClient(api_method).SetInputValue(0,stock_code)
            self.getClient(api_method).BlockRequest()

            data_count = self.getClient(api_method).GetHeaderValue(3)

            for i in range(data_count):
                return self.getClient(api_method).GetDataValue(0, i)
        else:
            return 'check the connected'


    

#print(CpUtil().getConnect('CpCybos'))

#print('Test [CpUtil.getConnect] --- ', CpUtil().getConnect())

#print('Test [CpUtil.getCount] --- ', CpUtil().getCount())

#print('Test [CpUtil.getStockCodeList] --- ', CpUtil().getStockCodeList())

#print('Test [CpUtil.getStockCodeToName] --- ',dashiCpUtilnApi().getStockCodeToName('A002220'))

print('Test [CpUtil.getStockCodeAndName] --- ', CpUtil().getStockCodeAndName())

#print('Test [] --- ', CpSysDib().getStockChart('A005930'))