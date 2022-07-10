import sqlite3

conn = sqlite3.connect('DNS-server.db')
conn.execute('''CREATE TABLE IF NOT EXISTS user
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL);''')
conn.close()

def register(firstname, lastname, username, password):
    conn = sqlite3.connect('DNS-server.db')
    try:
        conn.execute("INSERT INTO user (first_name, last_name, username, password) VALUES (?, ?, ?, ?)", (firstname, lastname, username, password))
        conn.commit()
        return "Registeration done successfully"
    except sqlite3.Error as error:
        return "Repetitive username"
    finally:
        conn.close()

def login(username, password):
    conn = sqlite3.connect('DNS-server.db')
    try:
        record = conn.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password)).fetchone()
        if (record is None):
            return False
        else:
            return True
    finally:
        conn.close()