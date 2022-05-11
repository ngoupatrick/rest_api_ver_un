import pathlib
from flask import Flask  # type:ignore
from flask_sqlalchemy import SQLAlchemy  # type:ignore
from flask_marshmallow import Marshmallow  # type:ignore
from flask_restful import Api  # type:ignore

current_folder = pathlib.Path(__file__).parent.resolve()  # current directory
database_path = current_folder / "data_test/test.sqlite3"
database_uri = "sqlite:///{}".format(database_path)

app = Flask(__name__)
app.url_map.strict_slashes = False

app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db = SQLAlchemy(app)
ma = Marshmallow(db)

api = Api(app)
