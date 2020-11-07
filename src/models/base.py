from datetime import datetime
from src.core.database import db

class BaseModel():
    """ generalize model's common functions """
    
    _created_at = db.Column(db.DateTime, nullable = False, default = datetime.now)
    _updated_at = db.Column(db.DateTime, nullable = True, onupdate = datetime.now)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        