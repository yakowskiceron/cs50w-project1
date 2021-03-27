import os, csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://kbsgmcmxsiigtq:1b07e5c59561e10e54c6200d58e156b2d34b61e9e77163abb2a6d30f0234e4c8@ec2-34-198-31-223.compute-1.amazonaws.com:5432/d7asutiku5v9h3")
db=scoped_session(sessionmaker(bind=engine))

data = open("books.csv")
reader = csv.reader(data)
for isbn, title, author, year in reader:
    db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
    {"isbn":isbn,"title":title,"author": author, "year":year})

    db.commit()