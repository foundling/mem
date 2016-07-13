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
@click.argument('task_name')
def add(task_name):
    click.echo('Adding task %s' % task_name)



if __name__ == '__main__':
    cli()
