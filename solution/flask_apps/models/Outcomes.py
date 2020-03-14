from ..services.db.db_handler import PostgresDBService
import psycopg2

import pandas as pd

from .AbstractModel import AbstractModel


class Outcomes:

    def __init__(self, person_id, class_id):
        self.id = None
        self.person_id = person_id
        self.class_id = class_id


class OutcomesSql(AbstractModel):

    db_handler = PostgresDBService()

    def save(self, outcomes_object):

        outcomes_exists = self.get_by_id(outcomes_object.id)

        if outcomes_exists:
            print({"message": "Outcomes aleady exists"})
        else:
            save_sql = """
                INSERT INTO outcomes(person_id, class_id) VALUES\
                (%s, %s) RETURNING id, person_id, class_id
            """
            outcomes_params = (outcomes_object.person_id,
                                 outcomes_object.class_id)

            outcomes_obj = self.db_handler.insert_update(
                save_sql, outcomes_params)

            if not outcomes_obj:
                print("Could not add Outcomes", psycopg2.DatabaseError)

            outcomes_object.id = outcomes_obj[0]
            outcomes_instance = {
                "id": outcomes_obj[0],
                "person_id": outcomes_obj[1],
                "class_id": outcomes_obj[2]
            }
            print({
                "message": "Outcomes added successfully",
                "category_added": outcomes_instance,
                "status": 200
            })
        # TODO - Ask jack if this is necessary especially condidering the with context
        # self.db_handler.close_connection()

    def get_by_id(self, id):
        sql = """
            SELECT * FROM outcomes WHERE id = %s
        """
        fetched_class = self.db_handler.fetch(sql, params=(id,), one=True)
        return fetched_class

    def get_all(self) -> list:
        sql = """
            SELECT * FROM outcomes
        """

        all_outcomes = self.db_handler.fetch_dict(sql, one=False)

        # class_lst = []

        return all_outcomes

    def get_df(self) -> pd.DataFrame:
        sql = """
            SELECT * FROM outcomes
        """

        outcomes_df = self.db_handler.fetch_df(sql)

        return outcomes_df

    def update_by_id(self):
        pass

    def delete_by_id(self):
        pass

    def clear_all(self):
        pass
