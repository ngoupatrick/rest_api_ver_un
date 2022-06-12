from flask import Flask, url_for  # type:ignore
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
    bcrypt = Bcrypt(app)
    
    with app.app_context():
        # import blueprints
        from main.routes import default_routes,admin_routes
        
        # Register Blueprints
        app.register_blueprint(default_routes)
        app.register_blueprint(admin_routes)
        
        print(app.url_map)
        #database intialisation
        db.create_all()
        
        return app, db, bcrypt, ma

