'''
@author:wangchengyuan
@file:datadeal.py
@time:2018/11/16下午10:18
@desc:操作数据库、跳板机操作数据库
'''

import pymysql
from sshtunnel import SSHTunnelForwarder
from bin import readConfig
import paramiko


class DataDeal():

    # 初始化读取配合文件
    def __init__(self):
        self.rdf = readConfig.ReadConfig()

    # 通过ssh方式访问数据库
    def db_overssh(self, sql):
        with SSHTunnelForwarder(ssh_address_or_host=self.rdf.get_sshrelate('hostname'),
                                ssh_port=22,
                                ssh_username=self.rdf.get_sshrelate('username'),
                                ssh_password=self.rdf.get_sshrelate('password')) as tunnel:
            conn = pymysql.connect(
                host=self.rdf.get_database('host'),
                port=tunnel.local_bind_port,
                user=self.rdf.get_database('user'),
                passwd=self.rdf.get_database('passwd'),
                db='quxuexi',
                charset='utf8',
            )
            cur = conn.cursor()
            try:
                cur.execute(sql)
                data = cur.fetchall()
            finally:
                cur.close()
                conn.commit()
                conn.close()
            return data

    # 直接访问数据库
    def db_read(self, sql):
        conn = pymysql.connect(
            host=self.rdf.get_database('host'),
            port=3306,
            user=self.rdf.get_database('user'),
            passwd=self.rdf.get_database('passwd'),
            db='quxuexi',
            charset='utf8'
        )
        cur = conn.cursor()
        try:
            cur.execute(sql)
            data = cur.fetchall()
        finally:
            cur.close()
            conn.commit()
            conn.close()

        return data

    # 查询数据
    def db_select(self, sql, ssh=True):
        if (ssh):
            data = self.db_overssh(sql)
        else:
            data = self.db_read(sql)

        return data

    # 查询数据
    def db_select(self, sql):
        data = self.db_read(sql)
        return data
