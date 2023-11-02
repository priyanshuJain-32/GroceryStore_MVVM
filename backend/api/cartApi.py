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

@cart.route('/cart_product/<int:product_id>',methods=['POST']) #### Add tables for cart data
@token_required
def cart_product(user, product_id):
	product_data = Product.query.filter_by(product_id=product_id).first()
	cart_data = Cart.query.filter_by(cart_product_id=product_id, cart_user_id = user.user_id)
	if cart_data:
		for cart_product in cart_data:
			if cart_product.cart_product_id==product_id:
				cart_product.cart_product_quantity += 1
				product_data.product_quantity -= 1
				db.session.commit()
				return redirect(url_for('main.product_page'))

	new_cart_entry = Cart(cart_product_id = product_id, cart_product_quantity = 1, cart_user_id = user.user_id)
	product_data.product_quantity -= 1
	db.session.add(new_cart_entry)
	db.session.commit()
	return redirect(url_for('main.product_page'))


@cart.route('/view_cart',methods=['GET']) #### Add tables for cart data
@token_required
def view_cart(user):
	if request.method=='GET':
		cart_data=Cart.query.filter_by(cart_user_id=user.user_id).all()
		total_value = 0
		for product in cart_data:
			total_value += product.cart_product_quantity*product.products.sell_price
		return render_template('cart.html',cart_data=cart_data, total_value=total_value)


@cart.route('/reduce_cart_item/<int:cart_product_id>',methods=['GET']) #### Add tables for cart data
@token_required
def reduce_cart(user, cart_product_id):
	cart_data = Cart.query.filter_by(cart_product_id=cart_product_id, cart_user_id = user.user_id).first()
	
	if cart_data:	
		cart_data.cart_product_quantity -= 1
		cart_data.products.product_quantity += 1
		if cart_data.cart_product_quantity<=0:
			db.session.delete(cart_data)
		db.session.commit()

	cart_data=Cart.query.filter_by(cart_user_id=user.user_id).all()
	return render_template('cart.html',cart_data=cart_data)


@cart.route('/delete_cart_item/<int:cart_product_id>',methods=['GET'])
@token_required
def delete_cart(user, cart_product_id):
	cart_data = Cart.query.filter_by(cart_product_id=cart_product_id, cart_user_id=user.user_id).first()
	
	if cart_data:
		cart_data.products.product_quantity += cart_data.cart_product_quantity
		cart_data.cart_product_quantity = 0
		db.session.delete(cart_data)
		db.session.commit()

	cart_data=Cart.query.filter_by(cart_user_id=user.user_id).all()
	return render_template('cart.html',cart_data=cart_data)

@cart.route('/buy_cart_item/<int:cart_product_id>',methods=['GET'])
@token_required
def buy_cart(user, cart_product_id):
	cart_data = Cart.query.filter_by(cart_product_id=cart_product_id, cart_user_id=user.user_id).first()
	cart_data.cart_product_quantity = 0
	db.session.delete(cart_data)
	db.session.commit()

	cart_data=Cart.query.filter_by(cart_user_id=user.user_id).all()
	return render_template('cart.html',cart_data=cart_data)

@cart.route('/checkout_cart',methods=['GET'])
@token_required
def checkout_cart(user):
	cart_data = Cart.query.filter_by(cart_user_id=user.user_id).all()
	sell_date = datetime.now()

	order_user_id = user.user_id
	for product in cart_data:
		order_product_id = product.cart_product_id
		order_quantity = product.cart_product_quantity
		new_order = Orders(order_quantity=order_quantity,
			sell_date=sell_date,
			order_user_id = order_user_id,
			order_product_id = order_product_id)
		db.session.add(new_order)
		db.session.delete(product)

	db.session.commit()
	return redirect(url_for('main.product_page'))
