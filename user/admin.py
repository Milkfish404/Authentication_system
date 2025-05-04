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

class admin_data():
    conn = table.conn
    c = table.c
    def __init__(self):
        self.conn = admin_data.conn
        self.c = admin_data.c
    def show(self):
        self.c.execute("SELECT * FROM system_data")
        show = self.c.fetchall()
        if show:
            print("Users")
            print("________________________________________________________")
            for rows in show:
                print(f"user_id: {rows[0]} \t| username: {rows[1]}")
            print("________________________________________________________")
        else:
            print("No users available")
    def deactivate(self, name):
        with self.conn:
            self.c.execute("DELETE FROM system_data WHERE name = :name", {'name': name})
            print(f"User {name} has been deactivated")

class user_data:
    conn = table.conn
    c = table.c
    def __init__(self, id):
        self.conn = user_data.conn
        self.c = user_data.c
        self.id = id
    def show(self):
        self.c.execute("SELECT * FROM system_data WHERE id = :id", {'id': self.id})
        show = self.c.fetchone()
        print(f"{show[1]}'s profile")
        print("____________________________________________")
        if show:
            print(f"Username :\t {show[1]}")
            print(f"Password :\t {show[2]}")
            print(f"Gmail Account:\t {show[1]}@gmail.com")
        else:
            print("No users available")
    def deactivate(self):
        self.c.execute("DELETE FROM system_data WHERE id = :id", {'id': self.id})
        print(f"User {self.id} has been deactivated")

class admin_data:
    conn = table.conn
    c = table.c
    def __init__(self):
        self.conn = user_data.conn
        self.c = user_data
        self.id = id
    def show(self):
        self.c.execute("SELECT * FROM system_data WHERE id = :id", {'id': self.id})
        show = self.c.fetchone()
        print(f"{show[1]}'s profile")
        print("debug authentic")
        if show:
            print(f"username: {show[1]}")
            print(f"password: {show[2]}")
            print(f"password: {show[3]}")

admin = admin_data()
user = user_data(3)
system = table()

def main():
    print("a. hash pass")
    print("b. User terminate")
    print("c. user execution")


user.show()

# MISSING
# FUCKING PASSWORD HASHING
# IMPLEMENTING FLASK
# RENDER_TEMPLATE HTML
# CSS FUCKING STATIC
# DATABASE SECURITY
# AUTHENTICATION LOGIC(webpage?)


#do not change
admin.conn.commit()
admin.conn.close()