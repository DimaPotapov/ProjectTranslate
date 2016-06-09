import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import requests

# конфигурация
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# создаём наше маленькое приложение :)
app = Flask(__name__)
app.config.from_object(__name__)

# Загружаем конфиг по умолчанию и переопределяем в конфигурации часть
# значений через переменную окружения
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Если ещё нет соединения с базой данных, открыть новое - для
    текущего контекста приложения
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.route('/') 
def index_page():
   return render_template('index.html')

@app.route('/translate', methods = ['POST', 'GET']) 
def translate_():
    db = get_db()
    if request.method == 'POST':
        db.execute('insert into entries (title, text) values (?, ?)', [request.form['input_text']])
        db.commit()
    return render_template('index.html')
@app.route('/text_input')
def translate():
     return render_template('index.html')

if __name__ == '__main__':
    app.run()