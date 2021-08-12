import sqlite3
ID = 0
IP = '10.100.102.11'

conn = sqlite3.connect('db.db')
curs = conn.cursor()
curs.execute("""CREATE TABLE if not exists links(
                id integer PRIMARY KEY,
                link text 
                );
            """)

ids = curs.execute("""SELECT id FROM links""").fetchall()
if len(ids) > 0:
    ID = ids[-1][0] + 1

conn.commit()
conn.close()


from flask import Flask
server = Flask(__name__)

from app import views
