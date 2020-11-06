from models.base import BaseModel
from core.database import db

class Todo(db.Model, BaseModel):
    __tablename__ = "todos"
    
    id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    title = db.Column(db.String(255), nullable = False)
    dateline = db.Column(db.DateTime, nullable = True)
    isCompleted = db.Column(db.Boolean, nullable = True, default = False)
    
    def __init__(self, title, dateline, isCompleted, **kwargs):
        super(Todo, self).__init__(**kwargs)
        
        self.title = title
        self.dateline = dateline
        self.isCompleted = isCompleted
        
    def __repr__(self):
        return "ToDo({}, {}, {})".format(self.id, self.title, self.isCompleted)