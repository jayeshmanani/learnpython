from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# get db url from the heroku database created as resource add on in heroku server
DB_URI = os.environ.get('DATABASE_URL')
app = Flask(__name__)

#Local DB
# password = 'postgres'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:{password}@localhost/quotes'

# Heroku DB
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route("/")
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result = result)

@app.route("/quotes")
def quotes():
    return render_template("quotes.html")

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author = author, quote = quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))