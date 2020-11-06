import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	DEBUG = True
	SECRET_KEY = os.getenv('SECRET_KEY', 'UEl753051733SL8e73qd4MPezy4Mzg')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:128Parsecs!@localhost/challenge?charset=utf8mb4'

key = Config.SECRET_KEY
