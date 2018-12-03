'''
@author:wangchengyuan
@file:readConfig.py
@time:2018/11/21下午7:40
@desc:增加读取配置文件类和方法
'''

import os
import configparser

# 定义获取配置文件的路径
proDir = os.path.dirname(os.path.dirname(__file__))
configDir = os.path.join(proDir, 'config/config.ini')


class ReadConfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configDir)

    # 增加获取对应配置的方法，获取 DATABASE、SSHRELATE，如有新配置，新增方法即可
    # 配置文件中DATABASE相关配置的获取和修改
    def get_database(self, name):
        value = self.cf.get('DATABASE', name)
        return value

    def set_database(self,name,value):
        self.cf.set('DATABASE',name,value)
        print('test')
        with open(configDir,'w+') as f:
            self.cf.write(f)

    # 配置文件中SSHRELATE相关配置的获取和修改
    def get_sshrelate(self, name):
        value = self.cf.get('SSHRELATE', name)
        return value

    def set_sshrelate(self,name,value):
        self.cf.set('SSHRELATE',name,value)
        with open(configDir,'w+') as f:
            self.cf.write(f)



