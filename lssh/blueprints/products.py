from flask import Blueprint, render_template

# The database is accessed in this manner from blueprints
from lssh.models import db #, other objects defined in models
products = Blueprint('products', __name__, url_prefix = '/products')

# Routes should be added here
# Like this:
"""
 @products.route("/test")
 def test_route():
     return "hej världen"
"""

@products.route("/catalog")
def catalog():
    return render_template('product_catalog.html')

@products.route("/product/<int:x>")
def product():
    return render_template('product_single_view.html')