#!/usr/bin/env python

import click
import sqlite3

from config import config
from db import Database

db = Database(config['DB_PATH'])

@click.version_option(1.0)

# f :: tasks -> string 
def format(tasks):
    for task in tasks:
        print 'NAME: ', task[1]
        print 'DESCRIPTION:', task[2]
        print ''


@click.group()
def cli():
    pass

@cli.command(short_help='short help')
@click.argument('name', type=click.STRING)
@click.argument('description', type=click.STRING)
def add(name, description):

    task_properties = [ 
        name,
        description,
    ]
    db.add_task( *task_properties )


@cli.command()
def all():

    formatted = format(db.get_all_tasks())
    click.echo(formatted)

cli.add_command(add)
cli.add_command(all)

if __name__ == '__main__':
    cli()
