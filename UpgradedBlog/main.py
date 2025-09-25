from flask import Flask, render_template
import requests
data = requests.get(url="https://api.npoint.io/05f69b858072c818aa58").json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/posts/<int:post_id>")
def post(post_id):
    return render_template("post.html", post=data[post_id-1])


if __name__ == "__main__":
    app.run(debug=True)
