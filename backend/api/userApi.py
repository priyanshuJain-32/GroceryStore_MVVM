# ========================= Library Imports ============================
from werkzeug.exceptions import HTTPException
from flask import make_response
import json
from flask import Blueprint, request, jsonify
from datetime import datetime

# ========================= Local Imports ============================
from .. import db
from ..models.category import Category
from ..models.product import Product
from ..models.user import Users
from ..decorators.token_deco import token_required
from ..decorators.admin_deco import admin_required
from ..decorators.staff_deco import staff_required

user = Blueprint('userApi',__name__)

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

	
# ==========================================================================
# # =======================USER API=========================================
# ==========================================================================

