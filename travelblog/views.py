from flask import Flask, render_template, flash, redirect, session, request, url_for
from .models import Member_table, User_Fav_table, db
import os
from travelblog import app
 
@app.route('/')

@app.route('/index.html', methods=['GET','POST'])
def index():
    username = session.get('username','')
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike1=False
    alreadylike2=False
    alreadylike3=False
    alreadylike4=False
    file_name1 = "place_watarun"
    file_name2 = "place_suanluang"
    file_name3 = "place_museum_artinparadise"
    file_name4 = "place_rodfai"
    for each_like1 in likes:
        if username == each_like1.account_name and file_name1 == each_like1.file_name:
            alreadylike1=True         
        if file_name1 == each_like1.file_name:
            count1 = count1 + 1  
    for each_like2 in likes:
        if username == each_like2.account_name and file_name2 == each_like2.file_name:
            alreadylike2=True         
        if file_name2 == each_like2.file_name:
            count2 = count2 + 1
    for each_like3 in likes:
        if username == each_like3.account_name and file_name3 == each_like3.file_name:
            alreadylike3=True         
        if file_name3 == each_like3.file_name:
            count3 = count3 + 1
    for each_like4 in likes:
        if username == each_like4.account_name and file_name4 == each_like4.file_name:
            alreadylike4=True         
        if file_name4 == each_like4.file_name:
            count4 = count4 + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')  
    return render_template("index.html", username=username, countmsg1=count1, likemsg1=str(alreadylike1), countmsg2=count2, likemsg2=str(alreadylike2), countmsg3=count3, likemsg3=str(alreadylike3), countmsg4=count4, likemsg4=str(alreadylike4))

@app.route("/place_asiatique.html", methods=['GET','POST'])
def place_asiatique():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_asiatique"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True         
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()                   
                    return redirect(url_for('place_asiatique'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_asiatique'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_asiatique.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_benjakiti.html", methods=['GET','POST'])
def place_benjakiti():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_benjakiti"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True           
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()                                                    
                    return redirect(url_for('place_benjakiti'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_benjakiti'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_benjakiti.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_dusit.html", methods=['GET','POST'])
def place_dusit():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_dusit"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True            
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()                    
                    return redirect(url_for('place_dusit'))                                                                              
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_dusit'))                                                                                   
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_dusit.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_khlongladmayom.html", methods=['GET','POST'])
def place_khlongladmayom():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_khlongladmayom"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True
            flash('alreadylike','likemsg')
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()
                    return redirect(url_for('place_khlongladmayom'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_khlongladmayom'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_khlongladmayom.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_museum_artinparadise.html", methods=['GET','POST'])
def place_museum_artinparadise():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_museum_artinparadise"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True
            flash('alreadylike','likemsg')
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()
                    return redirect(url_for('place_museum_artinparadise'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_museum_artinparadise'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"               
    return render_template("place_museum_artinparadise.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_museum_fabricqueen.html", methods=['GET','POST'])
def place_museum_fabricqueen():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_museum_fabricqueen"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True            
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()
                    return redirect(url_for('place_museum_fabricqueen'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_museum_fabricqueen'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_museum_fabricqueen.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_museum_nelsonlib.html", methods=['GET','POST'])
def place_museum_nelsonlib():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_museum_nelsonlib"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True            
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()
                    return redirect(url_for('place_museum_nelsonlib'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_museum_nelsonlib'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_museum_nelsonlib.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_museum_siriraj.html", methods=['GET','POST'])
def place_museum_siriraj():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_museum_siriraj"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True
            flash('alreadylike','likemsg')
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()                 
                    return redirect(url_for('place_museum_siriraj'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_museum_siriraj'))                                                                                 
                except:
                    db.session.rollback()
                    error = "Can't like"                                                               
    return render_template("place_museum_siriraj.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_panaikrung.html", methods=['GET','POST'])
def place_panaikrung():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_panaikrung"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True
            flash('alreadylike','likemsg')
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()
                    return redirect(url_for('place_panaikrung'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_panaikrung'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_panaikrung.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_rodfai.html", methods=['GET','POST'])
def place_rodfai():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_rodfai"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True     
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()
                    return redirect(url_for('place_rodfai'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_rodfai'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_rodfai.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_suanluang.html", methods=['GET','POST'])
def place_suanluang():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_suanluang"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True 
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()
                    return redirect(url_for('place_suanluang'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_suanluang'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_suanluang.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_watarun.html", methods=['GET','POST'])
def place_watarun():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_watarun"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True           
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()
                    return redirect(url_for('place_watarun'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_watarun'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_watarun.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_watbenjama.html", methods=['GET','POST'])
def place_watbenjama():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_watbenjama"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True            
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()
                    return redirect(url_for('place_watbenjama'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_watbenjama'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_watbenjama.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_watgloden.html", methods=['GET','POST'])
def place_watgloden():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_watgloden"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True           
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()                    
                    return redirect(url_for('place_watgloden'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_watgloden'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_watgloden.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/place_watprakeaw.html", methods=['GET','POST'])
def place_watprakeaw():
    username = session.get('username', '')
    count = 0
    error = None
    likes = User_Fav_table.query.all()
    alreadylike=False
    file_name = "place_watprakeaw"
    for each_like in likes:
        if username == each_like.account_name and file_name == each_like.file_name:
            alreadylike=True           
        if file_name == each_like.file_name:
            count = count + 1
    if request.method == "POST":            
        if username == '':
            error = "Please Login first"
            flash('Please Login first','loginfirst')
        else:                       
            if alreadylike==True:                
                try:
                    db.session.query(User_Fav_table).\
                    filter(User_Fav_table.account_name == username).\
                    filter(User_Fav_table.file_name == file_name).\
                    delete()
                    db.session.commit()                   
                    return redirect(url_for('place_watprakeaw'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('place_watprakeaw'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"
    return render_template("place_watprakeaw.html", username=username, countmsg=count, likemsg=str(alreadylike))

@app.route("/type_art_museum.html")
def type_art_museum():
    username = session.get('username', '')
    return render_template("type_art_museum.html", username=username)

@app.route("/type_market.html")
def type_market():
    username = session.get('username', '')
    return render_template("type_market.html", username=username)

@app.route("/type_natural.html")
def type_natural():
    username = session.get('username', '')
    return render_template("type_natural.html", username=username)

@app.route("/type_religious.html")
def type_religious():
    username = session.get('username', '')
    return render_template("type_religious.html", username=username)

app.secret_key = os.urandom(12)
@app.route('/login.html', methods=['GET','POST'])
def login():
    error = None
    username = ''
    password = ''       
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
                flash('Invalid username or password. Please try again.', 'error')
    return render_template('login.html', username=username, error=error)
    

@app.route('/register.html', methods=['GET','POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['rusername']
        password = request.form['rpassword']
        account_name = request.form['rname']
        picture = ""
        try:
            new_user = Member_table(account_name = account_name, username = username, password = password, picture=picture)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            session['password'] = password
            session['account_name'] = account_name
            flash('Register Successfully', 'success')
            return redirect(url_for('.login'))
        except:
            db.session.rollback()
            error = "Username or Password already exists."
            flash('Something Wrong! , please try again.', 'error')
            return render_template("register.html")
    return render_template("register.html", error=error)

@app.route('/logout')
def logout():
    session['username'] = ''
    flash('You were logged out')
    return redirect(url_for('index'))