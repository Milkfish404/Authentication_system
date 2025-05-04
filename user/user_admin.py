
import sqlite3


class table():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()

    def __init__(self):
        self.conn = table.conn
        self.c = table.c
        self.c.execute("""CREATE TABLE IF NOT EXISTS system_data (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT)""")
    def show(self):
        self.c.execute("SELECT * FROM system_data")
        show = self.c.fetchall()
        if show:
            print("Users")
            print("________________________________________________________")
            for rows in show:
                print(f"user_id: {rows[0]} \t| username: {rows[1]} \t| password: {rows[2]}")
            print("________________________________________________________")
        else:
            print("No user_data found")
    def add(self, name, password):
        self.c.execute("INSERT INTO system_data (name, password) VALUES(:name, :password)", {'name': name, 'password': password})


table.conn.commit()
table.conn.close()