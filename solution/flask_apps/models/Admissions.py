from ..services.db.db_handler import PostgresDBService
import psycopg2

from .AbstractModel import AbstractModel


class Admissions:

    def __init__(self, person_id, class_id):
        self.id = -1
        self.person_id = person_id
        self.class_id = class_id


class AdmissionsSql(AbstractModel):

    db_handler = PostgresDBService()

    def save(self, admissions_object):

        admissions_exists = self.get_by_id(admissions_object.id)

        if admissions_exists:
            print({"message": "Admission aleady exists"})
        else:
            save_sql = """
                INSERT INTO admissions(person_id, class_id) VALUES\
                (%s, %s) RETURNING id, person_id, class_id
            """
            admissions_params = (admissions_object.person_id, admissions_object.class_id)

            admissions_obj = self.db_handler.insert_update(
                save_sql, admissions_params)

            if not admissions_obj:
                print("Could not add Admission", psycopg2.DatabaseError)

            admissions_object.id = admissions_obj[0]
            admissions_instances = {
                "id": admissions_obj[0],
                "person_id": admissions_obj[1],
                "class_id": admissions_obj[2]
            }
            print({
                "message": "Admissions added successfully",
                "category_added": admissions_instances,
                "status": 200
            })
        # TODO - Ask jack if this is necessary especially condidering the with context
        # self.db_handler.close_connection()

    def get_by_id(self, id):
        sql = """
            SELECT * FROM admissions WHERE id = %s
        """
        fetched_class = self.db_handler.fetch(sql, params=(id,), one=True)
        return fetched_class

    def get_all(self) -> list:
        sql = """
            SELECT * FROM admissions
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
