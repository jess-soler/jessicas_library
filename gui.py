# I used AI to help build the GUI
# I asked for a tkinter GUI that would allow the entire program
# to function in one window
# I then edited the code to fit the program per my preferences

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# import the library_database module
import library_database

# main app class
class LibraryApp:
    def __init__(self, main_app_window):
        self.main_app_window = main_app_window
        self.main_app_window.title("Jessica's Library Database")
        self.main_app_window.geometry("800x500")
        
        # set up frames - database, input fields, and buttons
        self.create_frames()
        
        # set up buttons
        self.create_buttons()
        
        # set up input fields
        self.create_input_fields()
        
        # create a treeview to display the database
        
        # run window
        self.main_app_window.mainloop()
        
    def create_frames(self):
        """
            upper left frame = input fields
            bd=2 means border width is 2 pixels
            relief=tk.RAISED means the border is raised
        """
        self.input_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        
        
        """
            main_app_window is 800 pixels wide
            the input_frame is in the upper left corner
            800/2 = 400 with 10 pixels of padding on each side = 380
            main_app_window is 500 pixels tall
            the input_frame is in the upper left corner
            500/2 = 250 with 10 pixels of padding on each side = 240
        """
        self.input_frame.place(x=10, y=10, width=380, height=240)
        
        # upper right frame = buttons
        """
            upper right frame is 400 pixels wide
            but it needs to be placed 410 pixels from the left side
            the input_frame is 380 pixels wide
            the input_frame is 10 pixels from the left side
            410 + 380 + 10 = 800
        """
        self.button_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        self.button_frame.place(x=410, y=10, width=380, height=240)
        
        
        # bottom half frame = database display
        """
            database_display frame is the bottom half of the window
            the bottom half frame is 800 pixels wide
            800 - 20 = 780 pixels wide with 10 padding on each side
            it is placed 250 pixels from the top with 10 padding on top
            500 - 10 = 490 pixels tall with 10 padding on top
        """
        self.database_display_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        self.database_display_frame.place(x=10, y=250, width=780, height=240)
        
    def create_buttons(self):
        # add, edit, delete, close buttons
        
        # add book button
        # used format from AI code
        self.add_book_button = tk.Button(self.button_frame, text="Add Book", command=self.call_add_book)
        self.add_book_button.pack(side="top", fill="x", padx=5, pady=5)
        
        # edit book button
        # used format from AI code
        self.edit_book_button = tk.Button(self.button_frame, text="Edit Book", command=self.call_edit_book)
        self.edit_book_button.pack(side="top", fill="x", padx=5, pady=5)
        
        # delete book button
        # used format from AI code
        self.delete_book_button = tk.Button(self.button_frame, text="Delete Book", command=self.call_delete_book)
        self.delete_book_button.pack(side="top", fill="x", padx=5, pady=5)
        
        # close app button
        # used format from AI code
        self.close_app_button = tk.Button(self.button_frame, text="Close App", command=self.close_app)
        self.close_app_button.pack(side="top", fill="x", padx=5, pady=5)
        
    def create_input_fields(self):
        # title, author, genre, rating, pub_date
        # AI Code, edited
        
        # Title input field
        tk.Label(self.input_frame, text="Title:").pack(anchor="w")
        self.title_entry = tk.Entry(self.input_frame)
        self.title_entry.pack(fill="x", padx=5, pady=2)

        # Author input field
        tk.Label(self.input_frame, text="Author:").pack(anchor="w")
        self.author_entry = tk.Entry(self.input_frame)
        self.author_entry.pack(fill="x", padx=5, pady=2)

        # Genre input field
        tk.Label(self.input_frame, text="Genre:").pack(anchor="w")
        self.genre_entry = tk.Entry(self.input_frame)
        self.genre_entry.pack(fill="x", padx=5, pady=2)

        # Rating input field
        tk.Label(self.input_frame, text="Rating (1-5):").pack(anchor="w")
        self.rating_entry = tk.Entry(self.input_frame)
        self.rating_entry.pack(fill="x", padx=5, pady=2)

        # Publication Date input field
        tk.Label(self.input_frame, text="Publication Date (YYYY-MM-DD):").pack(anchor="w")
        self.pub_date_entry = tk.Entry(self.input_frame)
        self.pub_date_entry.pack(fill="x", padx=5, pady=2)
        
        

        
#---WRAPPER FUNCTIONS----------------------------------------------------------------------------------------------------#
# Call to: library_database.py
# Add, Edit, Delete

    def call_add_book():
        library_database.add_book()
        
    def call_edit_book():
        library_database.edit_book()
        
    def call_delete_book():
        library_database.delete_book()
        
    def close_app():
        library_database.close_app()
    

    


# initialize tkinter and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)