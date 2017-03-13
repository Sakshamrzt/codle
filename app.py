from flask import Flask,render_template,redirect,url_for,session, request, flash
from functools import wraps
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

#config

import os
app.config.from_object(os.environ['APP_SETTINGS'])

#Setting up the database
db = SQLAlchemy(app)
from models import *
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('welcome'))
	return wrap

def logout_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' not in session:
			return f(*args,**kwargs)
		else:
			flash('You need to logout first.')
			return redirect(url_for('home'))
	return wrap

@app.route('/')
def home():
	if 'logged_in' in session:
		name=session['name']	
		posts=db.session.query(BlogPosts).all()
 		return render_template('index.html',posts=posts, name=name)
	return redirect(url_for('welcome'))

@app.route('/welcome')
@logout_required
def welcome():
	if 'logged_in' in session:
		return redirect(url_for('home'))
	return render_template('welcome.html')

@app.route('/login',methods = ['GET','POST'])
@logout_required
def login():
	error=None
	if request.method=='POST':
		if (request.form['username'] == 'admin' or request.form['username'] == 'himank') and request.form['password'] == 'admin':
			session['logged_in'] = True
			session['name'] = request.form['username']
			flash('Logged in successfully')
			return redirect(url_for('home'))
		else:
			error='Please Check, Username or Password'
	return render_template('login.html',error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in',None)
	session.pop('name',None)
	flash("logged out successfuly")
	return redirect(url_for('welcome'))

if __name__ == '__main__':
	app.run()