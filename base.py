import sqlite3
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

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
    test = ["salut", "bite"]

    if request.method =="POST":
        famille = request.form["famille"]
        annee = request.form["an"]
        mois = request.form["mois"]
        if mois == "None":
            mois = "__"
        if famille == "None":
            truc = f"SELECT date FROM velages WHERE date LIKE '__/{mois}/{annee}'"
            res = cursor.execute(truc)
            res = res.fetchall()
            for i in range(len(res)):
                res[i]= res[i][0]
            nombre = len(res)

            mois_annee = res
            dict = {}
            labels = []
            data = []
            print(res)
            for i in range(len(res)):
                if res[i] not in dict :
                    dict[res[i]] = 1
                else:
                    dict[res[i]] += 1
            for key, value in dict.items():
                labels.append(key)
                data.append(value)                

            return render_template("velages.html", test = test, mois_annee = labels, nombre_velage = data, mois = mois, annee = annee, velage = nombre)
            
        
        if famille != "None":
            truc = f"SELECT date FROM velages WHERE date LIKE '%%/{mois}/{annee}' AND id IN(SELECT velage_id FROM animaux_velages WHERE animal_id IN (SELECT id FROM animaux WHERE famille_id = (SELECT id FROM familles WHERE nom == '{famille}')))"
            res = cursor.execute(truc)
            res = res.fetchall()
            for i in range(len(res)):
                res[i]= res[i][0]
            nombre = len(res)

            mois_annee = res
            dict = {}
            labels = []
            data = []
            print(res)
            for i in range(len(res)):
                if res[i] not in dict :
                    dict[res[i]] = 1
                else:
                    dict[res[i]] += 1
            for key, value in dict.items():
                labels.append(key)
                data.append(value)                

            return render_template("velages.html", test = test, mois_annee = labels, nombre_velage = data, mois = mois, annee = annee, velage = nombre)
            
            #res = cursor.execute(truc)
            #res = res.fetchall()
            #nombre = len(res)
            #return render_template("velages.html", mois = mois, annee = annee, nombre_velage = nombre)
            #return f"voila {res}"


@app.route("/GraphPL", methods =["POST", "GET"])
def GraphPL():
    
    connection = sqlite3.connect("vache.db")
    cursor = connection.cursor()

    if request.method =="POST":
        famille = request.form["famille"]
        annee = request.form["an"]
        mois = request.form["mois"]
        if mois == "None":
            mois = "__"
        if famille == "None":
            truc = f"SELECT date FROM velages WHERE date LIKE '__/{mois}/{annee}'"
            res = cursor.execute(truc)
            res = res.fetchall()
            nombre = len(res)
            mois_annee = res
            nombre_velage = [3]
            return render_template("velages.html", mois_annee = mois_annee, nombre_velage = nombre_velage, mois = mois, annee = annee, velage = nombre)
            
        
        if famille != "None":
            truc = f"SELECT date FROM velages WHERE date LIKE '%%/{mois}/{annee}' AND id IN(SELECT velage_id FROM animaux_velages WHERE animal_id IN (SELECT id FROM animaux WHERE famille_id = (SELECT id FROM familles WHERE nom == '{famille}')))"
            res = cursor.execute(truc)
            res = res.fetchall()
            nombre = len(res)
            return render_template("velages.html", mois = mois, annee = annee, nombre_velage = nombre)
            #return f"voila {res}"

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
