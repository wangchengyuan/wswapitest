'''
@author:wangchengyuan
@file:datadeal.py
@time:2018/11/16下午10:18
@desc:
'''

import pymysql
from sshtunnel import SSHTunnelForwarder
import paramiko

class DataDeal():

    #初始化读取配合文件
    def __init__(self):
        print()

    #通过ssh方式访问数据库
    def dboverssh(self):
        with SSHTunnelForwarder(ssh_address_or_host='120.26.54.37',ssh_port=22,ssh_username='wangchengyuan',ssh_password='tianyalieren89') as tunnel:
            conn=pymysql.connect(
                host='',
                port='',
                user='',
                passwd='',
                db='',
                charset='utf8',
            )
            cur=conn.cursor()
            try:
                cur.execute("")
            finally:
                cur.close()
                conn.commit()
                conn.close()

    #直接访问数据库
    def dbread(self):
        conn=pymysql.connect(
            host='',
            port='',
            user='',
            passwd='',
            db='',
            charset='utf8'
        )
        cur=conn.cursor()
        try:
            cur.execute()
        finally:
            cur.close()
            conn.commit()
            conn.close()


    #
    





