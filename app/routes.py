from app import app
from flask import render_template, request
from app.models import User
from app import db

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/new_member")
def new_form():
	return render_template("new_member.html")

@app.route("/add_member", methods = ['GET', 'POST'])
def add_member():
	user = User(first_name = request.form['first_name'], last_name = request.form['last_name'], email = request.form['email'], password = request.form['password'])
	#add user to the database
	db.session.add(user)
	db.session.commit()
	return("Successfully written to database")
	