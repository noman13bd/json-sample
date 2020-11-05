from flask_alchemy import SQLAlchemy
from .flask_app import app

db = SQLAlchemy(app)