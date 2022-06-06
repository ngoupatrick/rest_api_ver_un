from src import current_folder


database_path = current_folder / "db.sqlite"
database_uri = "sqlite:///{}".format(database_path)

SQLALCHEMY_DATABASE_URI = database_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

TESTING = True
DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = 'GDtfDCFYjD'
