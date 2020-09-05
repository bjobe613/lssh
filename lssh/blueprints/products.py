from flask import Blueprint, render_template, request, make_response, jsonify
import os

# The database is accessed in this manner from blueprints
from lssh.models import db, Product, ProductPictures, Category, Condition, PaymentMethod  #, other objects defined in models
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
    return render_template('product_catalog.html', products = prod, categories=Category.query.all(), conditions=Condition.query.all(), paymentMethods=PaymentMethod.query.all())

@products.route("/products_content", methods=['GET', 'POST'])
def products_content():

    prodList = [p.serialize() for p in Product.query.filter((Product.status == "Available") | (Product.status == "Reserved")).all()]
    return jsonify(prodList)


@products.route("/categories", methods=['GET'])
def categories():
    catList=[c.serialize() for c in Category.query.all()]
    return jsonify(catList)
    
@products.route("/conditions", methods=['GET'])
def conditions():
    catList=[c.serialize() for c in Condition.query.all()]
    return jsonify(catList)

@products.route("/paymentMethods", methods=['GET'])
def paymentMethods():
    catList=[c.serialize() for c in PaymentMethod.query.all()]
    return jsonify(catList)




@products.route("/product/<int:x>", methods=['GET'])
def product(x):
    prod = Product.query.filter(Product.articleNumber == x).first()
    return render_template("product_single_view.html", product = prod)

@products.route("/add/", methods=['POST'])
def add_product():
    fields = ["name", "price", "condition", "paymentMethod", "description"]
    for field in fields:
        if not request.form.get(field):
            return {"msg": "missing {0} from form".format(field)}, 400
    try:
        prod = Product(name = request.form.get("name"),
                       price = int(request.form.get("price")),
                       category_id = int(request.form.get("category")),
                       condition_id = int(request.form.get("condition")),
                       payment_method_id = int(request.form.get("paymentMethod")),
                       comment = request.form.get("description"))
        db.session.add(prod)
        db.session.commit()
    except:
        return jsonify({"msg": "An exception was raised. Could be because the specified condition, paymentmethod or category does not exist in the databse"}), 400

    for file in request.files.getlist("file"):
        prod.addPicture(file)

    return prod.serialize(), 200
