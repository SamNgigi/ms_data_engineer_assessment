import psycopg2
from psycopg2 import Error

create_tables_queries = [
    """CREATE TABLE IF NOT EXISTS classes(
        id SERIAL NOT NULL,
        class VARCHAR PRIMARY KEY NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL
    );""",
    """CREATE TABLE IF NOT EXISTS modules(
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR NOT NULL UNIQUE,
        position INTEGER NOT NULL,
        week INTEGER NOT NULL,
    );""",
    """CREATE TABLE IF NOT EXISTS people(
        id SERIAL PRIMARY KEY NOT NULL,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR NOT NULL,
        phone VARCHAR NOT NULL,
        email VARCHAR NOT NULL,
        gender VARCHAR NOT NULL,
    );""",
    """CREATE TABLE IF NOT EXISTS applications(
        id SERIAL PRIMARY KEY NOT NULL,
        person_id INT REFERENCES peoples(id) ON DELETE\
        CASCADE,
        class_id INT REFERENCES classes(id) ON DELETE\
        CASCADE
        date DATE NOT NULL
    );""",
    """CREATE TABLE IF NOT EXISTS admissions(
        id SERIAL PRIMARY KEY NOT NULL,
        person_id INT REFERENCES peoples(id) ON DELETE\
        CASCADE,
        class_id INT REFERENCES classes(id) ON DELETE\
        CASCADE
    );""",
    """CREATE TABLE IF NOT EXISTS enrollments(
        id SERIAL PRIMARY KEY NOT NULL,
        person_id INT REFERENCES peoples(id) ON DELETE\
        CASCADE,
        class_id INT REFERENCES classes(id) ON DELETE\
        CASCADE,
        module_id INT REFERENCES module(id) ON DELETE\
        CASCADE,
        score INTEGER NOT NULL,
        attendance INTEGER NOT NULL,
        passed BOOLEAN NOT NULL ,
        dropped_reason VARCHAR,
    );""",
    """CREATE TABLE IF NOT EXISTS outcomes(
        id SERIAL PRIMARY KEY NOT NULL,
        person_id INT REFERENCES peoples(id) ON DELETE\
        CASCADE,
        class_id INT REFERENCES classes(id) ON DELETE\
        CASCADE
    );"""
]

drop_tables_queries = [
    """DROP TABLE IF EXISTS classes CASCADE""",
    """DROP TABLE IF EXISTS modules CASCADE""",
    """DROP TABLE IF EXISTS peoples CASCADE""",
    """DROP TABLE IF EXISTS applications CASCADE""",
    """DROP TABLE IF EXISTS admissions CASCADE""",
    """DROP TABLE IF EXISTS enrollments CASCADE""",
    """DROP TABLE IF EXISTS outcomes CASCADE"""
]
