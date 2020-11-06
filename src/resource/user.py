from src.models.user import User
from flask import Blueprint
from src.utils import ResponseGenerator
from src.models import user

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/api/v1/register', methods=['POST'])
def user_register():
    new_user = User('Ismail', 'imn@imn.com', '123456')
    new_user.save()
    return ResponseGenerator.generate_response('ok', 200)