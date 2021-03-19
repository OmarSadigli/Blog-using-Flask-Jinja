from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
all_posts = requests.get(blog_url).json()
post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:id>")
def show_post(id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
