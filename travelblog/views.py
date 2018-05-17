from flask import Flask, render_template, flash, redirect, session, request, url_for
from .models import Member_table, db
import os
from travelblog import app
 
@app.route('/')
@app.route('/index.html')
def index():
    username = session.get('username', '')
    return render_template("index.html")
    
app.secret_key = os.urandom(12)
@app.route('/login.html', methods=['GET','POST'])
def login():
    error = None
    username = session.get('username','')
    password = session.get('password','')
    if request.method == 'POST':
        users = User.query.all()
        for user in users:
            if request.form['password'] == user.password and request.form['username'] == user.username:
                flash('Login successfully.', 'success')
                if username:
                    session['username'] = username
                else:
                    session['username'] = request.form['username']
                return redirect(url_for('.index'))
            else:
                error = 'Invalid username or password. Please try again.'
    return render_template('login.html', error=error, username=username, password=password)
  

@app.route('/register.html', methods=['GET','POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['rusername']
        password = request.form['rpassword']
        name = request.form['rname']
        try:
            new_user = Member_table(account_name = name, username = username, password = password)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            session['password'] = password
            flash('Register Successfully', 'success')
            return redirect(url_for('.login'))
        except:
            db.session.rollback()
            error = "Username or Password already exists."
            flash('Something wrong!, please try again. ', 'error')
    return render_template("register.html", error=error)

