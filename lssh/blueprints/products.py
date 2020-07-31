from flask import Blueprint, render_template


# The database is accessed in this manner from blueprints
from lssh.models import db, Furniture, FurniturePictures  #, other objects defined in models
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
    furn = Furniture.query.filter(Furniture.archived == False).all()
    form = FilterForm
    return render_template('product_catalog.html', furnitures = furn, filterform = form)

@products.route("/product/<int:x>", methods=['GET'])
def product(x):
    furn = Furniture.query.filter(Furniture.articleNumber == x).first()
    return render_template('product_single_view.html', furniture = furn)