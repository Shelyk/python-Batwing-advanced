class Config:
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'postgresql://library:library@db:5432/library'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
