import sqlite3
import flask

app = flask.Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("vache.sqlite")  # tante de se connecter a la base de données
    except sqlite3.error as e:
        print(e)
    return conn

<<<<<<< Updated upstream

@app.route("/", methods=('GET','POST'))
def home():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nom FROM familles")  #defini une liste des noms de familles
    all_fam = cursor.fetchall()

    if flask.request.method == 'POST':
        famille = flask.request.form["famille"]

        print(famille)

    return flask.render_template("index.html" , familles=all_fam)

    if true:
        cursor.execute("SELECT id FROM animaux WHERE famille_id IN (SELECT id FROM familles WHERE nom LIKE 'Lila')".format())


@app.route("/<name>")
def perso(name):
    return flask.render_template("index.html", oui="oui")

if __name__ == "__main__":
    app.run()

=======
@app.route("/")
def home():
    if request.method =="POST":
        return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("index.html")


@app.route("/graph", methods =["POST", "GET"])
def graph(nm, dt, et, grh):
    if request.method =="POST":
        famille = request.form["famille"]
        date = request.form["date"]
        etat = request.form["etat"]
        graphique = request.form["graphique"]
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug = True)
>>>>>>> Stashed changes
