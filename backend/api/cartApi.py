from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from datetime import datetime, date
import os

from .. import db

from ..models.product import Product 
from ..models.order import Orders 
from ..models.cart import Cart
from ..decorators.token_deco import token_required

current_dir = os.path.abspath(os.path.dirname(__file__))

cart = Blueprint('cartApi',__name__)

#======================= Cart User Controls =====================================

def check_cart(id):
	cart_data=Cart.query.filter_by(cart_user_id = id)
	if not cart_data:
		return None
	for cart_product in cart_data:
		if cart_product.cart_product_quantity==0:
			db.session.delete(cart_product)


@cart.route('/cart_products',methods=['PUT']) #### Add tables for cart data
@token_required
def cart_products(user):
	data = request.get_json()

	if not data:
		return jsonify({'message': 'Nothing to cart'})
	cart_data = Cart.query.filter_by(cart_user_id = user.user_id)
	for product_id, product_quantity in data.items():
		product_data = Product.query.filter_by(product_id=product_id).first()
		flag = False
	
		if cart_data:
			for cart_product in cart_data:
				if cart_product.cart_product_id==int(product_id):
					if product_quantity==0:
						product_data.product_quantity -= product_quantity - cart_product.cart_product_quantity
						db.session.delete(cart_product)
						# db.session.commit()
						flag = True

					else:
						product_data.product_quantity -= product_quantity - cart_product.cart_product_quantity
						cart_product.cart_product_quantity = product_quantity
						# db.session.commit()
						flag = True
	
		if (not flag):
			new_cart_entry = Cart(cart_product_id = product_id, cart_product_quantity = product_quantity, cart_user_id = user.user_id)
			product_data.product_quantity -= product_quantity
			db.session.add(new_cart_entry)
			# db.session.commit()
	check_cart(user.user_id)
	db.session.commit()
	return jsonify({'message': 'Carting Successful'})



@cart.route('/view_cart',methods=['GET']) #### Add tables for cart data
@token_required
def view_cart(user):
	cart_data=Cart.query.filter_by(cart_user_id=user.user_id).all()
	data = {}
	for product in cart_data:
		data[product.cart_product_id] = product.cart_product_quantity
	return jsonify({'cart_data': data}), 200


#Fix the checkout cart according to new database design for orders
@cart.route('/checkout_cart', methods=['GET'])
@token_required
def checkout_cart(user):
	cart_data = Cart.query.filter_by(cart_user_id=user.user_id).all()
	
	if not cart_data:
		return jsonify({'message': 'Nothing to checkout'}), 200
	
	sell_date_ = datetime.now()
	order_user_id_ = user.user_id
	for product in cart_data:
		order_quantity_ = product.cart_product_quantity
		order_product_id_ = product.cart_product_id
		order_product_name_ = product.products.product_name
		order_product_desc_ = product.products.product_desc
		order_sell_price_ = product.products.sell_price
		order_cost_price_ = product.products.cost_price
		order_unit_of_measurement_ = product.products.unit_of_measurement
		order_discount_ = product.products.discount
		order_expiry_date_ = product.products.expiry_date

		new_order = Orders(order_quantity=order_quantity_,
					sell_date=sell_date_,
					order_user_id = order_user_id_,
					order_product_id = order_product_id_,
					order_product_name = order_product_name_,
					order_product_desc = order_product_desc_,
					order_sell_price = order_sell_price_,
					order_cost_price = order_cost_price_,
					order_unit_of_measurement = order_unit_of_measurement_,
					order_discount = order_discount_,
					order_expiry_date = order_expiry_date_)
		
		db.session.add(new_order)
		
		db.session.delete(product)
	db.session.commit()
	return jsonify({'message': 'checkout Successful'}), 200