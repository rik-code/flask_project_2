import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'poprobui-ugadai'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///students.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

