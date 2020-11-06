import os
from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand
from app.main import create_app, db
from app import blueprint

from app.main.model.user import User
from app.main.model.lead import Lead
from app.main.model.opportunity import Opportunity
from app.main.model.customer import Customer
from app.main.model.status import Status

app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
	app.run()

if __name__ == '__main__':
	manager.run()
