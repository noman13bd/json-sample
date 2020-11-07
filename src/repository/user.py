from typing import List, Dict, Union, Optional
from src.models.user import User

class UserRepository:
    @staticmethod
    def create_user(name: str, email: str, password: str, **kwargs) -> Optional[User]:
        existing_user = UserRepository.get_by_email(email)
        if existing_user:
            return None
        
        new_user = User(name, email, password, **kwargs)
        return new_user.save()
    
    @staticmethod
    def get_by_email(email: str) -> User:
        return User.query.filter(
            User.email == email
        ).first()
        
    @staticmethod
    def check_password(email: str, password: str):
        existing_user = UserRepository.get_by_email(email)
        if not existing_user:
            return None
        if User.check_password(existing_user, password):
            return existing_user
        return None