import tkinter as tk
from tkinter import messagebox
import AI_LIBRARY  # Import your AI_LIBRARY file with functions defined

# # Initialize database
# AI_LIBRARY.initialize_database()

# Main App Class
# class LibraryApp:
#     def __init__(self, root):
        # self.root = root
        # self.root.title("Library Database")
        # self.root.geometry("600x400")
        
        # # Set up main frame for the content display area
        # self.main_frame = tk.Frame(self.root)
        # self.main_frame.pack(fill="both", expand=True)
        
        # Menu Buttons
        # self.create_menu_buttons()
        
        # # Set default view
        # self.display_view_all()

    # def create_menu_buttons(self):
    #     # menu_frame = tk.Frame(self.root, bd=2, relief=tk.RAISED)
    #     # menu_frame.pack(fill="x")

    #     btn_add = tk.Button(menu_frame, text="Add Book", command=self.display_add_book)
    #     btn_add.pack(side="left", padx=5, pady=5)
        
    #     btn_view = tk.Button(menu_frame, text="View All Books", command=self.display_view_all)
    #     btn_view.pack(side="left", padx=5, pady=5)
        
    #     btn_search = tk.Button(menu_frame, text="Search Book", command=self.display_search_book)
    #     btn_search.pack(side="left", padx=5, pady=5)
        
    #     btn_delete = tk.Button(menu_frame, text="Delete Book", command=self.display_delete_book)
    #     btn_delete.pack(side="left", padx=5, pady=5)
        
    # def clear_main_frame(self):
    #     for widget in self.main_frame.winfo_children():
    #         widget.destroy()

    def display_add_book(self):
        self.clear_main_frame()
        
        tk.Label(self.main_frame, text="Add a New Book", font=("Helvetica", 16)).pack(pady=10)
        
        # Entry fields
        tk.Label(self.main_frame, text="Title:").pack(anchor="w")
        self.title_entry = tk.Entry(self.main_frame)
        self.title_entry.pack(fill="x", padx=5, pady=2)
        
        tk.Label(self.main_frame, text="Author:").pack(anchor="w")
        self.author_entry = tk.Entry(self.main_frame)
        self.author_entry.pack(fill="x", padx=5, pady=2)
        
        tk.Label(self.main_frame, text="Genre:").pack(anchor="w")
        self.genre_entry = tk.Entry(self.main_frame)
        self.genre_entry.pack(fill="x", padx=5, pady=2)
        
        tk.Label(self.main_frame, text="Rating (1-5):").pack(anchor="w")
        self.rating_entry = tk.Entry(self.main_frame)
        self.rating_entry.pack(fill="x", padx=5, pady=2)
        
        tk.Label(self.main_frame, text="Publication Date (YYYY-MM-DD):").pack(anchor="w")
        self.pub_date_entry = tk.Entry(self.main_frame)
        self.pub_date_entry.pack(fill="x", padx=5, pady=2)
        
        # Submit button
        submit_btn = tk.Button(self.main_frame, text="Add Book", command=self.add_book)
        submit_btn.pack(pady=10)
        
    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        rating = self.rating_entry.get()
        pub_date = self.pub_date_entry.get()
        
        if not (title and author and genre and rating.isdigit() and pub_date):
            messagebox.showerror("Input Error", "Please fill out all fields correctly.")
            return
        
        if not (1 <= int(rating) <= 5):
            messagebox.showerror("Input Error", "Rating must be between 1 and 5.")
            return
        
        success = AI_LIBRARY.add_book(title, author, genre, int(rating), pub_date)
        
        if success:
            messagebox.showinfo("Success", "Book added successfully.")
            self.display_view_all()
        else:
            messagebox.showerror("Error", "Failed to add book.")

    def display_view_all(self):
        self.clear_main_frame()
        
        tk.Label(self.main_frame, text="All Books", font=("Helvetica", 16)).pack(pady=10)
        
        books = AI_LIBRARY.fetch_all_books()
        if not books:
            tk.Label(self.main_frame, text="No books in the database.").pack()
            return
        
        for book in books:
            book_str = f"{book[0]}: {book[1]} by {book[2]} | Genre: {book[3]} | Rating: {book[4]} | Published: {book[5]}"
            tk.Label(self.main_frame, text=book_str).pack(anchor="w")

    def display_search_book(self):
        self.clear_main_frame()
        
        tk.Label(self.main_frame, text="Search for a Book", font=("Helvetica", 16)).pack(pady=10)
        
        tk.Label(self.main_frame, text="Search by Title, Author, or Genre:").pack(anchor="w")
        self.search_entry = tk.Entry(self.main_frame)
        self.search_entry.pack(fill="x", padx=5, pady=5)
        
        search_btn = tk.Button(self.main_frame, text="Search", command=self.search_book)
        search_btn.pack(pady=5)

    def search_book(self):
        keyword = self.search_entry.get()
        
        results = AI_LIBRARY.search_books(keyword)
        if not results:
            messagebox.showinfo("Search Results", "No matching books found.")
            return
        
        self.clear_main_frame()
        
        tk.Label(self.main_frame, text="Search Results", font=("Helvetica", 16)).pack(pady=10)
        
        for book in results:
            book_str = f"{book[0]}: {book[1]} by {book[2]} | Genre: {book[3]} | Rating: {book[4]} | Published: {book[5]}"
            tk.Label(self.main_frame, text=book_str).pack(anchor="w")
    
    def display_delete_book(self):
        self.clear_main_frame()
        
        tk.Label(self.main_frame, text="Delete a Book by ID", font=("Helvetica", 16)).pack(pady=10)
        
        tk.Label(self.main_frame, text="Book ID to delete:").pack(anchor="w")
        self.delete_entry = tk.Entry(self.main_frame)
        self.delete_entry.pack(fill="x", padx=5, pady=5)
        
        delete_btn = tk.Button(self.main_frame, text="Delete", command=self.delete_book)
        delete_btn.pack(pady=5)

    def delete_book(self):
        try:
            book_id = int(self.delete_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Invalid Book ID. Please enter a valid number.")
            return

        if AI_LIBRARY.delete_book_by_id(book_id):
            messagebox.showinfo("Success", "Book deleted successfully.")
            self.display_view_all()
        else:
            messagebox.showerror("Error", "Failed to delete book or book not found.")
        
# Initialize Tkinter and run the app
root = tk.Tk()
app = LibraryApp(root)
root.mainloop()