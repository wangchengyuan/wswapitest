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
        self.log = Log.get_log()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None

    def set_url(self, url):
        self.url = host + url

    def set_header(self, headers):
        self.headers = headers

    def set_params(self, params):
        self.params = params

    def set_data(self, data):
        self.data = data

    def set_file(self,file):
        self.file=file

    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            return response
        except TimeoutError:
            self.log.trace("time out")
            return None

    def post(self):
        try:
            response = requests.post(self.url,headers=self.headers,data=self.data,files=self.file,timeout=float(timeout))
            return response
        except TimeoutError:
            self.log.trace("time out")
            return None
