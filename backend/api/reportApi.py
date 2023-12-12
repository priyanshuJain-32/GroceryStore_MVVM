from flask import Blueprint, jsonify, render_template
import os
from datetime import datetime, date

from ..models.category import Category
from .. import db
from ..decorators.token_deco import token_required
from ..decorators.staff_deco import staff_required

current_dir = os.path.abspath(os.path.dirname(__file__))

report = Blueprint('reportApi',__name__)

#============================== Reports Controls ====================================

@report.route('/analytics', methods=['GET'])
@token_required
@staff_required
def analytics(user):
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
	return category_names, category_sales, product_names, product_sales