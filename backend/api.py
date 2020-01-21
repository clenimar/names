
import json
import sqlite3

from flask import g
from flask import Flask
from flask import request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
DB = "db/names.db"


conn = sqlite3.connect(DB)
cursor = conn.cursor()

# create the table "users" if the database is empty.
cursor.execute("create table if not exists users (id integer primary key, firstName text, middleName text, lastName text);")
# if "users" is empty, insert "James Smith Doe" as user #1.
cursor.execute("insert or ignore into users values(1, 'Jane', 'Smith', 'Doe');")
conn.commit()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB)
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/user/<int:uid>/firstname", methods=["GET"])
def get_first_name(uid):
    """get the first name of given a user."""
    fn = query_db("select firstName from users where id = ?", [uid], one=True)
    return json.dumps({"firstName": fn[0]})


@app.route("/user/<int:uid>/middlename", methods=["GET"])
def get_middle_name(uid):
    """get the middle name of given a user."""
    mn = query_db("select middleName from users where id = ?", [uid], one=True)
    return json.dumps({"middleName": mn[0]})


@app.route("/user/<int:uid>/lastname", methods=["GET"])
def get_last_name(uid):
    """get the last name of given a user."""
    ln = query_db("select lastName from users where id = ?", [uid], one=True)
    return json.dumps({"lastName": ln[0]})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
