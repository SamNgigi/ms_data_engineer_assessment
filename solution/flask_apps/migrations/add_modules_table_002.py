from .abstractmigration import AbstractMigrations


class CreateModulesTable(AbstractMigrations):
    number = 2
    name = "create modules table"
    up_sql = """
    CREATE TABLE IF NOT EXISTS modules(
        id SERIAL PRIMARY KEY NOT NULL,
        module_name VARCHAR NOT NULL UNIQUE,
        position INTEGER NOT NULL,
        week INTEGER NOT NULL
    );"""
    down_sql = """DROP TABLE IF EXISTS modules CASCADE"""
