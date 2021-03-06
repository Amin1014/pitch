import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
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
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('://','ql://')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:Amin1234@localhost/pitch'

    DEBUG = False

config_options = {
'development':DevConfig,
'production':ProdConfig

}