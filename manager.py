from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from src.core.flask_app import app
from src.core.database import db
from src.models.user import User
from src.models.todos import Todo

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()