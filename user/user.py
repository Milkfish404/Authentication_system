
class person():
    import sqlite3
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    def __init__(self):
        self.conn = person.conn
        self.c = person.c
        self.c.execute("""
        CREATE TABLE user_data (id INETEGER PRIMARY KEY AUTOINCREMENT, name TEXT)
        """)
    def add(self, name):
        self.c.execute("INSERT INTO user_data (:name) VALUES (':name')", {'name': name})
    def show(self):
        show = self.c.fetchall()
        if show:
            print("______________________________________")
            for names in show:
                print(names[1])
            print("______________________________________")
        else:
            print("No data found.")


#Do not change

do = person()

do.conn.commit()
do.conn.close()

