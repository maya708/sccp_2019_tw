import sqlite3

dbpath = 'sample.sqlite3'

connection = sqlite3.connect(dbpath)

cursor = connection.cursor()

try:
    cursor.execute()
    def add_user(username,password):
