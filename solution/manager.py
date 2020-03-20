from flask_script import Server, Manager

from app import create_flask

from flask_apps.commands.resource_commands import MapResources
from flask_apps.commands.migrate_command import MigrateCommand

flask_app  = create_flask()

manager = Manager(flask_app)

manager.add_command("runserver", Server(use_debugger=True))
manager.add_command("gspread", MapResources)
manager.add_command("migrate", MigrateCommand)

if __name__ == "__main__":
    manager.run()
