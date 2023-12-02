from .. import db
from .user import Users
# ====================================== Requests =======================================

class Requests(db.Model):
	request_id = db.Column(db.Integer(), primary_key = True)

	requester_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
	request_type = db.Column(db.String(50), nullable = False)
	request_status = db.Column(db.String(20), default='pending', nullable = False)
	users = db.relationship('Users', backref='requests')