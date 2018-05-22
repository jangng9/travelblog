import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from travelblog import app

#project_dir = os.path.dirname(os.path.abspath(__file__))
#database_file = "sqlite:///{}".format(os.path.join(project_dir, "travelblog.db"))
 
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///travelblog.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)

class Member_table(db.Model):
    """User model."""
    __tablename__ = 'MEMBER'
    username = db.Column(db.String(255), primary_key=True)
    account_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(255))

    def __init__(self, account_name, username, password, picture):
        self.account_name = account_name
        self.username = username
        self.password = password
        self.picture = picture

    def __repr__(self):
        return "<Username: {}>".format(self.account_name)


class User_Fav_table(db.Model):
    """User Favoutite."""
    __tablename__ = 'USER_FAV'
    user_fav_id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(255), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)

    def __init__(self, account_name, file_name):
        self.account_name = account_name
        self.file_name = file_name
    
    def __repr__(self):
        return "<User_fav_id: {}>".format(self.user_fav_id)

