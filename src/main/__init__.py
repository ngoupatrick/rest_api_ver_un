from flask import Flask  # type:ignore
from flask_bcrypt import Bcrypt  # type:ignore
from flask_sqlalchemy import SQLAlchemy  # type:ignore
from flask_marshmallow import Marshmallow  # type:ignore

from logging.config import fileConfig
from config.base import LogConfig

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_filename=None):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    
    # Database configs
    if (app.config["ENV"] == 'development'):
        app.config.from_object('config.base.Config') # for wsgi.py
        #app.config.from_object('src.config.base.Config') # for main.py
    elif (app.config["ENV"] == 'production'):
        app.config.from_object('config.base.ProdConfig') # for wsgi.py
        #app.config.from_object('src.config.base.ProdConfig') # for main.py
    elif config_filename:
        app.config.from_pyfile(config_filename)
    else:
        raise RuntimeError('Unknown environment setting provided.')
    
    #Logs configs
    fileConfig(LogConfig.CONF_LOG_FILE_PATH, defaults={'logfilename': LogConfig.LOG_FILE_PATH}, disable_existing_loggers=False)
        
    db.init_app(app)
    ma = Marshmallow(db)
    bcrypt = Bcrypt(app)
    
    with app.app_context():
        from main.routes.routes import default_routes,admin_routes # for wsgi.py
        #from src.main.routes.routes import default_routes,admin_routes # for main.py
        
        # Register Blueprints
        app.register_blueprint(default_routes)
        app.register_blueprint(admin_routes)
        
        print(app.url_map)
        #from main.utils.query import Query
        #db.Query=Query
        #database intialisation
        db.create_all()
        
        return app, db, bcrypt, ma

