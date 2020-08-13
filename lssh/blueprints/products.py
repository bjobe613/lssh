from flask import Blueprint, render_template
#from lssh.blueprints.forms import FilterForm

# The database is accessed in this manner from blueprints
from lssh.models import db, Product, ProductPictures  #, other objects defined in models
products = Blueprint('products', __name__, url_prefix = '/products')

# Routes should be added here
# Like this:
"""
 @products.route("/test")
 def test_route():
     return "hej världen"
     
"""

@products.route("/catalog", methods=['GET', 'POST'])
def catalog():
    prod = Product.query.filter((Product.status == "Available") | (Product.status == "Reserved")).all()
    return render_template('product_catalog.html', products = prod)

@products.route("/product/<int:x>", methods=['GET'])
def product(x):
    prod = Product.query.filter(Product.articleNumber == x).first()
    return render_template('product_single_view.html', product = prod)