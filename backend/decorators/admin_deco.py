from functools import wraps
from flask import jsonify

def admin_required(f):
    @wraps(f)
    def _admin_verify(user, *args, **kwargs):
        role = user.role
        if role!='admin':
            return jsonify({'message': 'Only Admin Access'}), 401
        return f(user, *args, **kwargs)
    return _admin_verify