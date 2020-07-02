from flask import Flask


app = Flask(__name__, static_folder = 'static', static_url_path = '/')

from lssh.blueprints import products, users

app.register_blueprint(products.bp)
app.register_blueprint(users.bp)

@app.route("/")
def client():
    return "Hej"