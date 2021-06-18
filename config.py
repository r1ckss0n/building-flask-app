import os

# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xa0\xa4S\\o\xc6\xadD5\xf9\x9aY\xcc\x97\xbd<\xac(ntI\x87\xb2K'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# We are overriding the parent class's debug class variable which is set to false, by signing it here is set to trueclass DevelopmentConfig(BaseConfig):
class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

