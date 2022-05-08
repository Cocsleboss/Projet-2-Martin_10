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

@app.route("/GraphV", methods =["POST", "GET"])
def GraphV():
    
    if request.method =="POST":
        famille = request.form["famille"]
        date = request.form["date"]
      #  etat = request.form["etat"]
       # graphique = request.form["graphique"]
        #return render_template("velages.html")
        return f"<p>cest bon {famille}</p>"

@app.route("/GraphPL", methods =["POST", "GET"])
def GraphPL():
    
    if request.method =="POST":
        famille = request.form["famille"]
        année = request.form["annee"]
        mois = request.form["mois"]
       # graphique = request.form["graphique"]
        #return render_template("velages.html")
        return f"<p>cest bon {famille}  {année} {mois}</p>"

@app.route("/GraphR", methods =["POST", "GET"])
def GraphR():
    
    if request.method =="POST":
        #famille = request.form["famille"]
        #année = request.form["annee"]
        #mois = request.form["mois"]
       # graphique = request.form["graphique"]
        #return render_template("velages.html")
        return f"<p>cest bon</p>"

@app.route("/velage", methods =["POST", "GET"])
def velage():
    return render_template("menu-velage.html")

@app.route("/pl", methods =["POST", "GET"])
def pl():
    return render_template("menu-pl.html")

@app.route("/rep", methods =["POST", "GET"])
def rep():
    return render_template("menu-repartition.html")


if __name__ == "__main__":
    app.run(debug = True)
