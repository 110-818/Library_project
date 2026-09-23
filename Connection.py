import sqlite3


class Database():
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def read(self, table_name):
        query = f"SELECT * FROM {table_name}"
        result = self.cursor.execute(query)
        export_data = result.fetchall()
        return export_data

    def insert(self, name, author, year, gender, price, pages_count):
        try:
            query = f'INSERT INTO book (Name, Author, Year, Gender, Price, "Pages Count") VALUES (\'{name}\', \'{author}\', \'{year}\', \'{gender}\', \'{price}\', \'{pages_count}\')'
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print("INSERT ERROR:", e)
            return False

    def delete(self, table_name, id):
        try:
            query = f"DELETE FROM {table_name} WHERE ID = {id};"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print("DELETE ERROR:", e)
            return False

    def update(self, name, author, year, gender, price, pages, id):
        try:
            query = f'UPDATE book SET Name=\'{name}\', Author=\'{author}\', Year=\'{year}\', Gender=\'{gender}\', Price=\'{price}\', "Pages Count"=\'{pages}\' WHERE ID={id};'
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print("UPDATE ERROR:", e)
            return False