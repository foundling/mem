import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('a', type=int, default=0)
@click.argument('b', type=int, default=0)
def add(a, b):
    click.echo(a + b)
