from typing import List, Dict, Union, Optional
from src.models.todos import Todo

class TodoRepository:
    @staticmethod
    def create_todo(title: str, isCompleted: bool, **kwargs) -> Optional[Todo]:
        new_todo = Todo(title, None, isCompleted, **kwargs)
        return new_todo.save()