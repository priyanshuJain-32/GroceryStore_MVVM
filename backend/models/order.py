from .. import db
from .user import Users
from .product import Product

class Orders(db.Model):
	order_id = db.Column(db.Integer(), primary_key = True)
	order_quantity = db.Column(db.Integer(), nullable = False)
	sell_date = db.Column(db.DateTime(), nullable = False)
	
	order_user_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
	order_product_id = db.Column(db.Integer(), db.ForeignKey('product.product_id'))
	products = db.relationship('Product', backref='orders')
