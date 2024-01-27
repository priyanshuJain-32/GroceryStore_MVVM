# ==============================Validation================================================
from werkzeug.exceptions import HTTPException
from flask import make_response
import json
from flask import Blueprint, request, jsonify


from .. import db
from ..models.category import Category
from ..decorators.token_deco import token_required
from ..decorators.admin_deco import admin_required
from ..decorators.staff_deco import staff_required
from ..instance.instances import cache

category = Blueprint('categoryApi',__name__)

#======================= Category API =====================================

#------------------------ GET All Category ---------------------------------------------
@category.route("/get_all_category", methods=['GET'])
@token_required
@cache.cached(timeout=60)
def get_all_category(user):
	category_data = Category.query.all()
	category_list = []
	if category_data:
		for category in category_data:
			category_list.append({"category_id":category.category_id,"category_name":category.category_name,"category_product_id": [product.product_id for product in category.products]})
		return jsonify(category_list), 200
		
	return jsonify({"message": "No category found"}), 404

#------------------------ GET Category ---------------------------------------------
@category.route("/get_category/<int:category_id>", methods=['GET'])
@token_required
def get_category(user, category_id):
	category_data = Category.query.filter_by(category_id=category_id).first()
	category_products = []
	if category_data:
		for product_data in category_data.products:
			category_products.append({"product_id": product_data.product_id,
				"product_name": product_data.product_name,
				"product_desc":product_data.product_desc,
				"sell_price":product_data.sell_price,
				"cost_price":product_data.cost_price,
				"discount":product_data.discount,
				"product_quantity":product_data.product_quantity,
				"unit_of_measurement":product_data.unit_of_measurement,
				"expiry_date":product_data.expiry_date})
		return jsonify({ "category_id": category_data.category_id, "category_name": category_data.category_name, "products":category_products}), 200
	return jsonify({"message": "No category found"}), 404


#------------------------ POST Category ---------------------------------------------
@category.route("/post_category", methods=['POST'])
@token_required
@admin_required
def post_category(user, data={}):
	if data == {}:
		request_data = request.get_json()

		if (request_data['category_name']==None):
			return jsonify({"message": "Category name is missing"}), 400

		existing_category = Category.query.all()
		for category in existing_category:
			if (request_data['category_name']).lower() == (category.category_name).lower():
			
				return jsonify({"message": "Category name is already present"}), 400

		new_category = Category(category_name=request_data['category_name'])
		db.session.add(new_category)
		db.session.commit()
		return jsonify({"message": "Category successfully added"}), 200
	else:
		request_data = data

		if (request_data['category_name']==None):
			return jsonify({"message": "Category name is missing"}), 400

		existing_category = Category.query.all()
		for category in existing_category:
			if (request_data['category_name']).lower() == (category.category_name).lower():
			
				return jsonify({"message": "Category name is already present"}), 400

		new_category = Category(category_name=request_data['category_name'])
		db.session.add(new_category)
		db.session.commit()
		return jsonify({"message": "Category successfully added"}), 200

#------------------------ PUT Category ---------------------------------------------
@category.route("/put_category", methods=['PUT'])
@token_required
@admin_required
def put_category(user, data={}):
	if data=={}:
		request_data = request.get_json()
		updated_category_name = request_data['category_name']

		old_category = Category.query.filter_by(category_id=request_data['category_id']).first()
		if old_category == None:
			return jsonify({'message': 'Category not found'}), 404

		if (updated_category_name==None):
			return jsonify({'message': 'Category name is missing'}), 400

		existing_category = Category.query.all()
		for category in existing_category:
			if (request_data['category_name']).lower() == (category.category_name).lower():
				return jsonify({'message': 'Category name is already present'}), 400

		old_category.category_name = updated_category_name
		db.session.commit()

		return jsonify({'message': 'Successfully updated'})
	else:
		request_data = data
		updated_category_name = request_data['category_name']

		old_category = Category.query.filter_by(category_id=request_data['category_id']).first()
		if old_category == None:
			return jsonify({'message': 'Category not found'}), 404

		if (updated_category_name==None):
			return jsonify({'message': 'Category name is missing'}), 400

		existing_category = Category.query.all()
		for category in existing_category:
			if (request_data['category_name']).lower() == (category.category_name).lower():
				return jsonify({'message': 'Category name is already present'}), 400

		old_category.category_name = updated_category_name
		db.session.commit()

		return jsonify({'message': 'Successfully updated'})


#------------------------ DELETE Category ---------------------------------------------
@category.route("/delete_category/<int:category_id>", methods=['DELETE'])
@token_required
@admin_required
def delete_category(user, category_id):
	category_data = Category.query.filter_by(category_id=category_id).first()
	product_data = category_data.products
	if category_data:
		db.session.delete(category_data)
		for product in product_data:
			for cart in product.cart:
				db.session.delete(cart)
			db.session.delete(product)
		db.session.commit()
		return jsonify({'message': 'Successfully Deleted'}), 200
	else:
		return jsonify({'message': 'Category not found'}), 404