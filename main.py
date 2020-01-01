import click


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
    click.echo('mint-tools Version 1.0')
    ctx.exit()


@click.group()
@click.option('--version', '-v', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def cli():
    pass


@cli.group(help='管理服务器')
def server():
    pass


@server.command("list", help='显示所有服务器配置')
def server_list():
    click.echo('server_list')


@server.command("add", help='添加服务器配置')
def server_add():
    click.echo("server_add")


@server.command("remove", help='删除服务器配置')
def server_remove():
    click.echo("server_remove")


@server.command('edit', help='编辑服务器配置')
def server_edit():
    click.echo("server_edit")


if __name__ == '__main__':
    cli()
