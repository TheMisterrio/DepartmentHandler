"""Settings database for server and tests"""


class ApiConfiguration:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://zvx3895FX7:Dur4UnX1x6@remotemysql.com:3306/zvx3895FX7'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfiguration:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://G7PajAyxic:BA2aYVjUJ6@remotemysql.com:3306/G7PajAyxic'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    DEBUG = True

