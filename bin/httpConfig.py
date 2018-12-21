'''
@author:wangchengyuan
@file:httpConfig.py
@time:2018/12/7下午3:58
@desc:
'''

import requests
from bin import readConfig
from bin.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()


class HttpConfig():
    def __init__(self):
        global host, port, timeout
        host=localReadConfig.get_urlrelate('host')
        timeout= localReadConfig.get_urlrelate('timeout')
        self.log = Log.get_log()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = ''

    def set_url(self):
        self.url = host + self.url

    def set_header(self, headers):
        self.headers = headers

    def set_params(self, params):
        self.params = params

    def set_data(self, data):
        self.data = data

    def set_file(self,file):
        self.file=file

    def get(self):
        self.set_url()
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            return response
        except TimeoutError:
            self.log.trace("time out")
            return None

    def post(self):
        self.set_url()
        try:
            response = requests.post(self.url,headers=self.headers,data=self.data,files=self.file,timeout=float(timeout))
            return response
        except TimeoutError:
            self.log.trace("time out")
            return None


