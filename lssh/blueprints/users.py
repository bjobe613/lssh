from flask import Blueprint, render_template
from lssh.models import db, Admin
from lssh.blueprints.forms import AdminLoginForm, RegisterAdminForm

users = Blueprint('users', __name__, url_prefix = '/users')

@users.route("/login", methods = ['GET', 'POST'])
def adminlogin():
    form = AdminLoginForm()
    if form.validate_on_submit():
        username = form.userName.data
        password = form.password.data
        user = Admin.query.filter(Admin.userName == username).first()
        if user != None:
            if user.passwordHash == HashThisShit(password): #need the bcrypt function for this, and maybe seperate if's
                pass #create the JWT-token and send to user, then redirect to the admin home page
            else:
                pass #return error for wrong password
        else:
            pass #return error for no user found
            
    return render_template('login.html', adminLoginForm = form)

    @users.route("/register", methods = ['GET', 'POST'])
    def adminRegister():
    form = RegisterAdminForm()
    if form.validate_on_submit():
        pass
    return render_template('register.html', registerAdminForm = form)