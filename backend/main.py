from flask import Blueprint, request, render_template, redirect, url_for
from . import db
from flask_login import login_required, current_user
from .models import Category, Product, Orders, Cart
from datetime import datetime, date
import os

current_dir = os.path.abspath(os.path.dirname(__file__))

main = Blueprint('main',__name__)

#======================= Home Controls =====================================

@main.route('/')
def home():
	if request.method == 'GET':
		return render_template('home.html')

#--------------------------------------------------------------------------
# User specific controllers -----------------------------------------------
#--------------------------------------------------------------------------

#======================= Product User Controls =====================================

@main.route('/product_page')
@login_required
def product_page():
	category_data = Category.query.all()
	return render_template('product_page.html', name=current_user.name, 
		category_data=category_data,current_user=current_user)

#======================= Order User Controls =====================================

@main.route('/order_product/<int:product_id>', methods=['GET','POST'])
@login_required
def order_product(product_id):
	
	product_data = Product.query.filter_by(product_id=product_id).first()
	if request.method=='GET':
		return render_template('order.html',product_data=product_data)
	
	order_quantity_ = int(request.form.get('product_quantity'))
	
	# Handling the quantity of order and stock remaining
	product_data.product_quantity -= order_quantity_
	
	sell_date_ = datetime.now()
	order_user_id_ = current_user.user_id
	order_product_id_ = product_id
	new_order = Orders(order_quantity=order_quantity_,sell_date=sell_date_,
		order_user_id=order_user_id_,order_product_id=order_product_id_)
	db.session.add(new_order)
	db.session.commit()
	return redirect(url_for('main.product_page'))

#======================= Cart User Controls =====================================

@main.route('/cart_product/<int:product_id>',methods=['POST']) #### Add tables for cart data
@login_required
def cart_product(product_id):
	product_data = Product.query.filter_by(product_id=product_id).first()
	cart_data = Cart.query.filter_by(cart_product_id=product_id, cart_user_id = current_user.user_id)
	if cart_data:
		for cart_product in cart_data:
			if cart_product.cart_product_id==product_id:
				cart_product.cart_product_quantity += 1
				product_data.product_quantity -= 1
				db.session.commit()
				return redirect(url_for('main.product_page'))

	new_cart_entry = Cart(cart_product_id = product_id, cart_product_quantity = 1, cart_user_id = current_user.user_id)
	product_data.product_quantity -= 1
	db.session.add(new_cart_entry)
	db.session.commit()
	return redirect(url_for('main.product_page'))

	return ('Cart',product_id)


@main.route('/view_cart',methods=['GET']) #### Add tables for cart data
@login_required
def view_cart():
	if request.method=='GET':
		cart_data=Cart.query.filter_by(cart_user_id=current_user.user_id).all()
		total_value = 0
		for product in cart_data:
			total_value += product.cart_product_quantity*product.products.sell_price
		return render_template('cart.html',cart_data=cart_data, total_value=total_value)


@main.route('/reduce_cart_item/<int:cart_product_id>',methods=['GET']) #### Add tables for cart data
@login_required
def reduce_cart(cart_product_id):
	cart_data = Cart.query.filter_by(cart_product_id=cart_product_id, cart_user_id = current_user.user_id).first()
	
	if cart_data:	
		cart_data.cart_product_quantity -= 1
		cart_data.products.product_quantity += 1
		if cart_data.cart_product_quantity<=0:
			db.session.delete(cart_data)
		db.session.commit()

	cart_data=Cart.query.filter_by(cart_user_id=current_user.user_id).all()
	return render_template('cart.html',cart_data=cart_data)


@main.route('/delete_cart_item/<int:cart_product_id>',methods=['GET'])
@login_required
def delete_cart(cart_product_id):
	cart_data = Cart.query.filter_by(cart_product_id=cart_product_id, cart_user_id=current_user.user_id).first()
	
	if cart_data:
		cart_data.products.product_quantity += cart_data.cart_product_quantity
		cart_data.cart_product_quantity = 0
		db.session.delete(cart_data)
		db.session.commit()

	cart_data=Cart.query.filter_by(cart_user_id=current_user.user_id).all()
	return render_template('cart.html',cart_data=cart_data)

@main.route('/buy_cart_item/<int:cart_product_id>',methods=['GET'])
@login_required
def buy_cart(cart_product_id):
	cart_data = Cart.query.filter_by(cart_product_id=cart_product_id, cart_user_id=current_user.user_id).first()
	cart_data.cart_product_quantity = 0
	db.session.delete(cart_data)
	db.session.commit()

	cart_data=Cart.query.filter_by(cart_user_id=current_user.user_id).all()
	return render_template('cart.html',cart_data=cart_data)

@main.route('/checkout_cart',methods=['GET'])
@login_required
def checkout_cart():
	cart_data = Cart.query.filter_by(cart_user_id=current_user.user_id).all()
	sell_date = datetime.now()

	order_user_id = current_user.user_id
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

#======================= Profile User Controls (Phase2) =====================================

@main.route('/profile')
@login_required
def profile():
	return 'Profile'

#--------------------------------------------------------------------------
# Admin specific controllers ----------------------------------------------
#--------------------------------------------------------------------------

#======================= Category Admin Controls =====================================

@main.route('/list_category',methods=['GET'])
@login_required
def list_category():
	category_data = Category.query.all()
	return render_template("list_category.html", category_data=category_data)


