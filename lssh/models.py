from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
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

class Furniture(db.Model):
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
    pictures = db.relationship('FurniturePictures', backref = 'furniturePicture')
    reservations = db.relationship('FurnitureReservation', backref = 'furnitureReservation')
    seller = db.Column(db.Integer, db.ForeignKey('seller.sellerID'))

class FurniturePictures(db.Model): 
    pictureID = db.Column(db.Integer, primary_key = True)
    path = db.Column(db.String, nullable = False)
    furnitureID = db.Column(db.Integer, db.ForeignKey('furniture.articleNumber')) 

class FurnitureReservation(db.Model):
    reservationID = db.Column(db.Integer, primary_key = True)
    liuID = db.Column(db.String(8), nullable = False)
    date = db.Column(db.DateTime(timezone = True), server_default = func.now())
    furnitureID = db.Column(db.Integer, db.ForeignKey('furniture.articleNumber')) 

class Seller(db.Model): # will be ralated to furniture
    sellerID = db.Column(db.Integer, primary_key = True)
    liuID = db.Column(db.String(8), nullable = False)
    phone = db.Column(db.String, nullable = True)
    #other info for payment???
    #maybe should have the payment method here? and use LSSh as seller if there is no one else?
    furnitures = db.relationship('Furniture', backref = 'sellerOfFurniture')

class Blacklist(db.Model):
    liuID = db.Column(db.String(8), primary_key = True)
    numOfOffences = db.Column(db.Integer, default = 0)

class Newsletter(db.Model):
    liuID = db.Column(db.String(8), primary_key = True)

class News(db.Model):
    date = db.Column(db.DateTime(timezone = True), server_default = func.now(), primary_key = True)
    title = db.Column(db.String, nullable = False)
    text = db.Column(db.Text, nullable = False)
    pictures = db.relationship('NewsPictures', backref = 'news')

class NewsPictures(db.Model): 
    pictureID = db.Column(db.Integer, primary_key = True)
    path = db.Column(db.String, nullable = False)
    newsID = db.Column(db.DateTime, db.ForeignKey('news.date')) 

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
    price = db.Column(db.Integer, nullable = True) #should we make this a relation?
    category = db.Column(db.String, nullable = True)#should this be here??

'''class HIRequestPictures(db.Model): 
    pictureID = db.Column(db.Integer, primary_key = True)
    path = db.Column(db.String, nullable = False)
    requestID = db.Column(db.Integer, db.ForeignKey('handinrequest.requestID')) 
'''


def resetDB():
    db.drop_all()
    db.create_all()
    print("Reset database successfully")

def createDB():

    furn1 = Furniture(name = 'Stol', price = 500, condition = 3, paymentMethod = "Swish")
    furn2 = Furniture(name = 'Bord', price = 800, category = 2, condition = 1, height = 150, width = 60, depth = 40, paymentMethod = "Cash")

    furn1pic = FurniturePictures()

    db.session.add_all([furn1, furn2])
    db.session.commit()


