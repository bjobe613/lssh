from flask import Blueprint, render_template
from lssh.models import db, Product, News, Category, PaymentMethod, Condition
import json


admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route("/")
def admin_home():
    return render_template('admin/home.html')


@admin.route("/products/")
def admin_products():
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('admin/products.html', categories=categories, products=products)


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
        products = Product.query.filter_by(category=category)
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

@ admin.route("/faq/")
def admin_faq():
    return render_template('admin/faq.html')

@ admin.route("/login/")
def admin_login():
    return render_template('admin/login.html')
