from library import app
from library.models import *
from flask import render_template, redirect, url_for, request, flash
from library.forms import *

@app.route('/')
@app.route('/home')
def home():
    search_query = request.args.get('search_query')
    if search_query:
        books = Book.query.filter(Book.title.ilike(f'%{search_query}%')).all()
        flash("Search results for book title: '{}'".format(search_query), 'success')
    else:
        books = Book.query.all()
    return render_template('home.html', books=books)

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

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
        return redirect(url_for('home'))
    return render_template('create.html')