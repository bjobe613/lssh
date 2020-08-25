from flask import Blueprint, render_template
from lssh.models import db, Product, News
import json


admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route("/")
def admin_home():
    return render_template('admin/home.html')


@admin.route("/products/")
def admin_products():
    products = Product.query.all()

    cat = []

    for prod in products:
        if cat.count(prod.category) == 0:
            cat.append({"name": prod.category})

    return render_template('admin/products.html', categories=cat, products=products)


@admin.route("/products/search/<int:articleNumber>/")
def admin_products_search(articleNumber):
    products = Product.query.filter_by(articleNumber=articleNumber)

    cat = []

    for prod in products:
        if cat.count(prod.category) == 0:
            cat.append({"name": prod.category})

    return render_template('admin/products.html', categories=cat, products=products, optional_table_header="Search results for: {0}".format(articleNumber))


@admin.route("/products/category/<string:category>/")
def admin_products_category(category):
    products = Product.query.filter_by(category=category)

    cat = []

    for prod in products:
        if cat.count(prod.category) == 0:
            cat.append({"name": prod.category})

    return render_template('admin/products.html', categories=cat, products=products, optional_table_header="Filtered by category: {0}".format(category))


@admin.route("/products/add")
def admin_add_product():
    cat = [
        {"name": "Chairs"},
        {"name": "Desks"},
        {"name": "Tables"},
        {"name": "Sofas"}
    ]

    return render_template('admin/add_product.html', categories=cat)


@admin.route("/news/edit/<int:id>")
def admin_edit_news(id):
    news = News.query.get_or_404(id)
    return render_template('admin/edit_news.html')


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
