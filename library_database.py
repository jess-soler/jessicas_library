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

FETCH_RECORD = "SELECT * FROM tbl_book WHERE bk_id = ?;"

DELETE_RECORD = "DELETE FROM tbl_book WHERE bk_id = ?;"




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
        
def print_books():
            # display all books
            books = fetch_books()
            
            # iterate through the list of tuples returned
            # from the database query
            for book in books:
                # print each item in the tuple using the [] bracket operator
                # to retrieve each itme in the tuple
                record = f"ID:({book[0]}) {book[1]} "
                record += f"{book[2]} {book[3]} {book[4]} {book[5]}"
                print(record)


def find_book():
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object to interact with the database
        cursor = connection.cursor()
        
        bk_id = int(input("Enter the book ID: "))
        
        # a list of tuples
        # each tuple is a record/row in the database
        book = cursor.execute(FETCH_RECORD, (bk_id,)).fetchone()
        
        if book:
            # print each item in the tuple using the [] bracket operator
            # to retrieve each itme in the tuple
            record = f"ID:({book[0]}) {book[1]} "
            record += f"{book[2]} {book[3]} {book[4]} {book[5]}"
            print(record)
        else:
                print("Book not found.")


def delete_book(bk_id: int):
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object to interact with the database
        cursor = connection.cursor()
        
        # delete the selected record
        cursor.execute(DELETE_RECORD, (bk_id, ))
        
def edit_book(bk_id: int):
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object to interact with the database
        cursor = connection.cursor()
        
        # delete the selected record
        cursor.execute(DELETE_RECORD, (bk_id, ))
        
        bk_title = input("Enter the book title: ")
        bk_author = input("Enter the author: ")
        bk_genre = input("Enter the genre: ")
        bk_rating = input("Enter rating (1-5): ")
        bk_pub_date = input("Enter publication date: ")

        # add book to database
        add_book(
            bk_title,
            bk_author,
            bk_genre,
            bk_rating,
            bk_pub_date
        )
        
    def save_book():
        pass
        
    def close_app():
        print("Goodbye!")
        exit()