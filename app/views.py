from app import server
from flask import render_template, request, redirect
import sqlite3
import time
from app import ID, IP

@server.route('/')
def home():
    return render_template('home/home.html')


@server.route('/open/<id>')
def redirect_user(id):
    conn = sqlite3.connect('db.db')
    curs = conn.cursor()
    link = curs.execute(f'SELECT link from links WHERE id=?',(id,)).fetchone()[0]
    print('LINK', repr(link))
    return redirect(link)


@server.route('/addlink')
def add_link():

    global ID
    global IP

    params = request.args
    link = params['link']

    data = ID, link

    conn = sqlite3.connect('db.db')
    curs = conn.cursor()
    curs.execute("""INSERT INTO links(id ,link)
                    VALUES(?,?)
                    """, data)
    conn.commit()
    conn.close()
    ID += 1

    return f"""
            {IP}/open/{ID-1}
            <a href="open/{ID-1}">tinyorl</a>
           """
