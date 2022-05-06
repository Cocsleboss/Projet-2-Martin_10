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
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("index.html")

@app.route("/graph", methods =["POST", "GET"])
def graph():
    
    if request.method =="POST":
        famille = request.form["famille"]
        date = request.form["date"]
        etat = request.form["etat"]
        graphique = request.form["graphique"]
        return render_template("graph.html")

if __name__ == "__main__":
    app.run(debug = True)
