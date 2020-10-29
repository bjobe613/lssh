from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from lssh import app
from werkzeug.utils import secure_filename


from delta import html as quill_parser


import os
import html

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

#######################################################################
# The following three classes are helper classes to store data for 
# Product. These are here to prevent deletion and update anomalies and
# to simplify displaying of for example all categories, all conditions
# and all available payment methods
#######################################################################
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    products = db.relationship('Product', back_populates='category')

class Condition(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    products = db.relationship('Product', back_populates='condition')

class PaymentMethod(db.Model):
    __tablename__ = 'paymentmethod'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    products = db.relationship('Product', back_populates='payment_method')

class Product(db.Model):
    articleNumber = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    pubDate = db.Column(db.DateTime,server_default = func.now())
    color = db.Column(db.String, default = "None")

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)
    category = db.relationship('Category', back_populates='products')

    condition_id = db.Column(db.Integer, db.ForeignKey('condition.id'), nullable=False)
    condition = db.relationship('Condition', back_populates='products')

    payment_method_id = db.Column(db.Integer, db.ForeignKey('paymentmethod.id'), nullable=False)
    payment_method = db.relationship('PaymentMethod', back_populates='products')

    height = db.Column(db.Integer, nullable = True)
    width = db.Column( db.Integer, nullable = True)
    depth = db.Column(db.Integer, nullable = True)
    status = db.Column(db.String, default = "Available")
    quantity = db.Column(db.Integer, default = 1)
    comment = db.Column(db.Text)
    pictures = db.relationship('ProductPictures', backref = 'productIDPicture')
    reservations = db.relationship('ProductReservation', backref = 'productIDReservation')
    seller = db.Column(db.Integer, db.ForeignKey('seller.buyerID'))
    buyer = db.Column(db.Integer, db.ForeignKey('buyer.liuID'))

    def getSinglePictureName(self):
        piclist = self.pictures
        if not piclist:
            pic = "default.jpg"
        else :
            pic = piclist[0].pictureName
        return pic

    #This serialize is urrently fitted for filter
    def serialize(self):
        return dict(
            articleNumber=self.articleNumber, 
            name=self.name, 
            price=self.price, 
            pubDate=self.pubDate,
            category=self.category.name,
            color=self.color,
            condition=self.condition.name,
            status=self.status,
            paymentMethod=self.payment_method.name
        )

    def addPicture(self, picture):
        pic = ProductPictures(productID = self.articleNumber)
        db.session.add(pic)
        db.session.commit()

        safeName = secure_filename(picture.filename)
        fileEnding = safeName.rsplit('.')[len(safeName.rsplit('.')) - 1]
        fileName = 'product-' + str(self.articleNumber) + '-' + str(pic.pictureID) + '.' + fileEnding
        picture.save(os.path.join(os.path.curdir, 'lssh', 'static', 'pictures', fileName))
        pic.renameReference(fileName)
    
    def addPictureFromHardDive(self, path):
        pic = ProductPictures(productID = self.articleNumber)

        fileEnding = path.rsplit('.')[len(path.rsplit('.')) - 1]
        fileName = 'product-' + str(self.articleNumber) + '-' + str(pic.pictureID) + '.' + fileEnding
        with open(path, 'rb') as f:
            data = f.read()
            with open(os.path.join('static', 'pictures', fileName), 'wb') as wf:
                wf.write(data)

        pic.renameReference(fileName)
        db.session.add(pic)
        db.session.commit()

class ProductPictures(db.Model):
    pictureID = db.Column(db.Integer, primary_key = True)
    pictureName = db.Column(db.String, default = "default.jpg")
    productID = db.Column(db.Integer, db.ForeignKey('product.articleNumber'))

    def renameReference(self, fileName):
        self.pictureName = fileName
        db.session.commit()

class ProductReservation(db.Model):
    reservationID = db.Column(db.Integer, primary_key = True)
    liuID = db.Column(db.String(8), nullable = False)
    date = db.Column(db.DateTime(timezone = True), server_default = func.now())
    productID = db.Column(db.Integer, db.ForeignKey('product.articleNumber'))

class Seller(db.Model): # will be ralated to furniture
    buyerID = db.Column(db.Integer, db.ForeignKey('buyer.liuID'), primary_key = True)
    phone = db.Column(db.String(15), nullable = True)
    #other info for payment???
    #maybe should have the payment method here? and use LSSh as seller if there is no one else?
    products = db.relationship('Product', backref = 'sellerOfProduct')

class Buyer(db.Model):
    liuID = db.Column(db.String(8), nullable = False, unique = True, primary_key = True, autoincrement=False)
    email = db.Column(db.String, nullable = False, unique = True)
    name = db.Column(db.String)
    program = db.Column(db.String)
    international = db.Column(db.Boolean)
    products = db.relationship('Product', backref = 'buyerOfProduct')

    seller = db.relationship('Seller', backref = 'sellerInheritance')

    


