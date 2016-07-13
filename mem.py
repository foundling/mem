#!/usr/bin/env python

import click
import sqlite3
from config import config

DB_PATH = config['db']
db = sqlite3.connect(DB_PATH)


@click.version_option(1.0)
@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('description', default='', type=click.STRING)
@click.argument('created', default='now', type=click.STRING)
@click.argument('complete', default=0, type=click.INT)
def add(name, description, created, complete):
    click.echo('Adding task %s' % name)



if __name__ == '__main__':
    cli()
