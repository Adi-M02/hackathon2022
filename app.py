from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


url="https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-plus-12g-oc-lhr/p/N82E16814137712?quicklink=true"
result=requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")

prices=doc.find_all(text="$")
print(prices)