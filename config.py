# Configuration settings for the Flask application

# Secret key for session management
SECRET_KEY = 'mysecretkey'

# Other application-specific configurations


class Config:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    # Database connection details
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_NAME = 'mydatabase'
    DB_USER = 'myuser'
    DB_PASSWORD = 'mypassword'
    

class ProductionConfig(Config):
    DEBUG = False
    # Database connection details
    DB_HOST = 'prod-db-server'
    DB_PORT = 5432
    DB_NAME = 'mydatabase'
    DB_USER = 'myuser'
    DB_PASSWORD = 'mypassword'