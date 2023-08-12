from library import app
from library.models import *
from flask import render_template, redirect, url_for, request, flash
from sqlalchemy import desc, asc, exists
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime

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

    # Ensure that borrowed books do not show up
    borrowed = exists().where(Book.isbn == Borrowed.isbn)
    books_query = books_query.filter(~borrowed)

    books = books_query.limit(500).all()
    
    return render_template('home.html', books=books, search_query=search_query)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        verify = request.form['confirm']
        if password != verify:
            flash("Passwords do not match.")
            return redirect(url_for('register'))
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        try:
            db.session.commit()
            login_user(user)
            return redirect(url_for('home'))
        except Exception as e:
            flash(f'There was an error with creating account: {e}', category='danger')
            db.session.rollback()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user or user.password != password:
            flash("Username or password is incorrect.")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/rate/<int:isbn>', methods=['GET', 'POST'])
@login_required
def rate_book(isbn):
    book = Book.query.get_or_404(isbn)
    user_rating = Rating.query.filter_by(username=current_user.username, isbn=isbn).first()

    if request.method == 'POST':
        rating_value = int(request.form['rating'])

        if user_rating:
            user_rating.rating = rating_value
        else:
            new_rating = Rating(username=current_user.username, isbn=isbn, rating=rating_value)
            db.session.add(new_rating)

        db.session.commit()

        # Retain search query and sort option
        search_query = request.args.get('search_query')
        return redirect(url_for('home', search_query=request.args.get('search_query')))
    
    return render_template('rating.html', book=book, user_rating=user_rating)

@app.route('/rate/<int:isbn>/change', methods=['GET', 'POST'])
@login_required
def change_rating(isbn):
    book = Book.query.get_or_404(isbn)
    user_rating = Rating.query.filter_by(username=current_user.username, isbn=isbn).first()

    if request.method == 'POST':
        rating_value = int(request.form['rating'])

        if user_rating:
            user_rating.rating = rating_value
        else:
            new_rating = Rating(username=current_user.username, isbn=isbn, rating=rating_value)
            db.session.add(new_rating)

        db.session.commit()

        # Retain search query and sort option
        search_query = request.args.get('search_query')
        return redirect(url_for('home', search_query=request.args.get('search_query')))
    
    return render_template('change_rating.html', book=book, user_rating=user_rating)

@app.route('/borrow_book/<int:isbn>')
@login_required
def borrow_book(isbn):
    new_borrow = Borrowed(username=current_user.username, isbn=isbn, date=datetime.now())
    db.session.add(new_borrow)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/borrowed', methods=['GET', 'POST'])
@login_required
def borrowed():
    borrowed_query = Book.query.join(Borrowed).filter_by(username = current_user.username)
    borrowed = borrowed_query.all()
    return render_template('borrowed.html', borrowed=borrowed)

@app.route('/return_book/<int:isbn>')
@login_required
def return_book(isbn):
    Borrowed.query.filter(Borrowed.isbn == isbn).delete()
    db.session.commit()
    return redirect(url_for('borrowed'))