from app import db
from models import User

db.session.add(User('himank','himank.juit@gmail.com','1hC0aG,cS'))
db.session.add(User('admin','admin@gmail.com','administrator'))

db.session.commit();