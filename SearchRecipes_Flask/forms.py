from wtforms import StringField, SelectField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class RecipeQuiz(FlaskForm):
    ingredients = StringField("Ingredients", validators=[DataRequired()])
    allergies = StringField("Any allergies? (comma-separated)")
    diet = SelectField("Any diet preferences?", choices=[
        ('', 'None'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('ketogenic', 'Keto'),
        ('gluten free', 'Gluten Free')
    ])

    submit = SubmitField("Find Your Recipes")
