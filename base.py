import sqlite3                                                          #import le module sqlite3
from flask import Flask, redirect, url_for, render_template, request    #import le module Flask 

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])            #defini page principal
def home():
    return render_template("index.html")            #redirige vers "index.html"

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("index.html")            #redirige vers "index.html"

@app.route("/GraphV", methods =["POST", "GET"])
def GraphV():
    connection = sqlite3.connect("vache.db")    #se connecte a la base de données
    cursor = connection.cursor()

    if request.method =="POST":        #verifie si il y a bien une requette POST
        famille = request.form["famille"]   #recupere les données du formulaire 
        annee = request.form["an"]          #recupere les données du formulaire
        mois = request.form["mois"]         #recupere les données du formulaire
        if mois == "None":      
            mois = "__"         #si l'utilisateur n'a pas choisit de mois on le change en caractere non specifié pour la requete SQL
        if famille == "None":   #si l'utilisateur n'a pas choisit de famille on execute cette requete SQL
            truc = f"SELECT date FROM velages WHERE date LIKE '__/{mois}/{annee}'"   # la requete SQL vaas recuperer toutes les données correspondant à la demande de l'utilisateur dans la database
            res = cursor.execute(truc)
            res = res.fetchall()
            for i in range(len(res)):       #on change la liste de tuples en un liste de dates
                res[i]= res[i][0]
            nombre = len(res)

            mois_annee = res
            dict = {}
            labels = []
            data = []
            for i in range(len(res)):
                if res[i] not in dict :
                    dict[res[i]] = 1
                else:
                    dict[res[i]] += 1
            for key, value in dict.items(): #on defini les data du graphs en utlilisant le dictionnaire creer au dessus
                labels.append(key)
                data.append(value)                

            return render_template("velages.html", mois_annee = labels, nombre_velage = data, mois = mois, annee = annee, velage = nombre) #redirige vers "velages.html" avec toutes les variables definies"
            
        
        if famille != "None":   #si l'utilisateur a choisit une famille on execute cette requete SQL (la requete SQL vaas recuperer toutes les données correspondant à la demande de l'utilisateur dans la database)
            truc = f"SELECT date FROM velages WHERE date LIKE '%%/{mois}/{annee}' AND id IN(SELECT velage_id FROM animaux_velages WHERE animal_id IN (SELECT id FROM animaux WHERE famille_id = (SELECT id FROM familles WHERE nom == '{famille}')))"
            res = cursor.execute(truc)
            res = res.fetchall()
            for i in range(len(res)):       #on change la liste de tuples en un liste de dates
                res[i]= res[i][0]
            nombre = len(res)

            mois_annee = res
            dict = {}
            labels = []
            data = []
            for i in range(len(res)):
                if res[i] not in dict :
                    dict[res[i]] = 1
                else:
                    dict[res[i]] += 1
            for key, value in dict.items():
                labels.append(key)
                data.append(value)                

            return render_template("velages.html", mois_annee = labels, nombre_velage = data, mois = mois, annee = annee, velage = nombre)
            


