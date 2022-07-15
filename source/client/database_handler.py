import sqlite3

conn = sqlite3.connect('DNS-client.db')
conn.execute('''CREATE TABLE IF NOT EXISTS key_management
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        public_key TEXT NOT NULL,
        private_key TEXT NOT NULL);''')
conn.close()

def add_new_key(username, public_key, private_key):
    print (public_key)
    print (private_key)
    conn = sqlite3.connect('DNS-client.db')
    try:
        conn.execute("INSERT INTO key_management (username, public_key, private_key) VALUES (?, ?, ?)", (username, public_key, private_key))
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()

def get_keys(username):
    conn = sqlite3.connect('DNS-client.db')
    try:
        record = conn.execute("SELECT public_key, private_key FROM key_management WHERE username=?", (username)).fetchone()
        if (record is None):
            return False
        else:
            return [record[0], record[1]]
    finally:
        conn.close()