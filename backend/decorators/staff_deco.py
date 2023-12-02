from functools import wraps
from flask import jsonify

def staff_required(f):
    @wraps(f)
    def _staff_verify(user, *args, **kwargs):
        role = user.role
        if (role != 'admin') and (role != 'manager'):
            return jsonify({'message':'Only Staff Access'}), 401
        return f(user, *args, **kwargs)
    return _staff_verify