#default config
import os

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\x89\xf2\xea\xc9\x11\xab\xda\xaf\x0c-)w\xf9AJ<U\x04Dh\x8112'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False