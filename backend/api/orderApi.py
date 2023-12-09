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
	order_product_id_ = data.get('product_id')
	order_quantity_ = data.get('order_quantity')

	product_data = Product.query.filter_by(product_id=order_product_id_).first()
	
	if product_data.product_quantity < order_quantity_:
		return jsonify({'message': 'Not Enough Stock', 'available': product_data.product_quantity})
	
	# Handling the quantity of order and stock remaining
	product_data.product_quantity -= order_quantity_
	
	sell_date_ = datetime.now()
	order_user_id_ = user.user_id
	order_product_id_ = product_data.product_id
	order_product_name_ = product_data.product_name
	order_product_desc_ = product_data.product_desc
	order_sell_price_ = product_data.sell_price
	order_cost_price_ = product_data.cost_price
	order_unit_of_measurement_ = product_data.unit_of_measurement
	order_discount_ = product_data.discount
	order_expiry_date_ = product_data.expiry_date

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
	db.session.commit()
	return jsonify({'message': 'Product ordered'}), 200

@order.route('/get_all_order', methods=['GET'])
@token_required
def get_all_order(user):
	
	all_order_data = Orders.query.filter_by(order_user_id = user.user_id)
	orders_list = []
	if all_order_data:
		for order in all_order_data:
			orders_list.append({"order_id": order.order_id,
					   "order_quantity" : order.order_quantity,
					   "sell_date" : order.sell_date,
					   "order_user_id" : order.order_user_id,
					   "order_product_id" : order.order_product_id,
					   "order_product_name" : order.order_product_name,
					   "order_product_desc" : order.order_product_desc,
					   "order_sell_price" : order.order_sell_price,
					   "order_cost_price" : order.order_cost_price,
					   "order_unit_of_measurement" : order.order_unit_of_measurement,
					   "order_discount" : order.order_discount,
					   "order_expiry_date" : order.order_expiry_date})
		return jsonify(orders_list), 200

	return jsonify({"message": "No orders found"})