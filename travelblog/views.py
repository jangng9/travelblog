from flask import Flask, render_template, flash, redirect, session, request, url_for
from .models import Member_table, db
import os
from travelblog import app
 
@app.route('/')

@app.route('/index.html')
def index():
    username = session.get('username', '')
    return render_template("index.html")
    
@app.route("/place_asiatique.html")
def place_asiatique():
    username = session.get('username', '')
    return render_template("place_asiatique.html")

@app.route("/place_benjakiti.html")
def place_benjakiti():
    username = session.get('username', '')
    return render_template("place_benjakiti.html")

@app.route("/place_dusit.html")
def place_dusit():
    username = session.get('username', '')
    return render_template("place_dusit.html")

@app.route("/place_khlongladmayom.html")
def place_khlongladmayom():
    username = session.get('username', '')
    return render_template("place_khlongladmayom.html")

@app.route("/place_museum_artinparadise.html")
def place_museum_artinparadise():
    username = session.get('username', '')
    return render_template("place_museum_artinparadise.html")

@app.route("/place_museum_fabricqueen.html")
def place_museum_fabricqueen():
    username = session.get('username', '')
    return render_template("place_museum_fabricqueen.html")

@app.route("/place_museum_nelsonlib.html")
def place_museum_nelsonlib():
    username = session.get('username', '')
    return render_template("place_museum_nelsonlib.html")

@app.route("/place_museum_siriraj.html")
def place_museum_siriraj():
    username = session.get('username', '')
    return render_template("place_museum_siriraj.html")

@app.route("/place_panaikrung.html")
def place_panaikrung():
    username = session.get('username', '')
    return render_template("place_panaikrung.html")

@app.route("/place_rodfai.html")
def place_rodfai():
    username = session.get('username', '')
    return render_template("place_rodfai.html")

@app.route("/place_suanluang.html")
def place_suanluang():
    username = session.get('username', '')
    return render_template("place_suanluang.html")

@app.route("/place_watarun.html")
def place_watarun():
    username = session.get('username', '')
    return render_template("place_watarun.html")

@app.route("/place_watbenjama.html")
def place_watbenjama():
    username = session.get('username', '')
    return render_template("place_watbenjama.html")

@app.route("/place_watgloden.html")
def place_watgloden():
    username = session.get('username', '')
    return render_template("place_watgloden.html")

@app.route("/place_watprakeaw.html")
def place_watprakeaw():
    username = session.get('username', '')
    return render_template("place_watprakeaw.html")

@app.route("/type_art_museum.html")
def type_art_museum():
    username = session.get('username', '')
    return render_template("type_art_museum.html")

@app.route("/type_market.html")
def type_market():
    username = session.get('username', '')
    return render_template("type_market.html")

@app.route("/type_natural.html")
def type_natural():
    username = session.get('username', '')
    return render_template("type_natural.html")

@app.route("/type_religious.html")
def type_religious():
    username = session.get('username', '')
    return render_template("type_religious.html")

app.secret_key = os.urandom(12)
@app.route('/login.html', methods=['GET','POST'])
def login():
    error = None
    username = session.get('username','')
    password = session.get('password','')
    if request.method == 'POST':
        users = Member_table.query.all()
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
        picture = ""
        try:
            new_user = Member_table(account_name = name, username = username, password = password, picture=picture)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            session['password'] = password
            flash(username)
            flash('Register Successfully', 'success')
            return render_template("login.html")
        except:
            db.session.rollback()
            error = "Username or Password already exists."
            flash('Something Wrong!', 'error')
    return render_template("register.html", error=error)

@app.route('/logout')
def logout():
    session['username'] = ''
    flash('You were logged out')
    return redirect(url_for('index'))