@main.route('/add_category',methods=['GET','POST']) #TESTED OK
@login_required
def add_category():
	if request.method=='GET':
		return render_template('add_category_details.html')
	category_name_ = request.form.get('category_name')
	new_category = Category(category_name = category_name_)
	db.session.add(new_category)
	db.session.commit()
	return redirect(url_for('main.list_category')) #TESTED OK


@main.route('/edit_category/<int:category_id>',methods=['GET','POST']) #TESTED OK
@login_required
def edit_category(category_id):
	category_data = Category.query.filter_by(category_id=category_id).first()
	if request.method=='GET':
		return render_template('edit_category.html', category_data=category_data)
	category_data.category_name = request.form.get('category_name')
	db.session.commit()
	return redirect(url_for('main.list_category')) #TESTED OK


@main.route('/delete_category/<int:category_id>',methods=['GET','POST']) #TESTED OK
@login_required
def delete_category(category_id):
	category_data = Category.query.filter_by(category_id=category_id).first()
	product_data = category_data.products
	db.session.delete(category_data)
	if product_data:
		for product in product_data:
			db.session.delete(product)
	db.session.commit()
	return redirect(url_for('main.list_category')) #TESTED OK

#================ Product Admin Controls ========================


@main.route('/add_product/<int:category_id>', methods=['GET','POST']) #TESTED OK
@login_required
def add_product(category_id):
	if request.method=='GET':
		category_data = Category.query.filter_by(category_id=category_id).first()
		return render_template('add_product.html',category_data=category_data, date_today = date.today())
	product_name = request.form.get('product_name')
	product_desc = request.form.get('product_desc')
	unit_of_measurement=request.form.get('unit_of_measurement')
	sell_price = int(request.form.get('sell_price'))
	cost_price = int(request.form.get('cost_price'))
	discount = int(request.form.get('discount'))
	product_quantity = int(request.form.get('product_quantity'))
	ed = request.form.get('expiry_date')
	d_format = '%Y-%m-%d'
	expiry_date = datetime.strptime(ed,d_format)
	new_product = Product(product_name=product_name,product_desc=product_desc,unit_of_measurement=unit_of_measurement,sell_price=sell_price,
		cost_price=cost_price,discount=discount,product_quantity=product_quantity,expiry_date=expiry_date,
		product_category_id=category_id)
	db.session.add(new_product)
	db.session.commit()
	return redirect(url_for('main.list_category')) #TESTED OK


@main.route('/edit_product/<int:product_id>', methods=['GET','POST']) #TESTED OK
@login_required
def edit_product(product_id):

	product_data = Product.query.filter_by(product_id=product_id).first()
	
	if request.method=='GET':
		return render_template('edit_product.html',product_data=product_data)
	
	product_data.product_name = request.form.get('product_name')
	product_data.product_desc = request.form.get('product_desc')
	product_data.unit_of_measurement = request.form.get('unit_of_measurement')
	product_data.sell_price = int(request.form.get('sell_price'))
	product_data.cost_price = int(request.form.get('cost_price'))
	product_data.discount = int(request.form.get('discount'))
	product_data.product_quantity = int(request.form.get('product_quantity'))
	ed = request.form.get('expiry_date')
	d_format = '%Y-%m-%d'
	product_data.expiry_date = datetime.strptime(ed,d_format)
	
	db.session.commit()
	return redirect(url_for('main.edit_category',category_id=product_data.product_category_id)) #TESTED OK


@main.route('/delete_product/<int:product_id>', methods=['GET','POST']) #TESTED OK
@login_required
def delete_product(product_id):
	product_data = Product.query.filter_by(product_id=product_id).first()
	# Delete product from user carts also
	for cart in product_data.cart:
		db.session.delete(cart)
	
	db.session.delete(product_data)
	db.session.commit()
	return redirect(url_for('main.edit_category',category_id=product_data.product_category_id)) #TESTED OK

#============================== Analytics Admin Controls ====================================

@main.route('/analytics', methods=['GET'])
@login_required
def analytics():
	category_data = Category.query.all()

	category_names, category_sales = [],[]
	product_names, product_sales = [],[]

	for category in category_data:
		category_names.append(category.category_name)
		category_total = 0
		for product in category.products:
			product_names.append(product.product_name)
			product_total = 0
			for order in product.orders:
				category_total += order.order_quantity*product.sell_price
				product_total += order.order_quantity*product.sell_price
			product_sales.append(product_total)
		category_sales.append(category_total)
 	
 	# Importing necessary library for plotting.
		
	import matplotlib.pyplot as plt
	  
	# Creating list of Month and Share_buy for Plotting Line Graph
	  
	# Plotting Line Graph
	plt.figure(1)
	plt.title("Revenue by category")
	plt.xlabel('Categories')
	plt.ylabel("Revenue in INR")
	plt.bar(category_names, category_sales)
	plt.savefig(os.path.join(current_dir, "static/category_bar_plot.png"), format='png')

	# Plotting Line Graph
	plt.figure(2)
	plt.title("Revenue by product")
	plt.xlabel('Products')
	plt.ylabel("Revenue in INR")
	plt.bar(product_names, product_sales)
	
	plt.savefig(os.path.join(current_dir, "static/product_bar_plot.png"), format='png')
	return render_template('analytics.html')