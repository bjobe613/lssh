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
                        text=article["ops"])
            news.escape_html()
        db.session.add(news)
        db.session.commit()

        return {
            "msg": "ok",
            "id": news.id
        }, 200
    else:
        return {'msg': 'ej ok'}, 400


@news.route("/<int:x>")
def product():
    return render_template('news_single_view.html')


@news.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_prod():
    if request.method == "GET":
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
