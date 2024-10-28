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
        self.main_app_window.geometry("800x600")
        
    # set up main frame for the database display
    self.database_frame = tk.Frame(self.main_app_window)
    # allow the database to expand with the window
    # fill the window with the database frame
    self.database_frame.grid(fill="both", expand=True)
    
    # menu buttons
    self.create_menu_buttons()
    
    # set the default view
    self.  