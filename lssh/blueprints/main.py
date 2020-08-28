from flask import Blueprint, render_template, request, jsonify, Response
from lssh.models import db, Newsletter, Product

import smtplib, ssl, re

main = Blueprint('main', __name__, url_prefix = '/')
'''this is the regular expression used to khnow if what is sent is an email:'''
emailregex = '^[a-z0-9]+[/._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

@main.route("/")
def startup():

    prodCount = Product.query.filter(Product.articleNumber).count()
    print(prodCount)

    return render_template('index.html', productCount = prodCount)
    
#@main.route("/home")
#def home():
#    return render_template('index.html')

@main.route("/subscribe", methods = ['POST'])
def subscribe():

    if request.method == 'POST':

      
        email = request.get_json()
     
        if (re.search(emailregex, email)):
            exist = Newsletter.query.filter(Newsletter.email == email).first()
            if not exist:
                sub = Newsletter(email = email)
                db.session.add(sub)
                db.session.commit()
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

@main.route("/help/faq")
def faq():
    return render_template('faq.html')

@main.route("/transport")
def transport():
    return render_template('transport.html')

@main.route("/hand_in")
def hand_in():
    return render_template('hand_in.html')

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

@main.route("/admin_login")
def admin_login():
    return render_template('admin_login.html')


# Not working with gmail?

def mail(email, name, message, subject):

  port = 587  # For starttls
  smtp_server = "smtp.gmail.com"
  sender_email = "testsson828@gmail.com"
  receiver_email = email
  password = "qkjgnpbpnohjtoxp"
  mess =str("Subject:"+name + ", "+ email +", " +subject +
  "\n \n"  +
  message)
  print(mess)
  context = ssl.create_default_context()
  with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo()  # Can be omitted
      server.starttls(context=context)
      server.ehlo()  # Can be omitted
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, mess.encode("utf8"))
