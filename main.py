import tkinter as tk
import sqlite3
from firearms_ui import create_treeview
from helpers.helpers import center_window
from data.db_init import initialize_database
firearms_data = []

root = tk.Tk()
root.title("Firearms Manager")
root.configure(bg="#2E2E2E")
root.geometry(center_window(root, 500,500))


title = tk.Label(root, text="Firearms Data Base (AUS)", font= ("Helvetica", 20), bg="grey", )
title.pack(padx=5, pady=5)


create_treeview(root)


initialize_database('data/firearms.db', 'data/schema.sql')
root.mainloop()