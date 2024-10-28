"""
    Name: library_app.py
    Author: Jessica Soler
    Date: 10/27/24
    Purpose: user interface for Jessica's Library Database
"""

import library_database

MENU_PROMPT = """------ Library Database App ------
    (1) Add new book
    (2) Display all books
    (3) Find book by ID
    (4) Delete book
    (5) Exit
    Your selection: """


def main():
    library_database.create_table()
    menu()
    
    
def menu():
    while True:
        user_input = input(MENU_PROMPT)
        
        if user_input == '1':
            # get data from user
            bk_title = input("Enter the book title: ")
            bk_author = input("Enter the author: ")
            bk_genre = input("Enter the genre: ")
            bk_rating = input("Enter rating (1-5): ")
            bk_pub_date = input("Enter publication date: ")
        
            library_database.add_book(
                bk_title,
                bk_author,
                bk_genre,
                bk_rating,
                bk_pub_date
            )
        
        elif user_input == '2':
            books = library_database.display_books()
            
            # iterate through the list of tuples returned
            # from the database query
            for book in books:
                # print each item in the tuple using the [] bracket operator
                # to retrieve each itme in the tuple
                record = f"ID:({book[0]}) {book[1]} "
                record += f"{book[2]} {book[3]} {book[4]} {book[5]}"
                print(record)
            
        elif user_input == '3':
            library_database.find_book()
            
        elif user_input == '4':
            library_database.delete_book()
            
        elif user_input == '5':
            break
        
        else:
            print("Invalid input. Please try again.")
            
main()