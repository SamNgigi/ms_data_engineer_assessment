from .abstractmigration import AbstractMigrations


class CreateOutcomesTable(AbstractMigrations):
    number = 7
    name = "create outcomes table"
    up_sql = """
    CREATE TABLE IF NOT EXISTS outcomes(
        id SERIAL PRIMARY KEY NOT NULL,
        person_id INT REFERENCES peoples(id) ON DELETE\
        CASCADE,
        class_id INT REFERENCES classes(id) ON DELETE\
        CASCADE
    );"""
    down_sql = """DROP TABLE IF EXISTS outcomes CASCADE"""
