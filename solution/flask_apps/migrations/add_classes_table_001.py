from .abstractmigration import AbstractMigrations

class CreateClassTable(AbstractMigrations):
    number = 1
    name = "create classes table"
    up_sql = """
    CREATE TABLE IF NOT EXISTS classes(
        id SERIAL PRIMARY KEY,
        class_name VARCHAR NOT NULL,
        code VARCHAR NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL
    );"""
    down_sql = """DROP TABLE IF EXISTS classes CASCADE"""
