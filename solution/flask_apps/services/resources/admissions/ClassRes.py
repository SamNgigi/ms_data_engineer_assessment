from ..abstract_resource import AbstractSpreadSheetResource
from ..abstract_resource import gsheets_dict

from ....models.Classes import Classes, ClassesSql

import pandas as pd

class ClassResource(AbstractSpreadSheetResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sheet_id = gsheets_dict['admissions']
        self.parsers = {
            "^classes$" : self.parse_classes
        }
    
    def parse_classes(self, sheet_name, classes_df)->pd.DataFrame:
        
        '''
        Feature engineering start_date & end_data from data

        {"name":"HC_1","start_date":2019-01-01,"end_date":2019-06-01,"code":xyz}
        '''
        classes_df[['start_date', 'end_date']] = classes_df.code.str.rsplit(
            pat='_', n=2, expand=True)[[1,  2]]

        return classes_df
        
    def store(self):
        cls_sql = ClassesSql()
        # self.parsed_data is dict of sheets-names and dataframes
        clean_resource = self.parsed_data

        for sheet in clean_resource.keys():
            class_res = clean_resource[sheet].to_dict(orient='records')

            for entry in class_res:
                class_name = entry.get('name')
                class_code = entry.get('code')
                start_date = entry.get('start_date')
                end_date = entry.get('end_date')

                class_obj = Classes(class_name, class_code, start_date, end_date)
                cls_sql.save(class_obj)






