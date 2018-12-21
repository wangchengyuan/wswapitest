'''
@author:wangchengyuan
@file:sshReadLog.py
@time:2018/12/21上午10:55
@desc:
'''

import paramiko
from bin.readConfig import ReadConfig

localConifg=ReadConfig() #读取本地配置

ssh = paramiko.SSHClient()  # 实例化ssh
#加上这句话不用担心选yes的问题，会自动选上（用ssh连接远程主机时，第一次连接时会提示是否继续进行远程连接，选择yes）
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接远程主机，SSH端口号为22
ssh.connect(hostname=localConifg.get_sshrelate('hostname'), port=22, username=localConifg.get_sshrelate('username'), password=localConifg.get_sshrelate('password'))
strl = "tail -f /home/wangchengyuan/2.txt "
stdin, stdout, stderr = ssh.exec_command(strl)

def line_buffered(f):
    line_buf = ""
    while not f.channel.exit_status_ready():
        line_buf += f.readline(1)
        if line_buf.endswith('\n'):
            yield line_buf
            line_buf = ''
for l in line_buffered(stdout):
    print(l)

ssh.close()