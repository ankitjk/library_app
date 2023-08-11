from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email = StringField(label='email')
    password = PasswordField(label='password')
    verify = PasswordField(label='verify')
    submit = SubmitField(label='submit')