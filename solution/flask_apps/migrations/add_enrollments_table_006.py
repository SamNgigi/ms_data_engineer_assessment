from .abstractmigration import AbstractMigrations


class CreateEnrollmentsTable(AbstractMigrations):
    number = 6
    name = "create enrollments table"
    up_sql = """
    CREATE TABLE IF NOT EXISTS enrollments(
        id SERIAL PRIMARY KEY NOT NULL,
        person_id INT REFERENCES peoples(id) ON DELETE\
        CASCADE,
        class_id INT REFERENCES classes(id) ON DELETE\
        CASCADE,
        module_id INT REFERENCES modules(id) ON DELETE\
        CASCADE,
        score INTEGER NOT NULL,
        attendance INTEGER NOT NULL,
        passed BOOLEAN NOT NULL ,
        dropped_reason VARCHAR
    );"""
    down_sql = """DROP TABLE IF EXISTS enrollments CASCADE"""