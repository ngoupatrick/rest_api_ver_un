from . import api
from main.resources import PersonneResource, UserResource
def load_routes():
    api.add_resource(PersonneResource,
                 '/personnes/',
                 '/personnes/<string:eid>')

    api.add_resource(UserResource,
                 '/users/',
                 '/users/<string:eid>')