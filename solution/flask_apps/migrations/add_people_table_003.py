from .abstractmigration import AbstractMigrations


class CreatePeoplesTable(AbstractMigrations):
    number = 3
    name = "create peoples table"
    up_sql = """
    CREATE TABLE IF NOT EXISTS peoples(
        id SERIAL PRIMARY KEY NOT NULL,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR NOT NULL,
        phone VARCHAR NOT NULL,
        email VARCHAR NOT NULL,
        gender VARCHAR NOT NULL
    );"""
    down_sql = """DROP TABLE IF EXISTS peoples CASCADE"""
