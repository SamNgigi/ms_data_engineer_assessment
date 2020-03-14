from ..services.db.db_handler import PostgresDBService
import psycopg2

import pandas as pd

from .AbstractModel import AbstractModel


class Applications:

    def __init__(self, person_id, class_id, date):
        self.id = None
        self.person_id = person_id
        self.class_id = class_id
        self.date = date

class ApplicationsSql(AbstractModel):

    db_handler = PostgresDBService()

    def save(self, application_object):

        application_exists = self.get_by_id(application_object.id)

        if application_exists:
            print({"message": "Application aleady exists"})
        else:
            save_sql = """
                INSERT INTO applications(person_id, class_id, date) VALUES\
                (%s, %s, %s) RETURNING id, person_id, class_id, date
            """
            application_params = (application_object.person_id, application_object.class_id,
                             application_object.date)

            application_obj = self.db_handler.insert_update(save_sql, application_params)

            if not application_obj:
                print("Could not add applications", psycopg2.DatabaseError)

            application_object.id = application_obj[0]
            application_instance = {
                "id": application_obj[0],
                "person_id": application_obj[1],
                "class_id": application_obj[2]
            }
            print({
                "message": "Application added successfully",
                "category_added": application_instance,
                "status": 200
            })
        # TODO - Ask jack if this is necessary especially condidering the with context
        # self.db_handler.close_connection()

    def get_by_id(self, id):
        sql = """
            SELECT * FROM applications WHERE id = %s
        """
        fetched_class = self.db_handler.fetch(sql, params=(id,), one=True)
        return fetched_class

    def get_all(self) -> list:
        sql = """
            SELECT * FROM applications
        """

        all_applications = self.db_handler.fetch_dict(sql, one=False)

        # class_lst = []

        return all_applications

    def get_df(self)->pd.DataFrame:
        sql = """
            SELECT * FROM applications
        """

        applications_df = self.db_handler.fetch_df(sql)

        return applications_df
        

    def update_by_id(self):
        pass

    def delete_by_id(self):
        pass

    def clear_all(self):
        pass


