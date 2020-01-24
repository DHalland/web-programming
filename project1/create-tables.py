import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
   db.execute("CREATE SCHEMA IF NOT EXISTS booksapi")
   db.execute('''CREATE TABLE IF NOT EXISTS booksapi.books (
      isbn VARCHAR(14) PRIMARY KEY,
      title VARCHAR(100) NOT NULL,
      author VARCHAR(40) NOT NULL,
      year integer)'''
   )

   f = open("books.csv")
   reader = csv.reader(f)
   next(reader)
   for isbn, title, author, year in reader:
      db.execute('''INSERT INTO booksapi.books (isbn, title, author, year) 
         VALUES (:isbn, :title, :author, :year)''', 
         {"isbn":isbn,"title":title,"author":author, "year":year})
      print("Added book with ISBN=%s" % isbn)
   db.commit()

if __name__ == "__main__":
   main()