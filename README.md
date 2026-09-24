# 📚 Library Manager

A simple desktop application for managing a personal library, built with Python (v3.12) and PySide6 (Qt for Python).

You can add, edit, delete, and view books stored in a local SQLite database. The table displays all books with their details, and a stylish gradient UI makes it easy on the eyes.

---

## ✨ Features

- ➕ Add new books (Name, Author, Year, Genre, Price, Pages Count)
- 📝 Edit selected book details
- ❌ Delete selected book
- 📊 View all books in a table
- 💾 SQLite-powered persistent storage
- 🎨 Modern gradient UI with rounded corners
- 🖱️ Click on any row to load its data into the form
- ⚡ Auto-refresh after every change

---

## 🎯 How It Works

The application is built around two main classes:

| Class | File | Responsibility |
|-------|------|----------------|
| `Database` | `Connection.py` | Handles all SQL operations (read, insert, update, delete) |
| `Main` | `main.py` | Handles UI logic, button clicks, and table selection |
| `Ui_MainWindow` | `main_window.py` | Auto-generated UI from Qt Designer |

### 🧠 Workflow

1. On startup, `refresh()` loads all books from the database into the table.
2. Clicking a row fills the LineEdits with that book's details.
3. The `add` button inserts a new book into the database.
4. The `update` button edits the selected book.
5. The `delete` button removes the selected book.
6. After every operation, `refresh()` is called to update the table.

---

## 🗂️ Project Structure

```
project-folder/
│── main.py
│── Connection.py
│── main_window.py
│── main_window.ui
│── library_DB.db
│── README.md
```

---

## 🛠️ How to Run

Install dependencies:

```bash
pip install PySide6
```

Run the application:

```bash
python main.py
```

---

## 📦 Database

The SQLite database stores all books in a table named `book` with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| ID | INTEGER | Primary key (auto) |
| Name | TEXT | Book name |
| Author | TEXT | Book author |
| Year | TEXT | Publication year |
| Gender | TEXT | Book genre |
| Price | TEXT | Book price |
| Pages Count | TEXT | Number of pages |

---

## 🚀 Future Improvements

- 🔍 Search and filter books
- 🖼️ Book cover preview
- 📚 Category management
- 🧾 Borrow / Return tracking

---

## 👨‍💻 Author

Created by **Ali Asghari**
