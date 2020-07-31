from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed #will be used later to submit pictures
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class FilterForm(FlaskForm):
        ###Categories and Types###
        category1 = BooleanField('Chairs', description = "Chairs") 
        category2 = BooleanField('Armchairs', description = "Armchairs") 
        subCategory2_1 = BooleanField('Footstools & Pouffes', description = "Footstools & Pouffes")
        category3 = BooleanField('Sofas', description = "Sofas") 
        category4 = BooleanField('Beds', description = "Beds") 
        category5 = BooleanField('Tables & Desks', description = "Tables & Desks") 
        subCategory5_1 = BooleanField('Tables', description = "Tables")
        subCategory5_2 = BooleanField('Desks', description = "Desks")
        subCategory5_3 = BooleanField('Cofee tables', description = "Cofee tables")
        subCategory5_4 = BooleanField('Bedside tables', description = "Bedside tables")
        category6 = BooleanField('TV stands', description = "TV stands") 
        category7 = BooleanField('Storage', description = "Storages")
        subCategory7_1 = BooleanField('Bookcases', description = "Bookcases")
        subCategory7_2 = BooleanField('Wardrobes', description = "Wardrobes")
        subCategory7_3 = BooleanField('Chests of drawers', description = "Chests of drawers")
        subCategory7_4 = BooleanField('Hooks', description = "Hooks")
        subCategory7_5 = BooleanField('Racks', description = "Racks")
        subCategory7_6 = BooleanField('Boxes', description = "Boxes")
        category8 = BooleanField('Electronics', description = "Electronics")
        category9 = BooleanField('Decoration', description = "Decorations")
        category10 = BooleanField('Kitchen', description = "Kitchens")
        category11 = BooleanField('Outdoor furniture', description = "Outdoor furniture")
        category12 = BooleanField('Miscellaneous', description = "Micellaneous")
        ###Colors###
        color = SelectField('Color', choices = [('black'), ('white'), ('red'), ('brown')]) #might have to change this to boolean fields
        ###Condition###

        ###Payment###

        ###Availability###

        ###Sort By###
        sortby = SelectField('Sort by', choices = [('Most recent'), ('Less recent'), ('Most expensive'), ('Less expensive')])
        ###The sort button###
        sortButton = SubmitField('Sort')