#default config
from random import * 
#import os

char_set=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'I', u'J', u'K', u'L', u'M', u'N', u'O', u'P', u'Q', u'R', u'S', u'T', u'U', u'V', u'W', u'X', u'Y', u'Z', u'a', u'b', u'c', u'd', u'e', u'f', u'g', u'h', u'i', u'j', u'k', u'l', u'm', u'n', u'o', u'p', u'q', u'r', u's', u't', u'u', u'v', u'w', u'x', u'y', u'z', u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9']

aplhanumeric_set = "".join([choice(char_set) for _ in range(randint(1,1000))])


class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\x89\xf2\xea\xc9\x11\xab\xda\xaf\x0c-)w\xf9AJ<U\x04Dh\x8112'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL ']
	SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False