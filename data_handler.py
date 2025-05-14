import sqlite3

def load_firearms_data(treeview, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT id, make, model, caliber, serial_number FROM firearms")
    rows = cursor.fetchall()

    for row in rows:
        treeview.insert("", "end", values=row)

    conn.close()
