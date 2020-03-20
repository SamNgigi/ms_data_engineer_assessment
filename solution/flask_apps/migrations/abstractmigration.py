import abc

from ..services.db.db_handler import PostgresDBService

class AbstractMigrations(abc.ABC):

    # Class vars
    number=-1
    name=None
    up_sql=None
    down_sql=None

    def __init__(self, db_handler):
        self.db_handler = db_handler

    def up(self):
        self.db_handler.execute_sql(self.up_sql)
    
    def down(self):
        self.db_handler.execute_sql(self.down_sql)