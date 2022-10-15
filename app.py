from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "jklasjdflkwejr234"

class SearchForm(FlaskForm):
    search = StringField("", validators=[DataRequired()])
    submit = SubmitField("Search")

@app.route("/", methods=["GET", "POST"])
def index():
    search = None
    form = SearchForm()
    if form.validate_on_submit():
        search = form.search.data
        form.search.data = ""
    return render_template("index.html", search=search, form=form)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")