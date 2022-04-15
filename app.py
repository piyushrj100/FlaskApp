# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from  flask import render_template
# app=Flask(__name__)
# db=SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'

# class Item(db.Model) :
#     id=db.Column(db.Integer(), primary_key=True)
#     name=db.Column(db.String(length=30), nullable=False, unique=True)
#     price=db.Column(db.Integer(), nullable=False)
#     barcode=db.Column(db.String(length=12), nullable=False, unique=True)
#     description=db.Column(db.String(length=1024),nullable=False,unique=True)

#     def __repr__(self) :
#         return f'Item {self.name}'


# @app.route("/")
# @app.route("/Home")
# def home_page():
#     return render_template('home.html')

# @app.route('/market')
# def market_page():
#     items=Item.query.all()   
#     return render_template('market.html', items=items)

# @app.route("/about")
# def about_page():
#     return "<h1>About Page</h1>"

# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>This is about page of {username}</h1>'
