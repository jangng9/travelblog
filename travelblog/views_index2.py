from flask import Flask, render_template, flash, redirect, session, request, url_for
from .models import Member_table, User_Fav_table, db
import os
from travelblog import app
 
@app.route('/')

@app.route('/index.html', methods=['GET','POST'])
def index():
    username = session.get('username','')
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
                    return redirect(url_for('.index'))                                                                           
                except:
                    db.session.rollback()
                    error = "Can't removlike"                                                    
            else:                
                try:
                    new_like = User_Fav_table(account_name=username, file_name=file_name)
                    db.session.add(new_like)
                    db.session.commit()
                    return redirect(url_for('.index'))                                                                                
                except:
                    db.session.rollback()
                    error = "Can't like"    
    return render_template("index.html", username=username, countmsg2=count, likemsg2=str(alreadylike))