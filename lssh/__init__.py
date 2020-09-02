from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__, static_folder = 'static', static_url_path = '/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'FHSGAJH48242T58GRTJ853FBIQVJ4B5IQU5H9G58G'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
#app.config['JWT_ACCESS_COOKIE_PATH'] ='/user/'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True 
app.config['JWT_SECRET_KEY'] = 'FHSGAJH48242T58GRTJ853FBIQVJ4B5IQU5H9G58G' 

flask_bcrypt = Bcrypt(app)
flask_jwt = JWTManager(app)

# Imports blueprints from blueprint package
from lssh.blueprints import products, users, main, news

# Regisers the blueprints, adding all defined routes
app.register_blueprint(products.products)
app.register_blueprint(users.users)
app.register_blueprint(main.main)
app.register_blueprint(news.news)