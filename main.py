import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from main_window import Ui_MainWindow
from Connection import Database


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget_books.cellClicked.connect(self.select)
        self.ui.pushButton_add.clicked.connect(self.add)
        self.ui.pushButton_delete.clicked.connect(self.remove)
        self.ui.pushButton_update.clicked.connect(self.edit)
        self.library = Database("library_DB.db")
        self.selected_id = 0
        self.row = 0
        self.refresh()

    def refresh(self):
        books = self.library.read("book")
        self.ui.tableWidget_books.setRowCount(len(books))
        for i in range(len(books)):
            for j in range(len(books[i])):
                self.ui.tableWidget_books.setItem(i, j, QTableWidgetItem(str(books[i][j])))
        self.ui.lineEdit_name.setText("")
        self.ui.lineEdit_author.setText("")
        self.ui.lineEdit_year.setText("")
        self.ui.lineEdit_price.setText("")
        self.ui.lineEdit_pages.setText("")
        self.ui.lineEdit_genre.setText("")

    def add(self):
        if self.ui.lineEdit_author.text() == "" and self.ui.lineEdit_genre.text() == "" and \
           self.ui.lineEdit_name.text() == "" and self.ui.lineEdit_price.text() == "":
            QMessageBox.information(self, "Error", "Please fill all the fields")
        else:
            author = self.ui.lineEdit_author.text()
            genre = self.ui.lineEdit_genre.text()
            name = self.ui.lineEdit_name.text()
            price = self.ui.lineEdit_price.text()
            year = self.ui.lineEdit_year.text()
            pages = self.ui.lineEdit_pages.text()
            self.library.insert(name, author, year, genre, price, pages)
            self.refresh()

    def select(self, row, col):
        self.row = row
        self.selected_id = self.ui.tableWidget_books.item(row, 0).text()
        self.ui.lineEdit_name.setText(self.ui.tableWidget_books.item(row, 1).text())
        self.ui.lineEdit_author.setText(self.ui.tableWidget_books.item(row, 2).text())
        self.ui.lineEdit_year.setText(self.ui.tableWidget_books.item(row, 3).text())
        self.ui.lineEdit_genre.setText(self.ui.tableWidget_books.item(row, 4).text())
        self.ui.lineEdit_price.setText(self.ui.tableWidget_books.item(row, 5).text())
        self.ui.lineEdit_pages.setText(self.ui.tableWidget_books.item(row, 6).text())

    def remove(self):
        if self.selected_id != 0:
            self.library.delete("book", self.selected_id)
            self.selected_id = 0
            self.refresh()

    def edit(self):
        if self.selected_id != 0:
            self.library.update(
                self.ui.lineEdit_name.text(),
                self.ui.lineEdit_author.text(),
                self.ui.lineEdit_year.text(),
                self.ui.lineEdit_genre.text(),
                self.ui.lineEdit_price.text(),
                self.ui.lineEdit_pages.text(),
                self.selected_id
            )
            self.selected_id = 0
            self.refresh()


app = QApplication(sys.argv)
main = Main()
main.show()
app.exec()