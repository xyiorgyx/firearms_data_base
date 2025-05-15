import sqlite3

def initialize_database(db_path, schema_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables
    with open(schema_path, 'r') as f:
        schema = f.read()
    cursor.executescript(schema)

    # Seed data only if empty
    cursor.execute("SELECT COUNT(*) FROM firearms")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO firearms (make, model, caliber, serial_number) VALUES (?, ?, ?, ?)",
                       ("Glock", "19", "9mm", "ABC123"))

    conn.commit()
    conn.close()