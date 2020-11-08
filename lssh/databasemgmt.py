#!/usr/bin/env python3

#######################################################################
# This file contains various utilities for adding dummy values to the
# database. This could be used for testing or development purposes.
# The functions here should not be used in a production setting since
# they only add dummy data or remove data from the database.
#######################################################################

from lssh.models import *

######################################################################
# Drops all tables from the database, ie. deletes everything.
#
# DO NOT use in a production setting or when storing important data in
# the database
#######################################################################
def resetDB():
    db.drop_all()
    db.create_all()
    print("Reset database successfully")

def fillTestDB():
    addCategories()
    addConditions()
    addPaymentMethods()
    addProducts()

    addNews()
    addFaqCategoryQuestions()
    print("Added all items to DB successfully")

#######################################################################
# Adds the categories: Chairs, Sofas, Tables and Electronics
#######################################################################
def addCategories():
    db.session.add_all([
        Category(name="Chairs"),
        Category(name="Sofas"),
        Category(name="Tables"),
        Category(name="Electronics")
    ])
    db.session.commit()

#######################################################################
# Adds the conditions: Good, Okay and Bad
#######################################################################
def addConditions():
    db.session.add_all([
        Condition(name="Good"),
        Condition(name="Okay"),
        Condition(name="Bad")
    ])
    db.session.commit()

#######################################################################
# Adds the payment methods: Swish, Revolut and Swish or Revolut
#######################################################################
def addPaymentMethods():
    db.session.add_all([
        PaymentMethod(name = "Swish"),
        PaymentMethod(name = "Revolut"),
        PaymentMethod(name = "Card")
    ])

    paym_card = PaymentMethod.query.filter_by(name = "Card").first()

    # TEMPORARY, how is this defined?
    seller = User(liuID="lssh", email="lssh@navitas.se", name="LiU Student Secondhand")

    seller.payment_method = [paym_card]
    db.session.add(seller)
    db.session.commit()

#######################################################################
# Adds a few products to the database. This function should only be
# called after calling 'addCategories()', 'addConditions()' and 
# 'addPaymentMethods()' since it assumes that the data needed exists in
# the database.
#######################################################################
def addProducts():
    cat_chairs = Category.query.filter_by(name="Chairs").first()
    cat_sofas = Category.query.filter_by(name="Sofas").first()
    cat_tables = Category.query.filter_by(name="Tables").first()
    cat_electronics = Category.query.filter_by(name="Electronics").first()

    cond_good = Condition.query.filter_by(name="Good").first()
    cond_okay = Condition.query.filter_by(name="Okay").first()
    cond_bad = Condition.query.filter_by(name="Bad").first()

    paym_s = PaymentMethod.query.filter_by(name = "Swish").first()
    paym_r = PaymentMethod.query.filter_by(name = "Revolut").first()
    paym_sr = PaymentMethod.query.filter_by(name = "Card").first()

    product0 = Product(name = "White sofa", price = 200, color = "Grey", category = cat_sofas, condition = cond_good, height = 80, width = 40, depth = 40, sellerID = "lssh")
    
    product1 = Product(name = "Lamp", price = 20, color = "Black", category = cat_electronics, condition = cond_okay, height = 80, width = 200, depth = 80, sellerID = "lssh")
    product2 = Product(name = "Chair", price = 300, color = "White", category = cat_chairs, condition = cond_bad, height = 100, width = 50, depth = 50, sellerID = "lssh")
    product3 = Product(name = "Very nice chair", price = 1000, color = "White", category = cat_chairs, condition = cond_good, height = 50, width = 40, depth = 10, sellerID = "lssh")
    product4 = Product(name = "Tv bench", price = 400, color = "Black", category = cat_tables, condition = cond_good, height = 90, width = 230, depth = 60, sellerID = "lssh")
    
    db.session.add_all([
        product0,
        product1,
        product2,
        product3,
        product4
    ])
    db.session.commit()

    product0.addPictureFromHardDive(os.path.join("mock-product-pictures", "whitesofa.jfif"))
    product1.addPictureFromHardDive(os.path.join("mock-product-pictures", "lamp.jfif"))
    product2.addPictureFromHardDive(os.path.join("mock-product-pictures", "chair.jfif"))
    product3.addPictureFromHardDive(os.path.join("mock-product-pictures", "chairwhite.jfif"))
    product4.addPictureFromHardDive(os.path.join("mock-product-pictures", "tvbench.jfif"))

