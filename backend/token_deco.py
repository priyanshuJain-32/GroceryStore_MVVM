from functools import wraps
from flask import current_app, jsonify, request
import jwt
from .models import Users

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()
        print(auth_headers)
        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }
        
        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401
        
        try:
            token = auth_headers[1]
        
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms="HS256")
            print(data)
            user = Users.query.filter_by(user_name=data['sub']).first() # This needs fixing
            if not user:
                raise RuntimeError('User not found')
            return f(user,*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify

