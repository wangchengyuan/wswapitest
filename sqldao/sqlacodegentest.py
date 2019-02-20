'''
@author:wangchengyuan
@file:sqlacodegentest.py
@time:2019/1/30下午7:00
@desc:
'''

import os
from bin import readConfig

proDir=os.path.dirname(__file__)
print(proDir)

def sqlacodegenTest(tablename):
    readconf = readConfig.ReadConfig()
    filename = tablename + '.py'
    host = readconf.get_database('host')
    user = readconf.get_database('user')
    passwd = readconf.get_database('passwd')
    db = readconf.get_database('db')
    dbaddress = 'mysql+pymysql://{}:{}@{}/{}'.format(user, passwd, host, db)
    lines = 'sqlacodegen --tables %s --outfile %s ' % (tablename, filename) + dbaddress
    print(lines)
    if os.path.exists(filename):
        print('文件已存在')
    else:
        print('文件不存在')
        os.system(lines)


if __name__ == '__main__':
    sqlacodegenTest('users')