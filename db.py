#!/usr/bin/python3

import sqlite3

class DB():
    def __init__(self, datebase='test'):
        self.conn = sqlite3.connect(datebase+'.db')
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()