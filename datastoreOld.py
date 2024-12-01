from flask import Flask, g, redirect, url_for, session
import sqlite3

app = Flask(__name__)
db_location = 'var/test.db'

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db



