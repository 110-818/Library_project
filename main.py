# from library import Library
import sqlite3 as db
from Connection import Database
from book import Book

Book1 = Book(1,'Game Theory' ,'John von Neumann',2015)                  #نظریه بازی ها
Book2 =Book(2,'The Shadow Effect','Deepak Chopra',2005)                # اثر سایه
Book3 = Book(3,'The Compound Effect','Darren Hardy',2000)              # اثر مرکب
Book4 =Book(4,'The Art of War' ,'Sun Tzu',1660)                         # هنر جنگ
Book5 = Book(5,'A Brief History of Time' ,'Stephen Hawking',2000)      #تااریخچه مختصر از زمان
Book6 = Book(6,'Harry Potter','Sajjad Saljouqi',2026)                   # هری پاتر، نوشته سجاد سلجوقی 😄
library = Database('libraryDB.db')
Books = [Book1,Book2,Book3,Book4,Book5]

for book in Books:
    library.insert(book)
library.read(Book5)     #چرا خوانده نمی شود!؟
library.update(Book6,3)
library.Delete(Book1)
