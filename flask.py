from flask import Flask

app = Flask("Scrapper")


@app.route("/")
def home():
    return "hey there!"


app.run("127.0.0.1")
