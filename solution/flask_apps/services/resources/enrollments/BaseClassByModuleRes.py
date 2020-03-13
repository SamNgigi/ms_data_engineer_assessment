from ..abstract_resource import AbstractSpreadSheetResource
from ..abstract_resource import gsheets_dict

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
