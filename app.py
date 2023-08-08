import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import csv

filepath = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(filepath, 'library.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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

# create tables
with app.app_context():
    db.create_all()
    # with open("BookData.csv", mode='r') as f:
    #     csvFile = csv.reader(f)
    #     i = 0
    #     for row in csvFile:
    #         if row[0] == "ISBN":
    #             continue
    #         if i > 100:
    #             break
    #         try:
    #             book = Book(isbn=int(row[0]), title=row[1], author=row[2], year_published=int(row[3]), publisher=row[4])
    #             db.session.add(book)
    #         except:
    #             continue
    #         i += 1
    # with open("BookRating.csv", mode='r') as f:
    #     csvFile = csv.reader(f)
    #     i = 0
    #     for row in csvFile:
    #         if row[0] == "User-ID":
    #             continue
    #         if i > 1000:
    #             break
    #         try:
    #             rating = Rating(user_id=int(row[0]), isbn=int(row[1]), rating=int(row[2]))
    #             db.session.add(rating)
    #         except:
    #             continue
    #         i += 1
    # with open("UserData.csv", mode='r') as f:
    #     csvFile = csv.reader(f)
    #     i = 0
    #     for row in csvFile:
    #         if row[0] == "User-ID":
    #             continue
    #         if i > 10000:
    #             break
    #         try:
    #             user = User(user_id=int(row[0]), isbn=int(row[1]), rating=int(row[2]))
    #             db.session.add(user)
    #         except:
    #             continue
    #         i += 1
    # db.session.commit()

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        isbn = request.form['isbn']
        title = request.form['title']
        author = request.form['author']
        year_published = request.form['year_published']
        publisher = request.form['publisher']
        book = Book(isbn=isbn, title=title, author=author, year_published=year_published, publisher=publisher)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')