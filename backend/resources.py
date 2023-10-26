# ==============================Validation================================================
from werkzeug.exceptions import HTTPException
from flask import make_response
import json
from flask import Blueprint, request, jsonify
from . import db
from .models import Category, Product
from datetime import datetime

resource = Blueprint('resource',__name__)

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
@resource.route("/api/category", methods=['GET'])
def get_all_category():
	category_data = Category.query.all()
	category_list = []
	if category_data:
		for category in category_data:
			category_list.append({"category_id":category.category_id,"category_name":category.category_name})
		return jsonify(category_list)
		
	raise NotFoundError(404)


#------------------------ GET Category ---------------------------------------------
@resource.route("/api/category/<int:category_id>", methods=['GET'])
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
@resource.route("/api/category", methods=['POST'])
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
@resource.route("/api/category/<int:category_id>", methods=['PUT'])
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
@resource.route("/api/category/<int:category_id>", methods=['DELETE'])
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


# #======================= Product API =====================================


#------------------------ GET All Product ---------------------------------------------
@resource.route("/api/product", methods=['GET'])	
def get_all_product():
	
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

	raise NotFoundError(404)


#------------------------ GET Product ---------------------------------------------
@resource.route("/api/product/<int:product_id>", methods=['GET'])	
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
	raise NotFoundError(404)


#------------------------ POST Product ---------------------------------------------
@resource.route("/api/product", methods=['POST'])
def post_product():
	
	request_data = request.form
	
	if (request_data['product_name']==None):
		raise BadRequest('Product name is missing',400)
	elif (request_data['sell_price']==None):
		raise BadRequest('Product selling price is missing',400)
	elif (request_data['cost_price']==None):
		raise BadRequest('Product cost price is missing',400)
	elif (request_data['discount']==None):
		raise BadRequest('Product discount is missing, enter 0 if no discount',400)
	elif (request_data['product_quantity']==None):
		raise BadRequest('Product quantity is missing',400)
	elif (request_data['unit_of_measurement']==None):
		raise BadRequest('Product unit of measurement is missing',400)
	elif (request_data['expiry_date']==None):
		raise BadRequest('Product expiry_date is missing',400)
	elif (request_data['product_category_id']==None):
		raise BadRequest('Product category_id is missing, check category first',400)

	existing_products = Category.query.filter_by(category_id=request_data['product_category_id']).first()
	for product in existing_products.products:
		if (request_data['product_name']).lower() == (product.product_name).lower():
			raise BadRequest('Product name is already present',400)
	d_format = '%Y-%m-%d'
	expiry_date = datetime.strptime(request_data['expiry_date'],d_format)
	new_product = Product(product_name=request_data['product_name'],
		product_desc=request_data['product_desc'],
		unit_of_measurement=request_data['unit_of_measurement'],
		sell_price=request_data['sell_price'],
		cost_price=request_data['cost_price'],
		discount=request_data['discount'],
		product_quantity=request_data['product_quantity'],
		expiry_date=expiry_date,
		product_category_id=request_data['product_category_id'])
	db.session.add(new_product)
	db.session.commit()
	raise SuccessfullyAdded(200)


#------------------------ PUT Product ---------------------------------------------
@resource.route("/api/product/<int:product_id>", methods=['PUT'])
def put_product(product_id):
	
	request_data = request.form
	
	product_data = Product.query.filter_by(product_id=product_id).first()
	if product_data:
		if (request_data['product_name']==None):
			raise BadRequest('Product name is missing',400)
		elif (request_data['sell_price']==None):
			raise BadRequest('Product selling price is missing',400)
		elif (request_data['cost_price']==None):
			raise BadRequest('Product cost price is missing',400)
		elif (request_data['discount']==None):
			raise BadRequest('Product discount is missing, enter 0 if no discount',400)
		elif (request_data['product_quantity']==None):
			raise BadRequest('Product quantity is missing',400)
		elif (request_data['unit_of_measurement']==None):
			raise BadRequest('Product unit of measurement is missing',400)
		elif (request_data['expiry_date']==None):
			raise BadRequest('Product expiry_date is missing',400)
		elif (request_data['product_category_id']==None):
			raise BadRequest('Product category_id is missing, check category first',400)
		
		existing_products = Category.query.filter_by(category_id=request_data['product_category_id']).first()
		for product in existing_products.products:
			if (request_data['product_name']).lower() == (product.product_name).lower():
				raise BadRequest('Product name is already present',400)
		
		product_data.product_name = request_data['product_name']
		product_data.product_desc = request_data['product_desc']
		product_data.unit_of_measurement = request_data['unit_of_measurement']
		product_data.sell_price = request_data['sell_price']
		product_data.cost_price = request_data['cost_price']
		product_data.discount = request_data['discount']
		product_data.product_quantity = request_data['product_quantity']

		d_format = '%Y-%m-%d'
		expiry_date = datetime.strptime(request_data['expiry_date'],d_format)
		
		product_data.expiry_date = expiry_date
		product_data.product_category_id = request_data['product_category_id']
		db.session.commit()
		raise SuccessfullyUpdated(200)
	raise NotFoundError(404)


#------------------------ DELETE Product ---------------------------------------------
@resource.route("/api/product/<int:product_id>", methods=['DELETE'])
def delete_product(product_id):
	product_data = Product.query.filter_by(product_id=product_id).first()
	if product_data:
		for cart in product_data.cart:
			db.session.delete(cart)	
		db.session.delete(product_data)
		db.session.commit()
		raise SuccessfullyDeleted(200)
	else:
		raise NotFoundError(404)