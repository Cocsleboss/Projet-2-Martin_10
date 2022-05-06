import sqlite3
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("vache.sqlite")  # tante de se connecter a la base de données
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/")
def home():
    if request.method =="POST":
        return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("index.html")

@app.route("/test", methods =["POST", "GET"])
def test():
    
    if request.method =="POST":
        famille = request.form["famille"]
        date = request.form["date"]
        etat = request.form["etat"]
        graphique = request.form["graphique"]
        return f"<p>hello {famille}  {date}  {etat}  {graphique}</p>"

if __name__ == "__main__":
    app.run(debug = True)
