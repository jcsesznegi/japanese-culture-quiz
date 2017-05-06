#!/usr/local/bin/python3

from flask import Flask, request, jsonify
app = Flask(__name__)

import sys, os, datetime
from config import config

"""
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://jcsesznegi:swejaK3r!@localhost/japan_culture_quiz', convert_unicode=True)

from models import testvar, users

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Text, DateTime
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('user_agent', Text),
    Column('insert_date', DateTime),
)
metadata.create_all(engine)
conn = engine.connect()

from sqlalchemy.sql import select

s = select( [users] )
result = conn.execute(s)
for row in result:
    print(row)

"""

from database import db_session, init_db
from models import User

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

init_db()


"""
f = '%Y-%m-%d %H:%M:%S'
now = datetime.datetime.now()

u = User('test2', 'test2@localhost', '', now.strftime(f))
db_session.add(u)
db_session.commit()

User.query.all()
print(User.query.filter(User.name == 'test2').first())

sys.exit()

print( _config.get('route_index_users') )
sys.exit()
"""

@app.route( config.get('route_user_index'), methods=['POST'] )
def user_index():
    user_string = ""
    user_list = User.query.all()
    for u in user_list:
        if not user_string:
            user_string = u.name
        else:
            user_string = user_string + ", " + u.name
    return user_string

@app.route( config.get('route_user_add'), methods=['POST'] )
def user_add():
    f = '%Y-%m-%d %H:%M:%S'
    now = datetime.datetime.now()
    name = request.values['name'] 
    email = request.values['email'] 
    user_agent = request.headers.get('User-Agent') 
    insert_date = now.strftime(f) 
    u = User(name, email, user_agent, insert_date)
    db_session.add(u)
    db_session.commit()
    return 'Added user!?'

@app.route( config.get('route_user_delete'), methods=['POST'] )
def user_delete():
    id = int(request.values['id'])
    u = User.query.get(id)
    db_session.delete(u)
    db_session.commit()
    return jsonify(msg='Deleted user!?')

@app.route( config.get('route_user_update'), methods=['POST'] )
def user_update():
    id = int(request.values['id'])
    u = User.query.get(id)
    u.name = request.values['name'] 
    u.email = request.values['email'] 
    u.user_agent = request.headers.get('User-Agent') 
    db_session.commit()
    return 'Updated user!?'



if __name__ == '__main__':
    app.run(debug=True)

"""
# Turn on debug mode.
import cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

print ("Hello, world!")

"""
