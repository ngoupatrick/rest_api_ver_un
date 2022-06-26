from flask import Blueprint
from flask_restful import Api  # type:ignore
from . import *

# creation des differentes urls de bases
default_routes = Blueprint('default_routes', __name__, url_prefix="/V1")
admin_routes = Blueprint('admin_routes', __name__, url_prefix="/admin")

# ajout des sous-routes
default_routes.register_blueprint(auth)

#BLUEPRINT = RESOURCE
# Utilisation des Ressources et Blueprint
api = Api(default_routes)
api_admin = Api(admin_routes)

# Ajout des ressources

# ressource de gestion des groupes
api.add_resource(GroupResource,
                 '/groups/',
                 '/groups/<string:guid>')
# ressource de gestion des users
api.add_resource(UserResource,
                 '/users/',
                 '/users/<string:puid>')
# ressource de gestion des structures
api.add_resource(StructureResource,
                 '/structures/',
                 '/structures/<string:pstid>')
# ressource de gestion des types de users
api.add_resource(UserTypeResource,
                 '/userTypes/',
                 '/userTypes/<string:putid>')
# ressource de gestion des patients
api.add_resource(PatientResource,
                 '/patients/',
                 '/patients/<string:ppid>')
# ressource de gestion des types de symptomes
api.add_resource(SymptomesTypeResource,
                 '/symptomeTypes/',
                 '/symptomeTypes/<string:ptsid>')
# ressource de gestion des symptomes
api.add_resource(SymptomeResource,
                 '/symptomes/',
                 '/symptomes/<string:psid>')
# ressource de gestion des liens consultations - symptomes
api.add_resource(ConsultationSymptomeResource,
                 '/consultationSymptomes/',
                 '/consultationSymptomes/<string:pcsid>')
# ressource de gestion des resultats d'analyse labo
api.add_resource(ResultatResource,
                 '/resultats/',
                 '/resultats/<string:prid>')
# ressource de gestion des consultations
api.add_resource(ConsultationResource,
                 '/consultations/',
                 '/consultations/<string:pcid>')
# ressource de gestion des requetes sql
api_admin.add_resource(SQLResource,
                       '/sql/')
