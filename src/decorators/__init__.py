from functools import wraps
from flask import request
from src.utils import ResponseGenerator
from src.core.flask_app import app
import jwt

def json_data_required(f):
    """ check if request contains json data """
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return ResponseGenerator.json_data_expected()
        
        try:
            request.get_json()
        except Exception as _e:
            return ResponseGenerator.json_data_expected()
        
        return f(*args, **kwargs)
    return wrapper

def check_if_authorized(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if request.headers.has_key('Access-Token'):
            token = request.headers['Access-Token']
        if not token:
            return ResponseGenerator.forbidden_op('Missing Token')
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return ResponseGenerator.forbidden_op('Invalid Token')
            
        return f(*args, **kwargs)
    
    return wrapper



