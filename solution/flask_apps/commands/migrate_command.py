from flask_script import Command
from ..migrations import MIGRATIONS, create_migrations_table
from ..services.db.db_handler import PostgresDBService

class MigrateCommand(Command):
    
    def run(self):  # pylint: disable=E0202
        db_handler = PostgresDBService()
        # Creating the migration table before creating
        # other tables
        create_migrations_table(db_handler)
        # Ordering the way we want tables created
        MIGRATIONS.sort(key=lambda x:x.number)

        for migration in MIGRATIONS:
            print(f"Migration {migration.number}: {migration.name}")
            sql = 'SELECT id FROM migrations WHERE number=%s'
            check = db_handler.fetch(sql, params=(migration.number,))

            if check:
                print(f"Migration {migration.name} exists. Skipping ....")
                continue
            migration = migration(db_handler)
            migration.up()
            db_handler.execute_sql("INSERT INTO migrations(number, name) VALUES (%s, %s)",\
                params=(migration.number, migration.name))

        db_handler.close_connection()
