import pathlib
from os import environ, path
from dotenv import load_dotenv  # type:ignore

BASE_DIR = pathlib.Path(__file__).parent.resolve()  # current directory
ENV_FILE = BASE_DIR / '.env'
load_dotenv(ENV_FILE)


class Config:
    DEBUG = False
    TESTING = True
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_ENV = "development"

    # sqlite
    DATABASE_NAME = "../data_test/test.sqlite3"
    DATABASE_PATH = BASE_DIR / DATABASE_NAME
    SQLALCHEMY_DATABASE_URI = environ.get(
        "SQLALCHEMY_DATABASE_URI"
    ) or "sqlite:///{}".format(DATABASE_PATH)
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS").lower().strip() == 'true'


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    FLASK_ENV = 'production'

    # PG config
    DATABASE_HOST = environ.get("DATABASE_HOST")
    DATABASE_NAME = environ.get("DATABASE_NAME")  # type:ignore
    DATABASE_USERNAME = environ.get('DATABASE_USERNAME')
    DATABASE_PASSWORD = environ.get('DATABASE_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS").lower().strip() == 'true'

class LogConfig:
    CONF_LOG_FILE_NAME = environ.get("CONF_LOG_FILE_NAME")
    LOG_FILE_NAME = environ.get("LOG_FILE_NAME")
    CONF_LOG_FILE_PATH = BASE_DIR / CONF_LOG_FILE_NAME
    LOG_FILE_PATH = BASE_DIR / LOG_FILE_NAME
    