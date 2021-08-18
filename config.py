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
    SQLALCHEMY_DATABASE_URI = 'postgres://ysgsdfkpizmbia:804af2a93c640e729c5f3e5d033c8e19fa4f7c7cadf205cf80f068e824b8479b@ec2-35-174-56-18.compute-1.amazonaws.com:5432/d79cri6rbkjsk'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Amin1234@localhost/pitch'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}