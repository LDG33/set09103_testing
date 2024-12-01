from flask import Flask, redirect, url_for, session
import sqlite3
app = Flask(__name__)

DB = 'var/sqlite3.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()




@app.route('/') 
def databaseResult():
        sql = "SELECT * FROM albums"
        cursor.execute(sql)
        
        conn.commit()
        return cursor.fetchall()

    #return 'Hello Napier'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)