import click

from src.config.global_config import default_config_dir

# 默认配置file
sync_config_default_file = default_config_dir + '/sync_config.yaml'


def details():
    click.echo("查看同步仓库配置")


def create():
    click.echo("创建同步仓库配置")


def remove():
    click.echo("删除同步仓库配置")


def edit():
    click.echo("编辑同步仓库配置")


def pull():
    click.echo("sync pull config")


def push():
    click.echo("sync push config ")


def checkSyncConfig():
    click.echo("检查 同步仓库配置")


class SyncConfig(object):
    """
    同步配置 对象
    暂时只支持 http/https 协议git 操作
    """
    # 地址
    host: str
    # git用户名
    username: str
    # 密码
    password: str

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    @staticmethod
    def to_obj(d: dict):
        """
        将读取的dict 转换为 serverConfig
        :param d:  dict
        :return: ServerConfig
        """
        return SyncConfig(host=d['host'], username=d['username'],
                          password=d['password'])
