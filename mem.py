#!/usr/bin/env python

import click
import sqlite3

from config import config
from db import Database

db = Database(config['DB_PATH'])

def format(tasks):
    print ''
    for task in tasks:
        print 'Name: ', task[1]
        print 'Description:', task[2]
        print ''

@click.version_option(1.0)
@click.group()
def cli():
    pass

@cli.command(short_help='add a name or description in-line, entirely optional')
@click.argument('name', type=click.STRING, required=False)
@click.argument('description', type=click.STRING, required=False)
def add(name, description):

    ''' 
    add a task to the task database.
    mem add [TASK_NAME] [TASK_DESCRIPTION] 
    ''' 

    both = name and description
    task_properties = both or [
        click.prompt('name', type=str, default=name),\
        click.prompt('description', type=str)
    ]
    db.add_task(*task_properties)


@cli.command()
def all():
    ''' get all the tasks from the database or print no tasks'''

    tasks = db.get_all_tasks()
    if not tasks: 
        print('no tasks ...')
        return
    click.echo( format(tasks) )

@cli.command('deletedb')
def delete_db():
    ''' delete the database '''
    db.delete_db()
     

cli.add_command(add)
cli.add_command(all)



if __name__ == '__main__':

    cli()
