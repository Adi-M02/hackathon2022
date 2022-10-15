from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

with open("./templates/index.html","r") as f:
    doc =BeautifulSoup(f,"html.parser")

print(doc.prettify())