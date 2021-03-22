"""A flask application"""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

# app routes
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))

# Create User class
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Create User table
# The code below was run in the terminal:

# db.create_all()

# admin = User(username='admin', email='admin@example.com')
# guest = User(username='guest', email='guest@example.com')

# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()
