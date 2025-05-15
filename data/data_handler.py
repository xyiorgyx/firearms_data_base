import sqlite3

DB_PATH = "data/firearms.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_all_firearms():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                f.id, 
                f.make, 
                f.model, 
                f.serial_number, 
                f.caliber, 
                e.first_name || ' ' || e.last_name AS employee_name,
                s.name AS location
            FROM firearms f
            LEFT JOIN employees e ON f.current_owner_id = e.id
            LEFT JOIN sites s ON e.site_id = s.id
        """)
        return cursor.fetchall()


