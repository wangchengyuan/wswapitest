'''
@author:wangchengyuan
@file:Log.py
@time:2018/12/3上午11:34
@desc:
'''
import logging
from datetime import datetime
import time
import threading
import os
from bin import readConfig


class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        date = time.strftime('%Y%m%d%H%M%S')
        resultPath = os.path.join(proDir, 'result/%sresult' % date)
        logPath = os.path.join(proDir, 'log/%soutput.log' % date)

        # 定义logger
        self.logger = logging.getLogger()

        # 定义logger的level,level分为DEBUG、INFO、WARNING、ERROR、CRITICAL
        self.logger.setLevel(logging.DEBUG)

        # 定义handler,打印到日志文件中
        self.fh = logging.FileHandler(logPath, 'w')

        # 定义handler，打印到终端
        self.sh = logging.StreamHandler()

        # 定义formatter
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        self.fh.setFormatter(formatter)
        self.sh.setFormatter(formatter)

    def trace(self, message):
        self.logger.addHandler(self.fh)
        self.logger.info(message)

    def step(self, message):
        self.logger.addHandler(self.sh)
        self.logger.info(message)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log