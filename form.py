from flask_wtf import Form
from wtforms import validators
from wtforms import TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = TextField('Username', validators=[DataRequired])
	password = PasswordField('Password', validators=[DataRequired])

class SignUpForm(Form):
	username = TextField('Username', validators=[DataRequired])
	email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
	password = PasswordField('Password', validators=[DataRequired])