from tkinter import ttk
import tkinter as tk
from data_handler import load_firearms_data
def create_treeview(window):
    columns = ("id", "make", "model", "caliber", "serial_number")

    tree = ttk.Treeview(window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=100)

    tree.pack(fill="both", expand=True)
    return tree

def show_firearms_window():
    root = tk.Tk()
    root.title("Firearms Inventory")
    root.geometry("600x400")

    tree = create_treeview(root)
    load_firearms_data(tree, "data/firearms.db")  # Adjust path as needed

    root.mainloop()