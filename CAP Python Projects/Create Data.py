import sqlite3

def create_table():
    conn = sqlite3.connect('cadets.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS cadets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            test_required TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Table created successfully.")
