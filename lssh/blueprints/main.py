from flask import Blueprint, render_template
from lssh.models import db, Newsletter

main = Blueprint('main', __name__, url_prefix = '/')

@main.route("/", methods = ['GET', 'POST'])
def startup():
    '''form = SubscribeToMailForm() 
    if form.validate_on_submit():
        exist = Newsletter.query.filter(Newsletter.email == form.email.data).first()
        if not exist:
            sub = Newsletter(email = form.email.data)
            db.session.add(sub)
            db.session.commit()'''

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