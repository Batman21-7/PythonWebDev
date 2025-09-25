from flask import Flask, render_template
import requests
all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    return render_template('post.html', posts=all_posts, id=(blog_id-1      ))


if __name__ == "__main__":
    app.run(debug=True)
