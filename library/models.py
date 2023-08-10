from library import db

class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(256), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.String(256))
    borrowed = db.Column(db.Boolean, nullable=False)
    
class Rating(db.Model):
    username = db.Column(db.String(50), db.ForeignKey('user.username'), primary_key=True)
    isbn = db.Column(db.Integer, db.ForeignKey('book.isbn'), primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

class User(db.Model):
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(256), nullable=False)