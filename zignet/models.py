from zignet import db
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String, unique = True)
	password = db.Column(db.String)
	Rfid = db.Column(db.Integer, unique = True)
	pincode = db.Column(db.Integer(6))
	username = db.Column(db.String, unique = True)
	first_name = db.Column(db.String)
	last_name = db.Column(db.String)
	phone = db.Column(db.Integer)
	address = db.Column(db.String)
	zip_code = db.Column(db.Integer)
	country = db.Column(db.String)

	def hash_password(password):
		return pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password)

	def verify_pincode(self, pincode):
		return pwd_context.verify(pincode, self.pincode)

	def __init__(self, email, password, username):
		self.email = email
		self.password = hash_password(password)
		self.username = username



