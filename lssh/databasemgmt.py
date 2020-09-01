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

    product0 = Product(name = "Gray small chair", price = 100, color = "Grey", category = cat_chairs, condition = cond_good, payment_method = paym_sr, height = 80, width = 40, depth = 40)
    
    product1 = Product(name = "Leather sofa", price = 200, color = "Brown", category = cat_sofas, condition = cond_okay, payment_method = paym_s, height = 80, width = 200, depth = 80)
    product2 = Product(name = "Small kitchen table", price = 300, color = "Brown", category = cat_tables, condition = cond_bad, payment_method = paym_r, height = 100, width = 50, depth = 50)
    product3 = Product(name = "Panasonic TV", price = 1000, color = "Black", category = cat_electronics, condition = cond_good, payment_method = paym_sr, height = 50, width = 40, depth = 10)
    product4 = Product(name = "Large desk", price = 400, color = "Brown", category = cat_tables, condition = cond_good, payment_method = paym_sr, height = 90, width = 230, depth = 60)
    
    db.session.add_all([
        product0,
        product1,
        product2,
        product3,
        product4
    ])
    db.session.commit()

    product0.addPictureFromHardDive(os.path.join("mock-product-pictures", "chair.jpg"))
    product1.addPictureFromHardDive(os.path.join("mock-product-pictures", "sofa.jpg"))
    product2.addPictureFromHardDive(os.path.join("mock-product-pictures", "table.jpg"))
    product3.addPictureFromHardDive(os.path.join("mock-product-pictures", "tv.jpg"))
    product4.addPictureFromHardDive(os.path.join("mock-product-pictures", "desk.jpg"))

#######################################################################
# Adds news to the database.
#######################################################################
def addNews():
    news1 = News(title = "En nyhet", ingress = "En liten ingress som beskriver innehållet i artikeln väl", text = {"ops" : [{"insert" : "Detta är <div> brödtexten"}]})   
    news1.addPictureFromHardDive(os.path.join('mock-product-pictures', 'chair.jpg'))

    db.session.add_all([
        news1
    ])
    db.session.commit()