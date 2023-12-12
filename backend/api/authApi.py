# Library imports
from flask import Blueprint, current_app, request, jsonify
from werkzeug.security import generate_password_hash
import jwt
from datetime import datetime, timedelta

# Internal imports
from .. import db
from ..models.user import Users
from ..models.requests import Requests

auth = Blueprint('authApi', __name__)

@auth.route('/login', methods=['POST'])
def login():
	
	data = request.get_json()
	user = Users.authenticate(**data)
	
	if not user:
		return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 401
	
	user.last_login = datetime.utcnow()
	db.session.commit()
	token = jwt.encode({
		'sub': user.user_name,
		'iat': datetime.utcnow(),
		'exp': datetime.utcnow() + timedelta(minutes=30)
	}, current_app.config['SECRET_KEY'], algorithm="HS256")
	return jsonify({'token': token}), 200
	

@auth.route('/signup', methods=['POST'])
def signup():
	
	data = request.get_json()
	name_ = data.get('name')
	role_ = data.get('role')
	user_name_ = data.get('user_name')
	email_ = data.get('email')
	password_ = generate_password_hash(data.get('password'), method='sha256')
	
	user = Users.authenticate(**data)
	if user:
		return jsonify({'message': 'User already exist', 'authenticated': False})

	# Create the new_user and commit to the database
	if role_=='manager':
		new_user = Users(name=name_, user_name=user_name_, email = email_, password=password_, role=role_)
		db.session.add(new_user)
		new_request = Requests(requester_id = new_user.user_id, request_type = 'signup_' + user_name_)
		db.session.add(new_request)
		db.session.commit()
		return jsonify({'message': 'Manager signup request submitted', 'authenticated' : True}), 200
	else:
		new_user = Users(name=name_, user_name=user_name_, email = email_, password=password_, role=role_, status='active', last_login=datetime.utcnow())
		db.session.add(new_user)
		db.session.commit()

	token = jwt.encode({
		'sub': new_user.user_name,
		'iat': datetime.utcnow(),
		'exp': datetime.utcnow() + timedelta(minutes=30)
	}, current_app.config['SECRET_KEY'], algorithm="HS256")
	return jsonify({'token': token})