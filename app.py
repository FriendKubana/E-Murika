from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "emurika-secret-key"

@app.route("/language")
def language():
    return render_template("language.html")

@app.route("/login")
def login():
    lang = session.get("lang", "en")
    return render_template("login.html", lang=lang)
