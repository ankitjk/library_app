from library import app, db
from library.models import *
import csv

if __name__ == '__main__':
    # create tables
    with app.app_context():
        # uncomment this to make create tables from scratch
        # db.drop_all()
        db.create_all()
        # uncomment this to read book data when creating tables from scratch
        # with open("BookData.csv", mode='r') as f:
        #     csvFile = csv.reader(f)
        #     i = 0
        #     for row in csvFile:
        #         if row[0] == "ISBN":
        #             continue
        #         if i > 100000:
        #             break
        #         try:
        #             book = Book(isbn=int(row[0]), title=row[1], author=row[2], year_published=int(row[3]), publisher=row[4])
        #             db.session.add(book)
        #         except:
        #             continue
        #         i += 1
        db.session.commit()
    app.run()