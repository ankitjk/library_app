from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

filepath = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(filepath, 'library.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create tables
with app.app_context():
     db.create_all()
#     with open("BookData.csv", mode='r') as f:
#         csvFile = csv.reader(f)
#         i = 0
#         for row in csvFile:
#             if row[0] == "ISBN":
#                 continue
#             if i > 100:
#                 break
#             try:
#                 book = Book(isbn=int(row[0]), title=row[1], author=row[2], year_published=int(row[3]), publisher=row[4])
#                 db.session.add(book)
#             except:
#                 continue
#             i += 1
#     with open("BookRating.csv", mode='r') as f:
#         csvFile = csv.reader(f)
#         i = 0
#         for row in csvFile:
#             if row[0] == "User-ID":
#                 continue
#             if i > 1000:
#                 break
#             try:
#                 rating = Rating(user_id=int(row[0]), isbn=int(row[1]), rating=int(row[2]))
#                 db.session.add(rating)
#             except:
#                 continue
#             i += 1
#     with open("UserData.csv", mode='r') as f:
#         csvFile = csv.reader(f)
#         i = 0
#         for row in csvFile:
#             if row[0] == "User-ID":
#                 continue
#             if i > 10000:
#                 break
#             try:
#                 user = User(user_id=int(row[0]), isbn=int(row[1]), rating=int(row[2]))
#                 db.session.add(user)
#             except:
#                 continue
#             i += 1
     db.session.commit()

from library import routes