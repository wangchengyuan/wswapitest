'''
@author:wangchengyuan
@file:readConfig.py
@time:2018/11/21下午7:40
@desc:
'''

import os
import configparser
import codecs

#定义获取配置文件的路径
proDir = os.path.dirname(os.path.dirname(__file__))
configDir = os.path.join(proDir,'config/config.ini')

class ReadConfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configDir)

    #增加获取对应配置的方法，获取 DATABASE、SSHRELATE，如有新配置，新增方法即可
    def get_database(self,name):
        value = self.cf.get('DATABASE',name)
        return value

    def get_email(self,name):
        value = self.cf.get('SSHRELATE',name)
        return value




