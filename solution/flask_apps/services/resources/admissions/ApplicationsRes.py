from ..abstract_resource import AbstractSpreadSheetResource
from ..abstract_resource import gsheets_dict

from ....models.Classes import ClassesSql
from ....models.People import People, PeopleSql
from ....models.Applications import Applications, ApplicationsSql

import pandas as pd

class AllApplicationsResource(AbstractSpreadSheetResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sheet_id = gsheets_dict['admissions']
        self.parsers = {
            "^all_applications$": self.parse_allApplications
        }

    def parse_allApplications(self, sheet_name, applications_df)->pd.DataFrame:
        applications_df[['first_name', 'last_name']] = applications_df['name'].str.split(
            pat=' ', expand=True)[[0, 1]]
        return applications_df


    def store(self):
        people_sql = PeopleSql()
        classes_sql = ClassesSql()
        applications_sql = ApplicationsSql()
        # self.parsed_data is dict of sheets-names and dataframes
        clean_resource = self.parsed_data

        for sheet in clean_resource.keys():
            application_res = clean_resource[sheet].to_dict(orient='records')

            for entry in application_res:
                first_name = entry.get('first_name')
                last_name = entry.get('last_name')
                phone = entry.get('phone')
                email = entry.get('email')
                gender = entry.get('gender')
                class_name = entry.get('class')
                date = entry.get('date')

                person_instance = People(
                    first_name, last_name, phone, email, gender)
                people_sql.save(person_instance)

                person_obj = people_sql.get_by_email(email)
                class_obj = classes_sql.get_by_name(class_name)

                application_instance = Applications(
                    person_obj['id'], class_obj['id'], date)
                applications_sql.save(application_instance)





                
    

# TODO
# *1. Feature engineer first and last name from peoples
# *2. Get people by email and assign id to application
# *3 Get class by name and assign to application
