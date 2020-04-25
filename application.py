from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/resume.html")
def resume():
    return render_template("resume.html")

    