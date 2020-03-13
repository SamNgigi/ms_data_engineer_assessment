# from flask import jsonify, json
from ..services.db.db_handler import PostgresDBService
import psycopg2 

from .AbstractModel import AbstractModel


class Classes:
    
    def __init__(self, name, code, start_date, end_date):
        self.id = None 
        self.name = name
        self.code = code
        self.start_date = start_date
        self.end_date = end_date

class ClassesSql(AbstractModel):

    db_handler = PostgresDBService()

    def save(self, class_object):

        class_exists = self.get_by_name(class_object.name)

        if class_exists:
            print({"message": "Cohort aleady exists"})
        else:
            save_sql = """
                INSERT INTO classes(class_name, code, start_date, end_date) VALUES\
                (%s, %s, %s, %s) RETURNING id, class_name, code, start_date, end_date
            """
            class_params = (class_object.name, class_object.code, class_object.start_date, class_object.end_date)
            class_obj = self.db_handler.insert_update(save_sql, class_params)

            if not class_obj:
                print("Could not add classes", psycopg2.DatabaseError)
                
            class_object.id = class_obj[0]
            class_instance = {
                "class_id": class_obj[0],
                "class_name": class_obj[1],
                "class_code": class_obj[2],
                "start_date": class_obj[3],
                "end_date": class_obj[4]
            }
            print({
                "message": "Classes added successfully",
                "category_added": class_instance,
                "status": 200
            })
        # TODO - Ask jack if this is necessary especially condidering the with context
        # self.db_handler.close_connection()

    def get_by_id(self, id):
        sql = """
            SELECT * FROM classes WHERE id = %s
        """
        fetched_class = self.db_handler.fetch(sql, params=(id,), one=True)
        return fetched_class

    def get_by_name(self, name):
        sql = """
            SELECT * FROM classes WHERE class_name = %s
        """
        fetched_class = self.db_handler.fetch(sql, params=(name,), one=True)
        return fetched_class

    def get_all(self) -> list:
        sql = """
            SELECT * FROM classes
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

