from os import name
from flask import Flask, render_template, url_for, flash, redirect, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import camel_to_snake_case
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField # We will only use StringField and SubmitField in our simple form.
from wtforms.validators import DataRequired, Length, ValidationError


app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY']='SOME_KEY' #Configure a secret key for CSRF protection.

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class dog(db.Model):
   id = db.Column('dog_id', db.Integer, primary_key = True)
   breed = db.Column(db.String(100))
   name = db.Column(db.String(50))  
   weight = db.Column(db.Integer)
   food = db.Column(db.String(20))
   age= db.Column(db.Integer)
   
def __init__(breed, name, weight, food, age):
    dog.breed = breed
    dog.name = name
    dog.weight = weight
    dog.food = food
    dog.age = age

class cat(db.Model):
   id = db.Column('dog_id', db.Integer, primary_key = True)
   breed = db.Column(db.String(100))
   name = db.Column(db.String(50))  
   weight = db.Column(db.Integer)
   food = db.Column(db.String(20))
   age= db.Column(db.Integer)
   
def __init__(breed, name, weight, food, age):
   cat.breed = breed
   cat.name = name
   cat.weight = weight
   cat.food = food
   cat.age = age

submit = SubmitField('Submit')



class CatForm(FlaskForm):
    breed = StringField('Breed' , validators=[DataRequired(), Length(min=1, max=15)])
    name = StringField('Name' , validators=[DataRequired(), Length(min=1, max=15)])
    weight = IntegerField('Weight', validators=[DataRequired(), Length(min=1, max=2)])
    food = StringField('Food', validators=[DataRequired(), Length(min=1, max=10)])
    age = IntegerField('Age', validators=[DataRequired(), Length(min=1, max = 2)])
    
    def validate(self, breed):
        cats = cat.query.filter_by(breed=breed.data).first()
        
       
    

class DogForm(FlaskForm):
    breed = StringField('Breed' , validators=[DataRequired(), Length(min=1, max=15)])
    name = StringField('Name' , validators=[DataRequired(), Length(min=1, max=15)])
    weight = IntegerField('Weight', validators=[DataRequired(), Length(min=1, max=2)])
    food = StringField('Food', validators=[DataRequired(), Length(min=1, max=10)])
    age = IntegerField('Age', validators=[DataRequired(), Length(min=1, max = 2)])

    def validate(self, breed):
        dogs = dog.query.filter_by(breed=breed.data).first()
      
@app.route('/')
def home():
    form = MyForm()
    dogs = dog.query.all()
    cats = cat.query.all()
    return render_template('home.html', form = MyForm, dogs=dog, cats=cat)


@app.route('/cats', methods=['GET','POST'])
def cats():
    form = CatForm()
    if form.validate_on_submit():
        cats = cat(id = form.id.data , breed = form.breed.data , name = form.name.data , weight = form.weight.data , food = form.food.data , age = form.age.data)
        return render_template('cats.html', form = CatForm, name = name)
         

@app.route('/dogs', methods=['GET','POST'])
def dogs():
    form = DogForm()
    if form.validate_on_submit():
        dogs = dog(id = form.id.data , breed = form.breed.data , name = form.name.data , weight = form.weight.data , food = form.food.data , age = form.age.data)
        return render_template('dogs.html', form = DogForm, name = name)


         



