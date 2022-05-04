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


@app.route("/", methods=["POST", "GET"])
def home():
    conn = db_connection()
    cursor = conn.cursor()
   # cursor = conn.execute("SELECT nom FROM familles")  #defini une liste des noms de familles
    if request.method =="POST":
        famille = request.form["famille"]
        date = request.form["start"]
        etat = request.form["etat"]
        graphique = request.form["graphique"]
    else:
        return render_template("index.html", famille = cursor )

@app.route("/<name>")
def perso(name):
    return render_template("index.html", name = name)

if __name__ == "__main__":
    app.run()
