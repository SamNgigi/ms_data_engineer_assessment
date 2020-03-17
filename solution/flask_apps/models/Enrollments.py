from ..services.db.db_handler import PostgresDBService
import psycopg2
import pandas as pd

from .AbstractModel import AbstractModel


class Enrollments:

    def __init__(self, person_id, class_id, module_id, score, attendance, passed, dropped_reason):
        self.id = None
        self.person_id = person_id
        self.class_id = class_id
        self.module_id = module_id
        self.score = score
        self.attendance = attendance
        self.passed = passed
        self.dropped_reason = dropped_reason


class EnrollmentsSql(AbstractModel):

    db_handler = PostgresDBService()

    def save(self, enrollment_object):

        enrollment_exists = self.get_by_name(enrollment_object.name)

        if enrollment_exists:
            print({"message": "Module already exists"})
        else:
            save_sql = """
                INSERT INTO enrollments(person_id, class_id, module_id, score, attendance, passed, dropped_reason) VALUES\
                    (%s, %s, %s) RETURNING id, person_id, class_id, module_id, score
            """
            enrollment_params = (enrollment_object.name,
                             enrollment_object.position, enrollment_object.weeks)
            enrollment_obj = self.db_handler.insert_update(save_sql, enrollment_params)

            if not enrollment_obj:
                print("Could not add enrollment", psycopg2.DatabaseError)

            enrollment_object.id = enrollment_obj[0]
            enrollment_instance = {
                "enrollment_id": enrollment_obj[0],
                "enrollment_person_id": enrollment_obj[1],
                "enrollment_class_id": enrollment_obj[2],
                "enrollment_module_id": enrollment_obj[3],
                "enrollment_score": enrollment_obj[4],
            }

            print({
                "message": "Enrollments added successfully",
                "enrollment_added": enrollment_instance,
                "status": 200
            })

    def get_by_id(self, id):
        sql = """  
            SELECT * FROM enrollments WHERE id = %s
        """
        fetched_enrollment = self.db_handler.fetch_dict(
            sql, params=(id,), one=True)

        return fetched_enrollment

    def get_by_name(self, name):
        sql = """  
            SELECT * FROM enrollments WHERE enrollment_name = %s
        """
        fetched_enrollment = self.db_handler.fetch_dict(
            sql, params=(name, ), one=True)
        return fetched_enrollment

    def get_all(self) -> list:
        sql = """  
            SELECT * FROM enrollments
        """
        all_enrollments = self.db_handler.fetch_dict(sql, one=False)

        return all_enrollments

    def get_df(self) -> pd.DataFrame:

        sql = """  
            SELECT * FROM enrollments
        """

        enrollments_df = self.db_handler.fetch_df(sql)

        return enrollments_df

    def update_by_id(self, id):
        pass

    def delete_by_id(self, id):
        pass

    def clear_all(self):
        pass
