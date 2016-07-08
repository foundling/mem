import click

@click.command()
@click.argument('a', type=int, default=0)
@click.argument('b', type=int, default=0)
def cli(a,b):
    click.echo(a + b)
