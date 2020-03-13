# from flask import jsonify, json
from ..services.db.db_handler import PostgresDBService
import psycopg2

from .AbstractModel import AbstractModel


class People:

    def __init__(self, first_name, last_name, phone, email, gender):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.gender = gender


class PeopleSql(AbstractModel):

    db_handler = PostgresDBService()

    def save(self, people_object):

        person_exists = self.get_by_email(people_object.email)

        if person_exists:
            print({"message": "Person aleady exists"})
        else:
            save_sql = """
                INSERT INTO peoples(first_name, last_name, phone, email, gender) VALUES\
                (%s, %s, %s, %s, %s) RETURNING id, first_name, last_name, phone
            """
            people_params = (people_object.first_name, people_object.last_name,
                            people_object.phone, people_object.email, people_object.gender)

            people_obj = self.db_handler.insert_update(save_sql, people_params)

            if not people_obj:
                print("Could not add classes", psycopg2.DatabaseError)

            people_object.id = people_obj[0]
            people_instance = {
                "id": people_obj[0],
                "first_name": people_obj[1],
                "last_name": people_obj[2]
            }
            print({
                "message": "Person added successfully",
                "category_added": people_instance,
                "status": 200
            })
        # TODO - Ask jack if this is necessary especially condidering the with context
        # self.db_handler.close_connection()

    def get_by_id(self, id):
        sql = """
            SELECT * FROM peoples WHERE id = %s
        """
        fetched_class = self.db_handler.fetch_dict(sql, params=(id,), one=True)
        return fetched_class

    def get_by_email(self, email):
        sql = """
            SELECT * FROM peoples WHERE email = %s
        """
        fetched_class = self.db_handler.fetch_dict(sql, params=(email,), one=True)
        return fetched_class

    def get_all(self) -> list:
        sql = """
            SELECT * FROM peoples
        """

        all_classes = self.db_handler.fetch_dict(sql, one=False)

        # class_lst = []

        return all_classes

    def update_by_id(self):
        pass

    def delete_by_id(self):
        pass

    def clear_all(self):
        pass
