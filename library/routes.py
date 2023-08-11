from library import app
from library.models import *
from flask import render_template, redirect, url_for, request, flash
from library.forms import *
from sqlalchemy import or_, desc, asc

@app.route('/')
@app.route('/home')
def home():
    search_query = request.args.get('search_query')
    sort_option = request.args.get('sort')
    
    # Filter books by search query
    if search_query and search_query.lower() != "all":
        books_query = Book.query.filter(Book.title.ilike(f'%{search_query}%'))
        flash("Search results for book title: '{}'".format(search_query), 'success')
    else:
        books_query = Book.query
    
    # Sort books based on the selected option for searched books
    if sort_option == 'title_az':
        books_query = books_query.order_by(asc(Book.title))
    elif sort_option == 'title_za':
        books_query = books_query.order_by(desc(Book.title))
    elif sort_option == 'year_oldest':
        books_query = books_query.order_by(asc(Book.year_published))
    elif sort_option == 'year_newest':
        books_query = books_query.order_by(desc(Book.year_published))
    
    books = books_query.all()
    
    return render_template('home.html', books=books, search_query=search_query)

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