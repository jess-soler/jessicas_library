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
        # get user input for menu selection
        user_input = input(MENU_PROMPT)
        
        # (1) Add new book
        if user_input == '1':
            
            # get data from user
            bk_title = input("Enter the book title: ")
            bk_author = input("Enter the author: ")
            bk_genre = input("Enter the genre: ")
            bk_rating = input("Enter rating (1-5): ")
            bk_pub_date = input("Enter publication date: ")

            # add book to database
            library_database.add_book(
                bk_title,
                bk_author,
                bk_genre,
                bk_rating,
                bk_pub_date
            )
            
            # display all books
            library_database.print_books()
        
        # (2) Display all books
        elif user_input == '2':
            
            # display all books
            library_database.print_books()
        
        # (3) Find book by ID    
        elif user_input == '3':
            # display all books
            library_database.print_books()
            
            library_database.find_book()
        
        # (4) Delete book
        elif user_input == '4':
            # display all books
            library_database.print_books()
            
            book = int(input("Enter the book ID: "))
            
            library_database.delete_book(book)
            
            library_database.print_books()
        
        # (5) Exit   
        elif user_input == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid input. Please try again.")
            




main()