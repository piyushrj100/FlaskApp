from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='b23c721a5fd672162bb74a7e'
bcrypt=Bcrypt(app)
from market import routes