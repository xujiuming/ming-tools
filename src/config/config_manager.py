import click


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
