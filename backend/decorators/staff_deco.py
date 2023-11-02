from functools import wraps
from flask import jsonify, request

def staff_required(f):
    @wraps(f)
    def _staff_verify(*args, **kwargs):
        data = request.get_json()
        role = data.get('role')
        if role != 'admin' and role != 'manager':
            return jsonify({'message':'Only Staff Access'}), 401
        return f(*args, **kwargs)
    return _staff_verify