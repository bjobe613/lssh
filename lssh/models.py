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

    #This serialize is urrently fitted for filter
    def serialize(self):
        return dict(articleNumber=self.articleNumber, name=self.name, price=self.price, pubDate=self.pubDate,
        category=self.category, subcategory=self.subcategory, color=self.color, condition=self.condition,
        status=self.status, paymentMethod=self.paymentMethod)

    def addPicture(self, picture):
        pic = ProductPictures(productID = self.articleNumber)
        db.session.add(pic)
        db.session.commit()

        safeName = secure_filename(picture.filename)
        fileEnding = safeName.rsplit('.')[len(safeName.rsplit('.')) - 1]
        fileName = 'product-' + str(self.articleNumber) + '-' + str(pic.pictureID) + '.' + fileEnding
        picture.save(os.path.join(os.path.curdir, 'lssh', 'static', 'pictures', fileName))
        pic.renameReference(fileName)

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

    news1 = News(title = "En nyhet", ingress = "En liten ingress som beskriver innehållet i artikeln väl", text = {"ops" : [{"insert" : "Detta är <div> brödtexten"}]})   

    seller1 = Seller(liuID = 'LSSH')
    seller1.products.append(prod1)
    seller1.products.append(prod2)
    seller2 = Seller(liuID = 'qwert123')
    seller2.products.append(prod3)

    bl1 = Blacklist(liuID = 'uiojk890')

    nl1 = Newsletter(email = 'tyuvb456@student.liu.se')

    cat0 = Categoryfaq(name = "Generellt")
    cat1 = Categoryfaq(name = "Sälja")
    cat2 = Categoryfaq(name = "Köpa")
    cat3 = Categoryfaq(name = "Leverans")
    qCat = [cat0, cat1, cat2, cat3]

    q0 = Question(questionTitle = "TestGenerellt0", questionAnswer = "Ett svar", categoryfaq=cat0)
    q1 = Question(questionTitle = "TestGenerellt1", questionAnswer = "Ett svar", categoryfaq=cat0)
    q2 = Question(questionTitle = "TestGenerellt2", questionAnswer = "Ett svar", categoryfaq=cat0)
    q3 = Question(questionTitle = "TestGenerellt3", questionAnswer = "Ett svar", categoryfaq=cat0)
 
    q4 = Question(questionTitle = "TestSälja0", questionAnswer = "Ett svar", categoryfaq=cat1)
    q5 = Question(questionTitle = "TestSälja1", questionAnswer = "Ett svar", categoryfaq=cat1)
    q6 = Question(questionTitle = "TestSälja2", questionAnswer = "Ett svar", categoryfaq=cat1)
  
    q7 = Question(questionTitle = "TestKöpa0", questionAnswer = "Ett svar", categoryfaq=cat2)
    q8 = Question(questionTitle = "TestKöpa1", questionAnswer = "Ett svar", categoryfaq=cat2)
    q9 = Question(questionTitle = "TestKöpa2", questionAnswer = "Ett svar", categoryfaq=cat2)
   
    q10 = Question(questionTitle = "TestLeverans0", questionAnswer = "Ett svar", categoryfaq=cat3)
    q11 = Question(questionTitle = "TestLeverans1", questionAnswer = "Ett svar", categoryfaq=cat3)
    questions = [q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]


<<<<<<< HEAD
    
    db.session.add_all([prod1, prod2, prod3, prod1pic1, prod1pic2, prod2pic1, prod1res1, prod2res1,
                        prod3res1, prod3res2, seller1, seller2, bl1, nl1, news1])
=======
    db.session.add_all([prod1, prod2, prod3, prod1pic1, prod1pic2, prod2pic1, prod1res1, prod2res1,
                        prod3res1, prod3res2, seller1, seller2, bl1, nl1, news1])
    db.session.add_all(qCat)
    db.session.add_all(questions)
>>>>>>> origin
    db.session.commit()

    print("Filled the database")


resetDB()
fillTestDB()



'''
def test():
    pic = FurniturePictures.query.filter_by(pictureID = 1).first()
    pic.pictureName = str(pic.pictureID) + ".jpg"
    db.session.commit()
'''
