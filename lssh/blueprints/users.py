from flask import Blueprint, render_template, jsonify, request, redirect, url_for, make_response
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity,
                                set_access_cookies, unset_jwt_cookies, get_jwt_claims,
                                verify_jwt_in_request, jwt_optional)
from lssh.models import db, Admin
from lssh.blueprints.forms import AdminRegisterForm
from lssh import flask_bcrypt, flask_jwt
from functools import wraps

users = Blueprint('users', __name__, url_prefix = '/users')

def admin_level2_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['auth_level'] != 1:
            return jsonify(msg='You are not authorized.')
        else:
            return fn(*args, **kwargs)
    return wrapper

@flask_jwt.user_claims_loader
def add_claims_to_access_token(admin):
    return {'auth_level': admin.authorization}

@flask_jwt.user_identity_loader
def user_identity_lookup(admin):
    return admin.name


@users.route("/login", methods = ['GET', 'POST'])
def adminLogin():
    
    if request.method == 'POST':
        content = request.get_json()        
        username = content["username"] # MUST prevent an sql-injection!!!
        password = content['password']
        user = Admin.query.filter(Admin.name == username).first()
        if not user:
            return 'No user', 404
        else:
            if flask_bcrypt.check_password_hash(user.passwordHash, password):     
                access_token = create_access_token(identity=user)
                resp = make_response(redirect(url_for('users.protected_first_level')))
                set_access_cookies(resp, access_token)
                return resp 
            else:
                return 'wrong password', 404
    elif request.method == 'GET':
        if get_jwt_identity() != None:
            return redirect(url_for('users.adminRegister'))   #this shit doesn't work     
        return render_template('login.html')
       

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
            print('added admin')
        else:
            print('user already exist')
                
    return render_template('register.html', adminRegisterForm = form)

@users.route("/logout", methods = ['GET'])
@jwt_required
def adminLogout():
    resp = jsonify({'logout': True})
    resp = make_response(redirect(url_for('users.adminLogin')))
    unset_jwt_cookies(resp)
    return resp, 200 

@users.route("/protected1", methods = ['GET'])
@jwt_required
def protected_first_level():
    claims = get_jwt_claims()
    return render_template('protected1.html')
    

@users.route("/protected2", methods = ['GET'])
@admin_level2_required
def protected_second_level():
    return render_template('protected2.html')
    