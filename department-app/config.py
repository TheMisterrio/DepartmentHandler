"""Settings database for server and tests"""


class ApiConfiguration:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://sql7323829:3rBGJdfIew@sql7.freemysqlhosting.net:3306/sql7323829'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfiguration:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://sql7323829:3rBGJdfIew@sql7.freemysqlhosting.net:3306/sql7323829'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    DEBUG = True

