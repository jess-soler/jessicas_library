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
        self.main_app_window.geometry("1200x500")
        
        # set up frames - database, input fields, and buttons
        self.create_frames()
        
        # set up buttons
        self.create_buttons()
        
        # set up input fields
        self.create_input_fields()
        
        # set up database display
        self.create_database_display()
        
        # update the treeview
        self.update_treeview()
        
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
            main_app_window is 1200 pixels wide
            the input_frame is in the upper left corner
            1200/2 = 600 with 100 pixels of padding on each side = 700
            frame width = 380 pixels
            main_app_window is 500 pixels tall
            the input_frame is in the upper left corner
            500/2 = 250 with 10 pixels of padding on each side = 240
        """
        self.input_frame.place(x=100, y=10, width=380, height=240)
        
        
        # upper right frame = buttons
        """
            upper right frame is 400 pixels wide
            but it needs to be placed 710 pixels from the left side
            the input_frame is 380 pixels wide
            the input_frame is 100 pixels from the left side
            410 + 380 + 10 = 800
        """
        self.button_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        self.button_frame.place(x=710, y=10, width=380, height=240)
        
        
        # bottom half frame = database display
        """
            database_display frame is the bottom half of the window
            the bottom half frame is 1200 pixels wide
            1200 - 20 = 1180 pixels wide with 10 padding on each side
            it is placed 250 pixels from the top with 10 padding on top
            500 - 10 = 490 pixels tall with 10 padding on top
        """
        self.database_display_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        self.database_display_frame.place(x=10, y=250, width=1180, height=240)
        
        
        
    def create_buttons(self):
        # add, edit, delete, close buttons
        
        # add book button
        # used format from AI code
        self.add_book_button = tk.Button(self.button_frame, text="Add Book", command=self.call_add_book)
        self.add_book_button.pack(side="top", fill="x", padx=5, pady=15)
        
        # edit book button
        # used format from AI code
        self.edit_book_button = tk.Button(self.button_frame, text="Edit Book", command=self.call_edit_book)
        self.edit_book_button.pack(side="top", fill="x", padx=5, pady=15)
        
        # delete book button
        # used format from AI code
        self.delete_book_button = tk.Button(self.button_frame, text="Delete Book", command=self.call_delete_book)
        self.delete_book_button.pack(side="top", fill="x", padx=5, pady=15)
        
        # save button
        # used format from AI code
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.call_save_book)
        self.save_button.pack(side="top", fill="x", padx=5, pady=15)
        
        # close app button
        # used format from AI code
        self.close_app_button = tk.Button(self.button_frame, text="Close App", command=self.close_app)
        self.close_app_button.pack(side="top", fill="x", padx=5, pady=15)
        

        
        
        
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
        
        
        
    def create_database_display(self):
        # create a treeview to display the database
        # AI Code, edited
        self.tree = ttk.Treeview(self.database_display_frame, columns=("ID", "Title", "Author", "Genre", "Rating", "Publication Date"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Genre", text="Genre")
        self.tree.heading("Rating", text="Rating")
        self.tree.heading("Publication Date", text="Publication Date")
        self.tree.pack(fill="both", expand=True)        
        
        # insert data into treeview
        
        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.database_display_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

    def update_treeview(self):
        # AI Code
        
        # clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # fetch updated records from the database
        books = library_database.fetch_books()
        
        # insert the updated records into the treeview
        for book in books:
            self.tree.insert("", "end", text=book[0], values=(book[1], book[2], book[3], book[4], book[5]))
        
#---WRAPPER FUNCTIONS----------------------------------------------------------------------------------------------------#
# Call to: library_database.py
# Add, Edit, Save, Delete

    def call_add_book(self):
        
        # .get() the text from the entry field
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        rating = self.rating_entry.get()
        pub_date = self.pub_date_entry.get()
        
        library_database.add_book(title, author, genre, rating, pub_date)
        self.update_treeview()
        
        
    def call_edit_book(self):
        # AI Code
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Edit Book", "Please select a book from the database.")
            return
        
        # AI Code
        # get the book details from the selected item
        book_details = self.tree.item(selected_item)["values"]
        
        # AI Code
        # populate input fields with current details
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, book_details[0])
        self.author_entry.delete(0, tk.END)
        self.author_entry.insert(0, book_details[1])
        self.genre_entry.delete(0, tk.END)
        self.genre_entry.insert(0, book_details[2])
        self.rating_entry.delete(0, tk.END)
        self.rating_entry.insert(0, book_details[3])
        self.pub_date_entry.delete(0, tk.END)
        self.pub_date_entry.insert(0, book_details[4])
        
        # .get() the text from the entry field
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        rating = self.rating_entry.get()
        pub_date = self.pub_date_entry.get()

        library_database.edit_book(title, author, genre, rating, pub_date)
        
    def call_delete_book():
        library_database.delete_book()
        
    def call_save_book():
        library_database.save_book()
        
    def close_app():
        library_database.close_app()
    


# initialize tkinter and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)