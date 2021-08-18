import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = 'SQLAlchemy engine=postgresql://pitch:Amin1234@ec2-54-224-194-214.compute-1.amazonaws.com:5432/dc91pqn3gimkq5'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Amin1234@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #Email configuration
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,

}