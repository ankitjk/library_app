from library import app
from library.models import *
from flask import render_template, redirect, url_for, request

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/login')
def login():
    pass

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