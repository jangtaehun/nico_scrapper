from flask import Flask, render_template

app = Flask("Scrapper")


@app.route("/")
def home():
    return render_template("home.html", name="ZZang")


@app.route("/hello")
def hello():
    return "Hey there"


app.run("127.0.0.1")
