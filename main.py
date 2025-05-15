import tkinter as tk
from helpers.helpers import center_window
from ui.dashboard import create_dashboard

def main():
    root = tk.Tk()
    root.title("Firearms Manager (AUS)")
    root.configure(bg="#2E2E2E")

    # Set window size and center
    root.geometry(center_window(root, 1000, 700))  # width x height

    # App title label
    title_label = tk.Label(
        root,
        text="Firearms Manager (AUS)",
        font=("Helvetica", 20),
        fg="white",
        bg="#2E2E2E"
    )
    title_label.pack(pady=10)

    # Load the dashboard UI
    create_dashboard(root)

    root.mainloop()

if __name__ == "__main__":
    main()