class Config:
    SECRET_KEY = 'Your Secret Key'
    DEBUG = False
    TESTING = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'Your email adress'
    MAIL_PASSWORD = 'Your app password'

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_USERNAME = 'Your email adress for develoment'
    MAIL_PASSWORD = 'Your app password for develoment'

class ProductionConfig(Config):
    DEBUG = False