from flask import render_template, request,flash, redirect, url_for,session
from app import app, db
from app.models import *
import datetime 
import os,time
from itertools import cycle
from app.models import *
def login_required(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('beforelogin'))
	return wrap
@app.route('/' )
def index():
  return render_template('welcome.html') 
@app.route('/register',methods=['POST','GET'])
def reg():
	if request.method=="POST":
		user = Leaderboard.query.filter_by(username=request.form['username']).first()
		print user
		if user==None:
			if(request.form['password'] ==request.form['password-check']):
				a=Leaderboard(request.form['username'],request.form['email'],0,request.form['password'])
				db.session.add(a)
				db.session.commit()
				return redirect(url_for('index'))
			else:	
				flash("Passwords do not match")
		else:
			flash("Username already exists")	
	return render_template('page-register.html')		
@app.route('/login',methods=['POST','GET'])
def login():
	if request.method=="POST":
		user = Leaderboard.query.filter_by(username=request.form['username']).first()
		print user
		if user == None:
			flash("You are not registtered")
		else:
			if bcrypt.check_password_hash(user.password, request.form['password']) == False:
				flash('Password is wrong')
			else:
				session['logged_in'] = True
				flash('Logged in successfully')
				return render_template("bathroom.html")
	return render_template('page-login.html')    