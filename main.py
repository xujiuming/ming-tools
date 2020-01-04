import click

from local import pc_info, http_server
from server import server_config


def print_version(ctx, param, value):
    """
    输出工具版本
    :param ctx:   click上下文
    :param param: 参数
    :param value:  值
    :return:
    """
    if not value or ctx.resilient_parsing:
        return

    version_info = """
    仅适用linux 其他平台部分功能异常 
    ming-tools Version 1.0"""
    click.echo(version_info)
    ctx.exit()


@click.group()
@click.option('--version', '-v', help='工具版本', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def cli():
    pass


# ---------------------- server tools ----------------------------------------------------------------------------------

@cli.group(help='远程服务器管理')
def server():
    pass


@server.command("list", help='显示所有服务器配置')
def server_list():
    server_config.server_list()


@server.command("add", help='添加服务器配置')
@click.option('--name', '-n', prompt='请输入服务器名称')
@click.option('--host', '-h', prompt='请输入服务器地址')
@click.option('--port', '-p', prompt='请输入服务器ssh端口,默认为22', default=22)
@click.option('--password', '-pwd', prompt='请输入密码')
def server_add(name, host, port, password):
    server_config.server_add(name, host, port, password)


@server.command("remove", help='根据名称删除服务器配置')
@click.option('--name', '-n', type=str, prompt='请输入服务器名称', help='服务器名称')
def server_remove(name):
    server_config.server_remove(name)


@server.command('edit', help='编辑服务器配置')
def server_edit():
    click.echo("server_edit")


@server.command('connect', help='🔗连接服务器')
@click.option('--name', '-n', type=str, prompt='请输入服务器名称', help='服务器名称')
def server_connect(name):
    server_config.connect()


# ----------------------------------- local tools ----------------------------------------------------------------------

@cli.group(help='本机使用的工具')
def local():
    pass


@local.command('pc-info', help='电脑配置')
def local_pc_info():
    pc_info.echo_pc_info()


@local.command('http', help='根据指定文件夹开启临时http服务器')
@click.option('--d', '-d', type=click.Path(exists=True), default='.', nargs=1, help='指定静态文件目录,默认为.')
@click.option('--port', '-p', default=80, type=int, nargs=1, help='指定服务端口,默认为80')
@click.option('--host', '-h', default='0.0.0.0', type=str, nargs=1, help='指定服务监听地址,默认为0.0.0.0')
def local_tmp_http(d, port, host):
    http_server.http_server(d, port, host)


# main 函数
if __name__ == '__main__':
    cli()
