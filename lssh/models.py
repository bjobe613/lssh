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

class Product(db.Model):
    articleNumber = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    pubDate = db.Column(db.DateTime,server_default = func.now())
    category = db.Column(db.Integer, nullable = False, default = 0)
    subcategory = db.Column(db.Integer, nullable = True, default = 0)
    color = db.Column(db.String, default = "None")
    condition = db.Column(db.Integer, nullable = False)
    height = db.Column(db.Integer, nullable = True)
    width = db.Column( db.Integer, nullable = True)
    depth = db.Column(db.Integer, nullable = True)
    status = db.Column(db.String, default = "Available")
    comment = db.Column(db.Text)
    paymentMethod = db.Column(db.String, nullable = False)
    pictures = db.relationship('ProductPictures', backref = 'productIDPicture')
    reservations = db.relationship('ProductReservation', backref = 'productIDReservation')
    seller = db.Column(db.Integer, db.ForeignKey('seller.sellerID'))

    def getSinglePictureName(self):
        piclist = self.pictures
        if not piclist:
            pic = "default.jpg"
        else :
            pic = piclist[0].pictureName
        return pic

class ProductPictures(db.Model): 
    pictureID = db.Column(db.Integer, primary_key = True)
    pictureName = db.Column(db.String, default = "default.jpg")
    productID = db.Column(db.Integer, db.ForeignKey('product.articleNumber')) 

    def renamePictureAsID(self):
        self.pictureName = str(self.pictureID) + '.jpg'
        db.session.commit()

class ProductReservation(db.Model):
    reservationID = db.Column(db.Integer, primary_key = True)
    liuID = db.Column(db.String(8), nullable = False)
    date = db.Column(db.DateTime(timezone = True), server_default = func.now())
    productID = db.Column(db.Integer, db.ForeignKey('product.articleNumber')) 

class Seller(db.Model): # will be ralated to furniture
    sellerID = db.Column(db.Integer, primary_key = True)
    liuID = db.Column(db.String(8), nullable = False, unique = True)
    phone = db.Column(db.String(15), nullable = True)
    #other info for payment???
    #maybe should have the payment method here? and use LSSh as seller if there is no one else?
    products = db.relationship('Product', backref = 'sellerOfProduct') 

class Blacklist(db.Model):
    #listID = db.Column(db.Integer, primary_key = True)
    liuID = db.Column(db.String(8), primary_key = True)
    numOfOffences = db.Column(db.Integer, default = 1)

class Newsletter(db.Model):
    email = db.Column(db.String, primary_key = True)

class News(db.Model): #has to be reworked into files, not a model. 
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

def fillTestDB():

    prod1 = Product(name = 'Stol', price = 500, condition = 3, paymentMethod = "Swish")
    prod2 = Product(name = 'Bord', price = 800, category = 2, condition = 1, height = 150, width = 60, depth = 40, paymentMethod = "Cash")
    prod3 = Product(name = 'Soffa', price = 1200, category = 3, condition = 3, height = 70, width = 200, depth = 60, paymentMethod = "Swish eller Revolut")

    prod1pic1 = ProductPictures(productIDPicture = prod1)
    prod1pic2 = ProductPictures(productIDPicture = prod1)
    prod2pic1 = ProductPictures(productIDPicture = prod2)

    prod1res1 = ProductReservation(liuID = "asdfg123", productIDReservation = prod1)
    prod2res1 = ProductReservation(liuID = 'asdfg123', productIDReservation = prod2)
    prod3res1 = ProductReservation(liuID = 'jkler678', productIDReservation = prod3)
    prod3res2 = ProductReservation(liuID = 'qwert456', productIDReservation = prod3)
    
    seller1 = Seller(liuID = 'LSSH')
    seller1.products.append(prod1)
    seller1.products.append(prod2)
    seller2 = Seller(liuID = 'qwert123')
    seller2.products.append(prod3)

    bl1 = Blacklist(liuID = 'uiojk890')

    nl1 = Newsletter(email = 'tyuvb456@student.liu.se')


    db.session.add_all([prod1, prod2, prod3, prod1pic1, prod1pic2, prod2pic1, prod1res1, prod2res1,
                        prod3res1, prod3res2, seller1, seller2, bl1, nl1])
    db.session.commit()

    prod1pic2.renamePictureAsID()

    print("Filled the database")

'''
def test():
    pic = FurniturePictures.query.filter_by(pictureID = 1).first()
    pic.pictureName = str(pic.pictureID) + ".jpg"
    db.session.commit()
'''

