# ========================= Library Imports ============================
from flask import Blueprint, request, jsonify

# ========================= Local Imports ============================
from .. import db
from ..models.category import Category
from ..models.product import Product
from ..models.user import Users
from ..decorators.token_deco import token_required
from ..decorators.admin_deco import admin_required
from ..decorators.staff_deco import staff_required

product = Blueprint('productApi',__name__)

# ==========================================================================
# #======================= Product API =====================================
# ==========================================================================

#------------------------ GET All Product ---------------------------------------------
@product.route("/get_all_product", methods=['GET'])
@token_required
def get_all_product(user):
	
	all_product_data = Product.query.all()
	product_list = []
	if all_product_data:
		for product_data in all_product_data:
			product_list.append({"product_category_id": product_data.product_category_id,
				"product_category": product_data.category.category_name,
				"product_id": product_data.product_id,
				"product_name": product_data.product_name,
				"product_desc":product_data.product_desc,
				"sell_price":product_data.sell_price,
				"cost_price":product_data.cost_price,
				"discount":product_data.discount,
				"product_quantity":product_data.product_quantity,
				"unit_of_measurement":product_data.unit_of_measurement,
				"expiry_date":product_data.expiry_date})
		return jsonify(product_list), 200

	return jsonify({'message': 'No products in db'}), 200


#------------------------ GET Product ---------------------------------------------
@product.route("/get_product/<int:product_id>", methods=['GET'])
@token_required
def get_product(product_id):
	
	product_data = Product.query.filter_by(product_id=product_id).first()
	if product_data:
		return jsonify({"product_category_id": product_data.product_category_id,
		"product_category": product_data.category.category_name,
		"product_id": product_data.product_id,
		"product_name": product_data.product_name,
		"product_desc":product_data.product_desc,
		"sell_price":product_data.sell_price,
		"cost_price":product_data.cost_price,
		"discount":product_data.discount,
		"product_quantity":product_data.product_quantity,
		"unit_of_measurement":product_data.unit_of_measurement,
		"expiry_date":product_data.expiry_date}), 200
	return jsonify({'message': 'Product not found'}), 404


#------------------------ POST Product ---------------------------------------------
@product.route("/post_product", methods=['POST'])
@token_required
@staff_required
def post_product(user):
	request_data = request.get_json()
	print(request_data)
	if (request_data['product_name']==None):
		return jsonify({'message': "Product name is missing"}),400
	elif (request_data['sell_price']==None):
		return jsonify({'message': "Product sell_price is missing"}),400
	elif (request_data['cost_price']==None):
		return jsonify({'message': "Product cost_price is missing"}),400
	elif (request_data['discount']==None):
		return jsonify({'message': "Product discount is missing"}),400
	elif (request_data['product_quantity']==None):
		return jsonify({'message': "Product quantity is missing"}),400
	elif (request_data['unit_of_measurement']==None):
		return jsonify({'message': "Product unit_of_measurement is missing"}),400
	elif (request_data['product_category_id']==None):
		return jsonify({'message': "Product category_id is missing"}),400
	print('line 111 productApi')
	existing_products = Category.query.filter_by(category_id=request_data['product_category_id']).first()
	for product in existing_products.products:
		if (request_data['product_name']).lower() == (product.product_name).lower():
			return jsonify({'message': "Product name is already present"}), 200
	print("line 116 in productApi")
	new_product = Product(product_name=request_data['product_name'],
		product_desc=request_data['product_desc'],
		unit_of_measurement=request_data['unit_of_measurement'],
		sell_price=request_data['sell_price'],
		cost_price=request_data['cost_price'],
		discount=request_data['discount'],
		product_quantity=request_data['product_quantity'],
		expiry_date=request_data['expiry_date'],
		product_category_id=request_data['product_category_id'])
	db.session.add(new_product)
	db.session.commit()
	return jsonify({'message': 'Added Product Successfully'})


#------------------------ PUT Product ---------------------------------------------
@product.route("/put_product", methods=['PUT'])
@token_required
@staff_required
def put_product(user):
	
	request_data = request.get_json()
	print(request_data)
	product_data = Product.query.filter_by(product_id=request_data['product_id']).first()
	if product_data:
		if (request_data['product_name']==None):
			return jsonify({'message': "Product name is missing"}),400
		elif (request_data['sell_price']==None):
			return jsonify({'message': "Product sell_price is missing"}),400
		elif (request_data['cost_price']==None):
			return jsonify({'message': "Product cost_price is missing"}),400
		elif (request_data['discount']==None):
			return jsonify({'message': "Product discount is missing"}),400
		elif (request_data['product_quantity']==None):
			return jsonify({'message': "Product quantity is missing"}),400
		elif (request_data['unit_of_measurement']==None):
			return jsonify({'message': "Product unit_of_measurement is missing"}),400
		elif (request_data['product_category_id']==None):
			return jsonify({'message': "Product category_id is missing"}),400	
		existing_products = Category.query.filter_by(category_id=request_data['product_category_id']).first()
		print(existing_products)
		
		product_data.product_name = request_data['product_name']
		product_data.product_desc = request_data['product_desc']
		product_data.unit_of_measurement = request_data['unit_of_measurement']
		product_data.sell_price = request_data['sell_price']
		product_data.cost_price = request_data['cost_price']
		product_data.discount = request_data['discount']
		product_data.product_quantity = request_data['product_quantity']		
		product_data.expiry_date = request_data['expiry_date']
		product_data.product_category_id = request_data['product_category_id']
		db.session.commit()
		return jsonify({'message': 'Product updated successfully'}), 200
	return jsonify({'message': "No product found"}), 404


#------------------------ DELETE Product ---------------------------------------------
@product.route("/delete_product/<int:product_id>", methods=['DELETE'])
@token_required
@admin_required
def delete_product(user, product_id):
	product_data = Product.query.filter_by(product_id=product_id).first()
	if product_data:
		for cart in product_data.cart:
			db.session.delete(cart)	
		db.session.delete(product_data)
		db.session.commit()
		return jsonify({'message': 'Successfully Deleted'})
	else:
		return jsonify({'message': 'Product Not found'}), 404