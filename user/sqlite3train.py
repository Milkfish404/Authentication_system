import sqlite3

class table:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS database 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, password TEXT, email TEXT)""")
    def auth(self, name, password):
        self.c.execute("SELECT * FROM database")
        users = {}
        data = self.c.fetchall()
        for datas in data:
            users[datas[1]] = datas[3]
        if name in users and users[name] == password:
            self.c.execute("SELECT * FROM database WHERE name = :name", {'name': name})
            data = self.c.fetchone()
            if data[0] == 1:
                self.bool = 2
            else:
                self.bool = 1
        else:
            self.bool = 0
    def indication(self):
        return self.bool
    def add(self, name, age, password):
        email = f"{name}@gmail.com"
        self.c.execute("INSERT INTO database ('name', 'age', 'password', email) VALUES (:name, :age, :password, :email)", {'name': name, 'age': age, 'password': password, 'email': email})
    def show(self):
        self.c.execute("SELECT * FROM database")
        data = self.c.fetchall()
        if data:
            print("____________________________________________________________")
            for datas in data:
                print(f"user_id:{datas[0]}, name: {datas[1]}, age: {datas[2]}, email: {datas[3]}")
            print("____________________________________________________________")
        else:
            print("no user found")
    def delete(self, id):
        self.c.execute("SELECT * FROM database")
        data = self.c.fetchall()
        identity = []
        for datas in data:
            identity.append(datas[0])
        print(identity)
        if id in identity:
            self.c.execute("DELETE FROM database WHERE id = :id", {'id': id})
            identity.remove(id)
        else:
            print("user does not exist")
    def edit(self):
        pass

    #USER__________________________________________________FEATURES
    def user(self):
        self.c.execute("SELECT * FROM database WHERE ")

    #ADMIN_________________________________________________FEATURES

system = table()


#default users
system.add("admin", "20", "1234")
system.add("user2", "18", "qwerty")
system.add("user3", "16", "password")
system.add("user4", "21", "1990")

def login():
    print("Login to account")
    name = input("username: ")
    password = input("password: ")
    system.auth(name, password)
    if system.indication() == 1:
        user()
    elif system.indication() == 2:
        admin()
    elif system.indication() == 0:
        print("404 user does not exist")
    login()

def user():
    print("Hello user")
    system.cred_user()

def admin():
    print("Hello admin")

login()

#static
system.conn.commit()
system.conn.close()