from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)                                 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travelblog.db'
db = SQLAlchemy(app)

class Member_table(db.Model):
    """User model."""
    __tablename__ = 'MEMBER'
    account_name = db.Column(db.String(255),primary_key=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(255))

    def __init__(self, account_name, username, password, picture):
        self.account_name = account_name
        self.username = username
        self.password = password
        self.picture = picture

    def __repr__(self):
        return "<Username: {}>".format(self.account_name)