#######################################################################
# Adds news to the database.
#######################################################################
def addNews():
    news1 = News(title = "New stuff in store!", ingress = "We have a lot of new things on our store, come by to check it out!", text = {"ops" : [{"insert" : "We have vases, frames and much more"}]})   
    news1.addPictureFromHardDive(os.path.join('mock-product-pictures', 'news1.jpg'))

    news2 = News(title = "Do you know where we are located?", ingress = "We are located at Linköping University in the A-building", text = {"ops" : [{"insert" : "Easiest way to find us is to go inside at entrance 19 and go down the first stairs to the left. Here is our store, welcome inside!"}]})   
    news2.addPictureFromHardDive(os.path.join('mock-product-pictures', 'news2.jpg'))

    news3 = News(title = "Need help with transport", ingress = "We offer some solutions for this, read more here!", text = {"ops" : [{"insert" : "We have a tricycle and a bike with cart that you can use free of charge during our opening hours! Amazing right?"}]})   
    news3.addPictureFromHardDive(os.path.join('mock-product-pictures', 'news3.jpg'))

    db.session.add_all([
        news1,
        news2,
        news3
    ])
    db.session.commit()

#######################################################################
# Adds faq categories and questions
#######################################################################
def addFaqCategoryQuestions():
    cat_general    = Categoryfaq(name="General")
    cat_transport  = Categoryfaq(name="Transport")
    cat_handin     = Categoryfaq(name="Hand-in")
    cat_purchasing = Categoryfaq(name="Purchasing")

    db.session.add_all([
        cat_general,
        cat_transport,
        cat_handin,
        cat_purchasing
    ])
    db.session.add_all([
        Question(questionTitle="Who can sell or buy something through LiU Student Secondhand?", questionAnswer="Only current students, or soon-to-be students, that have been accepted to Linköping University can use LiU Student Secondhand. In order to buy or sell something, you will have to show us a valid student identification (apps: Mecenat or Studentkortet) or proof of acceptance. However, non-students can still donate furniture to us.", categoryfaq=cat_general),
        Question(questionTitle="Where is the shop of LiU Student Secondhand?", questionAnswer="In the A-building on Campus Valla, Linköping, Entrance 19 (the one closest to Kårallen/Blå havet) and down the stairs. There are signs showing the way.", categoryfaq=cat_general),
        Question(questionTitle="When can I pick something up or drop something off?", questionAnswer="During our opening hours, which are listed on the website. If none of the listed times works for you, you can contact us at lssh@navitas.se and we will see what we can do.", categoryfaq=cat_general),
        Question(questionTitle="How can I become part of the project group?", questionAnswer="During spring we will recruit the new LiU Student Secondhand group. Follow us on Facebook to not miss the event that will be created when it is time!", categoryfaq=cat_general),
        Question(questionTitle="Do you offer transportation?", questionAnswer="Yes, we have a cargo tricycle and a bike with a bike cart attached to it, which we lend out for free. Both come with a lock.", categoryfaq=cat_transport),
        Question(questionTitle="How do I book transportation?", questionAnswer="The bike cart and the cargo tricycle cannot be booked/reserved, so “first come, first served” applies. If we have it in our shop when you need it, you are welcome to borrow it.", categoryfaq=cat_transport),
        Question(questionTitle="How much does transportation cost?", questionAnswer="You can borrow the cargo tricycle and bike cart for free. We only take a deposit (valid ID-card, driver’s licence or passport) to make sure that it is returned in a good condition within a maximum of 2 hours and before the opening hour has ended.", categoryfaq=cat_transport),
        Question(questionTitle="What can I sell through LiU Student Secondhand?", questionAnswer="We focus on furniture and other things for your home. For now, we do not accept for example textiles, books, mattresses or bikes.", categoryfaq=cat_handin),
        Question(questionTitle="Can I take back furniture that I have put up for sale?", questionAnswer="If you wish to take back an item that you have handed in, write us an email. If the item has not yet been sold, we will remove it from the website and you have to come pick it up within one week.", categoryfaq=cat_handin),
        Question(questionTitle="How do I pay for something I want to buy?", questionAnswer="To buy something you need to come to our shop during our opening hours and pay with card, or in some cases Swish or Revolut. If Swish or Revolut is needed, it does not have to be your account, but you have to show us the confirmed transaction in person. ", categoryfaq=cat_purchasing),
        Question(questionTitle="What do I do if I don’t have Swish or Revolut and want to buy an item where this is needed?", questionAnswer="Maybe you have a friend who can make the Swish or Revolut transfer for you, or whose number you can use? As said before, many of our items can be paid for by card.", categoryfaq=cat_purchasing),
        Question(questionTitle="When can I pick something up?", questionAnswer="During our opening hours, which are listed on the website. If none of the listed times works for you, you can contact us at lssh@navitas.se and we will see what we can do.", categoryfaq=cat_purchasing),
    ])

    db.session.commit()
