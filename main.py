import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

if __name__=="__main__":
    filepath = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(filepath, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

    class Book(db.Model):
        isbn = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(256), nullable=False)
        author = db.Column(db.String(256), nullable=False)
        year_published = db.Column(db.Integer, nullable=False)
        publisher = db.Column(db.String(256))

        def __repr__(self):
            return f'<Book {self.isbn}>'