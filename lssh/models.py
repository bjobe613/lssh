from datetime import datetime
from flask_sqlalchemy import SQLAlchemy, DateTime, func, Time
from lssh import app

db = SQLAlchemy(app)

# Models can be defines here, like this:
"""
class Car(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Car {}: {} {}>".format(self.id, self.make, self.model)
"""

class Furniture(db.Model): #relations not made
    articleNumber = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    pubDate = db.Column(db.DateTime(timezone = True),server_default = func.now()) #havn't tested this yet, nor have I tested the imports
    category = db.Column(db.Integer, nullable = False, default = 0)
    subcategory = db.Column(db.Integer, nullable = True, default = 0)
    condition = db.Column(db.Integer, nullable = False)
    height = db.Column(db.Integer, nullable = True)
    width = db.Column( db.Integer, nullable = True)
    depth = db.Column(db.Integer, nullable = True)
    archived = db.Column(db.Boolean, default = False)
    paymentMethod = db.Column(db.String, nullable = False)

class Pictures(db.Model): #for all pictures on the site, need to be decided in a meeting. 
    pictureID = db.Column(db.Integer, primary_key = True)
    path = db.Column(db.String, nullable = False)

class FurnitureReservation(db.Model):
    reservationID = db.Column(db.Integer, primary_key = True)
    liuID = db.Column(db.String(8), nullable = False)
    date = db.Column(db.DateTime(timezone = True), server_default = func.now())

class Seller(db.Model): # will be ralated to furniture
    liuID = db.Column(db.String(8), primary_key = True)
    phone = db.Column(db.String, nullable = True)
    #other info for payment???

class Blacklist(db.Model):
    liuID = db.Column(db.String(8), primary_key = True)
    numOfOffences = db.Column(db.Integer, default = 0)

class Newsletter(db.Model):
    liuID = db.Column(db.String(8), primary_key = True)

class News(db.Model):
    date = db.Column(db.DateTime(timezone = True), server_default = func.now(), primary_key = True)
    title = db.Column(db.String, nullable = False)
    text = db.Column(db.Text, nullable = False)

class Admin(db.Model):
    name = db.Column(db.String, primary_key = True)
    passwordHash = db.Column(db.String, nullable = False)
    authorization = db.Column(db.Integer, default = 1)

class OpeningHours(db.Model):
    day = db.Column(db.String, primary_key = True)
    openingTime = db.Column(db.Time, nullable = False)
    closingTime = db.Column(db.Time, nullable = False)

class FAQ(db.Model):
    faqID = db.Column(db.Integer, primary_key = True)
    show = db.Column(db.Boolean, default = False) #or should it be true??
    headline = db.Column(db.String, nullable = False)
    question = db.Column(db.Text, nullable = False)
    answer = db.Column(db.Text, nullable = False)

class HandInRequest(db.Model):
    requestID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    liuID = db.Column(db.String(8), nullable = False)
    generalInfo = db.Column(db.Text, nullable = True)
    condition = db.Column(db.Integer, nullable = False)
    picturePath = db.Column(db.String, nullable = True)
    donate = db.Column(db.Boolean, default = False)
    price = db.Column(db.Integer, nullable = True)
    category = db.Column(db.String, nullable = True)#should this be here??

     
