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

@order.route('/order_product/<int:product_id>', methods=['GET', 'POST'])
@token_required
def order_product(user, product_id):
	
	product_data = Product.query.filter_by(product_id=product_id).first()
	if request.method=='GET':
		return render_template('order.html',product_data=product_data)
	
	order_quantity_ = int(request.form.get('product_quantity'))
	
	# Handling the quantity of order and stock remaining
	product_data.product_quantity -= order_quantity_
	
	sell_date_ = datetime.now()
	order_user_id_ = user.user_id
	order_product_id_ = product_id
	new_order = Orders(order_quantity=order_quantity_,sell_date=sell_date_,
		order_user_id=order_user_id_,order_product_id=order_product_id_)
	db.session.add(new_order)
	db.session.commit()
	return redirect(url_for('main.product_page'))

