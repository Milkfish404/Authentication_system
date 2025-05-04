import sqlite3
from flask import Flask, render_template, request, flash

conn = sqlite3.connect(':memory:')
c = conn.cursor()

app = Flask(__name__)
app.secret_key = "aspdjasuidhas"

@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(f"username: {username}, password: {password}")
    return render_template('login.html')



@app.route('/create', methods=["GET", "POST"])
def create():
    return render_template('create_account.html')

if __name__ == "__main__":
    app.run(debug=True)