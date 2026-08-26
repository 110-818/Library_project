import sqlite3 as db
from book import Book

class Database:
    def __init__(self,file_name):
        self.connection = db.connect(file_name)
        self.curser = self.connection.cursor()

    def insert(self,book:Book):
        self.curser.execute(f"insert into book values ({book.id},'{book.Name}','{book.Author}','{book.year}')")
        self.connection.commit()
        print('seved')
        
    def read(self,book:Book):
        self.curser.execute(f"select * from book where id = {book.id}")
        
    def update(self,newBook:Book,id):
        self.curser.execute(f"update book set ID = {newBook.id},name = '{newBook.Name}',Ather = '{newBook.Author}',year = {newBook.year} where ID = {id}")
        self.connection.commit()
        print("updated")

    def Delete(self,book:Book):
        self.curser.execute(f"DELETE from book where id = {book.id} ")
        self.connection.commit()
        print("Deleted")
        
    def close(self):
        self.connection.close()
        print("Closed")