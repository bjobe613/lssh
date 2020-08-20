from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed #will be used later to submit pictures
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class AdminLoginForm(FlaskForm):
        userName = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        loginButton = SubmitField('Login')

class AdminRegisterForm(FlaskForm):
        userName = StringField('Username', validators=[DataRequired()])
        authorizationLevel = IntegerField('AuthorizationLevel', validators=[DataRequired()])
        password = StringField('Password', validators=[DataRequired()])
        confirmPassword = StringField('Confirm Password', validators=[DataRequired(), EqualTo(password)])  #check that the EqualTo syntax is correct 
        registerButton = SubmitField('Register')