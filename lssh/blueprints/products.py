from flask import Blueprint, render_template, request, make_response, jsonify
import os

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

@products.route("/products_content", methods=['GET', 'POST'])
def products_content():

    prodList = [p.serialize() for p in Product.query.filter((Product.status == "Available") | (Product.status == "Reserved")).all()]
    #for i in Product.query.filter((Product.status == "Available") | (Product.status == "Reserved")).all():
    #    prodList.insert(i.serialize())
    #print(prodList)
    return jsonify(prodList)



@products.route("/product/<int:x>", methods=['GET'])
def product(x):
    prod = Product.query.filter(Product.articleNumber == x).first()
    return render_template('product_single_view.html', product = prod)

@products.route("/add/", methods=['POST'])
def add_product():
    print(request.form)
    if(request.form.get("name") and
       request.form.get("price") and
       request.form.get("condition") and
       request.form.get("category") and
       request.form.get("paymentMethod")):
        prod = Product(name = request.form.get("name"),
                       price = int(request.form.get("price")),
                       condition = int(request.form.get("condition")),
                       paymentMethod = request.form.get("paymentMethod"))
        db.session.add(prod)
        db.session.commit()

        for file in request.files.getlist("file"):
            prod.addPicture(file)

        return {"msg": "ok"}, 200
    else:
        return {'msg': 'ej ok'}, 400
