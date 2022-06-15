from flask import Blueprint
from flask_restful import Api  # type:ignore

from main.views.users_views import auth
from main.resources import PersonneResource, UserResource
from main.views.groupViews import GroupResource

#creation des differentes urls de bases
default_routes = Blueprint('default_routes', __name__,url_prefix="/V1")
admin_routes = Blueprint('admin_routes', __name__,url_prefix="/admin")

#ajout des sous-routes
default_routes.register_blueprint(auth)

#BLUEPRINT = RESOURCE
#Utilisation des Ressources et Blueprint
api = Api(default_routes)

#Ajout des ressources
api.add_resource(PersonneResource,
                 '/personnes/',
                 '/personnes/<string:eid>')

api.add_resource(GroupResource,
                 '/groups/',
                 '/groups/<string:guid>')
