from ..abstract_resource import AbstractSpreadSheetResource
from ..abstract_resource import gsheets_dict

from ....models.Classes import ClassesSql
from ....models.People import People, PeopleSql
from ....models.Admissions import Admissions, AdmissionsSql

import pandas as pd

class StudentsClassResource(AbstractSpreadSheetResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sheet_id = gsheets_dict['admissions']
        self.parsers = {
            r"^(HC_)(\d+)(_students)$": self.parse_studentsRes
        }

    def parse_studentsRes(self, sheet_name, student_class_df)->pd.DataFrame:
        return student_class_df


    def store(self):
        people_sql = PeopleSql()
        classes_sql = ClassesSql()
        admissions_sql = AdmissionsSql()

        clean_resource = self.parsed_data

        for sheet in clean_resource.keys():
            admission_res = clean_resource[sheet].to_dict(orient='records')
            for entry in admission_res:
                class_name = sheet.rsplit('_', 1)[0]
                email = entry.get('email')

                person_obj = people_sql.get_by_email(email)
                class_obj = classes_sql.get_by_name(class_name)

                admissions_instance = Admissions(person_obj['id'], class_obj['id'])
                admissions_sql.save(admissions_instance)




""" 
* The HC_1-12_students have unique names not present in the all
* applications sheet.
"""



