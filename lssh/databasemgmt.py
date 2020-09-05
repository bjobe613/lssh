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
        PaymentMethod(name = "Swish or Revolut")
    ])
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
    paym_sr = PaymentMethod.query.filter_by(name = "Swish or Revolut").first()

    product0 = Product(name = "White sofa", price = 200, color = "Grey", category = cat_sofas, condition = cond_good, payment_method = paym_sr, height = 80, width = 40, depth = 40)
    
    product1 = Product(name = "Lamp", price = 20, color = "Black", category = cat_electronics, condition = cond_okay, payment_method = paym_s, height = 80, width = 200, depth = 80)
    product2 = Product(name = "Chair", price = 300, color = "White", category = cat_chairs, condition = cond_bad, payment_method = paym_r, height = 100, width = 50, depth = 50)
    product3 = Product(name = "Very nice chair", price = 1000, color = "White", category = cat_chairs, condition = cond_good, payment_method = paym_sr, height = 50, width = 40, depth = 10)
    product4 = Product(name = "Tv bench", price = 400, color = "Black", category = cat_tables, condition = cond_good, payment_method = paym_sr, height = 90, width = 230, depth = 60)
    
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