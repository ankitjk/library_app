from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Username:')
    email = StringField(label='Email:')
    password = PasswordField(label='Password:')
    verify = PasswordField(label='Retype password:')
    submit = SubmitField(label='Create account')