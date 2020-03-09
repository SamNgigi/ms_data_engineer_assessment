import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'hard to guess string'
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DB_URL') or \
        'sqlite:///' + os.path.join(basedir, 'dev-db.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DB_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test-db.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}
