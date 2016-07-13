import sqlite3
import datetime
from config import config

class Database(object):

    def __init__(self, DB_PATH):
        self.DB_PATH = DB_PATH 
        self.con = sqlite3.connect(self.DB_PATH)

    def get_all_tasks(self):
        rows = self.con.execute('select * from tasks') 
        return [row for row in rows]

    def add_task(self, name, desc):

        created = str(datetime.date.today())
        insert_list = (name, desc, created, 0 ) # text, text, datetime string, 0 for False

        self.con.execute("insert into tasks values(Null,?,?,?,?)", insert_list)
        self.con.commit()
