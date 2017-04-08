from app import db
from app import bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), nullable=False)
	password = db.Column(db.String(100), nullable=False)
	posts = relationship("BlogPosts",backref="author")

	def __init__ (self,name,email,password):
		self.name = name
		self.email = email
		self.password = bcrypt.generate_password_hash(password)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def register(self):
		db.create_all()
		db.session.add(self)
		db.session.commit()

	def __repr__(self):
		return "{}".format(self.name)

class BlogPosts(db.Model):
	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(20), nullable=False)
	desc = db.Column(db.String(1000), nullable=False)
	author_id = db.Column(db.Integer, ForeignKey('users.id'))

	def __init__(self,title,desc):
		self.title=title
		self.desc=desc

	def __repr__(self):
		return '{}  {}'.format(self.title,self.desc)
