from ..abstract_resource import AbstractSpreadSheetResource
from ..abstract_resource import gsheets_dict

from ....models.People import PeopleSql
from ....models.Classes import ClassesSql
from ....models.Modules import ModulesSql

from ....models.Enrollments import Enrollments
from ....models.Enrollments import EnrollmentsSql

import pandas as pd


class BaseClassByModuleRes(AbstractSpreadSheetResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sheet_id = gsheets_dict['enrollments']
        self.parsers = {
         r"^(HC_)(\d+_)(charms|Dark Arts|Flying|Potions)$": self.parse_enrollments
        }

    def parse_enrollments(self, sheet_name, enrollments_df) -> pd.DataFrame:
        return enrollments_df

    def store(self):
        people_sql = PeopleSql()
        classes_sql = ClassesSql()
        module_sql = ModulesSql()
        enrollment_sql = EnrollmentsSql()

        clean_resource = self.parsed_data

        for sheet in clean_resource.keys():
            enrollment_res = clean_resource[sheet].to_dict(orient='records')
            for entry in enrollment_res:
                class_name = sheet.rsplit('_', 1)[0]
                module_name = sheet.rsplit('_', 1)[-1].lower()
                email = entry.get('email')

                score = entry.get('score')
                attendance = entry.get('attendance')
                passed = entry.get('passed')
                dropped_reason = entry.get('dropped_reason')

                person_obj = people_sql.get_by_email(email)
                class_obj = classes_sql.get_by_name(class_name)
                module_obj = module_sql.get_by_name(module_name)

                enrollment_instance = Enrollments(
                    person_obj[0], class_obj[0], module_obj[0], score, attendance, passed, dropped_reason)
                enrollment_sql.save(enrollment_instance)



