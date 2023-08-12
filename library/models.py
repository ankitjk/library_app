from library import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(256), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.String(256))
    ratings = db.relationship('Rating', backref='book', lazy='dynamic')
    borrowed = db.relationship('Borrowed', backref='book', lazy='dynamic')
    
class Rating(db.Model):
    username = db.Column(db.String(50), db.ForeignKey('user.username'), primary_key=True)
    isbn = db.Column(db.Integer, db.ForeignKey('book.isbn'), primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

class User(db.Model, UserMixin):
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    # name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    ratings = db.relationship('Rating', backref='user', lazy='dynamic')
    borrowed = db.relationship('Borrowed', backref='user', lazy='dynamic')

    def get_id(self):
        return self.username
    
class Borrowed(db.Model):
    username = db.Column(db.String(50), db.ForeignKey('user.username'), primary_key=True)
    isbn = db.Column(db.Integer, db.ForeignKey('book.isbn'), primary_key=True)
    date = db.Column(db.DateTime, nullable=False)