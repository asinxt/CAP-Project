import sqlite3

def add_cadet(name, test_required):
    conn = sqlite3.connect('cadets.db')
    c = conn.cursor()  
    c.execute('INSERT INTO cadets (name, test_required) VALUES (?, ?)', (name, test_required))  
    conn.commit()
    conn.close()

if __name__ == "__main__":
    name = input("Enter the cadet's name and grade: ")
    test_required = input("Enter the testing required: ")
    add_cadet(name, test_required)  
    print(f"Added {name} with {test_required}")
