from ..services.db.db_handler import PostgresDBService
import psycopg2

from .AbstractModel import AbstractModel


class Applications:

    def __init__(self, person_id, class_id, date):
        self.id = None
        self.person_id = person_id
        self.class_id = class_id
        self.date = date

class ApplicationsSql(AbstractModel):

    db_handler = PostgresDBService()

    def save(self, applications_obj):

        person_exists = self.get_by_id(application_object.id)

        if person_exists:
            print({"message": "Person aleady exists"})
        else:
            save_sql = """
                INSERT INTO classes(fperson_id, class_id, date) VALUES\
                (%s, %s, %s, %s) RETURNING id, person_id, class_id, date
            """
            people_params = (application_object.first_name, application_object.last_name,
                             application_object.phone)

            people_obj = self.db_handler.insert_update(save_sql, people_params)

            if not people_obj:
                print("Could not add classes", psycopg2.DatabaseError)

            application_object.id = people_obj[0]
            people_instance = {
                "id": people_obj[0],
                "first_name": people_obj[1],
                "last_name": people_obj[2]
            }
            print({
                "message": "Classes added successfully",
                "category_added": people_instance,
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

    def get_all(self) -> list:
        sql = """
            SELECT * FROM classes
        """

        all_classes = self.db_handler.fetch_dict(sql, one=False)

        # class_lst = []

        return all_classes



