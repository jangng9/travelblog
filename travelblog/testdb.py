from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)                                 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travelblog.db'
db = SQLAlchemy(app)

class Member_table(db.Model):
    """User model."""
    __tablename__ = 'MEMBER'
    username = db.Column(db.String(255), primary_key=True, nullable=False)
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
    account_name = db.Column(db.String(255), primary_key=True)
    file_name = db.Column(db.String(255), primary_key=True)

    def __init__(self, account_name, file_name):
        self.account_name = account_name
        self.file_name = file_name
    
    def __repr__(self):
        return "<User_fav_id: {}, {}>".format(self.file_name, self.account_name)
