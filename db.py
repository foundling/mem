import sqlite3
from config import config

class Database(object):

    def __init__(self, DB_PATH):
        self.DB_PATH = DB_PATH 
        self.con = sqlite3.connect(self.DB_PATH)

    def get_all_tasks(self):
        rows = self.con.execute('select * from tasks') 
        return [row for row in rows]

