from flask import Flask


app = Flask(__name__, static_folder = 'static', static_url_path = '/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'FHSGAJH48242T58GRTJ853FBIQVJ4B5IQU5H9G58G'

# Imports blueprints from blueprint package
from lssh.blueprints import products, users, main, news, admin


# Regisers the blueprints, adding all defined routes
app.register_blueprint(products.products)
app.register_blueprint(users.users)
app.register_blueprint(main.main)
app.register_blueprint(news.news)
app.register_blueprint(admin.admin)