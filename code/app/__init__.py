from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config.from_object('config')
bcrypt = Bcrypt(app)
app.secret_key = '\xff}M\xac\xbd#4F\xab\xcc.\x9b\xf3\xa7\xf8\x80x`Yu'
db = SQLAlchemy(app)
from app import views, models
