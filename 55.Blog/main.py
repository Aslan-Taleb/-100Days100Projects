from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = response.json()
    return render_template("index.html", all_posts=all_posts)


@app.route('/<id_post>')
def post(id_post):
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = response.json()
    post_to_show = all_posts[int(id_post)-1]
    title = post_to_show["title"]
    body = post_to_show["body"]
    return render_template("post.html", the_post=post_to_show, title=title, body=body)


if __name__ == "__main__":
    app.run(debug=True)
