import abc
import pandas as pd
import psycopg2 


class AbstractModel(abc.ABC):
    """ Create """
    @abc.abstractmethod
    def save(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_by_id(self, id):
        pass
    
    def get_by_name(self, name):
        pass

    @abc.abstractmethod
    def get_all(self)->list:
        pass
    
    @abc.abstractmethod
    def get_df(self)->pd.DataFrame:
        pass
    
    @abc.abstractmethod
    def update_by_id(self, id):
        pass

    @abc.abstractmethod
    def delete_by_id(self, id):
        pass

    @abc.abstractmethod
    def clear_all(self):
        pass


class AbstractHogwartsModel(AbstractModel):
    pass