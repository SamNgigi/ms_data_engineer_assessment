from .abstractmigration import AbstractMigrations


class CreateAdmissionsTable(AbstractMigrations):
    number = 5
    name = "create admissions table"
    up_sql = """
    CREATE TABLE IF NOT EXISTS admissions(
        id SERIAL PRIMARY KEY NOT NULL,
        person_id INT REFERENCES peoples(id) ON DELETE\
        CASCADE,
        class_id INT REFERENCES classes(id) ON DELETE\
        CASCADE
    );"""
    down_sql = """DROP TABLE IF EXISTS admissions CASCADE;"""
