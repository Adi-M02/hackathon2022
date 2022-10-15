from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

    
with open("./templates/index.html","r") as f:
    doc =BeautifulSoup(f,"html.parser")

print(doc.prettify())
