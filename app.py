from flask import Flask, render_template,redirect,url_for,session, request, flash
from functools import wraps
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager, login_user, logout_user
from form import LoginForm, SignUpForm


app=Flask(__name__)
bcrypt = Bcrypt(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
#config
app.config.from_object(os.environ['APP_SETTINGS'])
#Setting up the database
db = SQLAlchemy(app)
from models import *

#login_manager.login_view = "login"

# @login_manager.user_loader
# def load_user(user_id):
# 	return User.query.filter(User.id == int(user_id)).first()
user = None

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args,**kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('welcome'))
	return wrap

def logout_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' not in session:
			return test(*args,**kwargs)
		else:
			flash('You need to logout first.')
			return redirect(url_for('home'))
	return wrap

@app.route('/')
def home():
	if user is not None:
		name=user.name	
		posts=db.session.query(BlogPosts).all()
		sid=user.id
 		return render_template('index.html',sid=sid,posts=posts,name=name)
	return redirect(url_for('welcome'))

@app.route('/welcome')
@logout_required
def welcome():
	return render_template('welcome.html')


@app.route('/login',methods = ['GET','POST'])
@logout_required
def login():
	error=None
	form = LoginForm()
	if request.method=='POST':
		global user
		user = User.query.filter_by(name=request.form['username']).first()
		if user == None or bcrypt.check_password_hash(user.password, request.form['password']) == False:
			error='Please Check, Username or Password'
		else:
			session['logged_in'] = True
			#login_user(user)
			#session['name'] = request.form['username']
			#session['id'] = user.id
			flash('Logged in successfully')
			return redirect(url_for('home'))
	return render_template('login.html',form=form, error=error)

@app.route('/signup',methods = ['GET','POST'])
@logout_required
def signup():
	form = SignUpForm()
	if request.method == 'POST':
		global user
		user = User(str(request.form['username']),str(request.form['email']),str(request.form['password']))
		user.register()
		#login_user(user)
		flash("Created account successfully")
		return redirect(url_for('home'))
	return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
	global user
	#logout_user()
	user = None
	session.pop('logged_in',None)
	#session.pop('name',None)
	#session.pop('id',None)
	flash("logged out successfuly")
	return redirect(url_for('welcome'))

if __name__ == '__main__':
	app.run()