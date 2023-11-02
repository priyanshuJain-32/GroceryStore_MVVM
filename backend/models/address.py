from .. import db
from .user import Users
class Address(db.Model):
	address_id = db.Column(db.Integer(), primary_key = True)
	address_field1 = db.Column(db.String(250), nullable = False)
	address_field2 = db.Column(db.String(100))
	pincode = db.Column(db.Integer(), nullable = False)
	city = db.Column(db.String(100), nullable = False)
	state = db.Column(db.String(100), nullable = False)
	
	address_users = db.Column(db.Integer(), db.ForeignKey('users.user_id'))