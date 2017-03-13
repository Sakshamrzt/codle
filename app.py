from random import *
from flask import Flask,render_template,redirect,url_for,session, request, flash
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

char_set=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'I', u'J', u'K', u'L', u'M', u'N', u'O', u'P', u'Q', u'R', u'S', u'T', u'U', u'V', u'W', u'X', u'Y', u'Z', u'a', u'b', u'c', u'd', u'e', u'f', u'g', u'h', u'i', u'j', u'k', u'l', u'm', u'n', u'o', u'p', u'q', u'r', u's', u't', u'u', u'v', u'w', u'x', u'y', u'z', u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9']

app=Flask(__name__)

aplhanumeric_set = "".join([choice(char_set) for _ in range(randint(1,1000))])
app.secret_key = aplhanumeric_set
#SqlAlchemy stuff
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

#Setting up the database
db = SQLAlchemy(app)
#from models import *
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
@app.route('/<name>')
def home(name=None):
	if 'logged_in' in session:	
		posts=None#db.session.query(BlogPosts).all()
 		return render_template('index.html',posts=posts,name=name)
	return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
	if 'logged_in' in session:
		return redirect(url_for('home'))
	return render_template('welcome.html')

@app.route('/login',methods = ['GET','POST'])
@logout_required
def login():
	error=None
	if request.method=='POST':
		if request.form['username'] == 'admin' and request.form['password'] == 'admin':
			session['logged_in'] = True
			flash('Logged in successfully')
			return redirect(url_for('home',name=request.form['username']))
		else:
			error='Please Check, Username or Password'
	return render_template('login.html',error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in',None)
	flash("logged out successfuly")
	return redirect(url_for('welcome'))

if __name__ == '__main__':
	app.run(debug=True)