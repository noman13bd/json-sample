from src.models.user import User
from flask import Blueprint, request
from src.utils import ResponseGenerator
from src.decorators import json_data_required

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/api/v1/register', methods=['POST'])
@json_data_required
def user_register():
    data = request.get_json()
    new_user = User(data['name'], data['email'], data['password'])    
    new_user.save()
    return ResponseGenerator.generate_response(new_user.__repr__(), 200)