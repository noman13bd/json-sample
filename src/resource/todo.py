from src.repository.todo import TodoRepository
from flask import Blueprint, request
from src.utils import ResponseGenerator
from src.decorators import json_data_required, check_if_authorized

todo_blueprint = Blueprint('todo', __name__)

@todo_blueprint.route('/api/v1/todo', methods=['POST'])
@check_if_authorized
@json_data_required
def todo_create():
    data = request.get_json()
    new_todo = TodoRepository.create_todo(data['title'], data['isCompleted'])
    
    return ResponseGenerator.generate_response(new_todo.__repr__(), 200)