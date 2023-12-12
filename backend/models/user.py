from werkzeug.security import check_password_hash
from .. import db

# ======================================= User Data =======================================
class Users(db.Model):
	user_id = db.Column(db.Integer(), primary_key = True)
	name = db.Column(db.String(50))
	user_name = db.Column(db.String(20), nullable = False, unique=True)

	email = db.Column(db.String(50), nullable=False, unique = True)
	
	password = db.Column(db.String(250), nullable = False)
	role = db.Column(db.String(25), nullable = False)
	status = db.Column(db.String(25), default='inactive', nullable=False)
	last_login = db.Column(db.DateTime, nullable = True)
	
	addresses = db.relationship('Address')
	orders = db.relationship('Orders')
	
	def get_id(self):
		return self.user_id

	@classmethod
	def authenticate(cls, **kwargs):
		user_name_ = kwargs.get('user_name')
		password_ = kwargs.get('password')
		role_ = kwargs.get('role')

		if not user_name_ or not password_:
			return None
		user = cls.query.filter_by(user_name=user_name_).first()
		
		if (not user) or (not check_password_hash(user.password, password_)):
			return None
		if user.role != role_:
			return None
		if user.status != 'active':
			return None

		return user
	
	def to_dict(self):
		return dict(user_id=self.user_id, user_name=self.user_name)