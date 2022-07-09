import os

class Config:
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "")

class DevConfig(Config):
    pass

class ProdConfig(Config):
    DEBAG = False
    ENV = 'production'