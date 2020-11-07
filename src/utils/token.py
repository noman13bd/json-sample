from datetime import timedelta
from src.core.flask_app import app
import jwt
import datetime
from typing import Dict, Any

class TokenGenerator:
    @staticmethod
    def generate_jwt(payload: Dict[str, Any], minutes: int = 60):
        payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes = minutes)
        token = jwt.encode(
            payload
            , app.config['SECRET_KEY']
        )
        
        return token.decode('utf-8')