from flask import Flask, render_template, redirect

app = Flask(__name__)


tests = ["Conductivity", "TOC", "Bioburden", "Endotoxin", "Conductivity"]


@app.route('/')
def hello_world():
    return render_template("index.html", tests=tests)
