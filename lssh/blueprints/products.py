from flask import Blueprint

# The database is accessed in this manner from blueprints
from server.models import db #, other objects defined in models
bp = Blueprint('products', __name__, url_prefix = '/products')

# Routes should be added here
# Like this:
"""
 @bp.route("/test")
 def test_route():
     return "hej världen"
"""