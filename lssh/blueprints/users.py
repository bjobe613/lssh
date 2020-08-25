from flask import Blueprint, render_template, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from lssh.models import db, Admin
from lssh.blueprints.forms import AdminRegisterForm
from lssh import flask_bcrypt

import json

users = Blueprint('users', __name__, url_prefix = '/users')

@users.route("/login", methods = ['GET', 'POST'])
def adminLogin():
    if request.method == 'POST':
        content = request.get_json()
        print(content)
        #username = content["username"]
        #password = request.json.get('password')

        
        '''user = Admin.query.filter(Admin.name == username).first()
        if not user:
            print('No user') #return error for no user found
        else:
            if flask_bcrypt.check_password_hash(user.passwordHash, password):
                token = create_access_token(identity = username)  #create the JWT-token and send to user, then redirect to the admin home page?
                res = {}
                res["token"] = token
                res["user"] = user.name
                return jsonify(res), 200           
            else:
                print('wrong password')'''
            
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
        else:
            print('user already exist')
                
    return render_template('register.html', adminRegisterForm = form)

@users.route("/protected1", methods = ['GET'])
@jwt_required
def protected_first_level():
    print("first level access")
    return 200

@users.route("/protected2", methods = ['GET'])
@jwt_required
def protected_second_level():
    print("first second access")
    return 200
