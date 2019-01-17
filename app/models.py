from werkzeug.security import generate_password_hash, check_password_hash
class User():
	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password

	def __repr__(self):
		return('First Name: {0} /n Last Name: {1} /n Email: {2}'.format(self.first_name, self.last_name, self.email))

class User(db.model):
	__tablename__ = "users"
	user_id = db.column(db.Integer, primary_key = True)
	first_name = db.column(db.string(60))
	last_name = db.column(db.string(60))
	email = db.column(db.string(60), index = True, unique = True)
	password_hash = db.column(db.string(128))

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