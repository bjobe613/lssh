from flask import Blueprint, render_template
from lssh.models import db, Admin
from lssh.blueprints.forms import AdminLoginForm, AdminRegisterForm
from lssh import flask_bcrypt

users = Blueprint('users', __name__, url_prefix = '/users')

@users.route("/login", methods = ['GET', 'POST'])
def adminLogin():
    form = AdminLoginForm()
    if form.validate_on_submit():
        username = form.userName.data
        password = form.password.data
        user = Admin.query.filter(Admin.name == username).first()
        if not user:
            print('No user') #return error for no user found
        else:
            if flask_bcrypt.check_password_hash(user.passwordHash, password):
                print('Right password')  #create the JWT-token and send to user, then redirect to the admin home page
            else:
                print('wrong password')
            
    return render_template('login.html', adminLoginForm = form)

@users.route("/register", methods = ['GET', 'POST'])
def adminRegister():
    form = AdminRegisterForm()
    if form.validate_on_submit(): #you must check the password, and the auth.level so that it doesnt collide with functions
        exist = Admin.query.filter(Admin.name == form.userName.data).first()
        if not exist:
            hashedPassword = flask_bcrypt.generate_password_hash(form.password.data).decode('utf-8') 
            newAdmin = Admin(name = form.userName.data, passwordHash = hashedPassword, authorization = form.authorizationLevel.data)
            db.session.add(newAdmin)
            db.session.commit()
        else:
            print('user already exist')
                
    return render_template('register.html', adminRegisterForm = form)