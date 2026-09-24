# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(719, 553)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0 #1a1a2e,\n"
"    stop:1 #16213e\n"
");")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"text-align: center;")

        self.gridLayout_3.addWidget(self.label_name, 0, 0, 1, 1)

        self.lineEdit_name = QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.lineEdit_name, 0, 1, 1, 1)

        self.label_genre = QLabel(self.centralwidget)
        self.label_genre.setObjectName(u"label_genre")
        self.label_genre.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"text-align: center;")

        self.gridLayout_3.addWidget(self.label_genre, 0, 2, 1, 1)

        self.lineEdit_genre = QLineEdit(self.centralwidget)
        self.lineEdit_genre.setObjectName(u"lineEdit_genre")
        self.lineEdit_genre.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.lineEdit_genre, 0, 3, 1, 1)

        self.label_author = QLabel(self.centralwidget)
        self.label_author.setObjectName(u"label_author")
        self.label_author.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"text-align: center;")

        self.gridLayout_3.addWidget(self.label_author, 1, 0, 1, 1)

        self.lineEdit_author = QLineEdit(self.centralwidget)
        self.lineEdit_author.setObjectName(u"lineEdit_author")
        self.lineEdit_author.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.lineEdit_author, 1, 1, 1, 1)

        self.label_price = QLabel(self.centralwidget)
        self.label_price.setObjectName(u"label_price")
        self.label_price.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"text-align: center;")

        self.gridLayout_3.addWidget(self.label_price, 1, 2, 1, 1)

        self.lineEdit_price = QLineEdit(self.centralwidget)
        self.lineEdit_price.setObjectName(u"lineEdit_price")
        self.lineEdit_price.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.lineEdit_price, 1, 3, 1, 1)

        self.label_year = QLabel(self.centralwidget)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"text-align: center;")

        self.gridLayout_3.addWidget(self.label_year, 2, 0, 1, 1)

        self.lineEdit_year = QLineEdit(self.centralwidget)
        self.lineEdit_year.setObjectName(u"lineEdit_year")
        self.lineEdit_year.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.lineEdit_year, 2, 1, 1, 1)

        self.label_pages = QLabel(self.centralwidget)
        self.label_pages.setObjectName(u"label_pages")
        self.label_pages.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"text-align: center;")

        self.gridLayout_3.addWidget(self.label_pages, 2, 2, 1, 1)

        self.lineEdit_pages = QLineEdit(self.centralwidget)
        self.lineEdit_pages.setObjectName(u"lineEdit_pages")
        self.lineEdit_pages.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.lineEdit_pages, 2, 3, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 8px 15px;\n"
"font-size: 13px;")

        self.gridLayout_2.addWidget(self.pushButton_add, 0, 0, 1, 1)

        self.pushButton_update = QPushButton(self.centralwidget)
        self.pushButton_update.setObjectName(u"pushButton_update")
        self.pushButton_update.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 8px 15px;\n"
"font-size: 13px;")

        self.gridLayout_2.addWidget(self.pushButton_update, 0, 1, 1, 1)

        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 8px 15px;\n"
"font-size: 13px;")

        self.gridLayout_2.addWidget(self.pushButton_delete, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.tableWidget_books = QTableWidget(self.centralwidget)
        if (self.tableWidget_books.columnCount() < 7):
            self.tableWidget_books.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget_books.setObjectName(u"tableWidget_books")
        self.tableWidget_books.setStyleSheet(u"background-color: #2a2a4e;\n"
"color: white;\n"
"border: 1px solid #4a4a6e;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.gridLayout_4.addWidget(self.tableWidget_books, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 719, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Library", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645", None))
        self.label_genre.setText(QCoreApplication.translate("MainWindow", u"\u0698\u0627\u0646\u0631", None))
        self.label_author.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0648\u06cc\u0633\u0646\u062f\u0647", None))
        self.label_price.setText(QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a", None))
        self.label_year.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u0644 \u0627\u0646\u062a\u0634\u0627\u0631", None))
        self.label_pages.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u0635\u0641\u062d\u0627\u062a", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.pushButton_update.setText(QCoreApplication.translate("MainWindow", u"update", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        ___qtablewidgetitem = self.tableWidget_books.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tableWidget_books.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem2 = self.tableWidget_books.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        ___qtablewidgetitem3 = self.tableWidget_books.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        ___qtablewidgetitem4 = self.tableWidget_books.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        ___qtablewidgetitem5 = self.tableWidget_books.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        ___qtablewidgetitem6 = self.tableWidget_books.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Pages Count", None))
    # retranslateUi

