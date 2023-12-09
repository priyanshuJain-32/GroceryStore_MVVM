from .. import db
from .user import Users
from .product import Product

class Orders(db.Model):
	order_id = db.Column(db.Integer(), primary_key = True)
	order_quantity = db.Column(db.Float(), nullable = False)
	sell_date = db.Column(db.DateTime(), nullable = False)
	order_user_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
	order_product_id = db.Column(db.Integer(), db.ForeignKey('product.product_id'))
	
	order_product_name = db.Column(db.String(50), nullable = False)
	order_product_desc = db.Column(db.String(250), nullable = True)
	order_sell_price = db.Column(db.Float(), nullable = False)
	order_cost_price = db.Column(db.Float(), nullable = False)
	order_unit_of_measurement = db.Column(db.String(), nullable = False)
	order_discount = db.Column(db.Float())
	order_expiry_date = db.Column(db.String(25), nullable = True)
	
	products = db.relationship('Product', backref='orders')