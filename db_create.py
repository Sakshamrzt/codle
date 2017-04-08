from app import db
from models import BlogPosts

db.create_all()

db.session.add(BlogPosts("First","This is the first post"))
db.session.add(BlogPosts("Second","This is the second post"))

db.session.commit()