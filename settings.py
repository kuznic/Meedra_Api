#This file has config data for the web application

from flask import Flask
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password12@localhost/aom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE']  = 50
#app.config['SERVER_NAME'] = 'localhost'
#app.config['SQLALCHEMY_POOL_RECYCLE']= 10


