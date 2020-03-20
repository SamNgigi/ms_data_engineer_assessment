import abc
import re

from .gspread_service import GspreadService

import pandas as pd

gsheets_dict = {
    'admissions': '1zG8i_IqstrIenDAmQTtgdZ7lILKHY5x_v8jHKgkyDcs',
    'enrollments': '18tvRHT4qy15cSnC9tkrs5I1GkDfqzjC3LFaaUuy6jPg',
    'outcomes': '1yN-9oTIuF69w57oTzvQpEbfd3fmmRKnhhNvBUKJXdnc'
}

# Helper function
def sheet_to_df(sheet):
    data = sheet.get_all_values()
    df = pd.DataFrame(data)
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    return df

class AbstractResource(abc.ABC):

    @abc.abstractmethod
    def fetch(self):
        pass
    
    @abc.abstractmethod
    def process(self):
        pass
    
    @abc.abstractmethod
    def store(self):
        pass

class AbstractSpreadSheetResource(AbstractResource):
    def __init__(self):
        self.sheet_id = None  # google sheet id
        self.parsers = {} # sheet with parser function
        self.gsp_service = GspreadService()
        self.raw_data = {} # sheet name with raw data
        self.parsed_data = {} # sheet name with cleaned data

    def fetch(self):
        if self.sheet_id:
            self.raw_data = self.fetch_from_workbook(self.sheet_id)
        else:
            print('No Sheet_id given')

    def fetch_from_workbook(self, sheet_id, range=None):

       sheet_array = self.gsp_service.get_spread(sheet_id)

       data_raw = {sht.title: sheet_to_df(sht) for sht in sheet_array}

       return data_raw

    def process(self):
        for sheet_name, df in self.raw_data.items():
            for regex, func in self.parsers.items():
                pattern = re.compile(regex)
                if re.match(pattern, sheet_name):
                    no_dups_df = self.dups_handler(df) #
                    data = func(sheet_name, no_dups_df)
                    self.parsed_data[sheet_name]=data

    def dups_handler(self, df):
        # Dealing with duplicates
        if df.duplicated().any(axis=0):
            no_dups = df.drop_duplicates()
        else:
            no_dups = df

        return no_dups

    def store(self):
        pass



