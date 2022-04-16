from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  flask import render_template
app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='b23c721a5fd672162bb74a7e'
from market import routes