from ..abstract_resource import AbstractSpreadSheetResource
from ..abstract_resource import gsheets_dict

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
