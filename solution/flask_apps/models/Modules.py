from ..services.db.db_handler import PostgresDBService
import psycopg2
import pandas as pd

from .AbstractModel import AbstractModel


class Modules:

    def __init__(self, name, position, weeks):
        self.id =None
        self.name = name
        self.position = position
        self.weeks = weeks

class ModulesSql(AbstractModel):

    db_handler = PostgresDBService()

    
    def save(self, module_object):
        
        module_exists = self.get_by_name(module_object.name)

        if module_exists:
            print({"message": "Module already exists"})
        else:
            save_sql = """
                INSERT INTO modules(module_name, position, week) VALUES\
                    (%s, %s, %s) RETURNING id, module_name, position, week
            """
            module_params = (module_object.name, module_object.position, module_object.weeks)
            module_obj = self.db_handler.insert_update(save_sql, module_params)

            if not module_obj:
                print("Could not add module", psycopg2.DatabaseError)

            module_object.id = module_obj[0]
            module_instance = {
                "module_id": module_obj[0],
                "module_name": module_obj[1],
                "module_position": module_obj[2],
                "module_weeks": module_obj[3],
            }

            print({
                "message" : "Modules added successfully",
                "module_added" : module_instance,
                "status": 200
            })


    
    def get_by_id(self, id):
        sql = """  
            SELECT * FROM modules WHERE id = %s
        """
        fetched_module = self.db_handler.fetch_dict(sql, params=(id,), one=True)

        return fetched_module

    def get_by_name(self, name):
        sql = """  
            SELECT * FROM modules WHERE module_name = %s
        """
        fetched_module = self.db_handler.fetch_dict(sql, params=(name, ), one=True)
        return fetched_module

    
    def get_all(self) -> list:
        sql = """  
            SELECT * FROM modules
        """
        all_modules = self.db_handler.fetch_dict(sql, one=False)

        return all_modules

    
    def get_df(self) -> pd.DataFrame:
        
        sql = """  
            SELECT * FROM modules
        """

        modules_df = self.db_handler.fetch_df(sql)

        return modules_df

    
    def update_by_id(self, id):
        pass

    
    def delete_by_id(self, id):
        pass

    
    def clear_all(self):
        pass
