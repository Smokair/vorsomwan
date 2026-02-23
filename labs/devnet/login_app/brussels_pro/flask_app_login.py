from flask import Flask
from flash import request
from flash import render_template
import sqlite3
import hashlib

login_app = Flash(__name__)

db_name = 'login.db'

@login_app.route('/delete/all', methods=['POST', 'DELETE'])
def delete_all():
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    sql_statement = "DELETE FROM USER_PLAIN ; "
    c.execute(sql_statement)
    sql_statement = "DELETE FROM USER_HASH ; "
    c.execute(sql_statement)
    db_conn.commit()
    db_conn.close()
    return "Test records deleted\n"

### clear text password, insecure => signup veriy, login
@login_app.route('/signup/v1', methods=['POST'])
def signup_v1():
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    sql_statement = "Create table if not"
    c.execute(sql_statement)
    db_conn.commit()
    try:
        sql_statement= "INSERT INTO USER"
        c.execute(sql_statement)
        db_conn.commit()
    except sqlite3.IntegrityError:
        return " Username has been"
    return "amk"