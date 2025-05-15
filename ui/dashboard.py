import tkinter as tk
from tkinter import ttk
from data.data_handler import get_all_firearms  # We'll make this work with filtering later

def create_dashboard(root):
    dashboard_frame = ttk.Frame(root)
    dashboard_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # 🔍 FILTER SECTION
    filter_frame = ttk.LabelFrame(dashboard_frame, text="Filter/Search")
    filter_frame.pack(fill="x", padx=5, pady=5)

    # Filter Inputs
    filters = {}
    fields = [
        ("Employee Name", "employee_name"),
        ("Location", "location"),
        ("Make", "make"),
        ("Model", "model"),
        ("Serial Number", "serial_number"),
        ("Caliber", "caliber")
    ]

    for idx, (label_text, key) in enumerate(fields):
        label = ttk.Label(filter_frame, text=label_text)
        entry = ttk.Entry(filter_frame)
        label.grid(row=0, column=idx * 2, padx=5, pady=5, sticky="e")
        entry.grid(row=0, column=idx * 2 + 1, padx=5, pady=5)
        filters[key] = entry

    # Search Button
    def on_search():
        # We'll improve this later to apply filters
        load_firearms()

    search_button = ttk.Button(filter_frame, text="Search", command=on_search)
    search_button.grid(row=1, column=0, padx=5, pady=5)

    # 📋 TREEVIEW
    tree_frame = ttk.Frame(dashboard_frame)
    tree_frame.pack(fill="both", expand=True, padx=5, pady=5)

    columns = ("id", "make", "model", "serial_number", "caliber", "employee", "location")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=20)

    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=120, anchor="center")

    tree.pack(fill="both", expand=True)

    # 🔘 ACTION BUTTONS
    button_frame = ttk.Frame(dashboard_frame)
    button_frame.pack(pady=10)

    ttk.Button(button_frame, text="View Details").grid(row=0, column=0, padx=5)
    ttk.Button(button_frame, text="Armorer’s Inspection").grid(row=0, column=1, padx=5)
    ttk.Button(button_frame, text="Function Test").grid(row=0, column=2, padx=5)

    # 🔄 Load Firearms into Treeview
    def load_firearms():
        for row in tree.get_children():
            tree.delete(row)

        firearms = get_all_firearms()

        for firearm in firearms:
            tree.insert("", "end", values=firearm)

    load_firearms()
