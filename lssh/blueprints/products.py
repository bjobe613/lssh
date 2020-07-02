from flask import Blueprint

bp = Blueprint('products', __name__, url_prefix = '/products')

# Routes should be added here
# Like this:
"""
 @bp.route("/test")
 def test_route():
     return "hej världen"
"""