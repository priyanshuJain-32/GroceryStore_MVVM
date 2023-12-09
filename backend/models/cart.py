from .. import db
from .user import Users
from .product import Product

class Cart(db.Model):
	cart_id = db.Column(db.Integer(), primary_key = True)
	cart_product_quantity = db.Column(db.Float(), nullable = False)
	
	cart_user_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
	cart_product_id = db.Column(db.Integer(), db.ForeignKey('product.product_id'))
	products = db.relationship('Product', backref='cart')