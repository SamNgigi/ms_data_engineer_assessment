from ..abstract_resource import AbstractSpreadSheetResource
from ..abstract_resource import gsheets_dict

from ....models.Modules import Modules, ModulesSql

import pandas as pd


class ModulesResource(AbstractSpreadSheetResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sheet_id = gsheets_dict['enrollments']
        self.parsers = {
            r"^modules$": self.parse_modules
        }

    def parse_modules(self, sheet_name, modules_df) -> pd.DataFrame:
        return modules_df

    def store(self):
        modules_sql = ModulesSql()

        clean_resource = self.parsed_data

        for sheet in clean_resource.keys():
            module_res = clean_resource[sheet].to_dict(orient='records')

            for entry in module_res:
                module_name = entry.get('name')
                module_postion = entry.get('position')
                module_weeks = entry.get('weeks')

                module_obj = Modules(module_name, module_postion, module_weeks)
                modules_sql.save(module_obj)





