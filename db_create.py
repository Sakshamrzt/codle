from app import db
from models import BlogPosts

db.create_all()

db.session.commit()