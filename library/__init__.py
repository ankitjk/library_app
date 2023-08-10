from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import secrets

filepath = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(filepath, 'library.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Generate a random secret key
app.config['SECRET_KEY'] = secrets.token_hex(32)

db = SQLAlchemy(app)

from library import routes