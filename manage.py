from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

from app import app, db

app.config.from_object(os.environ.get('APP_SETTINS'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# Import all database Models
from models import *
db.create_all()

# user commands
@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
