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
            library_database.add_book()
        
        elif user_input == '2':
            library_database.display_books()
            
        elif user_input == '3':
            library_database.find_book()
            
        elif user_input == '4':
            library_database.delete_book()
            
        elif user_input == '5':
            break
        
        else:
            print("Invalid input. Please try again.")
            
main()