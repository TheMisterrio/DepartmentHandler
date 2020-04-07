"""Settings database for server and tests"""


ip = 'http://127.0.0.1:5000'


class ApiConfiguration:
    SQLALCHEMY_DATABASE_URI = 'postgresql://atstsfjvlugfjx:8ba88b179d24328feffd700ac2c730416668f103c2d7a64a5e9856d778076346@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/dbfg4v0954n0c'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfiguration:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://sql7323829:3rBGJdfIew@sql7.freemysqlhosting.net:3306/sql7323829'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    DEBUG = True

