from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from .. import db
from ..models.product import Product
from ..models.order import Orders
from datetime import datetime, date
import os
from ..decorators.token_deco import token_required

current_dir = os.path.abspath(os.path.dirname(__file__))

order = Blueprint('orderApi',__name__)

#--------------------------------------------------------------------------
# User specific controllers -----------------------------------------------
#--------------------------------------------------------------------------

#======================= Order User Controls =====================================

@order.route('/order_product', methods=['POST'])
@token_required
def order_product(user):
	
	data = request.get_json()
	product_id = data.get('product_id')
	order_quantity = data.get('order_quantity')

	product_data = Product.query.filter_by(product_id=product_id).first()
	
	if product_data.product_quantity < order_quantity:
		return jsonify({'message': 'Not Enough Stock', 'available': product_data.product_quantity})

	order_quantity_ = order_quantity
	
	# Handling the quantity of order and stock remaining
	product_data.product_quantity -= order_quantity_
	
	sell_date_ = datetime.now()
	order_user_id_ = user.user_id
	order_product_id_ = product_id
	new_order = Orders(order_quantity=order_quantity_,sell_date=sell_date_,
		order_user_id=order_user_id_,order_product_id=order_product_id_)
	db.session.add(new_order)
	db.session.commit()
	return jsonify({'message': 'Product ordered'}), 200

@order.route('/get_all_order', methods=['GET'])
@token_required
def get_all_order(user):
	
	all_order_data = Orders.query.filter_by(order_user_id = user.user_id)
	orders_list = []
	if all_order_data:
		for order_data in all_order_data:
			orders_list.append({"order_id": order_data.order_id,
				"order_quantity": order_data.order_quantity,
				"sell_date": order_data.sell_date,
				"order_product_id": order_data.order_product_id})
		return jsonify(orders_list), 200

	return jsonify({"message": "No orders found"})