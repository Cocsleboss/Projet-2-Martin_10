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
    connection = sqlite3.connect("vache.db")
    cursor = connection.cursor()

    if request.method =="POST":
        famille = request.form["famille"]
        annee = request.form["an"]
        mois = request.form["mois"]
        if mois == "None":
            mois = "__"
        if famille == "":
            truc = f"SELECT date FROM velages WHERE date LIKE '__/{mois}/{annee}'"
            res = cursor.execute(truc)
            res = res.fetchall()
            nombre = len(res)
            return render_template("velages.html", mois = mois, annee = annee, nombre_velage = nombre)
            
        
        if famille != "":
            truc = f"SELECT date FROM velages WHERE date LIKE '%%/{mois}/{annee}' AND id IN(SELECT velage_id FROM animaux_velages WHERE animal_id IN (SELECT id FROM animaux WHERE famille_id = (SELECT id FROM familles WHERE nom == '{famille}')))"
            res = cursor.execute(truc)
            res = res.fetchall()
            nombre = len(res)
            return render_template("velages.html", mois = mois, annee = annee, nombre_velage = nombre)
            #return f"voila {res}"


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
