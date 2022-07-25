from flask import Flask, make_response  # type:ignore
from flask_bcrypt import Bcrypt  # type:ignore
from flask_sqlalchemy import SQLAlchemy  # type:ignore
from flask_marshmallow import Marshmallow  # type:ignore
from flask_cors import CORS  # type:ignore

from logging.config import fileConfig
from src.config.base import LogConfig

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_filename=None):
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # Database configs
    if (app.config["ENV"] == 'development'):
        app.config.from_object('src.config.base.Config')
    elif (app.config["ENV"] == 'production'):
        app.config.from_object('src.config.base.ProdConfig')
    elif config_filename:
        app.config.from_pyfile(config_filename)
    else:
        raise RuntimeError('Unknown environment setting provided.')

    # Logs configs
    fileConfig(LogConfig.CONF_LOG_FILE_PATH, defaults={
               'logfilename': LogConfig.LOG_FILE_PATH}, disable_existing_loggers=False)

    db.init_app(app)
    ma = Marshmallow(db)
    bcrypt = Bcrypt(app)

    #CORS(app)
    #CORS(app, resources={r"/V1/*": {"origins": "*"}})
    CORS(app, resources={r"/*": {"origins": "*"}})
    # CORS Headers

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers","*"
                             )#"Content-Type,Authorization,x-access-token,X-Custom-Header,true"
        response.headers.add("Access-Control-Allow-Methods",
                             "*")#"GET,PUT,PATCH,POST,DELETE,OPTIONS"
        response.headers.add("Access-Control-Allow-Origin",
                             "*")
        return response

    #Handling errors. use abort(codeErr) to call manually these functions

    @app.errorhandler(400)
    def bad_request(error):
        return make_response({
            'success': False,
            'error': 400,
            'message': 'Server cannot or will not process the request due to client error (for example, malformed request syntax, invalid request message framing, or deceptive request routing).',
        }, 400)

    @app.errorhandler(403)
    def not_found(error):
        return make_response({
            'success': False,
            'error': 403,
            'message': 'Forbidden resource',
        }, 403)

    @app.errorhandler(404)
    def not_found(error):
        return make_response({
            'success': False,
            'error': 404,
            'message': 'resource not found',
        }, 404)

    @app.errorhandler(405)
    def not_found(error):
        return make_response({
            'success': False,
            'error': 405,
            'message': 'method not allowed',
        }, 405)

    @app.errorhandler(422)
    def unprocessable(error):
        return make_response({
            'success': False,
            'error': 422,
            'message': 'unprocessable',
        }, 422)

    @app.errorhandler(500)
    def internal_server_error(error):
        return make_response({
            'success': False,
            'error': 500,
            'message': 'Internall server error',
        }, 500)



    with app.app_context():
        from src.main.routes.routes import default_routes,admin_routes

        # Register Blueprints
        app.register_blueprint(default_routes)
        app.register_blueprint(admin_routes)

        #CORS(default_routes)
        #CORS(admin_routes)

        print(app.url_map)

        # database intialisation
        db.create_all()

        return app, db, bcrypt, ma
