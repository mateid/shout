from flask import Flask, request, render_template, url_for, flash, redirect
from models import Post
from queries import all_posts
from presentation import FlashMessageCategory


application = Flask(__name__)


@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@application.route("/")
def blog_home():
    posts = all_posts(1, 10)
    return render_template("home.html", posts = posts)


@application.route("/new_post/", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template("new_post.html")

    entry = request.form["post"]
    post = Post()
    post.content = entry
    post.put()
    flash("Post saved!", FlashMessageCategory.info)
    return redirect(url_for("blog_home"))