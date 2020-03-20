from .abstractmigration import AbstractMigrations


class CreateApplicationsTable(AbstractMigrations):
    number = 4
    name = "create applications table"
    up_sql = """
    CREATE TABLE IF NOT EXISTS applications(
        id SERIAL PRIMARY KEY,
        person_id INT REFERENCES peoples(id) ON DELETE\
        CASCADE,
        class_id INT REFERENCES classes(id) ON DELETE\
        CASCADE,
        date DATE NOT NULL
    );"""
    down_sql = """DROP TABLE IF EXISTS applications CASCADE"""
