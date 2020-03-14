from ..abstract_resource import AbstractSpreadSheetResource
from ..abstract_resource import gsheets_dict

from ....models.Classes import ClassesSql
from ....models.People import People, PeopleSql
from ....models.Outcomes import Outcomes, OutcomesSql

import pandas as pd


class OutcomesResource(AbstractSpreadSheetResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sheet_id = gsheets_dict['outcomes']
        self.parsers = {
            r"^(HC_)(\d+)$": self.parse_outcomes
        }

    def parse_outcomes(self, sheet_name, outcomes_df) -> pd.DataFrame:
        return outcomes_df

    def store(self):
        people_sql = PeopleSql()
        classes_sql = ClassesSql()
        outcomes_sql = OutcomesSql()

        clean_resource = self.parsed_data

        for sheet in clean_resource.keys():
            outcomes_res = clean_resource[sheet].to_dict(orient='records')
            for entry in outcomes_res:
                email = entry.get('email')
                class_name = sheet 

                person_obj = people_sql.get_by_email(email)
                class_obj = classes_sql.get_by_name(class_name)

                admissions_instance = Outcomes(
                    person_obj['id'], class_obj['id'])
                outcomes_sql.save(admissions_instance)
