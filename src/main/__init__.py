from flask import Flask  # type:ignore
from flask_restful import Api  # type:ignore
from flask_bcrypt import Bcrypt  # type:ignore
from flask_sqlalchemy import SQLAlchemy  # type:ignore
from flask_marshmallow import Marshmallow  # type:ignore

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_filename=None):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    if (app.config["ENV"] == 'development'):
        app.config.from_object('config.base.Config')
    elif (app.config["ENV"] == 'production'):
        app.config.from_object('config.base.ProdConfig')
    else:
        raise RuntimeError('Unknown environment setting provided.')
    if config_filename:
        app.config.from_pyfile(config_filename)
    db.init_app(app)
    ma = Marshmallow(db)
    api = Api(app)
    bcrypt = Bcrypt(app)
    with app.app_context():
        # import blueprints
        # Register Blueprints
        db.create_all()
        return app, db, api, bcrypt, ma


'''
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

'''
