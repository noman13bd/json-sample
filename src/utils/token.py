from datetime import timedelta
from src.core.flask_app import app
import jwt
import datetime
from typing import Dict, Any

class TokenGenerator:
    @staticmethod
    def generate_jwt(payload: Dict[str, Any], minutes: int = 60):
        token = jwt.encode({
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = minutes),
            'name': payload['name'],
            'email': payload['email']
        }, app.config['SECRET_KEY'])
        
        return token.decode('utf-8')