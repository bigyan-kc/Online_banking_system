from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
	__tablename__ = "users"
	user_id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(60))
	last_name = db.Column(db.String(60))
	email = db.Column(db.String(60), index = True, unique = True)
	password_hash = db.Column(db.String(128))

	def __init__(self, user_id, first_name, last_name, email, password):
		self.user_id = user_id
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password_hash = generate_password_hash(password)

	@property
	def password(self):
		raise AttributeError("password is not a readable")

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User: {}>'.format(self.first_name + self.last_name)