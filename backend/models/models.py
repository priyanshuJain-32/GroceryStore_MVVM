# from werkzeug.security import check_password_hash
# from .. import db

# # ====================================== Inventory =======================================
# class Category(db.Model):
# 	category_id = db.Column(db.Integer(), primary_key = True)
	
# 	category_name = db.Column(db.String(50), nullable = False)

# 	products = db.relationship('Product', backref='category')

# class Product(db.Model):
# 	product_id = db.Column(db.Integer(), primary_key = True)

# 	product_name = db.Column(db.String(50), nullable = False)
# 	product_desc = db.Column(db.String(250), nullable = True)
# 	sell_price = db.Column(db.Integer(), nullable = False)
# 	cost_price = db.Column(db.Integer(), nullable = False)
# 	unit_of_measurement = db.Column(db.String(), nullable = False)
# 	discount = db.Column(db.Integer())
# 	product_quantity = db.Column(db.Integer(), nullable = False)
# 	expiry_date = db.Column(db.Date())

# 	product_category_id = db.Column(db.Integer(), db.ForeignKey('category.category_id'))


# # ======================================= User Data =======================================
# class Users(db.Model):
# 	user_id = db.Column(db.Integer(), primary_key = True)
# 	name = db.Column(db.String(50))
# 	user_name = db.Column(db.String(50), nullable = False)
# 	password = db.Column(db.String(50), nullable = False)
# 	role = db.Column(db.String(10), nullable = False)
# 	last_login = db.Column(db.DateTime, nullable = True)
# 	addresses = db.relationship('Address')
# 	orders = db.relationship('Orders')
	
# 	def get_id(self):
# 		return self.user_id

# 	@classmethod
# 	def authenticate(cls, **kwargs):
# 		user_name_ = kwargs.get('user_name')
# 		password_ = kwargs.get('password')

# 		if not user_name_ or not password_:
# 			return None
# 		user = cls.query.filter_by(user_name=user_name_).first()
# 		if not user or not check_password_hash(user.password, password_):
# 			return None
# 		return user
	
# 	def to_dict(self):
# 		return dict(id=self.id, email=self.email)


# class Address(db.Model):
# 	address_id = db.Column(db.Integer(), primary_key = True)
# 	address_field1 = db.Column(db.String(250), nullable = False)
# 	address_field2 = db.Column(db.String(100))
# 	pincode = db.Column(db.Integer(), nullable = False)
# 	city = db.Column(db.String(100), nullable = False)
# 	state = db.Column(db.String(100), nullable = False)
	
# 	address_users = db.Column(db.Integer(), db.ForeignKey('users.user_id'))

# # ======================================== Orders =========================================
# class Cart(db.Model):
# 	cart_id = db.Column(db.Integer(), primary_key = True)
# 	cart_product_quantity = db.Column(db.Integer(), nullable = False)
	
# 	cart_user_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
# 	cart_product_id = db.Column(db.Integer(), db.ForeignKey('product.product_id'))
# 	products = db.relationship('Product', backref='cart')

# class Orders(db.Model):
# 	order_id = db.Column(db.Integer(), primary_key = True)
# 	order_quantity = db.Column(db.Integer(), nullable = False)
# 	sell_date = db.Column(db.DateTime(), nullable = False)
	
# 	order_user_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
# 	order_product_id = db.Column(db.Integer(), db.ForeignKey('product.product_id'))
# 	products = db.relationship('Product', backref='orders')
