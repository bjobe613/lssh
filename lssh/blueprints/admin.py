from flask import Blueprint, render_template
from lssh.models import db

admin = Blueprint('admin', __name__, url_prefix = '/admin')

@admin.route("/")
def admin_home():
    return render_template('admin/home.html')

@admin.route("/products/")
def admin_products():
    cat = [
        {"name": "Chairs"},
        {"name": "Desks"},
        {"name": "Tables"},
        {"name": "Sofas"}
    ]

    prod = [
        {
            "name": "Blue armchair",
            "category": "Chair",
            "id": "50"
        },
        {
            "name": "Green armchair",
            "category": "Chair",
            "id": "123456"
        },
        {
            "name": "Red armchair",
            "category": "Chair",
            "id": "200"
        },
        {
            "name": "Red armchair",
            "category": "Chair",
            "id": "200"
        },
        {
            "name": "Red armchair",
            "category": "Chair",
            "id": "200"
        },
        {
            "name": "Red armchair",
            "category": "Chair",
            "id": "200"
        },
        {
            "name": "Red armchair",
            "category": "Chair",
            "id": "200"
        },
        {
            "name": "Red armchair",
            "category": "Chair",
            "id": "200"
        },
        {
            "name": "Red armchair",
            "category": "Chair",
            "id": "200"
        },
        {
            "name": "Blue armchair",
            "category": "Chair",
            "id": "300"
        }
    ]
    return render_template('admin/products.html', categories=cat, products=prod)

@admin.route("/product/add")
def admin_add_product():
    cat = [
        {"name": "Chairs"},
        {"name": "Desks"},
        {"name": "Tables"},
        {"name": "Sofas"}
    ]

    return render_template('admin/add_product.html', categories=cat)

@admin.route("/news/add")
def admin_add_news():
    return render_template('admin/add_news.html')
    
@admin.route("/news/")
def admin_news():
    return render_template('admin/news.html')

@admin.route("/faq/")
def admin_faq():
    return render_template('admin/faq.html')

@admin.route("/login/")
def admin_login():
    return render_template('admin/login.html')