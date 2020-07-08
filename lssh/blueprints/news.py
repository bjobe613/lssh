from flask import Blueprint, render_template

# The database is accessed in this manner from blueprints
from lssh.models import db #, other objects defined in models
news = Blueprint('news', __name__, url_prefix = '/news')

# Routes should be added here
# Like this:
"""
 @news.route("/test")
 def test_route():
     return "hej världen"
"""

@news.route("/")
def catalog():
    return render_template('news.html')

@news.route("/<int:x>")
def product():
    return render_template('news_single_view.html')