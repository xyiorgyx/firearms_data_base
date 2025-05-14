import sqlite3

def initialize_database(path_to_db, path_to_schema):
    conn = sqlite3.connect(path_to_db)
    cursor = conn.cursor()

    with open(path_to_schema, 'r') as file:
        schema_sql = file.read()

    cursor.executescript(schema_sql)  # Runs all CREATE TABLE statements
    conn.commit()
    conn.close()
