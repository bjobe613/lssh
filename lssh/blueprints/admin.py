from flask import Blueprint, render_template, request, jsonify
from lssh.models import db, Product, News, Question, Categoryfaq, Category, PaymentMethod, Condition, User, ProductPictures
import json


admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route("/")
def admin_home():
    return render_template('admin/home.html')


@admin.route("/add_maintain_customers", methods=['GET'])
def add_maintain_customers():

    users = User.query.order_by(User.name).all()

    return render_template('admin/add_maintain_customers.html', users = users)

@admin.route("/add_maintain_customers/<string:liuID>/")
def add_maintain_customers_single(liuID):

    buyers = User.query.filter_by(liuID = liuID)

    return render_template('admin/add_maintain_customers.html', buyers = buyers, optional_search_header="Search with LiU ID")

@admin.route("/add_maintain_customers/email/<string:email>/")
def add_maintain_customers_single_email(email):

    buyers = User.query.filter_by(email = email)


    return render_template('admin/add_maintain_customers.html', buyers = buyers, optional_search_header="Search with email")


@admin.route("/add_maintain_customers/delete", methods=['GET', 'POST'])
def add_maintain_customers_delete():


    # Will there be foreign key problems with this?
    data = request.get_json()
    User.query.filter_by(liuID = data['liuID']).delete()
    db.session.commit()

    return ""

@admin.route("/buyingprocess/", methods=['GET', 'POST'])
def buying_process():



    if request.method == 'POST':
        data = request.get_json()

        print(data['product_id'])

        product = Product.query.filter(Product.articleNumber == data['product_id']).first()
        
        print(product.articleNumber)

        productJson = {
            'articleNumber' : product.articleNumber,
            'name' : product.name,
            'price' : product.price
        }

        return jsonify(productJson)

    elif request.method == 'GET':

        return render_template('admin/buy_process.html')
    
@admin.route("/buyingprocess/data", methods=['POST'])
def buying_process_data():

    data = request.get_json()

    product = Product.query.filter(Product.articleNumber == data['product_id'], Product.quantity != 0).first() 


    productPictures = ProductPictures.query.filter(ProductPictures.productID == data['product_id']).first()


    productJson = {
        'articleNumber' : product.articleNumber,
        'name' : product.name,
        'price' : product.price,
        'seller' : product.seller,
        'picture' : productPictures.pictureName,
        'quantity' : product.quantity,
        'boughtQuantity' : 1
    }

    return jsonify(productJson)

@admin.route("/buyingprocess/remove_product", methods=['POST'])
def buying_process_remove_product():
    data = request.get_json()

    print(data)

    

    product = Product.query.filter(Product.articleNumber == data['product_id']).first()

     # Need some form of control if this would be incorrect
    product.quantity = product.quantity - data['quantityToBuy']

    #If successful, shall send email to seller about the item sold
    
    db.session.commit()

    return "Success"

@admin.route("/buyingprocess/add_buyer", methods=['POST'])
def buying_process_add_buyer():
    data = request.get_json()

    newBuyer = User(liuID = data['liuid'], name = data['name'], email = data['email'], program = data['program'], international = data['international'])
    db.session.add(newBuyer)
    db.session.commit()

    return "Success"

    


@admin.route("/buyingprocess/customer", methods=['POST'])
def buying_process_customer():

    data = request.get_json()

    if (data['liu_id'] != ""):
        buyer = User.query.filter(User.liuID == data['liu_id']).first()
       

        buyerJson = {  
        'liuID' : buyer.liuID,
        'email' : buyer.email,
        'name' : buyer.name,
        'program' : buyer.program,
        'international' : buyer.international
        }
        return jsonify(buyerJson)

    elif (data['email'] != ""):
        buyer = User.query.filter(User.email == data['email']).first()
      
        buyerJson = {  
        'liuID' : buyer.liuID,
        'email' : buyer.email,
        'name' : buyer.name,
        'program' : buyer.program,
        'international' : buyer.international
        }
        return jsonify(buyerJson)
    else:
        return "", 400
  

@admin.route("/products/")
def admin_products():
    products = Product.query.filter(Product.quantity != 0).all()
    categories = Category.query.all()
    return render_template('admin/products.html', categories=categories, products=products)


@admin.route("/products/archive")
def admin_products_archive():
    products = Product.query.filter(Product.quantity == 0).all()
    categories = Category.query.all()
    return render_template('admin/products.html', categories=categories, products=products, optional_table_header="Archive")


@admin.route("/products/search/<int:articleNumber>/")
def admin_products_search(articleNumber):
    products = Product.query.filter_by(articleNumber=articleNumber)
    categories = Category.query.all()

    return render_template('admin/products.html', categories=categories, products=products, optional_table_header="Search results for: {0}".format(articleNumber))


@admin.route("/products/category/<string:category_str>/")
def admin_products_category(category_str):
    category = Category.query.filter_by(name=category_str).first()
    categories = Category.query.all()

    if category:
        products = Product.query.filter_by(category=category).filter(Product.quantity != 0)
        return render_template('admin/products.html', categories=categories, products=products, optional_table_header="Filtered by category: {0}".format(category_str))
    else:
        return render_template('admin/products.html', categories=categories, products=[], optional_table_header="There is no category named: {0} in the database".format(category_str))

@admin.route("/products/add")
def admin_add_product():
    categories = Category.query.all()
    paymentMethods = PaymentMethod.query.all()
    conditions = Condition.query.all()

    return render_template('admin/add_product.html', categories=categories, paymentMethods=paymentMethods, conditions=conditions)


@admin.route("/news/edit/<int:id>")
def admin_edit_news(id):
    news = News.query.get_or_404(id)
    return render_template('admin/edit_news.html', news_id=id)


@admin.route("/news/view/<int:id>")
def admin_view_news(id):
    news = News.query.get_or_404(id)
    return render_template('admin/view_news.html', article=news.get_article_as_html(), news_id=id)

@ admin.route("/news/add")
def admin_add_news():
    return render_template('admin/add_news.html')

@ admin.route("/news/")
def admin_news():
    all_news=News.query.all()
    return render_template('admin/news.html', all_news=all_news)

@ admin.route("/faq/", defaults={'categoryid': None})
@ admin.route("/faq/<int:categoryid>")
def admin_faq(categoryid):
    faqcategories = Categoryfaq.query.all()

    if not categoryid:
        categoryid = Categoryfaq.query.order_by(Categoryfaq.id).first().id
    
    chosenCategory=Categoryfaq.query.get_or_404(categoryid)
    faqquestions = Question.query.filter(Question.categoryID == categoryid).all()
    return render_template('admin/faq.html', chosenCategory=chosenCategory, faqquestions=faqquestions, faqcategories=faqcategories)

@ admin.route("faq/edit/<int:questionid>")
def admin_faq_edit(questionid):
    categories = Categoryfaq.query.all()
    question = Question.query.get_or_404(questionid)
    return render_template('admin/edit_faq_question.html', categories=categories, question=question)

@ admin.route("faq/add")
def faq_add_question():
    categories = Categoryfaq.query.all()
    return render_template('admin/add_faq_question.html', categories=categories)

@ admin.route("faq/add-category")
def faq_add_category():
    return render_template('admin/add_faq_category.html')

@ admin.route("/login/")
def admin_login():
    return render_template('admin/login.html')
