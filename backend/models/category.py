from .. import db

# ====================================== Inventory =======================================
class Category(db.Model):
	category_id = db.Column(db.Integer(), primary_key = True)
	
	category_name = db.Column(db.String(50), nullable = False)

	products = db.relationship('Product', backref='category')