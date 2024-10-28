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
        ath_id INTEGER, 
        bk_title TEXT,
        bk_genre TEXT,
        bk_rating INTEGER,
        bk_pub_date TEXT
    );
"""

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
        
