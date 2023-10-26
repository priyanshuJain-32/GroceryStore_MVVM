from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Importing the database objects and classes from models
import os
from flask_login import LoginManager
from flask_cors import CORS
from flask_restful import Api

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
	CORS(app)
	api.init_app(app)
	db.init_app(app)
	app.app_context().push()
	
	#adding blueprint for auth routes
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	#adding blueprint for other parts of the app
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	# adding blueprint for other parts of the app
	from .resources import resource as resource_blueprint
	app.register_blueprint(resource_blueprint)

	#adding Login framework
	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	from .models import Users

	@login_manager.user_loader
	def load_user(user_id):
		return Users.query.get(int(user_id))

	return app
 
	# Pushing it into the context refer https://flask.palletsprojects.com/en/2.3.x/appcontext/#:~:text=The%20Flask%20application,the%20current%20activity.