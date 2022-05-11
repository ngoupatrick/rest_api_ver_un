from src import api, app  # type:ignore
from src.resources import PersonneResource, UserResource


api.add_resource(PersonneResource,
                 '/personnes/',
                 '/personnes/<string:eid>')

api.add_resource(UserResource,
                 '/users/',
                 '/users/<string:eid>')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
