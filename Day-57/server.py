from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)


@app.route("/")
def home():
    current_year = dt.date.today().year
    return render_template("index.html", year=current_year)


@app.route("/guess/<name>")
def guess(name):
    age = requests.get(url="https://api.agify.io", params={"name": name}).json()["age"]
    gender = requests.get(url="https://api.genderize.io", params={"name": name}).json()["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog")
def blog():
    all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
