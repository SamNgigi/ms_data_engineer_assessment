import abc

import os

import psycopg2
import psycopg2.extras
from psycopg2 import Error
from config import configs

import pandas as pd


class AbstractDatabaseService(abc.ABC):

    @abc.abstractmethod
    def execute_sql(self, sql, *args, **kwargs):
        pass


class PostgresDBService(AbstractDatabaseService):

    def __init__(self):
        self.connection = psycopg2.connect(configs['dev'].DATABASE_URL) 

    def execute_sql(self, sql, params=None, commit=True):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            if commit:
                self.connection.commit()

    def fetch(self, sql, params=None, one=False):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            if one:
                return cursor.fetchone()
            return cursor.fetchall()
    
    def fetch_dict(self, sql, params=None, one=False):
        
        with self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(sql, params)
            if one:
                return cursor.fetchone()
            return cursor.fetchall()


    def fetch_df(self, sql)->pd.DataFrame:

        with self.connection as conn:
            df = pd.read_sql_query(sql, conn)

            return df

        

    def insert_update(self, sql, params=None, batch=False, returning=False):
        with self.connection.cursor() as cursor:
            if batch == False:
                cursor.execute(sql, params)
                instance_list = cursor.fetchone()
            else:
                psycopg2.extras.execute_batch(cursor, sql, params)
            self.connection.commit()
            return instance_list

    def close_connection(self):
        self.connection.close()
    
