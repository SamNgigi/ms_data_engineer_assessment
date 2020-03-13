from ..abstract_resource import AbstractSpreadSheetResource
from ..abstract_resource import gsheets_dict

from ....models.People import People, PeopleSql

import pandas as pd

class AllApplicationsResource(AbstractSpreadSheetResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sheet_id = gsheets_dict['admissions']
        self.parsers = {
            "^all_applications$": self.parse_allApplications
        }

    def parse_allApplications(self, sheet_name, applications_df)->pd.DataFrame:
        return applications_df


    def store(self):
        people_sql = PeopleSql()
        # self.parsed_data is dict of sheets-names and dataframes
        clean_resource = self.parsed_data

        for sheet in clean_resource.keys():
            people_res = clean_resource[sheet].to_dict(orient='records')

            for entry in people_res:
                first_name = entry.get('first_name')
                last_name = entry.get('last_name')
                phone = entry.get('phone')
                email = entry.get('email')
                gender = entry.get('gender')

                people_obj = PeopleSql(
                    first_name, last_name, phone, email, gender)
                people_sql.save(people_obj)
    
