from flask import Flask
from flask_mail import Mail


app = Flask(__name__, static_folder = 'static', static_url_path = '/')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://lssh:7wN9e@SQwdxgdtn@lssh.mysql.pythonanywhere-services.com/lssh$webshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'FHSGAJH48242T58GRTJ853FBIQVJ4B5IQU5H9G58G'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lithemobler@gmail.com'
app.config['MAIL_PASSWORD'] = 'LITHEmobler2020'
mail = Mail(app)

# Imports blueprints from blueprint package
from lssh.blueprints import products, users, main, news, admin, faq


# Regisers the blueprints, adding all defined routes
app.register_blueprint(products.products)
app.register_blueprint(users.users)
app.register_blueprint(main.main)
app.register_blueprint(news.news)
app.register_blueprint(faq.faq)

app.register_blueprint(admin.admin)