@app.route("/GraphPL", methods =["POST", "GET"])
def GraphPL():
    #liste de toute les dates de pleines lunes
    pl_lune = ['11/01/1990', '09/02/1990', '11/03/1990', '10/04/1990', '09/05/1990', '08/06/1990', '08/07/1990', '08/08/1990', '05/09/1990', '04/10/1990', '02/11/1990', '02/12/1990', '31/12/1990', '30/01/1991', '28/02/1991', '30/03/1991', '28/04/1991', '28/05/1991', '27/06/1991', '26/07/1991', '25/08/1991', '23/09/1991', '23/10/1991', '21/11/1991', '21/12/1991', '19/01/1992', '18/02/1992', '18/03/1992', '17/04/1992', '16/05/1992', '15/06/1992', '14/07/1992', '13/08/1992', '12/09/1992', '11/10/1992', '10/11/1992', '09/12/1992', '08/01/1993', '06/02/1993', '11/03/1993', '06/04/1993', '06/05/1993', '04/06/1993', '03/07/1993', '02/08/1993', '01/09/1993', '30/09/1993', '30/10/1993', '29/11/1993', '28/12/1993', '27/01/1994', '26/02/1994', '27/03/1994', '25/04/1994', '25/05/1994', '23/06/1994', '22/07/1994', '21/08/1994', '19/09/1994', '19/10/1994', '18/11/1994', '18/12/1994', '16/01/1995', '15/02/1995', '17/03/1995', '15/04/1995', '14/05/1995', '13/06/1995', '12/07/1995', '10/08/1995', '09/09/1995', '08/10/1995', '07/11/1995', '07/12/1995', '05/01/1996', '04/02/1996', '05/03/1996', '04/04/1996', '03/05/1996', '01/06/1996', '01/07/1996', '30/07/1996', '28/08/1996', '27/09/1996', '26/10/1996', '25/11/1996', '24/12/1996', '23/01/1997', '22/02/1997', '24/03/1997', '22/04/1997', '22/05/1997', '20/06/1997', '20/07/1997', '18/08/1997', '16/09/1997', '16/10/1997', '14/11/1997', '14/12/1997', '12/01/1998', '11/02/1998', '13/03/1998', '11/04/1998', '11/05/1998', '10/06/1998', '09/07/1998', '08/08/1998', '06/09/1998', '05/10/1998', '04/11/1998', '03/12/1998', '02/01/1999', '31/01/1999', '02/03/1999', '31/03/1999', '30/04/1999', '30/05/1999', '28/06/1999', '28/07/1999', '26/08/1999', '25/09/1999', '24/10/1999', '23/11/1999', '22/12/1999', '21/01/2000', '19/02/2000', '20/03/2000', '18/04/2000', '18/05/2000', '16/06/2000', '16/07/2000', '15/08/2000', '13/09/2000', '13/10/2000', '11/11/2000', '11/12/2000', '09/01/2001', '08/02/2001', '09/03/2001', '08/04/2001', '07/05/2001', '06/06/2001', '05/07/2001', '04/08/2001', '02/10/2001', '01/11/2001', '30/11/2001', '30/12/2001', '28/01/2002', '27/02/2002', '28/03/2002', '27/04/2002', '26/05/2002', '24/06/2002', '24/07/2002', '22/08/2002', '21/09/2002', '21/10/2002', '20/11/2002', '19/12/2002', '18/01/2003', '16/02/2003', '18/03/2003', '16/04/2003', '16/05/2003', '14/06/2003', '13/07/2003', '12/08/2003', '10/09/2003', '10/10/2003', '09/11/2003', '08/12/2003', '07/01/2004', '06/02/2004', '06/03/2004', '05/04/2004', '04/05/2004', '03/06/2004', '02/07/2004', '31/07/2004', '30/08/2004', '28/09/2004', '28/10/2004', '26/11/2004', '26/12/2004', '25/01/2005', '24/02/2005', '25/03/2005', '24/04/2005', '23/05/2005', '22/06/2005', '21/07/2005', '19/08/2005', '18/09/2005', '17/10/2005', '16/11/2005', '15/12/2005', '14/01/2006', '13/02/2006', '14/03/2006', '13/04/2006', '13/05/2006', '11/06/2006', '11/07/2006', '09/08/2006', '07/09/2006', '07/10/2006', '05/11/2006', '05/12/2006', '03/01/2007', '02/02/2007', '03/03/2007', '02/04/2007', '02/05/2007', '01/06/2007', '30/06/2007', '30/07/2007', '28/08/2007', '26/09/2007', '26/10/2007', '24/11/2007', '24/12/2007', '22/01/2008', '21/02/2008', '21/03/2008', '20/04/2008', '20/05/2008', '18/06/2008', '18/07/2008', '16/08/2008', '15/09/2008', '14/10/2008', '13/11/2008', '12/12/2008', '11/01/2009', '09/02/2009', '11/03/2009', '09/04/2009', '09/05/2009', '07/06/2009', '07/07/2009', '06/08/2009', '04/09/2009', '04/10/2009', '02/11/2009', '02/12/2009', '31/12/2009', '30/01/2010', '28/02/2010', '30/03/2010', '28/04/2010', '27/05/2010', '26/06/2010', '26/07/2010', '24/08/2010', '23/09/2010', '23/10/2010', '21/11/2010', '21/12/2010', '19/01/2011', '18/02/2011', '19/03/2011', '18/04/2011', '17/05/2011', '15/06/2011', '15/07/2011', '13/08/2011', '12/09/2011', '12/10/2011', '10/11/2011', '10/12/2011', '09/01/2012', '07/02/2012', '08/03/2012', '06/04/2012', '06/05/2012', '04/06/2012', '03/07/2012', '02/08/2012', '31/08/2012', '30/09/2012', '29/10/2012', '28/11/2012', '27/01/2013', '25/02/2013', '27/03/2013', '25/04/2013', '25/05/2013', '23/26/2013', '22/07/2013', '21/08/2013', '19/09/2013', '18/10/2013', '17/11/2013', '17/12/2013', '16/01/2014', '14/02/2014', '16/03/2014', '15/04/2014', '14/05/2014', '13/06/2014', '12/07/2014', '10/08/2014', '09/09/2014', '08/10/2014', '06/11/2014', '06/12/2014', '05/01/2015', '03/02/2015', '05/03/2015', '04/04/2015', '04/05/2015', '02/06/2015', '02/07/2015', '31/07/2015', '29/08/2015', '28/09/2015', '27/10/2015', '25/11/2015', '25/12/2015', '24/01/2016', '22/02/2016', '23/03/2016', '22/04/2016', '21/05/2016', '20/06/2016', '19/07/2016', '18/08/2016', '16/09/2016', '16/10/2016', '14/11/2016', '14/12/2016', '12/01/2017', '11/02/2017', '12/03/2017', '11/04/2017', '10/05/2017', '09/06/2017', '09/07/2017', '07/08/2017', '06/09/2017', '05/10/2017', '04/11/2017', '03/12/2017', '02/01/2018', '31/01/2018', '02/03/2018', '31/03/2018', '30/04/2018', '29/05/2018', '28/06/2018', '27/07/2018', '26/08/2018', '25/09/2018', '24/10/2018', '23/11/2018', '22/12/2018', '21/01/2019', '29/02/2019', '21/03/2019', '19/04/2019', '18/05/2019', '17/06/2019', '16/07/2019', '15/08/2019', '14/09/2019', '13/10/2019', '12/11/2019', '12/12/2019', '10/01/2020', '09/02/2020', '09/03/2020', '08/04/2020', '07/05/2020', '05/06/2020', '05/07/2020', '03/08/2020', '02/09/2020', '01/10/2020', '31/10/2020', '30/11/2020', '30/12/2020']
    connection = sqlite3.connect("vache.db")    #connection a la base de données
    cursor = connection.cursor()

    if request.method =="POST":     #verifie si il y a un requete POST
        famille = request.form["famille"]
        annee = request.form["an"]
        mois = request.form["mois"]
        if mois == "None":      # si l'utilisateur ne choisit pas de mois on le change en un caractere non specifié pour la requete SQL
            mois = "__"
        if famille == "None":
            truc = f"SELECT date FROM velages WHERE date LIKE '__/{mois}/{annee}'"  # la requete SQL vaas recuperer toutes les données correspondant à la demande de l'utilisateur dans la database
            res = cursor.execute(truc)
            res = res.fetchall()
            nombre = len(res)
            pl =0
            npl = 0

            for i in range(len(res)):       #compte combien de dates de "res" sont des dates de pleine lune
                if res[i][0] in pl_lune:
                    pl += 1
                else:
                    npl +=1
            
            #redirige vers la page du graph avec toutes les variable
            return render_template("pleine-lune.html", vache_naissance = [pl, npl], mois = mois, annee = annee, velage = nombre) 
            
        
        if famille != "None":   # la requete SQL vaas recuperer toutes les données correspondant à la demande de l'utilisateur dans la database
            truc = f"SELECT date FROM velages WHERE date LIKE '%%/{mois}/{annee}' AND id IN(SELECT velage_id FROM animaux_velages WHERE animal_id IN (SELECT id FROM animaux WHERE famille_id = (SELECT id FROM familles WHERE nom == '{famille}')))"
            res = cursor.execute(truc)
            res = res.fetchall()
            nombre = len(res)
            pl =0
            npl = 0

            for i in range(len(res)):       #compte combien de dates de "res" sont des dates de pleine lune
                if res[i][0] in pl_lune:
                    pl += 1
                else:
                    npl +=1
                    
             #redirige vers la page du graph avec toutes les variable
            return render_template("pleine-lune.html", vache_naissance = [pl, npl], mois = mois, annee = annee, velage = nombre)
            

@app.route("/GraphR", methods =["POST", "GET"])
def GraphR():
    
    if request.method =="POST":
        return f"<p>cella ne fonctionne pas</p>"        #redirige vers une page vide car pas fini 

@app.route("/velage", methods =["POST", "GET"])
def velage():
    return render_template("menu-velage.html")         #redirige vers "menu-velage.html"

@app.route("/pl", methods =["POST", "GET"])
def pl():
    return render_template("menu-pl.html")             #redirige vers "menu-pl.html"

@app.route("/rep", methods =["POST", "GET"])
def rep():
    return render_template("menu-repartition.html")    #redirige vers "menu-repartition.html"


if __name__ == "__main__":
    app.run(debug = True)
