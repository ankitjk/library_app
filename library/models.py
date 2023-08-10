from library import db

class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(256), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.String(256))
    
class Rating(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=True)