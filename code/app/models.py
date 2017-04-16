from app import db
from app import bcrypt
class Leaderboard(db.Model):
	__tablename__ = "leaderboard"

	#id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100),primary_key=True)
	email = db.Column(db.String(100), nullable=False)
	password = db.Column(db.String(100), nullable=False)
	score = db.Column(db.Integer,nullable=True)

	def __init__ (self,username,email,score,password):
		self.username = username
		self.email = email
		self.score=score
		self.password = bcrypt.generate_password_hash(password)

class Contest(db.Model):
	__tablename__ = "contest"
	file_name = db.Column(db.String(20),primary_key=True)
	def __init__(self,file_name):
		self.file_name=file_name
