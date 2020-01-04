# 默认配置路径
import copy
import os
import select
import sys
import termios
import tty

import click
import paramiko
import yaml

default_config_dir = '/etc/ming-tools'
if not os.path.exists(default_config_dir):
    os.makedirs(default_config_dir)

# 默认配置file
default_config_file = default_config_dir + '/server_config.yaml'


def server_add(name, host, port, password):
    """
    添加服务配置
    :param name: 服务器名称
    :param host: 服务器地址
    :param port: 服务器ssh端口
    :param password: 密码
    :return:
    """
    # 追加模式
    y_file = open(default_config_file, 'a+')
    sc = ServerConfig(name, host, port, password)
    yaml.safe_dump([sc.__dict__], y_file)
    click.echo('\n录入的服务器信息:\n名称:{}\n地址:{}\nssh端口:{}\n密码:{}'.format(name, host, port, password))


def server_remove(name):
    """
    删除服务器配置信息
    获取所有配置  删除其中name符合的数据
    :param name: 服务器名称
    :return:
    """
    y_read_file = open(default_config_file, 'r')
    config_list = yaml.safe_load(y_read_file)
    if config_list is None:
        click.echo("暂无服务器配置信息!")
        return
    # 深拷贝 配置列表 进行操作列表
    new_config_list = copy.deepcopy(config_list)
    for c in config_list:
        if c['name'] == name:
            new_config_list.remove(c)
            click.echo("删除{}服务器".format(c['name']))
    # 重新打开链接
    if len(new_config_list) != 0:
        yaml.safe_dump(new_config_list, open(default_config_file, 'w+'))
    else:
        # 清空配置
        open(default_config_file, 'w+').truncate()
        click.echo("服务器配置已清空!")


def server_list():
    y_read_file = open(default_config_file, 'r')
    config_list = yaml.safe_load(y_read_file)
    if config_list is None:
        click.echo("暂无服务器配置信息!")
        return
    config_str = '服务器配置信息:\n'
    for c in config_list:
        config_str += '名称:{},地址:{},端口{}'.format(c['name'], c['host'], str(c['port']) + '\n')
    click.echo(config_str)


def connect():
    # https://www.cnblogs.com/langqi250/p/10141295.html
    # 建立一个socket
    trans = paramiko.Transport(('127.0.0.1', 22))
    # 启动一个客户端
    trans.start_client()

    # 如果使用rsa密钥登录的话

    # 如果使用用户名和密码登录
    trans.auth_password(username='ming', password='ming')
    # 打开一个通道
    channel = trans.open_session()
    # 获取终端
    channel.get_pty()
    # 激活终端，这样就可以登录到终端了，就和我们用类似于xshell登录系统一样
    channel.invoke_shell()

    # 获取原操作终端属性
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        # 将现在的操作终端属性设置为服务器上的原生终端属性,可以支持tab了
        tty.setraw(sys.stdin)
        channel.settimeout(0)

        while True:
            readlist, writelist, errlist = select.select([channel, sys.stdin, ], [], [])
            # 如果是用户输入命令了,sys.stdin发生变化
            if sys.stdin in readlist:
                # 获取输入的内容，输入一个字符发送1个字符
                input_cmd = sys.stdin.read(1)
                # 将命令发送给服务器
                channel.sendall(input_cmd)

            # 服务器返回了结果,channel通道接受到结果,发生变化 select感知到
            if channel in readlist:
                # 获取结果
                result = channel.recv(1024)
                # 断开连接后退出
                if len(result) == 0:
                    print("\r\n**** EOF **** \r\n")
                    break
                # 输出到屏幕
                sys.stdout.write(result.decode())
                sys.stdout.flush()
    finally:
        # 执行完后将现在的终端属性恢复为原操作终端属性
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

    # 关闭通道
    channel.close()
    # 关闭链接
    trans.close()


class ServerConfig(object):
    def __init__(self, name, host, port, password):
        self.name = name
        self.host = host
        self.port = port
        self.password = password

    """
    服务器配置模板class
    """
    # 名字
    name: str
    # 地址
    host: str
    # ssh端口
    port: int
    # 密码
    password: str
    # 密钥位置
    secretKeyPath: str
