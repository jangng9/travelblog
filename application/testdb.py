from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)                                 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travelblog.db'
db = SQLAlchemy(app)

class Member_table(db.Model):
    """User model."""
    __tablename__ = 'MEMBER'
    account_id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(255))

    def __repr__(self):
        return '<Member_table %r %r>' % (self.account_name, self.username)
