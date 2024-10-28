"""
    Name: library_database.py
    Author: Jessica Soler
    Date: 10/27/24
    Purpose: CRUD module for Jessica's Library Database
"""

# Import sqlite3 database library
import sqlite3

DATABASE = 'library.db'

#---SQL STATEMENTS--------------------------------------------------------------SQL STATEMENTS----#
# SQL statements are text. SQL queries can be very long.
# A SQL statement can be assigned to a string variable.

CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS tbl_book (
        bk_id INTEGER PRIMARY KEY,
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
    

        
def user_input():
    pass


def display_books():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        
        # a list of tuples
        # each tuple is a record/row in the database
        records = cursor.execute(FETCH_ALL_RECORDS).fetchall()
        
        return records


def find_book():
    pass


def delete_book():
    pass