class Blacklist(db.Model):
    #listID = db.Column(db.Integer, primary_key = True)
    liuID = db.Column(db.String(8), primary_key = True)
    numOfOffences = db.Column(db.Integer, default = 1)

class Newsletter(db.Model):
    email = db.Column(db.String, primary_key = True)

class Newspicture(db.Model):
    pictureID = db.Column(db.Integer, primary_key = True)
    path = db.Column(db.String, nullable = False, default = "default.jpg")
    articles = db.relationship('News', backref = 'News.id')


    def savePicture(self, picture):
        safeName = secure_filename(picture.filename)
        fileEnding = safeName.rsplit('.')[len(safeName.rsplit('.')) - 1]
        fileName = 'news-' + str(self.pictureID) + '.' + fileEnding
        picture.save(os.path.join(os.path.curdir, 'lssh', 'static', 'pictures', fileName))
        self.path = fileName
        db.session.commit()
    
    def savePictureFromHardDrive(self, path):
        fileEnding = path.rsplit('.')[len(path.rsplit('.')) - 1]
        fileName = 'news-' + str(self.pictureID) + '.' + fileEnding
        with open(path, 'rb') as f:
            data = f.read()
            with open(os.path.join('static', 'pictures', fileName), 'wb') as wf:
                wf.write(data)
        self.path = fileName
        db.session.commit()

class News(db.Model): #has to be reworked into files, not a model.
    id = db.Column(db.Integer, primary_key = True)
    published = db.Column(db.Boolean, nullable=False, default = False)
    date = db.Column(db.DateTime(timezone = True), server_default = func.now())
    title = db.Column(db.String, nullable = False)
    ingress = db.Column(db.String, nullable = False)
    text = db.Column(db.JSON, nullable = False)
    titlePicture = db.Column(db.Integer, db.ForeignKey('newspicture.pictureID'))

    def get_img_url(self):

        url = ""

        if self.titlePicture:
            print("Hade bild")
            url= Newspicture.query.get(self.titlePicture).path
        else:
            print("Hade inte bild")
     
        return url

    def escape_html(self):
        self.title = html.escape(self.title)
        self.ingress = html.escape(self.ingress)

        for obj in self.text["ops"]:
            if type(obj["insert"]) is str:
                obj["insert"] = html.escape(obj["insert"])

        db.session.commit()

    def add_picture(self, picture):
        titlePicture = Newspicture()
        db.session.add(titlePicture)
        db.session.commit()
        
        self.titlePicture = titlePicture.pictureID
        titlePicture.savePicture(picture)

    def addPictureFromHardDive(self, path):
        titlePicture = Newspicture()
        db.session.add(titlePicture)
        db.session.commit()
        
        self.titlePicture = titlePicture.pictureID
        titlePicture.savePictureFromHardDrive(path)

    def get_article_as_html(self):
        article_html = ""
        if self.titlePicture:
            print("Hade bild")
            article_html = "<img class='img-fluid' src='/pictures/" + Newspicture.query.get(self.titlePicture).path + "'>"
        else:
            print("Hade inte bild")
        article_html += "<h1>" + self.title + "</h1>\n"
        article_html += "<p class='ingress'>" + self.ingress + "</p>\n"
        article_html += quill_parser.render(self.text["ops"])

        print(article_html)
        return article_html

    def get_article_as_html_user(self):
        article_html = ""
        article_html += quill_parser.render(self.text["ops"])
        return article_html

    def serialize(self):
        returnDict =  {
            "id": self.id,
            "published": self.published,
            "title": self.title,
            "ingress": self.ingress,
            "text": self.text
        }
        if self.titlePicture:
            returnDict.update({"imgpath": Newspicture.query.get(self.titlePicture).path})

        return returnDict
        


class Admin(db.Model):
    name = db.Column(db.String, primary_key = True)
    passwordHash = db.Column(db.String, nullable = False)
    authorization = db.Column(db.Integer, default = 1)

class OpeningHours(db.Model):
    day = db.Column(db.String, primary_key = True)
    openingTime = db.Column(db.Time, nullable = False)
    closingTime = db.Column(db.Time, nullable = False)

class Categoryfaq(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    questions = db.relationship("Question", back_populates="categoryfaq")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    questionTitle = db.Column(db.Text, nullable = False)
    questionAnswer = db.Column(db.Text, nullable = False)
    categoryID = db.Column(db.Integer, db.ForeignKey('categoryfaq.id'))
    categoryfaq = db.relationship("Categoryfaq", backref="question")

    def serialize(self):
        return {
            "id" : self.id,
            "questionTitle" : self.questionTitle,
            "questionAnswer" : self.questionAnswer,
            "categoryID" : self.categoryID,
        }


#class FAQQuestion(db.Model):
#    faqID = db.Column(db.Integer, primary_key = True)
#    show = db.Column(db.Boolean, default = False) #or should it be true??
#    headline = db.Column(db.String, nullable = False)
#    question = db.Column(db.Text, nullable = False)
#    answer = db.Column(db.Text, nullable = False)

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
