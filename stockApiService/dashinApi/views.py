from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

import asyncio

import win32com.client

import pythoncom
#from .dashin_api.connect import CpUtil, CpSysDib

# Create your views here.

class CpUtil():
    
    def getClient(self, api_method):
        api_enpoint = f'CpUtil.{api_method}'
        win_client = win32com.client.Dispatch(api_enpoint)
        return win_client

    def getTest(self):
        return 1

    # 연결 상태 확인
    def getConnect(self):
        return self.getClient('CpCybos').IsConnect

    def getCount(self):
        if self.getConnect() == 1:
            return self.getClient('CpStockCode').getCount()
        else:
            return 'check the connected'


def getClient(api_method):
    api_enpoint = f'CpUtil.{api_method}'
    win_client = win32com.client.Dispatch(api_enpoint)
    return win_client



@api_view(['GET'])
def getConnect(request):
    is_connected = CpUtil().getConnect()

    if is_connected == 1:
        data = {
            'result': True,
        }
    else:
        data = {
            'result': False,
        }
    return Response(data, content_type='application/json')



def getCount(request):
    stock_count = CpUtil().getCount()
    data = {
        'count': stock_count,
    }
    return Response(data, content_type='application/json')


@api_view(['GET'])
def getTest(request):
    if CpUtil().getTest() == 1:
        data = {
            'hello': 'world',
        }
    else:
        data = {
            'hello': 'll',
        }
    return Response(data)

