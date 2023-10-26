from functools import wraps
from flask import current_app, jsonify, request
import jwt
from .models import Users

def admin_required(f):
    @wraps(f)
    def _admin_verify(*args, **kwargs):
        data = request.get_json()
        role = data.get('role')
        if role!='admin':
            return jsonify({'message': 'Only Admin Access'}), 401
        return f(*args, **kwargs)
    return _admin_verify

def staff_required(f):
    @wraps(f)
    def _staff_verify(*args, **kwargs):
        data = request.get_json()
        role = data.get('role')
        if role != 'admin' and role != 'manager':
            return jsonify({'message':'Only Staff Access'}), 401
        return f(*args, **kwargs)
    return _staff_verify