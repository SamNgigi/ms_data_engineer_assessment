from ..abstract_resource import AbstractSpreadSheetResource
from ..abstract_resource import gsheets_dict

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
