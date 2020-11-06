from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from core.flask_app import app
from core.database import db
from models.user import User
from models.todos import Todo

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()