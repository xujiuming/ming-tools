import click


@click.group()
def cli():
    pass


@cli.group()
def server():
    click.echo("show server list ")


@server.command()
def list():
    click.echo('asdfasdfdas')


@cli.command()
def version():
    click.echo('ming tools 1.0.0')


if __name__ == '__main__':
    cli()
