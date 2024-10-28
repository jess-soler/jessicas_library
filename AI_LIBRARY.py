import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='library_errors.log', level=logging.ERROR)

def connect():
    return sqlite3.connect('library.db')

def create_table():
    with connect() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT,
                rating INTEGER CHECK(rating BETWEEN 1 AND 5),
                pub_date TEXT CHECK(pub_date LIKE '____-__-__')
            )
        ''')

def add_book(title, author, genre, rating, pub_date):
    """Adds a new book to the database."""
    try:
        with connect() as conn:
            conn.execute(
                "INSERT INTO books (title, author, genre, rating, pub_date) VALUES (?, ?, ?, ?, ?)",
                (title, author, genre, rating, pub_date)
            )
            return True
    except sqlite3.Error as e:
        logging.error(f"Error adding book: {e}")
        return False

def fetch_all_books():
    """Fetches all books in the database."""
    try:
        with connect() as conn:
            return conn.execute("SELECT * FROM books").fetchall()
    except sqlite3.Error as e:
        logging.error(f"Error fetching books: {e}")
        return []

def find_book_by_id(book_id):
    """Finds a book by its ID."""
    try:
        with connect() as conn:
            return conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    except sqlite3.Error as e:
        logging.error(f"Error finding book by ID {book_id}: {e}")
        return None

def delete_book_by_id(book_id):
    """Deletes a book by its ID."""
    try:
        with connect() as conn:
            conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
            return True
    except sqlite3.Error as e:
        logging.error(f"Error deleting book by ID {book_id}: {e}")
        return False

def search_books(keyword):
    """Searches books by title, author, or genre."""
    try:
        with connect() as conn:
            return conn.execute(
                "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR genre LIKE ?",
                (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
            ).fetchall()
    except sqlite3.Error as e:
        logging.error(f"Error searching for books: {e}")
        return []

def initialize_database():
    """Ensures the database and tables are created before use."""
    try:
        create_table()
    except sqlite3.Error as e:
        logging.error(f"Error initializing database: {e}")