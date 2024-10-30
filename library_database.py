"""
    Name: library_database.py
    Author: Jessica Soler
    Date: 10/27/24
    Purpose: CRUD module for Jessica's Library Database
"""

# Import sqlite3 database library
import sqlite3
from tkinter import messagebox
import LibraryApp as LibraryApp

DATABASE = 'library.db'

#---SQL STATEMENTS--------------------------------------------------------------SQL STATEMENTS----#
# SQL statements are text. SQL queries can be very long.
# A SQL statement can be assigned to a string variable.

CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS tbl_book (
        bk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        bk_title TEXT,
        bk_author TEXT, 
        bk_genre TEXT,
        bk_rating INTEGER,
        bk_pub_date TEXT
    );
"""

INSERT_RECORD = """
    INSERT INTO tbl_book (
        bk_title,
        bk_author,
        bk_genre,
        bk_rating,
        bk_pub_date
    ) VALUES (?, ?, ?, ?, ?);
"""

FETCH_ALL_RECORDS = "SELECT * FROM tbl_book;"

FETCH_RECORD = "SELECT * FROM tbl_book WHERE bk_id = ?;"

DELETE_RECORD = "DELETE FROM tbl_book WHERE bk_id = ?;"

UPDATE_RECORD = "UPDATE tbl_book SET bk_title = ?, bk_author = ?, bk_genre = ?, bk_rating = ?, bk_pub_date = ? WHERE bk_id = ?;"




#---FUNCTIONS--------------------------------------------------------------------FUNCTIONS----#

def create_table():
    # connect to database, automatically manages resources like files and databases
    # ensures resources are cleaned up, like closing a database connection,
    # after you're done-- even if an error occurs.
    # the cursor object and all connections to the database are closed
    # when the statement exits
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object to interact wiht the database
        cursor = connection.cursor()
        
        # execute the SQL statement
        cursor.execute(CREATE_TABLE)
        

def add_book(bk_title, bk_author, bk_genre, bk_rating, bk_pub_date):
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object to interact with the database
        cursor = connection.cursor()
        
        # execute the SQL script against the database
        cursor.execute(
            INSERT_RECORD,
            (bk_title,
             bk_author,
             bk_genre,
             bk_rating,
             bk_pub_date)
        )  
        

def fetch_books():
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object to interact with the database
        cursor = connection.cursor()
        
        # a list of tuples
        # each tuple is a record/row in the database
        records = cursor.execute(FETCH_ALL_RECORDS).fetchall()
        
        return records


def delete_book(bk_id: int):
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object to interact with the database
        cursor = connection.cursor()
        
        # need to pass the book ID as a tuple
        cursor.execute(DELETE_RECORD, (bk_id,))
    
    messagebox.showinfo("Book Deleted", "Book has been deleted.")
        
        
# GUI implemented
def edit_book():
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object to interact with the database
        cursor = connection.cursor()
        
        # .get() the text from the entry field
        bk_title = LibraryApp.title_entry.get()
        bk_author = LibraryApp.author_entry.get()
        bk_genre = LibraryApp.genre_entry.get()
        bk_rating = LibraryApp.rating_entry.get()
        bk_pub_date = LibraryApp.pub_date_entry.get()
        
        # update the selected record
        cursor.execute(UPDATE_RECORD, (bk_title, bk_author, bk_genre, bk_rating, bk_pub_date))

        
    def save_book():
        pass