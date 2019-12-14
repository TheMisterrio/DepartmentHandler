class ApiConfiguration:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://BwvKSyqOJr:pHUzJxlULe@remotemysql.com:3306/BwvKSyqOJr'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfiguration:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://G7PajAyxic:BA2aYVjUJ6@remotemysql.com:3306/G7PajAyxic'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    DEBUG = True

