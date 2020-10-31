from flask import Blueprint, render_template, request, jsonify, Response
from lssh.models import db, Product, Newsletter, News, Question, Categoryfaq
from flask_mail import Message
from lssh import mail
from lssh.blueprints.security import *

import re

main = Blueprint('main', __name__, url_prefix = '/')
'''this is the regular expression used to khnow if what is sent is an email:'''
emailregex = '^\w+[./_]?\w+@\w+[.](\w+[.])?\w{2,3}$'

@main.route("/")
def startup():
    '''form = SubscribeToMailForm() 
    if form.validate_on_submit():
        exist = Newsletter.query.filter(Newsletter.email == form.email.data).first()
        if not exist:
            sub = Newsletter(email = form.email.data)
            db.session.add(sub)
            db.session.commit()'''

    return render_template('index.html')

    prodCount = Product.query.filter(Product.articleNumber).count()
    news = News.query.all()
    products_sorted = Product.query.order_by(Product.articleNumber).limit(6)

    return render_template('index.html', productCount = prodCount, newsarticles = news, productlist = products_sorted)
    
#@main.route("/home")
#def home():
#    return render_template('index.html')

@main.route("/subscribe", methods = ['POST'])
def subscribe():

    if request.method == 'POST':

        email = request.get_json()
        
        if (re.match(emailregex, email)):
            exist = Newsletter.query.filter(Newsletter.email == email).first()
            if not exist:
                sub = Newsletter(email = email)
                db.session.add(sub)
                db.session.commit()

                msg = Message("LiU Student Second Newsletter", sender="lithemobler@gmail.com", recipients=[email])
                msg.body = "Welcome to our subscription list!"
                mail.send(msg)

                return Response(status= 201)

        return Response(status=406)

    


@main.route("/about/about_us")
def about_us():
    return render_template('about_us.html')

@main.route("/help/find_us")
def find_us():
    return render_template('find_us.html')

@main.route("/help/contact")
def contact():
    return render_template('contact.html')

@main.route("/contactform", methods = ['POST'])
def contactform():

    data = request.get_json()

    name = data["name"]
    email = data["email"]
    message = data["message"]
    

  
    msg = Message("Contact form - New message", sender="lithemobler@gmail.com", recipients=["lithemobler@gmail.com"])
    msg.body = "You have a new form reply from " + email + " : " + message
    mail.send(msg)

    print("hej")
    return ""

@main.route("/help/faq/<int:x>", methods = ['GET'])
def faq(x):
    x_minus_1 = x - 1
    categories = Categoryfaq.query.filter(Categoryfaq.id).all()
    questions = Question.query.filter(Question.categoryID == categories[x_minus_1].id).all()
 
    return render_template('faq.html', faqquestions = questions, faqcategories = categories)

@main.route("/transport")
def transport():
    return render_template('transport.html')

@main.route("/hand_in")
def hand_in():
    return render_template('hand_in.html')


@main.route("/news")
def news():
    news = News.query.all()
    return render_template('news.html', newsarticles = news)

@main.route("/news/<int:x>", methods=['GET'])
def news_single(x):

    news_article = News.query.filter(News.id == x).first()


    return render_template('news_single_view.html', single_article = news_article, article=news_article.get_article_as_html_user())


@main.route("/hand_in/hand_in_request", methods = ['GET', 'POST'])
def hand_in_request():

    if request.method == 'POST':

        req_data = request.get_json()
        email = req_data["email"]

        if (re.search(emailregex, email)):
            print("du postade")
            return Response(status= 201)

        return Response(status=406)

    elif request.method == 'GET':
        return render_template('hand_in_request.html')

@main.route("/admin_login", methods = ['GET', 'POST'])
def admin_login():
    
    if request.method == 'POST':
        content = request.get_json()        
        username = content["username"] # MUST prevent an sql-injection!!!
        password = content['password']
        user = Admin.query.filter(Admin.name == username).first()
        if not user:
            return 'No user', 404
        else:
            if flask_bcrypt.check_password_hash(user.passwordHash, password):     
                access_token = create_access_token(identity=user)
                resp = make_response('cookie')
                set_access_cookies(resp, access_token)
                return resp
            else:
                return 'wrong password', 404
    elif request.method == 'GET':
        if get_jwt_identity() != None:
            print('redirect to register') #return redirect(url_for('users.adminRegister'))   # this doesn't work     
        return render_template('admin_login.html')

@main.route("/admin_logout", methods = ['GET'])
@jwt_required
def admin_logout():
    resp = jsonify({'logout': True})
    resp = make_response(redirect(url_for('main.admin_login')))
    unset_jwt_cookies(resp)
    return resp, 200 

