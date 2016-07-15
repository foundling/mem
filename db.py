import os
import sqlite3
import datetime

from config import config

def log(msg):
    ''' logging decorator that logs a message after a db operation '''

    def outer(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)        
            print msg
        return inner
    return outer


class Database(object):

    def __init__(self, db_path):
        
        self.DB_PATH = db_path 
        self.con = sqlite3.connect(self.DB_PATH)
        self.con.executescript(open('schema.sqlite3').read())

    def get_all_tasks(self):
        ''' get all the tasks from the task database '''

        rows = self.con.execute('select * from tasks') 
        return [row for row in rows]

    @log('task added')
    def add_task(self, *args):
        ''' add task to the task database '''
        name, desc = args
        created = str(datetime.date.today())
        insert_list = (name, desc, created, 0)
        self.con.execute("insert into tasks values(Null,?,?,?,?)", insert_list)
        self.con.commit()

    def delete_db(self):
        ''' delete the task database '''

        os.unlink(self.DB_PATH)
