from src.repository.user import UserRepository
from flask import Blueprint, request
from src.utils import ResponseGenerator
from src.decorators import json_data_required
from src.utils.token import TokenGenerator

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/api/v1/register', methods=['POST'])
@json_data_required
def user_register():
    data = request.get_json()
    new_user = UserRepository.create_user(data['name'], data['email'], data['password'])
    print(new_user)
    return ResponseGenerator.generate_response(new_user.__repr__(), 200)

@user_blueprint.route('/api/v1/login', methods=['POST'])
@json_data_required
def user_login():
    data = request.get_json()
    existing_user = UserRepository.check_password(data['email'], data['password'])
    if existing_user:
        token = TokenGenerator.generate_jwt({'name':existing_user.name, 'email':existing_user.email})
        return ResponseGenerator.generate_response({'token':token}, 200)
    return ResponseGenerator.user_login_failed()