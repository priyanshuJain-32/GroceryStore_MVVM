from functools import wraps
from flask import jsonify, request

def admin_required(f):
    @wraps(f)
    def _admin_verify(*args, **kwargs):
        data = request.get_json()
        role = data.get('role')
        if role!='admin':
            return jsonify({'message': 'Only Admin Access'}), 401
        return f(*args, **kwargs)
    return _admin_verify