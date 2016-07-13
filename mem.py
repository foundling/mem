#!/usr/bin/env python

import click
import sqlite3
from config import config

DB_PATH = config['db']
db = sqlite3.connect(DB_PATH)


@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('description', default='')
@click.argument('created', default='')
@click.argument('complete', default='')
def add(name, description, created, complete):
    click.echo('Adding task %s' % name)



if __name__ == '__main__':
    cli()
