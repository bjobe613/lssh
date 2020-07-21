from flask import Blueprint, render_template
from lssh.models import db

admin = Blueprint('admin', __name__, url_prefix = '/admin')

@admin.route("/")
def admin_home():
    return render_template('admin/home.html')

@admin.route("/products/")
def admin_products():
    return render_template('admin/products.html')

@admin.route("/news/")
def admin_news():
    return render_template('admin/news.html')

@admin.route("/faq/")
def admin_faq():
    return render_template('admin/faq.html')