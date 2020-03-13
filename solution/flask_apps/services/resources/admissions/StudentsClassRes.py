from ..abstract_resource import AbstractSpreadSheetResource
from ..abstract_resource import gsheets_dict

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

