import os

import abc

import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

import pickle


class AbstractGSpread(abc.ABC):

    @abc.abstractmethod
    def authenticate(self):
        pass
    
    @abc.abstractmethod
    def get_spread(self):
        pass


class GspreadService(AbstractGSpread):

    def __init__(self):
        self.creds = None
        self.base_url = 'https://docs.google.com/spreadsheets/d'
        self.spread_url = None
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    
    def authenticate(self):
        self.creds = SAC.from_json_keyfile_name(
            'gspread-270619-05d12e0e0262.json', self.SCOPES)

        gsp = gspread.authorize(self.creds)

        return gsp

    def get_spread(self, sheet_id):

        gsp = self.authenticate()

        workbook = gsp.open_by_url(f'{self.base_url}/{sheet_id}')

        sheet_array = workbook.worksheets()

        return sheet_array



# gsp = gspread.authorize(creds)

# admiss = gsp.open_by_url(full_url)

# admiss
# < Spreadsheet 'hogwarts_admissions' id: 1lKrQ4NKwogywiDqnNuwva4zDVNi18x2BClQ6ugFU7SQ >

# admiss.worksheets()
