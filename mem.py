#!/usr/bin/env python

import click
import sqlite3

from config import config
from db import Database

db = Database(config['DB_PATH'])

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

@cli.command()
def all():
    click.echo(db.get_all_tasks())

cli.add_command(add)
cli.add_command(all)

if __name__ == '__main__':
    cli()
