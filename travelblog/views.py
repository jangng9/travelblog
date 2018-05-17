from flask import Flask, render_template, flash, redirect, session, request, url_for
from .models import Member_table, db
import os
from travelblog import app
 
@app.route('/')
@app.route('/index.html')
def index():
    username = session.get('username', '')
    return render_template("index.html")

@app.route('/')
def login():
    return render_template('index.html')
  

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

@app.route("/place_asiatique.html")
def place_asiatique():
    return render_template("place_asiatique.html")

@app.route("/place_benjakiti.html")
def place_benjakiti():
    return render_template("place_benjakiti.html")

@app.route("/place_dusit.html")
def place_dusit():
    return render_template("place_dusit.html")

@app.route("/place_khlongladmayom.html")
def place_khlongladmayom():
    return render_template("place_khlongladmayom.html")

@app.route("/place_museum_artinparadise.html")
def place_museum_artinparadise():
    return render_template("place_museum_artinparadise.html")

@app.route("/place_museum_fabricqueen.html")
def place_museum_fabricqueen():
    return render_template("place_museum_fabricqueen.html")

@app.route("/place_museum_nelsonlib.html")
def place_museum_nelsonlib():
    return render_template("place_museum_nelsonlib.html")

@app.route("/place_museum_siriraj.html")
def place_museum_siriraj():
    return render_template("place_museum_siriraj.html")

@app.route("/place_panaikrung.html")
def place_panaikrung():
    return render_template("place_panaikrung.html")

@app.route("/place_rodfai.html")
def place_rodfai():
    return render_template("place_rodfai.html")

@app.route("/place_suanluang.html")
def place_suanluang():
    return render_template("place_suanluang.html")

@app.route("/place_watarun.html")
def place_watarun():
    return render_template("place_watarun.html")

@app.route("/place_watbenjama.html")
def place_watbenjama():
    return render_template("place_watbenjama.html")

@app.route("/place_watgloden.html")
def place_watgloden():
    return render_template("place_watgloden.html")

@app.route("/place_watprakeaw.html")
def place_watprakeaw():
    return render_template("place_watprakeaw.html")

@app.route("/type_art_museum.html")
def type_art_museum():
    return render_template("type_art_museum.html")

@app.route("/type_market.html")
def type_market():
    return render_template("type_market.html")

@app.route("/type_natural.html")
def type_natural():
    return render_template("type_natural.html")

@app.route("/type_religious.html")
def type_religious():
    return render_template("type_religious.html")
