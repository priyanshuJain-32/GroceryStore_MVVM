from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Importing the database objects and classes from models
import os
from flask_cors import CORS
from flask_restful import Api
# from app.models import Address, Cart, Category, Order, Product

db = SQLAlchemy()
api = Api()

# ====================================== Configuration ===========================================================
# Start by creating a flask app object
def create_app():
	app = Flask(__name__) # Here we mentioned __name__ because we are converting this module to app
	current_dir = os.path.abspath(os.path.dirname(__file__))
	
	# Configuring the app
	app.config['SECRET_KEY'] = 'secret-key-goes-here'
	app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "instance/database.sqlite3") # adding the database to app

	 # Passing the app object into db object
	CORS(app, origins=["http://localhost:8080"])
	api.init_app(app)
	db.init_app(app)
	app.app_context().push()
	
	#adding blueprint for auth routes
	from .api.authApi import auth
	app.register_blueprint(auth)

	#adding blueprint for cart
	from .api.cartApi import cart
	app.register_blueprint(cart)

	# adding blueprint for category
	from .api.categoryApi import category
	app.register_blueprint(category)

	# adding blueprint for order
	from .api.orderApi import order
	app.register_blueprint(order)

	#adding blueprint for product
	from .api.productApi import product
	app.register_blueprint(product)

	#adding blueprint for reports
	from .api.reportApi import report
	app.register_blueprint(report)

	#adding blueprint for other parts of the app
	from .api.userApi import user
	app.register_blueprint(user)

	

	return app
 
	# Pushing it into the context refer https://flask.palletsprojects.com/en/2.3.x/appcontext/#:~:text=The%20Flask%20application,the%20current%20activity.