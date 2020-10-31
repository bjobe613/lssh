from flask import Blueprint, render_template, request
import json

# The database is accessed in this manner from blueprints
from lssh.models import db, News  # , other objects defined in models
news = Blueprint('news', __name__, url_prefix='/news')

# Routes should be added here
# Like this:
"""
 @news.route("/test")
 def test_route():
     return "hej världen"
"""


@news.route("/", methods=["GET", "POST"])
def catalog():
    if request.method == "GET":
        return render_template('news.html')
    elif request.method == "POST":
        if(request.form.get("title") and
           request.form.get("ingress") and
           request.form.get("article")):
            article = json.loads(request.form.get("article"))

            news = News(title=request.form.get("title"),
                        ingress=request.form.get("ingress"),
                        text=article)

            news.escape_html()

            db.session.add(news)
            db.session.commit()

            if 'news-picture' in request.files:
                file = request.files['news-picture']
                if file.filename != '':
                    news.add_picture(request.files.get("news-picture"))
            return {
                "msg": "ok",
                "id": news.id
            }, 200
        else:
            return {'msg': 'not ok'}, 400


@news.route("/<int:x>/")
def product():
    return render_template('news_single_view.html')


@news.route("/api/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_prod(id):
    if request.method == "GET":
        news = News.query.get_or_404(id)
        return news.serialize()
    elif request.method == "PUT":
        news = News.query.get_or_404(id)

        if request.form.get("title"):
            news.title = request.form.get("title")

        if request.form.get("ingress"):
            news.ingress = request.form.get("ingress")

        if request.form.get("article"):
            news.text = json.loads(request.form.get("article"))

        if 'news-picture' in request.files:
                file = request.files['news-picture']
                if file.filename != '':
                    news.add_picture(request.files.get("news-picture"))

        if request.form.get("published"):
            if request.form.get("published") == "true":
                news.published = True
            elif request.form.get("published") == "false":
                news.published = False

        news.escape_html()
        db.session.commit()
        return news.serialize()
    elif request.method == "DELETE":
        news = News.query.get_or_404(id)
        if news.published:
            return {"msg": "cant delete published articles"}
        else:
            db.session.delete(news)
            db.session.commit()
            return news.serialize()
    return ""
