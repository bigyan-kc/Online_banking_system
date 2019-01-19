from app import app
from flask import render_template
from app.models import User
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/new_member")
def new_form():
	return render_template("new_member.html")

@app.route("/add_member", methods = ['GET', 'POST'])
def add_member():
	user = User(first_name = request.get.form('first_name'), last_name = request.get.form('last_name'), email = request.get.form('email'), password = request.get.form('password'))
	#add user to the database
	db.session.add(user)
	db.session.commit()
	