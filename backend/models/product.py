from .. import db
from .category import Category

# ====================================== Inventory =======================================

class Product(db.Model):
	product_id = db.Column(db.Integer(), primary_key = True)

	product_name = db.Column(db.String(50), nullable = False)
	product_desc = db.Column(db.String(250), nullable = True)
	sell_price = db.Column(db.Float(), nullable = False)
	cost_price = db.Column(db.Float(), nullable = False)
	unit_of_measurement = db.Column(db.String(), nullable = False)
	discount = db.Column(db.Float())
	product_quantity = db.Column(db.Float(), nullable = False)
	expiry_date = db.Column(db.Date())

	product_category_id = db.Column(db.Integer(), db.ForeignKey('category.category_id'))