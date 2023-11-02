# ==============================Validation================================================
from werkzeug.exceptions import HTTPException
from flask import make_response
import json
from flask import Blueprint, request, jsonify
from .. import db
from ..models.category import Category
from ..decorators.token_deco import token_required
from ..decorators.admin_deco import admin_required

category = Blueprint('categoryApi',__name__)

class BadRequest(HTTPException):
	def __init__(self, error_message, status_code):
		message = {"error_message": error_message}
		self.response = make_response(json.dumps(message), status_code)

class NotFoundError(HTTPException):
	def __init__(self, status_code):
		self.response = make_response('Not found', status_code)

class SuccessfullyAdded(HTTPException):
	def __init__(self, status_code):
		self.response = make_response('SuccessfullyAdded', status_code)

class SuccessfullyUpdated(HTTPException):
	def __init__(self, status_code):
		self.response = make_response('SuccessfullyUpdated', status_code)

class SuccessfullyDeleted(HTTPException):
	def __init__(self, status_code):
		self.response = make_response('SuccessfullyDeleted', status_code)

#======================= Category API =====================================

#------------------------ GET All Category ---------------------------------------------
@category.route("/get_all_category", methods=['GET'])
@token_required
def get_all_category(user):
	category_data = Category.query.all()
	category_list = []
	if category_data:
		for category in category_data:
			category_list.append({"category_id":category.category_id,"category_name":category.category_name,"category_product_id": [product.product_id for product in category.products]})
		return jsonify(category_list)
		
	raise NotFoundError(404)


#------------------------ GET Category ---------------------------------------------
@category.route("/get_category/<int:category_id>", methods=['GET'])
@token_required
def get_category(category_id):
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
	raise NotFoundError(404)


#------------------------ POST Category ---------------------------------------------
@category.route("/post_category", methods=['POST'])
@token_required
@admin_required
def post_category():
	request_data = request.form

	if (request_data['category_name']==None):
		raise BadRequest('Category name is missing',400)

	existing_category = Category.query.all()
	for category in existing_category:
		if (request_data['category_name']).lower() == (category.category_name).lower():
		
			raise BadRequest('Category name is already present',400)

	new_category = Category(category_name=request_data['category_name'])
	db.session.add(new_category)
	db.session.commit()
	raise SuccessfullyAdded(200)


#------------------------ PUT Category ---------------------------------------------
@category.route("/put_category/<int:category_id>", methods=['PUT'])
@token_required
@admin_required
def put_category(category_id):
	request_data = request.form
	updated_category_name = request_data['category_name']

	old_category = Category.query.filter_by(category_id=category_id).first()
	if old_category == None:
		raise NotFoundError(404)

	if (updated_category_name==None):
		raise BadRequest('Category name is missing',400)

	existing_category = Category.query.all()
	for category in existing_category:
		if (request_data['category_name']).lower() == (category.category_name).lower():
			raise BadRequest('Category name is already present',400)

	old_category.category_name = updated_category_name
	db.session.commit()

	raise SuccessfullyUpdated(200)


#------------------------ DELETE Category ---------------------------------------------
@category.route("/delete_category/<int:category_id>", methods=['DELETE'])
@token_required
@admin_required
def delete_category(category_id):
	category_data = Category.query.filter_by(category_id=category_id).first()
	product_data = category_data.products
	if category_data:
		db.session.delete(category_data)
		for product in product_data:
			for cart in product.cart:
				db.session.delete(cart)
			db.session.delete(product)
		db.session.commit()
		raise SuccessfullyDeleted(200)
	else:
		raise NotFoundError(404)