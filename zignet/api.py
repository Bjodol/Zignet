from zignet import controller, db
from zignet.models import *
from flask import request, abort, make_response

@controller.route('/login', methods = ['POST'])
def login():
	username = request.get('username')
	password = request.get('password')
	Rfid = request.get('Rfid')
	pincode = request.get('pincode')

	if any(username) and any(password) :
		user = db.session.query(User).filter(User.username == username).first()
		if user.verify_password(password) :
			return make_response('true')
		else :
			abort(401)

	elif any(Rfid) and any(pincode):
		user = db.session.query(User).filter(User.Rfid == Rfid).first()
		if user.verify_pincode(pincode) :
			return make_response('true')

		else :
			abort(401)

	else :
		abort(400)

@controller.route('/create_user', methods = ['POST'])
def create_user():
	username = request.get('username')
	password = request.get('password')
	email = request.get('email')

	user = User(email = email, password = password, username = username)
	db.session.add(user)
	db.session.commit()
	return make_response('user created')

@controller.route('/update_user', methods = ['POST'])
def update_user():
	username = request.get('username')
	password = request.get('password')
	email = request.get('email')
	pincode = request.get('pincode')
	first_name = request.get('first_name')
	last_name = request.get('last_name')
	phone = request.get('phone')
	address = request.get('address')
	zip_code = request.get('zip_code')
	country = request.get('country')

	user = db.session.query(User).filter(User.username == username).first()

	if user.verify_password(password) :
		if any(email) :
			user.email = email

		if any(username) :
			user.username = username

		if any(password) :
			user.password = password

		if any(pincode) :
			user.pincode = pincode

		if any(first_name) :
			user.first_name = first_name

		if any(last_name) :
			user.last_name = last_name

		if any(phone) :
			user.phone = phone

		if any(address) :
			user.address = address

		if any(zip_code) :
			user.zip_code = zip_code

		if any(country) :
			user.country = country

		return make_response('user updated')

	else:
		abort(401)


