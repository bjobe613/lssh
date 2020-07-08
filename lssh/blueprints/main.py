from flask import Blueprint, render_template
from lssh.models import db

main = Blueprint('main', __name__, url_prefix = '/')

@main.route("/")
def startup():
    return render_template('index.html')

#@main.route("/home")
#def home():
#    return render_template('index.html')

@main.route("/about/about_us")
def about_us():
    return render_template('about_us.html')

@main.route("/about/find_us")
def find_us():
    return render_template('find_us.html')

@main.route("/help/contact")
def contact():
    return render_template('contact.html')

@main.route("/help/faq")
def faq():
    return render_template('faq.html')

@main.route("/transport")
def transport():
    return render_template('transport.html')